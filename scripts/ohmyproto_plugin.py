#!/usr/bin/env python
import sys
import re
from collections import defaultdict
from contextlib import contextmanager
from enum import Enum
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    Set,
    Tuple,
)

import google.protobuf.descriptor_pb2 as d
from google.protobuf.compiler import plugin_pb2 as plugin_pb2
from google.protobuf.internal.containers import RepeatedCompositeFieldContainer

__version__ = "0.1.0"

# SourceCodeLocation is defined by `message Location` here
# https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/descriptor.proto
SourceCodeLocation = List[int]

HEADER = f"""\"\"\"
DO NOT EDIT!
Generated by ohmyproto
isort:skip_file
\"\"\"
"""


def camel_to_snake(name):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


class FieldDescriptorProtoType(Enum):
    TYPE_DOUBLE = 1
    TYPE_FLOAT = 2
    TYPE_INT64 = 3
    TYPE_UINT64 = 4
    TYPE_INT32 = 5
    TYPE_FIXED64 = 6
    TYPE_FIXED32 = 7
    TYPE_BOOL = 8
    TYPE_STRING = 9
    TYPE_GROUP = 10
    TYPE_MESSAGE = 11
    TYPE_BYTES = 12
    TYPE_UINT32 = 13
    TYPE_ENUM = 14
    TYPE_SFIXED32 = 15
    TYPE_SFIXED64 = 16
    TYPE_SINT32 = 17
    TYPE_SINT64 = 18


# Organize proto types into categories
PROTO_FLOAT_TYPES = (
    FieldDescriptorProtoType.TYPE_DOUBLE,  # 1
    FieldDescriptorProtoType.TYPE_FLOAT,  # 2
)
PROTO_INT_TYPES = (
    FieldDescriptorProtoType.TYPE_INT64,  # 3
    FieldDescriptorProtoType.TYPE_UINT64,  # 4
    FieldDescriptorProtoType.TYPE_INT32,  # 5
    FieldDescriptorProtoType.TYPE_FIXED64,  # 6
    FieldDescriptorProtoType.TYPE_FIXED32,  # 7
    FieldDescriptorProtoType.TYPE_UINT32,  # 13
    FieldDescriptorProtoType.TYPE_SFIXED32,  # 15
    FieldDescriptorProtoType.TYPE_SFIXED64,  # 16
    FieldDescriptorProtoType.TYPE_SINT32,  # 17
    FieldDescriptorProtoType.TYPE_SINT64,  # 18
)
PROTO_BOOL_TYPES = (FieldDescriptorProtoType.TYPE_BOOL,)  # 8
PROTO_STR_TYPES = (FieldDescriptorProtoType.TYPE_STRING,)  # 9
PROTO_BYTES_TYPES = (FieldDescriptorProtoType.TYPE_BYTES,)  # 12
PROTO_MESSAGE_TYPES = (
    FieldDescriptorProtoType.TYPE_MESSAGE,  # 11
    FieldDescriptorProtoType.TYPE_ENUM,  # 14
)
PROTO_MAP_TYPES = (FieldDescriptorProtoType.TYPE_MESSAGE,)  # 11
PROTO_PACKED_TYPES = (
    FieldDescriptorProtoType.TYPE_DOUBLE,  # 1
    FieldDescriptorProtoType.TYPE_FLOAT,  # 2
    FieldDescriptorProtoType.TYPE_INT64,  # 3
    FieldDescriptorProtoType.TYPE_UINT64,  # 4
    FieldDescriptorProtoType.TYPE_INT32,  # 5
    FieldDescriptorProtoType.TYPE_FIXED64,  # 6
    FieldDescriptorProtoType.TYPE_FIXED32,  # 7
    FieldDescriptorProtoType.TYPE_BOOL,  # 8
    FieldDescriptorProtoType.TYPE_UINT32,  # 13
    FieldDescriptorProtoType.TYPE_SFIXED32,  # 15
    FieldDescriptorProtoType.TYPE_SFIXED64,  # 16
    FieldDescriptorProtoType.TYPE_SINT32,  # 17
    FieldDescriptorProtoType.TYPE_SINT64,  # 18
)

