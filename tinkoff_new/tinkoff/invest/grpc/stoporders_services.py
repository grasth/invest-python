"""
DO NOT EDIT!
Generated by ohmyproto
isort:skip_file
"""
from tinkoff.invest.grpc import stoporders


class StopOrdersService:
    """Сервис предназначен для работы со стоп-заявками:</br> **1**.
    выставление;</br> **2**. отмена;</br> **3**. получение списка стоп-заявок.
    """

    def __init__(self, channel, metadata):
        self.post_stop_order = channel.unary_unary(
            "/tinkoff.public.invest.api.contract.v1.StopOrdersService/PostStopOrder",
            request_serializer=stoporders.PostStopOrderRequest.serialize,
            response_deserializer=stoporders.PostStopOrderResponse.deserialize,
        )
        """Метод выставления стоп-заявки."""

        self.get_stop_orders = channel.unary_unary(
            "/tinkoff.public.invest.api.contract.v1.StopOrdersService/GetStopOrders",
            request_serializer=stoporders.GetStopOrdersRequest.serialize,
            response_deserializer=stoporders.GetStopOrdersResponse.deserialize,
        )
        """Метод получения списка активных стоп заявок по счёту."""

        self.cancel_stop_order = channel.unary_unary(
            "/tinkoff.public.invest.api.contract.v1.StopOrdersService/CancelStopOrder",
            request_serializer=stoporders.CancelStopOrderRequest.serialize,
            response_deserializer=stoporders.CancelStopOrderResponse.deserialize,
        )
        """Метод отмены стоп-заявки."""