PYTHON_RESERVED = {
    "False",
    "None",
    "True",
    "and",
    "as",
    "async",
    "await",
    "assert",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "finally",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "try",
    "while",
    "with",
    "yield",
}

PROTO_ENUM_RESERVED = {
    "Name",
    "Value",
    "keys",
    "values",
    "items",
}


def get_field_type_name(proto_type: int):
    return FieldDescriptorProtoType(proto_type).name.upper().replace("TYPE_", "")


class Descriptors(object):
    def __init__(self, request: plugin_pb2.CodeGeneratorRequest) -> None:
        files = {f.name: f for f in request.proto_file}
        to_generate = {n: files[n] for n in request.file_to_generate}
        self.files: Dict[str, d.FileDescriptorProto] = files
        self.to_generate: Dict[str, d.FileDescriptorProto] = to_generate
        self.messages: Dict[str, d.DescriptorProto] = {}
        self.message_to_fd: Dict[str, d.FileDescriptorProto] = {}

        def _add_enums(
            enums: "RepeatedCompositeFieldContainer[d.EnumDescriptorProto]",
            prefix: str,
            _fd: d.FileDescriptorProto,
        ) -> None:
            for enum in enums:
                self.message_to_fd[prefix + enum.name] = _fd
                self.message_to_fd[prefix + enum.name + ".ValueType"] = _fd

        def _add_messages(
            messages: "RepeatedCompositeFieldContainer[d.DescriptorProto]",
            prefix: str,
            _fd: d.FileDescriptorProto,
        ) -> None:
            for message in messages:
                self.messages[prefix + message.name] = message
                self.message_to_fd[prefix + message.name] = _fd
                sub_prefix = prefix + message.name + "."
                _add_messages(message.nested_type, sub_prefix, _fd)
                _add_enums(message.enum_type, sub_prefix, _fd)

        for fd in request.proto_file:
            start_prefix = "." + fd.package + "." if fd.package else "."
            _add_messages(fd.message_type, start_prefix, fd)
            _add_enums(fd.enum_type, start_prefix, fd)


class PkgWriter(object):
    """Writes a single pyi file"""

    def __init__(
        self,
        fd: d.FileDescriptorProto,
        descriptors: Descriptors,
        readable_stubs: bool,
        relax_strict_optional_primitives: bool,
        grpc: bool,
    ) -> None:
        self.fd = fd
        self.descriptors = descriptors
        self.readable_stubs = readable_stubs
        self.relax_strict_optional_primitives = relax_strict_optional_primitives
        self.grpc = grpc
        self.lines: List[str] = []
        self.indent = ""

        # Set of {x}, where {x} corresponds to to `import {x}`
        self.imports: Set[str] = set()
        # dictionary of x->(y,z) for `from {x} import {y} as {z}`
        # if {z} is None, then it shortens to `from {x} import {y}`
        self.from_imports: Dict[str, Set[Tuple[str, Optional[str]]]] = defaultdict(set)

        # Comments
        self.source_code_info_by_scl = {
            tuple(location.path): location for location in fd.source_code_info.location
        }

    def _import(self, path: str, name: str) -> str:
        """Imports a stdlib path and returns a handle to it
        eg. self._import("typing", "Optional") -> "Optional"
        """
        imp = path.replace("/", ".")
        if imp == "google.protobuf.timestamp":
            imp += "_pb2"
        if self.readable_stubs:
            self.from_imports[imp].add((name, None))
            return name
        else:
            self.imports.add(imp)
            return ".".join((imp + "." + name).split(".")[-2:])

    def _import_message(self, name: str) -> str:
        """Import a referenced message and return a handle"""
        message_fd = self.descriptors.message_to_fd[name]
        assert message_fd.name.endswith(".proto")

        # Strip off package name
        if message_fd.package:
            assert name.startswith("." + message_fd.package + ".")
            name = name[len("." + message_fd.package + ".") :]
        else:
            assert name.startswith(".")
            name = name[1:]

        # Use prepended "_r_" to disambiguate message names that alias python reserved keywords
        split = name.split(".")
        for i, part in enumerate(split):
            if part in PYTHON_RESERVED:
                split[i] = part + "_"
        name = ".".join(split)

        # Message defined in this file. Note: GRPC stubs in same .proto are generated into separate files
        if not self.grpc and message_fd.name == self.fd.name:
            return name

        # Not in file. Must import
        # Python generated code ignores proto packages, so the only relevant factor is
        # whether it is in the file or not.
        import_name = self._import(message_fd.name[:-6].replace("-", "_"), split[0])

        remains = ".".join(split[1:])
        if not remains:
            return import_name

        # remains could either be a direct import of a nested enum or message
        # from another package.
        return import_name + "." + remains

    @contextmanager
    def _indent(self) -> Iterator[None]:
        self.indent = self.indent + "    "
        yield
        self.indent = self.indent[:-4]

    def _write_line(self, line: str, *args: Any) -> None:
        if args:
            line = line.format(*args)
        if line == "":
            self.lines.append(line)
        else:
            self.lines.append(self.indent + line)

    def _break_text(self, text_block: str) -> List[str]:
        if text_block == "":
            return []
        return [
            l[1:] if l.startswith(" ") else l for l in text_block.rstrip().split("\n")
        ]

    def _has_comments(self, scl: SourceCodeLocation) -> bool:
        sci_loc = self.source_code_info_by_scl.get(tuple(scl))
        return sci_loc is not None and bool(
            sci_loc.leading_detached_comments
            or sci_loc.leading_comments
            or sci_loc.trailing_comments
        )

    def _write_comments(self, scl: SourceCodeLocation) -> bool:
        """Return true if any comments were written"""
        if not self._has_comments(scl):
            return False

        sci_loc = self.source_code_info_by_scl.get(tuple(scl))
        assert sci_loc is not None

        lines = []
        for leading_detached_comment in sci_loc.leading_detached_comments:
            lines.extend(self._break_text(leading_detached_comment))
            lines.append("")
        if sci_loc.leading_comments is not None:
            lines.extend(self._break_text(sci_loc.leading_comments))
        # Trailing comments also go in the header - to make sure it gets into the docstring
        if sci_loc.trailing_comments is not None:
            lines.extend(self._break_text(sci_loc.trailing_comments))

        lines = [
            # Escape triple-quotes that would otherwise end the docstring early.
            line.replace("\\", "\\\\").replace('"""', r"\"\"\"")
            for line in lines
        ]
        if len(lines) == 1:
            line = lines[0]
            if line.endswith(('"', "\\")):
                # Docstrings are terminated with triple-quotes, so if the documentation itself ends in a quote,
                # insert some whitespace to separate it from the closing quotes.
                # This is not necessary with multiline comments
                # because in that case we always insert a newline before the trailing triple-quotes.
                line = line + " "
            self._write_line(f'"""{line}"""')
        else:
            for i, line in enumerate(lines):
                if i == 0:
                    self._write_line(f'"""{line}')
                else:
                    self._write_line(f"{line}")
            self._write_line('"""')

        return True

    def write_protomodule(self):
        l = self._write_line
        proto_module = self._import("proto", "module")
        l(f"__protobuf__ = {proto_module}(package=__name__)")
        l("")

    def write_enum_values(
        self,
        values: Iterable[Tuple[int, d.EnumValueDescriptorProto]],
        scl_prefix: SourceCodeLocation,
    ) -> None:
        for i, val in values:
            val_name = val.name
            if val_name in PYTHON_RESERVED:
                val_name += "_"

            scl = scl_prefix + [i]
            self._write_line(
                f"{val_name} = {val.number}",
            )
            if self._write_comments(scl):
                self._write_line("")  # Extra newline to separate

    def write_enums(
        self,
        enums: Iterable[d.EnumDescriptorProto],
        prefix: str,
        scl_prefix: SourceCodeLocation,
    ) -> None:
        l = self._write_line
        l("")
        for i, enum in enumerate(enums):
            class_name = (
                enum.name if enum.name not in PYTHON_RESERVED else enum.name + "_"
            )
            scl = scl_prefix + [i]

            enum_class = self._import("proto", "Enum")
            l(f"class {class_name}({enum_class}):")
            with self._indent():
                self._write_comments(scl)
                l("")
                self.write_enum_values(
                    enumerate(enum.value),
                    scl + [d.EnumDescriptorProto.VALUE_FIELD_NUMBER],
                )
            l("")

    def get_sorted_messages(
        self,
        messages: Iterable[d.DescriptorProto],
    ) -> Iterable[Tuple[int, d.DescriptorProto]]:
        score = defaultdict(int)

        def get_class_name(desc):
            return desc.name if desc.name not in PYTHON_RESERVED else desc.name + "_"

        for desc in messages:
            for field in desc.field:
                if field.type not in (
                    d.FieldDescriptorProto.TYPE_MESSAGE,
                    d.FieldDescriptorProto.TYPE_GROUP,
                ):
                    continue
                field_proto_type = self.python_type(field)
                if "." in field_proto_type:
                    continue
                class_name = get_class_name(desc)
                score[field_proto_type] += 1
                score[class_name] -= 1

        return sorted(
            enumerate(messages),
            reverse=True,
            key=lambda val: score[get_class_name(val[1])],
        )

    def write_messages(
        self,
        messages: Iterable[d.DescriptorProto],
        prefix: str,
        scl_prefix: SourceCodeLocation,
    ) -> None:
        l = self._write_line

        for i, desc in self.get_sorted_messages(messages):
            qualified_name = prefix + desc.name

            class_name = (
                desc.name if desc.name not in PYTHON_RESERVED else desc.name + "_"
            )
            message_class = self._import("proto", "Message")
            l(f"class {class_name}({message_class}):")
            with self._indent():
                scl = scl_prefix + [i]
                self._write_comments(scl)

                # Nested enums/messages
                self.write_enums(
                    desc.enum_type,
                    qualified_name + ".",
                    scl + [d.DescriptorProto.ENUM_TYPE_FIELD_NUMBER],
                )
                self.write_messages(
                    desc.nested_type,
                    qualified_name + ".",
                    scl + [d.DescriptorProto.NESTED_TYPE_FIELD_NUMBER],
                )

                for idx, field in enumerate(desc.field):
                    field_name = field.name
                    if field_name in PYTHON_RESERVED:
                        field_name += "_"
                    field_proto_type = self.python_type(field)
                    try:
                        oneof_name = desc.oneof_decl[field.oneof_index].name
                        oneof_name_arg = f', oneof="{oneof_name}"'
                        optional_arg = ", optional=True"
                    except IndexError:
                        oneof_name_arg = ""
                        optional_arg = ""

                    if field.label != d.FieldDescriptorProto.LABEL_REPEATED:
                        field_cls = self._import("proto", "Field")
                        # Scalar non repeated fields are r/w
                        l(
                            f"{field_name} = {field_cls}({field_proto_type}, number={field.number}{oneof_name_arg}{optional_arg})"
                        )
                        if self._write_comments(
                            scl + [d.DescriptorProto.FIELD_FIELD_NUMBER, idx]
                        ):
                            l("")
                    else:
                        # r/o Getters for non-scalar fields and scalar-repeated fields
                        scl_field = scl + [d.DescriptorProto.FIELD_FIELD_NUMBER, idx]
                        field_cls = self._import("proto", "RepeatedField")
                        l(
                            f"{field_name} = {field_cls}({field_proto_type}, number={field.number}{oneof_name_arg}{optional_arg})"
                        )
                        if self._has_comments(scl_field):
                            self._write_comments(scl_field)
                            l("")

            l("")

    def write_methods(
        self,
        service: d.ServiceDescriptorProto,
        class_name: str,
        is_abstract: bool,
        scl_prefix: SourceCodeLocation,
    ) -> None:
        l = self._write_line
        l(
            "DESCRIPTOR: {}",
            self._import("google.protobuf.descriptor", "ServiceDescriptor"),
        )
        methods = [(i, m) for i, m in enumerate(service.method)]
        if not methods:
            l("pass")
        for i, method in methods:
            method_name = method.name
            if method_name in PYTHON_RESERVED:
                method_name += "_"
            if is_abstract:
                l("@{}", self._import("abc", "abstractmethod"))
            l(f"def {method_name}(")
            with self._indent():
                l(f"inst: {class_name},")
                l(
                    "rpc_controller: {},",
                    self._import("google.protobuf.service", "RpcController"),
                )
                l("request: {},", self._import_message(method.input_type))
                l(
                    "callback: {}[{}[[{}], None]]{},",
                    self._import("typing", "Optional"),
                    self._import("typing", "Callable"),
                    self._import_message(method.output_type),
                    "" if is_abstract else " = None",
                )

            scl_method = scl_prefix + [d.ServiceDescriptorProto.METHOD_FIELD_NUMBER, i]
            l(
                ") -> {}[{}]:{}",
                self._import("concurrent.futures", "Future"),
                self._import_message(method.output_type),
                " ..." if not self._has_comments(scl_method) else "",
            )
            if self._has_comments(scl_method):
                with self._indent():
                    self._write_comments(scl_method)
                    l("pass")

    def write_services(
        self,
        services: Iterable[d.ServiceDescriptorProto],
        scl_prefix: SourceCodeLocation,
    ) -> None:
        l = self._write_line
        for i, service in enumerate(services):
            scl = scl_prefix + [i]
            class_name = (
                service.name
                if service.name not in PYTHON_RESERVED
                else service.name + "_"
            )
            # The service definition interface
            l(
                "class {}({}, metaclass={}):",
                class_name,
                self._import("google.protobuf.service", "Service"),
                self._import("abc", "ABCMeta"),
            )
            with self._indent():
                self._write_comments(scl)
                self.write_methods(
                    service, class_name, is_abstract=True, scl_prefix=scl
                )

            # The stub client
            stub_class_name = service.name + "_Stub"
            l("class {}({}):", stub_class_name, class_name)
            with self._indent():
                self._write_comments(scl)
                l(
                    "def __init__(self, rpc_channel: {}) -> None: ...",
                    self._import("google.protobuf.service", "RpcChannel"),
                )
                self.write_methods(
                    service, stub_class_name, is_abstract=False, scl_prefix=scl
                )

    def _callable_type(
        self, method: d.MethodDescriptorProto
    ) -> Tuple[Optional[str], Optional[str]]:
        if method.client_streaming:
            if method.server_streaming:
                return (
                    self._import("typing", "Iterable"),
                    self._import("typing", "Iterable"),
                )
            else:
                return (
                    self._import("typing", "Iterable"),
                    None,
                )
        else:
            if method.server_streaming:
                return (
                    None,
                    self._import("typing", "Iterable"),
                )
            else:
                return (None, None)

    def _callable_type_tuple(
        self, method: d.MethodDescriptorProto
    ) -> Tuple[bool, bool]:
        if method.client_streaming:
            if method.server_streaming:
                return (
                    True,
                    True,
                )
            else:
                return (
                    True,
                    False,
                )
        else:
            if method.server_streaming:
                return (
                    False,
                    True,
                )
            else:
                return (False, False)

    def _input_type(
        self, method: d.MethodDescriptorProto, use_stream_iterator: bool = True
    ) -> str:
        result = self._import_message(method.input_type)
        if use_stream_iterator and method.client_streaming:
            result = f"{self._import('typing', 'Iterator')}[{result}]"
        return result

    def _output_type(
        self, method: d.MethodDescriptorProto, use_stream_iterator: bool = True
    ) -> str:
        result = self._import_message(method.output_type)
        if use_stream_iterator and method.server_streaming:
            result = f"{self._import('typing', 'Iterator')}[{result}]"
        return result

    def write_grpc_methods(
        self, service: d.ServiceDescriptorProto, scl_prefix: SourceCodeLocation
    ) -> None:
        l = self._write_line
        methods = [(i, m) for i, m in enumerate(service.method)]
        if not methods:
            l("pass")
            l("")
        for i, method in methods:
            method_name = method.name
            if method_name in PYTHON_RESERVED:
                method_name += "_"
            scl = scl_prefix + [d.ServiceDescriptorProto.METHOD_FIELD_NUMBER, i]

            l("@{}", self._import("abc", "abstractmethod"))
            l("def {}(self,", method_name)
            with self._indent():
                input_name = (
                    "request_iterator" if method.client_streaming else "request"
                )
                input_type = self._input_type(method)
                l(f"{input_name}: {input_type},")
                l("context: {},", self._import("grpc", "ServicerContext"))
            l(
                ") -> {}:{}",
                self._output_type(method),
                " ..." if not self._has_comments(scl) else "",
            ),
            if self._has_comments(scl):
                with self._indent():
                    self._write_comments(scl)
                    l("pass")
            l("")

    def write_grpc_stub_methods(
        self, service: d.ServiceDescriptorProto, scl_prefix: SourceCodeLocation
    ) -> None:
        l = self._write_line
        l("def __init__(self, channel, metadata):")
        with self._indent():
            methods = [(i, m) for i, m in enumerate(service.method)]
            if not methods:
                l("pass")
                l("")
            for i, method in methods:
                method_name = method.name
                if method_name in PYTHON_RESERVED:
                    method_name += "_"
                scl = scl_prefix + [d.ServiceDescriptorProto.METHOD_FIELD_NUMBER, i]

                py_method_name = camel_to_snake(method_name)
                request_serializer = self._input_type(method, False)
                response_deserializer = self._output_type(method, False)
                request_iterable, response_iterable = self._callable_type_tuple(method)
                input_type_method = "unary"
                output_type_method = "unary"
                if request_iterable:
                    input_type_method = "stream"
                if response_iterable:
                    output_type_method = "stream"

                path = f"/{self.fd.package}.{service.name}/{method.name}"
                l(
                    f"self.{py_method_name} = channel.{input_type_method}_{output_type_method}("
                )
                with self._indent():
                    l(f'"{path}",')
                    l(f"request_serializer={request_serializer}.serialize,")
                    l(f"response_deserializer={response_deserializer}.deserialize,")
                l(f")")
                self._write_comments(scl)
                l("")

    def write_grpc_services(
        self,
        services: Iterable[d.ServiceDescriptorProto],
        scl_prefix: SourceCodeLocation,
    ) -> None:
        l = self._write_line
        l("")
        for i, service in enumerate(services):
            service_name = service.name
            if service_name in PYTHON_RESERVED:
                service_name += "_"

            scl = scl_prefix + [i]

            # The stub client
            l(f"class {service_name}:")
            with self._indent():
                self._write_comments(scl)
                l("")
                self.write_grpc_stub_methods(service, scl)
            l("")

    def python_type(self, field: d.FieldDescriptorProto) -> str:
        """
        generic_container
          if set, type the field with generic interfaces. Eg.
          - Iterable[int] rather than RepeatedScalarFieldContainer[int]
          - Mapping[k, v] rather than MessageMap[k, v]
          Can be useful for input types (eg constructor)
        """

        mapping: Dict[d.FieldDescriptorProto.Type.V, Callable[[], str]] = {
            d.FieldDescriptorProto.TYPE_DOUBLE: lambda: self._import("proto", "DOUBLE"),
            d.FieldDescriptorProto.TYPE_FLOAT: lambda: self._import("proto", "FLOAT"),
            d.FieldDescriptorProto.TYPE_INT64: lambda: self._import("proto", "INT64"),
            d.FieldDescriptorProto.TYPE_UINT64: lambda: self._import("proto", "UINT64"),
            d.FieldDescriptorProto.TYPE_FIXED64: lambda: self._import(
                "proto", "FIXED64"
            ),
            d.FieldDescriptorProto.TYPE_SFIXED64: lambda: self._import(
                "proto", "SFIXED64"
            ),
            d.FieldDescriptorProto.TYPE_SINT64: lambda: self._import("proto", "SINT64"),
            d.FieldDescriptorProto.TYPE_INT32: lambda: self._import("proto", "INT32"),
            d.FieldDescriptorProto.TYPE_UINT32: lambda: self._import("proto", "UINT32"),
            d.FieldDescriptorProto.TYPE_FIXED32: lambda: self._import(
                "proto", "FIXED32"
            ),
            d.FieldDescriptorProto.TYPE_SFIXED32: lambda: self._import(
                "proto", "SFIXED32"
            ),
            d.FieldDescriptorProto.TYPE_SINT32: lambda: self._import("proto", "SINT32"),
            d.FieldDescriptorProto.TYPE_BOOL: lambda: self._import("proto", "BOOL"),
            d.FieldDescriptorProto.TYPE_STRING: lambda: self._import("proto", "STRING"),
            d.FieldDescriptorProto.TYPE_BYTES: lambda: self._import("proto", "BYTES"),
            d.FieldDescriptorProto.TYPE_ENUM: lambda: self._import_message(
                field.type_name
            ),
            d.FieldDescriptorProto.TYPE_MESSAGE: lambda: self._import_message(
                field.type_name
            ),
            d.FieldDescriptorProto.TYPE_GROUP: lambda: self._import_message(
                field.type_name
            ),
        }

        assert field.type in mapping, "Unrecognized type: " + repr(field.type)
        field_type = mapping[field.type]()

        return field_type

    def write(self) -> str:
        for reexport_idx in self.fd.public_dependency:
            reexport_file = self.fd.dependency[reexport_idx]
            reexport_fd = self.descriptors.files[reexport_file]
            reexport_imp = (
                reexport_file[:-6].replace("-", "_").replace("/", ".") + "_pb2"
            )
            names = (
                [m.name for m in reexport_fd.message_type]
                + [m.name for m in reexport_fd.enum_type]
                + [v.name for m in reexport_fd.enum_type for v in m.value]
                + [m.name for m in reexport_fd.extension]
            )
            if reexport_fd.options.py_generic_services:
                names.extend(m.name for m in reexport_fd.service)

            if names:
                # n,n to force a reexport (from x import y as y)
                self.from_imports[reexport_imp].update((n, n) for n in names)

        import_lines = []
        for pkg in sorted(self.imports):
            *pkgs, mod = pkg.split(".")
            pkg_path = ".".join(pkgs)
            if not pkgs:
                import_lines.append(f"import {mod}")
            else:
                import_lines.append(f"from {pkg_path} import {mod}")

        import_lines = sorted(import_lines, key=lambda s: not s.startswith("import"))

        for pkg, items in sorted(self.from_imports.items()):
            import_lines.append(f"from {pkg} import (")
            for (name, reexport_name) in sorted(items):
                if reexport_name is None:
                    import_lines.append(f"    {name},")
                else:
                    import_lines.append(f"    {name} as {reexport_name},")
            import_lines.append(")\n")
        import_lines.append("")

        return "\n".join(import_lines + self.lines)


def is_scalar(fd: d.FieldDescriptorProto) -> bool:
    return not (
        fd.type == d.FieldDescriptorProto.TYPE_MESSAGE
        or fd.type == d.FieldDescriptorProto.TYPE_GROUP
    )


def generate_mypy_stubs(
    descriptors: Descriptors,
    response: plugin_pb2.CodeGeneratorResponse,
    quiet: bool,
    readable_stubs: bool,
    relax_strict_optional_primitives: bool,
) -> None:
    for name, fd in descriptors.to_generate.items():
        pkg_writer = PkgWriter(
            fd,
            descriptors,
            readable_stubs,
            relax_strict_optional_primitives,
            grpc=False,
        )
        pkg_writer.write_protomodule()
        pkg_writer.write_enums(
            fd.enum_type, "", [d.FileDescriptorProto.ENUM_TYPE_FIELD_NUMBER]
        )
        pkg_writer.write_messages(
            fd.message_type, "", [d.FileDescriptorProto.MESSAGE_TYPE_FIELD_NUMBER]
        )
        if fd.options.py_generic_services:
            pkg_writer.write_services(
                fd.service, [d.FileDescriptorProto.SERVICE_FIELD_NUMBER]
            )

        assert name == fd.name
        assert fd.name.endswith(".proto")
        output = response.file.add()
        output.name = fd.name[:-6].replace("-", "_").replace(".", "/") + ".py"
        output.content = HEADER + pkg_writer.write()
        if not quiet:
            print("Writing mypy to", output.name, file=sys.stderr)


def generate_mypy_grpc_stubs(
    descriptors: Descriptors,
    response: plugin_pb2.CodeGeneratorResponse,
    quiet: bool,
    readable_stubs: bool,
    relax_strict_optional_primitives: bool,
) -> None:
    for name, fd in descriptors.to_generate.items():
        pkg_writer = PkgWriter(
            fd,
            descriptors,
            readable_stubs,
            relax_strict_optional_primitives,
            grpc=True,
        )
        pkg_writer.write_grpc_services(
            fd.service, [d.FileDescriptorProto.SERVICE_FIELD_NUMBER]
        )

        assert name == fd.name
        assert fd.name.endswith(".proto")
        output = response.file.add()
        output.name = fd.name[:-6].replace("-", "_").replace(".", "/") + "_services.py"
        output.content = HEADER + pkg_writer.write()
        if not quiet:
            print("Writing mypy to", output.name, file=sys.stderr)


@contextmanager
def code_generation() -> Iterator[
    Tuple[plugin_pb2.CodeGeneratorRequest, plugin_pb2.CodeGeneratorResponse],
]:
    if len(sys.argv) > 1 and sys.argv[1] in ("-V", "--version"):
        print("ohmyproto " + __version__)
        sys.exit(0)

    # Read request message from stdin
    data = sys.stdin.buffer.read()

    # Parse request
    request = plugin_pb2.CodeGeneratorRequest()
    request.ParseFromString(data)

    # Create response
    response = plugin_pb2.CodeGeneratorResponse()

    # Declare support for optional proto3 fields
    response.supported_features |= (
        plugin_pb2.CodeGeneratorResponse.FEATURE_PROTO3_OPTIONAL
    )

    yield request, response

    # Serialise response message
    output = response.SerializeToString()

    # Write to stdout
    sys.stdout.buffer.write(output)


def main() -> None:
    # Generate mypy
    with code_generation() as (request, response):
        generate_mypy_stubs(
            Descriptors(request),
            response,
            "quiet" in request.parameter,
            "readable_stubs" in request.parameter,
            "relax_strict_optional_primitives" in request.parameter,
        )


def grpc() -> None:
    # Generate grpc mypy
    with code_generation() as (request, response):
        generate_mypy_grpc_stubs(
            Descriptors(request),
            response,
            "quiet" in request.parameter,
            "readable_stubs" in request.parameter,
            "relax_strict_optional_primitives" in request.parameter,
        )
