"""
DO NOT EDIT!
Generated by ohmyproto
isort:skip_file
"""
import proto
from google.protobuf import timestamp_pb2
from tinkoff.invest.grpc import common

__protobuf__ = proto.module(package=__name__)


class OperationState(proto.Enum):
    """Статус запрашиваемых операций."""

    OPERATION_STATE_UNSPECIFIED = 0
    """Статус операции не определён"""

    OPERATION_STATE_EXECUTED = 1
    """Исполнена."""

    OPERATION_STATE_CANCELED = 2
    """Отменена."""

    OPERATION_STATE_PROGRESS = 3
    """Исполняется."""


class OperationType(proto.Enum):
    """Тип операции."""

    OPERATION_TYPE_UNSPECIFIED = 0
    """Тип операции не определён."""

    OPERATION_TYPE_INPUT = 1
    """Пополнение брокерского счёта."""

    OPERATION_TYPE_BOND_TAX = 2
    """Удержание НДФЛ по купонам."""

    OPERATION_TYPE_OUTPUT_SECURITIES = 3
    """Вывод ЦБ."""

    OPERATION_TYPE_OVERNIGHT = 4
    """Доход по сделке РЕПО овернайт."""

    OPERATION_TYPE_TAX = 5
    """Удержание налога."""

    OPERATION_TYPE_BOND_REPAYMENT_FULL = 6
    """Полное погашение облигаций."""

    OPERATION_TYPE_SELL_CARD = 7
    """Продажа ЦБ с карты."""

    OPERATION_TYPE_DIVIDEND_TAX = 8
    """Удержание налога по дивидендам."""

    OPERATION_TYPE_OUTPUT = 9
    """Вывод денежных средств."""

    OPERATION_TYPE_BOND_REPAYMENT = 10
    """Частичное погашение облигаций."""

    OPERATION_TYPE_TAX_CORRECTION = 11
    """Корректировка налога."""

    OPERATION_TYPE_SERVICE_FEE = 12
    """Удержание комиссии за обслуживание брокерского счёта."""

    OPERATION_TYPE_BENEFIT_TAX = 13
    """Удержание налога за материальную выгоду."""

    OPERATION_TYPE_MARGIN_FEE = 14
    """Удержание комиссии за непокрытую позицию."""

    OPERATION_TYPE_BUY = 15
    """Покупка ЦБ."""

    OPERATION_TYPE_BUY_CARD = 16
    """Покупка ЦБ с карты."""

    OPERATION_TYPE_INPUT_SECURITIES = 17
    """Перевод ценных бумаг из другого депозитария."""

    OPERATION_TYPE_SELL_MARGIN = 18
    """Продажа в результате Margin-call."""

    OPERATION_TYPE_BROKER_FEE = 19
    """Удержание комиссии за операцию."""

    OPERATION_TYPE_BUY_MARGIN = 20
    """Покупка в результате Margin-call."""

    OPERATION_TYPE_DIVIDEND = 21
    """Выплата дивидендов."""

    OPERATION_TYPE_SELL = 22
    """Продажа ЦБ."""

    OPERATION_TYPE_COUPON = 23
    """Выплата купонов."""

    OPERATION_TYPE_SUCCESS_FEE = 24
    """Удержание комиссии SuccessFee."""

    OPERATION_TYPE_DIVIDEND_TRANSFER = 25
    """Передача дивидендного дохода."""

    OPERATION_TYPE_ACCRUING_VARMARGIN = 26
    """Зачисление вариационной маржи."""

    OPERATION_TYPE_WRITING_OFF_VARMARGIN = 27
    """Списание вариационной маржи."""

    OPERATION_TYPE_DELIVERY_BUY = 28
    """Покупка в рамках экспирации фьючерсного контракта."""

    OPERATION_TYPE_DELIVERY_SELL = 29
    """Продажа в рамках экспирации фьючерсного контракта."""

    OPERATION_TYPE_TRACK_MFEE = 30
    """Комиссия за управление по счёту автоследования."""

    OPERATION_TYPE_TRACK_PFEE = 31
    """Комиссия за результат по счёту автоследования."""

    OPERATION_TYPE_TAX_PROGRESSIVE = 32
    """Удержание налога по ставке 15%."""

    OPERATION_TYPE_BOND_TAX_PROGRESSIVE = 33
    """Удержание налога по купонам по ставке 15%."""

    OPERATION_TYPE_DIVIDEND_TAX_PROGRESSIVE = 34
    """Удержание налога по дивидендам по ставке 15%."""

    OPERATION_TYPE_BENEFIT_TAX_PROGRESSIVE = 35
    """Удержание налога за материальную выгоду по ставке 15%."""

    OPERATION_TYPE_TAX_CORRECTION_PROGRESSIVE = 36
    """Корректировка налога по ставке 15%."""

    OPERATION_TYPE_TAX_REPO_PROGRESSIVE = 37
    """Удержание налога за возмещение по сделкам РЕПО по ставке 15%."""

    OPERATION_TYPE_TAX_REPO = 38
    """Удержание налога за возмещение по сделкам РЕПО."""

    OPERATION_TYPE_TAX_REPO_HOLD = 39
    """Удержание налога по сделкам РЕПО."""

    OPERATION_TYPE_TAX_REPO_REFUND = 40
    """Возврат налога по сделкам РЕПО."""

    OPERATION_TYPE_TAX_REPO_HOLD_PROGRESSIVE = 41
    """Удержание налога по сделкам РЕПО по ставке 15%."""

    OPERATION_TYPE_TAX_REPO_REFUND_PROGRESSIVE = 42
    """Возврат налога по сделкам РЕПО по ставке 15%."""

    OPERATION_TYPE_DIV_EXT = 43
    """Выплата дивидендов на карту."""

    OPERATION_TYPE_TAX_CORRECTION_COUPON = 44
    """Корректировка налога по купонам."""

    OPERATION_TYPE_CASH_FEE = 45
    """Комиссия за валютный остаток."""

    OPERATION_TYPE_OUT_FEE = 46
    """Комиссия за вывод валюты с брокерского счета."""

    OPERATION_TYPE_OUT_STAMP_DUTY = 47
    """Гербовый сбор."""

    OPERATION_TYPE_OUTPUT_SWIFT = 50
    """	SWIFT-перевод"""

    OPERATION_TYPE_INPUT_SWIFT = 51
    """	SWIFT-перевод"""

    OPERATION_TYPE_OUTPUT_ACQUIRING = 53
    """ Перевод на карту"""

    OPERATION_TYPE_INPUT_ACQUIRING = 54
    """	Перевод с карты"""

    OPERATION_TYPE_OUTPUT_PENALTY = 55
    """	Комиссия за вывод средств"""

    OPERATION_TYPE_ADVICE_FEE = 56
    """	Списание оплаты за сервис Советов"""

    OPERATION_TYPE_TRANS_IIS_BS = 57
    """ Перевод ценных бумаг с ИИС на Брокерский счет"""

    OPERATION_TYPE_TRANS_BS_BS = 58
    """ Перевод ценных бумаг с одного брокерского счета на другой"""

    OPERATION_TYPE_OUT_MULTI = 59
    """ Вывод денежных средств со счета"""

    OPERATION_TYPE_INP_MULTI = 60
    """ Пополнение денежных средств со счета"""

    OPERATION_TYPE_OVER_PLACEMENT = 61
    """ Размещение биржевого овернайта"""

    OPERATION_TYPE_OVER_COM = 62
    """ Списание комиссии"""

    OPERATION_TYPE_OVER_INCOME = 63
    """ Доход от оверанайта"""

    OPERATION_TYPE_OPTION_EXPIRATION = 64
    """Экспирация"""


class PortfolioSubscriptionStatus(proto.Enum):
    """Результат подписки."""

    PORTFOLIO_SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    """Тип не определён."""

    PORTFOLIO_SUBSCRIPTION_STATUS_SUCCESS = 1
    """Успешно."""

    PORTFOLIO_SUBSCRIPTION_STATUS_ACCOUNT_NOT_FOUND = 2
    """Счёт не найден или недостаточно прав."""

    PORTFOLIO_SUBSCRIPTION_STATUS_INTERNAL_ERROR = 3
    """Произошла ошибка."""


class InstrumentType(proto.Enum):
    """Тип инструмента."""

    INSTRUMENT_TYPE_UNSPECIFIED = 0
    INSTRUMENT_TYPE_BOND = 1
    """Облигация."""

    INSTRUMENT_TYPE_SHARE = 2
    """Акция."""

    INSTRUMENT_TYPE_CURRENCY = 3
    """Валюта."""

    INSTRUMENT_TYPE_ETF = 4
    """Exchange-traded fund. Фонд."""

    INSTRUMENT_TYPE_FUTURES = 5
    """Фьючерс."""

    INSTRUMENT_TYPE_SP = 6
    """Структурная нота."""

    INSTRUMENT_TYPE_OPTION = 7
    """Опцион."""


class PositionsAccountSubscriptionStatus(proto.Enum):
    """Результат подписки."""

    POSITIONS_SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    """Тип не определён."""

    POSITIONS_SUBSCRIPTION_STATUS_SUCCESS = 1
    """Успешно."""

    POSITIONS_SUBSCRIPTION_STATUS_ACCOUNT_NOT_FOUND = 2
    """Счёт не найден или недостаточно прав."""

    POSITIONS_SUBSCRIPTION_STATUS_INTERNAL_ERROR = 3
    """Произошла ошибка."""


class PositionsSecurities(proto.Message):
    """Баланс позиции ценной бумаги."""

    figi = proto.Field(proto.STRING, number=1)
    """Figi-идентификатор бумаги."""

    blocked = proto.Field(proto.INT64, number=2)
    """Заблокировано."""

    balance = proto.Field(proto.INT64, number=3)
    """Текущий незаблокированный баланс."""

    position_uid = proto.Field(proto.STRING, number=4)
    """Уникальный идентификатор позиции."""

    instrument_uid = proto.Field(proto.STRING, number=5)
    """Уникальный идентификатор  инструмента."""

    exchange_blocked = proto.Field(proto.BOOL, number=11)
    """Заблокировано на бирже."""

    instrument_type = proto.Field(proto.STRING, number=16)
    """Тип инструмента."""


class PositionsFutures(proto.Message):
    """Баланс фьючерса."""

    figi = proto.Field(proto.STRING, number=1)
    """Figi-идентификатор фьючерса."""

    blocked = proto.Field(proto.INT64, number=2)
    """Заблокировано."""

    balance = proto.Field(proto.INT64, number=3)
    """Текущий незаблокированный баланс."""

    position_uid = proto.Field(proto.STRING, number=4)
    """Уникальный идентификатор позиции."""

    instrument_uid = proto.Field(proto.STRING, number=5)
    """Уникальный идентификатор  инструмента."""


class PositionsOptions(proto.Message):
    """Баланс опциона."""

    position_uid = proto.Field(proto.STRING, number=1)
    """Уникальный идентификатор позиции опциона."""

    instrument_uid = proto.Field(proto.STRING, number=2)
    """Уникальный идентификатор  инструмента."""

    blocked = proto.Field(proto.INT64, number=11)
    """Заблокировано."""

    balance = proto.Field(proto.INT64, number=21)
    """Текущий незаблокированный баланс."""


class OperationTrade(proto.Message):
    """Сделка по операции."""

    trade_id = proto.Field(proto.STRING, number=1)
    """Идентификатор сделки."""

    date_time = proto.Field(timestamp_pb2.Timestamp, number=2)
    """Дата и время сделки в часовом поясе UTC."""

    quantity = proto.Field(proto.INT64, number=3)
    """Количество инструментов."""

    price = proto.Field(common.MoneyValue, number=4)
    """Цена за 1 инструмент. Для получения стоимости лота требуется умножить на лотность инструмента."""


class PortfolioPosition(proto.Message):
    """Позиции портфеля."""

    figi = proto.Field(proto.STRING, number=1)
    """Figi-идентификатора инструмента."""

    instrument_type = proto.Field(proto.STRING, number=2)
    """Тип инструмента."""

    quantity = proto.Field(common.Quotation, number=3)
    """Количество инструмента в портфеле в штуках."""

    average_position_price = proto.Field(common.MoneyValue, number=4)
    """Средневзвешенная цена позиции. **Возможна задержка до секунды для пересчёта**."""

    expected_yield = proto.Field(common.Quotation, number=5)
    """Текущая рассчитанная доходность позиции."""

    current_nkd = proto.Field(common.MoneyValue, number=6)
    """Текущий НКД."""

    average_position_price_pt = proto.Field(common.Quotation, number=7)
    """Deprecated Средняя цена позиции в пунктах (для фьючерсов). **Возможна задержка до секунды для пересчёта**."""

    current_price = proto.Field(common.MoneyValue, number=8)
    """Текущая цена за 1 инструмент. Для получения стоимости лота требуется умножить на лотность инструмента.."""

    average_position_price_fifo = proto.Field(common.MoneyValue, number=9)
    """Средняя цена позиции по методу FIFO. **Возможна задержка до секунды для пересчёта**."""

    quantity_lots = proto.Field(common.Quotation, number=10)
    """Deprecated Количество лотов в портфеле."""

    blocked = proto.Field(proto.BOOL, number=21)
    """Заблокировано."""

    position_uid = proto.Field(proto.STRING, number=24)
    """position_uid-идентификатора инструмента"""

    instrument_uid = proto.Field(proto.STRING, number=25)
    """instrument_uid-идентификатора инструмента"""

    var_margin = proto.Field(common.MoneyValue, number=26)
    """Вариационная маржа"""

    expected_yield_fifo = proto.Field(common.Quotation, number=27)
    """Текущая рассчитанная доходность позиции."""


class VirtualPortfolioPosition(proto.Message):

    position_uid = proto.Field(proto.STRING, number=1)
    """position_uid-идентификатора инструмента"""

    instrument_uid = proto.Field(proto.STRING, number=2)
    """instrument_uid-идентификатора инструмента"""

    figi = proto.Field(proto.STRING, number=3)
    """Figi-идентификатора инструмента."""

    instrument_type = proto.Field(proto.STRING, number=4)
    """Тип инструмента."""

    quantity = proto.Field(common.Quotation, number=5)
    """Количество инструмента в портфеле в штуках."""

    average_position_price = proto.Field(common.MoneyValue, number=6)
    """Средневзвешенная цена позиции. **Возможна задержка до секунды для пересчёта**."""

    expected_yield = proto.Field(common.Quotation, number=7)
    """Текущая рассчитанная доходность позиции."""

    expected_yield_fifo = proto.Field(common.Quotation, number=8)
    """Текущая рассчитанная доходность позиции."""

    expire_date = proto.Field(timestamp_pb2.Timestamp, number=9)
    """Дата до которой нужно продать виртуальные бумаги, после этой даты виртуальная позиция "сгорит" """

    current_price = proto.Field(common.MoneyValue, number=10)
    """Текущая цена за 1 инструмент. Для получения стоимости лота требуется умножить на лотность инструмента.."""

    average_position_price_fifo = proto.Field(common.MoneyValue, number=11)
    """Средняя цена позиции по методу FIFO. **Возможна задержка до секунды для пересчёта**."""


class GenerateBrokerReportRequest(proto.Message):

    account_id = proto.Field(proto.STRING, number=1)
    """Идентификатор счёта клиента."""

    from_ = proto.Field(timestamp_pb2.Timestamp, number=2)
    """Начало периода в часовом поясе UTC."""

    to = proto.Field(timestamp_pb2.Timestamp, number=3)
    """Окончание периода в часовом поясе UTC."""


class GenerateBrokerReportResponse(proto.Message):

    task_id = proto.Field(proto.STRING, number=1)
    """Идентификатор задачи формирования брокерского отчёта."""


class GetBrokerReportRequest(proto.Message):

    task_id = proto.Field(proto.STRING, number=1)
    """Идентификатор задачи формирования брокерского отчёта."""

    page = proto.Field(proto.INT32, number=2)
    """Номер страницы отчета (начинается с 1), значение по умолчанию: 0."""


class BrokerReport(proto.Message):

    trade_id = proto.Field(proto.STRING, number=1)
    """Номер сделки."""

    order_id = proto.Field(proto.STRING, number=2)
    """Номер поручения."""

    figi = proto.Field(proto.STRING, number=3)
    """Figi-идентификатор инструмента."""

    execute_sign = proto.Field(proto.STRING, number=4)
    """Признак исполнения."""

    trade_datetime = proto.Field(timestamp_pb2.Timestamp, number=5)
    """Дата и время заключения в часовом поясе UTC."""

    exchange = proto.Field(proto.STRING, number=6)
    """Торговая площадка."""

    class_code = proto.Field(proto.STRING, number=7)
    """Режим торгов."""

    direction = proto.Field(proto.STRING, number=8)
    """Вид сделки."""

    name = proto.Field(proto.STRING, number=9)
    """Сокращённое наименование актива."""

    ticker = proto.Field(proto.STRING, number=10)
    """Код актива."""

    price = proto.Field(common.MoneyValue, number=11)
    """Цена за единицу."""

    quantity = proto.Field(proto.INT64, number=12)
    """Количество."""

    order_amount = proto.Field(common.MoneyValue, number=13)
    """Сумма (без НКД)."""

    aci_value = proto.Field(common.Quotation, number=14)
    """НКД."""

    total_order_amount = proto.Field(common.MoneyValue, number=15)
    """Сумма сделки."""

    broker_commission = proto.Field(common.MoneyValue, number=16)
    """Комиссия брокера."""

    exchange_commission = proto.Field(common.MoneyValue, number=17)
    """Комиссия биржи."""

    exchange_clearing_commission = proto.Field(common.MoneyValue, number=18)
    """Комиссия клир. центра."""

    repo_rate = proto.Field(common.Quotation, number=19)
    """Ставка РЕПО (%)."""

    party = proto.Field(proto.STRING, number=20)
    """Контрагент/Брокер."""

    clear_value_date = proto.Field(timestamp_pb2.Timestamp, number=21)
    """Дата расчётов в часовом поясе UTC."""

    sec_value_date = proto.Field(timestamp_pb2.Timestamp, number=22)
    """Дата поставки в часовом поясе UTC."""

    broker_status = proto.Field(proto.STRING, number=23)
    """Статус брокера."""

    separate_agreement_type = proto.Field(proto.STRING, number=24)
    """Тип дог."""

    separate_agreement_number = proto.Field(proto.STRING, number=25)
    """Номер дог."""

    separate_agreement_date = proto.Field(proto.STRING, number=26)
    """Дата дог."""

    delivery_type = proto.Field(proto.STRING, number=27)
    """Тип расчёта по сделке."""


class GenerateDividendsForeignIssuerReportRequest(proto.Message):
    """Объект запроса формирования отчёта "Справка о доходах за пределами РФ"."""

    account_id = proto.Field(proto.STRING, number=1)
    """Идентификатор счёта клиента."""

    from_ = proto.Field(timestamp_pb2.Timestamp, number=2)
    """Начало периода (по UTC)."""

    to = proto.Field(timestamp_pb2.Timestamp, number=3)
    """Окончание периода (по UTC)."""


class GetDividendsForeignIssuerReportRequest(proto.Message):
    """Объект запроса сформированного отчёта "Справка о доходах за пределами РФ"."""

    task_id = proto.Field(proto.STRING, number=1)
    """Идентификатор задачи формирования отчёта."""

    page = proto.Field(proto.INT32, number=2)
    """Номер страницы отчета (начинается с 0), значение по умолчанию: 0."""


class GenerateDividendsForeignIssuerReportResponse(proto.Message):
    """Объект результата задачи запуска формирования отчёта "Справка о доходах за пределами РФ"."""

    task_id = proto.Field(proto.STRING, number=1)
    """Идентификатор задачи формирования отчёта."""


class DividendsForeignIssuerReport(proto.Message):
    """Отчёт "Справка о доходах за пределами РФ"."""

    record_date = proto.Field(timestamp_pb2.Timestamp, number=1)
    """Дата фиксации реестра."""

    payment_date = proto.Field(timestamp_pb2.Timestamp, number=2)
    """Дата выплаты."""

    security_name = proto.Field(proto.STRING, number=3)
    """Наименование ценной бумаги."""

    isin = proto.Field(proto.STRING, number=4)
    """ISIN-идентификатор ценной бумаги."""

    issuer_country = proto.Field(proto.STRING, number=5)
    """Страна эмитента. Для депозитарных расписок указывается страна эмитента базового актива."""

    quantity = proto.Field(proto.INT64, number=6)
    """Количество ценных бумаг."""

    dividend = proto.Field(common.Quotation, number=7)
    """Выплаты на одну бумагу"""

    external_commission = proto.Field(common.Quotation, number=8)
    """Комиссия внешних платёжных агентов."""

    dividend_gross = proto.Field(common.Quotation, number=9)
    """Сумма до удержания налога."""

    tax = proto.Field(common.Quotation, number=10)
    """Сумма налога, удержанного агентом."""

    dividend_amount = proto.Field(common.Quotation, number=11)
    """Итоговая сумма выплаты."""

    currency = proto.Field(proto.STRING, number=12)
    """Валюта."""


class AccountSubscriptionStatus(proto.Message):
    """Счет клиента."""

    account_id = proto.Field(proto.STRING, number=1)
    """Идентификатор счёта"""

    subscription_status = proto.Field(PortfolioSubscriptionStatus, number=6)
    """Результат подписки."""


class OperationItemTrade(proto.Message):
    """Сделка по операции."""

    num = proto.Field(proto.STRING, number=1)
    """Номер сделки"""

    date = proto.Field(timestamp_pb2.Timestamp, number=6)
    """Дата сделки"""

    quantity = proto.Field(proto.INT64, number=11)
    """Количество в единицах."""

    price = proto.Field(common.MoneyValue, number=16)
    """Цена."""

    yield_ = proto.Field(common.MoneyValue, number=21)
    """Доходность."""

    yield_relative = proto.Field(common.Quotation, number=22)
    """Относительная доходность."""


class PositionsSubscriptionStatus(proto.Message):
    """Счет клиента."""

    account_id = proto.Field(proto.STRING, number=1)
    """Идентификатор счёта"""

    subscription_status = proto.Field(PositionsAccountSubscriptionStatus, number=6)
    """Результат подписки."""


class PositionsMoney(proto.Message):
    """Валютная позиция портфеля."""

    available_value = proto.Field(common.MoneyValue, number=1)
    """Доступное количество валютный позиций."""

    blocked_value = proto.Field(common.MoneyValue, number=2)
    """Заблокированное количество валютный позиций."""


class OperationsRequest(proto.Message):
    """Запрос получения списка операций по счёту."""

    account_id = proto.Field(proto.STRING, number=1)
    """Идентификатор счёта клиента."""

    from_ = proto.Field(timestamp_pb2.Timestamp, number=2)
    """Начало периода (по UTC)."""

    to = proto.Field(timestamp_pb2.Timestamp, number=3)
    """Окончание периода (по UTC)."""

    state = proto.Field(OperationState, number=4)
    """Статус запрашиваемых операций."""

    figi = proto.Field(proto.STRING, number=5)
    """Figi-идентификатор инструмента для фильтрации."""


class Operation(proto.Message):
    """Данные по операции."""

    id = proto.Field(proto.STRING, number=1)
    """Идентификатор операции."""

    parent_operation_id = proto.Field(proto.STRING, number=2)
    """Идентификатор родительской операции."""

    currency = proto.Field(proto.STRING, number=3)
    """Валюта операции."""

    payment = proto.Field(common.MoneyValue, number=4)
    """Сумма операции."""

    price = proto.Field(common.MoneyValue, number=5)
    """Цена операции за 1 инструмент. Для получения стоимости лота требуется умножить на лотность инструмента."""

    state = proto.Field(OperationState, number=6)
    """Статус операции."""

    quantity = proto.Field(proto.INT64, number=7)
    """Количество единиц инструмента."""

    quantity_rest = proto.Field(proto.INT64, number=8)
    """Неисполненный остаток по сделке."""

    figi = proto.Field(proto.STRING, number=9)
    """Figi-идентификатор инструмента, связанного с операцией."""

    instrument_type = proto.Field(proto.STRING, number=10)
    """Тип инструмента. Возможные значения: </br>**bond** — облигация; </br>**share** — акция; </br>**currency** — валюта; </br>**etf** — фонд; </br>**futures** — фьючерс."""

    date = proto.Field(timestamp_pb2.Timestamp, number=11)
    """Дата и время операции в формате часовом поясе UTC."""

    type = proto.Field(proto.STRING, number=12)
    """Текстовое описание типа операции."""

    operation_type = proto.Field(OperationType, number=13)
    """Тип операции."""

    trades = proto.RepeatedField(OperationTrade, number=14)
    """Массив сделок."""

    asset_uid = proto.Field(proto.STRING, number=16)
    """Идентификатор актива"""


class PortfolioRequest(proto.Message):
    """Запрос получения текущего портфеля по счёту."""

    class CurrencyRequest(proto.Enum):

        RUB = 0
        """Рубли"""

        USD = 1
        """Доллары"""

        EUR = 2
        """Евро"""


    account_id = proto.Field(proto.STRING, number=1)
    """Идентификатор счёта пользователя."""

    currency = proto.Field(PortfolioRequest.CurrencyRequest, number=2)
    """Валюта, в которой требуется рассчитать портфель"""


class PositionsRequest(proto.Message):
    """Запрос позиций портфеля по счёту."""

    account_id = proto.Field(proto.STRING, number=1)
    """Идентификатор счёта пользователя."""


class WithdrawLimitsRequest(proto.Message):
    """Запрос доступного для вывода остатка."""

    account_id = proto.Field(proto.STRING, number=1)
    """Идентификатор счёта пользователя."""


class WithdrawLimitsResponse(proto.Message):
    """Доступный для вывода остаток."""

    money = proto.RepeatedField(common.MoneyValue, number=1)
    """Массив валютных позиций портфеля."""

    blocked = proto.RepeatedField(common.MoneyValue, number=2)
    """Массив заблокированных валютных позиций портфеля."""

    blocked_guarantee = proto.RepeatedField(common.MoneyValue, number=3)
    """Заблокировано под гарантийное обеспечение фьючерсов."""


class GetBrokerReportResponse(proto.Message):

    broker_report = proto.RepeatedField(BrokerReport, number=1)
    itemsCount = proto.Field(proto.INT32, number=2)
    """Количество записей в отчете."""

    pagesCount = proto.Field(proto.INT32, number=3)
    """Количество страниц с данными отчета (начинается с 0)."""

    page = proto.Field(proto.INT32, number=4)
    """Текущая страница (начинается с 0)."""


class GetDividendsForeignIssuerReportResponse(proto.Message):

    dividends_foreign_issuer_report = proto.RepeatedField(DividendsForeignIssuerReport, number=1)
    itemsCount = proto.Field(proto.INT32, number=2)
    """Количество записей в отчете."""

    pagesCount = proto.Field(proto.INT32, number=3)
    """Количество страниц с данными отчета (начинается с 0)."""

    page = proto.Field(proto.INT32, number=4)
    """Текущая страница (начинается с 0)."""


class PortfolioStreamRequest(proto.Message):
    """Запрос установки stream-соединения."""

    accounts = proto.RepeatedField(proto.STRING, number=1)
    """Массив идентификаторов счётов пользователя"""


class PortfolioSubscriptionResult(proto.Message):
    """Объект результата подписки."""

    accounts = proto.RepeatedField(AccountSubscriptionStatus, number=1)
    """Массив счетов клиента."""


class GetOperationsByCursorRequest(proto.Message):
    """Запрос списка операций по счёту с пагинацией."""

    account_id = proto.Field(proto.STRING, number=1)
    """Идентификатор счёта клиента. Обязательный параметр для данного метода, остальные параметры опциональны."""

    instrument_id = proto.Field(proto.STRING, number=2)
    """Идентификатор инструмента (Figi инструмента или uid инструмента)"""

    from_ = proto.Field(timestamp_pb2.Timestamp, number=6)
    """Начало периода (по UTC)."""

    to = proto.Field(timestamp_pb2.Timestamp, number=7)
    """Окончание периода (по UTC)."""

    cursor = proto.Field(proto.STRING, number=11)
    """Идентификатор элемента, с которого начать формировать ответ."""

    limit = proto.Field(proto.INT32, number=12)
    """Лимит количества операций. По умолчанию устанавливается значение **100**, максимальное значение 1000."""

    operation_types = proto.RepeatedField(OperationType, number=13)
    """Тип операции. Принимает значение из списка OperationType."""

    state = proto.Field(OperationState, number=14)
    """Статус запрашиваемых операций, возможные значения указаны в OperationState."""

    without_commissions = proto.Field(proto.BOOL, number=15)
    """Флаг возвращать ли комиссии, по умолчанию false"""

    without_trades = proto.Field(proto.BOOL, number=16)
    """Флаг получения ответа без массива сделок."""

    without_overnights = proto.Field(proto.BOOL, number=17)
    """Флаг не показывать overnight операций."""


class OperationItem(proto.Message):
    """Данные об операции."""

    cursor = proto.Field(proto.STRING, number=1)
    """Курсор."""

    broker_account_id = proto.Field(proto.STRING, number=6)
    """Номер счета клиента."""

    id = proto.Field(proto.STRING, number=16)
    """Идентификатор операции, может меняться с течением времени."""

    parent_operation_id = proto.Field(proto.STRING, number=17)
    """Идентификатор родительской операции, может измениться, если изменился id родительской операции."""

    name = proto.Field(proto.STRING, number=18)
    """Название операции."""

    date = proto.Field(timestamp_pb2.Timestamp, number=21)
    """Дата поручения."""

    type = proto.Field(OperationType, number=22)
    """Тип операции."""

    description = proto.Field(proto.STRING, number=23)
    """Описание операции."""

    state = proto.Field(OperationState, number=24)
    """Статус поручения."""

    instrument_uid = proto.Field(proto.STRING, number=31)
    """Уникальный идентификатор инструмента."""

    figi = proto.Field(proto.STRING, number=32)
    """Figi."""

    instrument_type = proto.Field(proto.STRING, number=33)
    """Тип инструмента."""

    instrument_kind = proto.Field(InstrumentType, number=34)
    """Тип инструмента."""

    payment = proto.Field(common.MoneyValue, number=41)
    """Сумма операции."""

    price = proto.Field(common.MoneyValue, number=42)
    """Цена операции за 1 инструмент."""

    commission = proto.Field(common.MoneyValue, number=43)
    """Комиссия."""

    yield_ = proto.Field(common.MoneyValue, number=44)
    """Доходность."""

    yield_relative = proto.Field(common.Quotation, number=45)
    """Относительная доходность."""

    accrued_int = proto.Field(common.MoneyValue, number=46)
    """Накопленный купонный доход."""

    quantity = proto.Field(proto.INT64, number=51)
    """Количество единиц инструмента."""

    quantity_rest = proto.Field(proto.INT64, number=52)
    """Неисполненный остаток по сделке."""

    quantity_done = proto.Field(proto.INT64, number=53)
    """Исполненный остаток."""

    cancel_date_time = proto.Field(timestamp_pb2.Timestamp, number=56)
    """Дата и время снятия заявки."""

    cancel_reason = proto.Field(proto.STRING, number=57)
    """Причина отмены операции."""

    trades_info = proto.Field(OperationItemTrades, number=61)
    """Массив сделок."""

    asset_uid = proto.Field(proto.STRING, number=64)
    """Идентификатор актива"""


class OperationItemTrades(proto.Message):
    """Массив с информацией о сделках."""

    trades = proto.RepeatedField(OperationItemTrade, number=6)

class PositionsStreamRequest(proto.Message):
    """Запрос установки stream-соединения позиций."""

    accounts = proto.RepeatedField(proto.STRING, number=1)
    """Массив идентификаторов счётов пользователя"""


class PositionsSubscriptionResult(proto.Message):
    """Объект результата подписки."""

    accounts = proto.RepeatedField(PositionsSubscriptionStatus, number=1)
    """Массив счетов клиента."""


class OperationsResponse(proto.Message):
    """Список операций."""

    operations = proto.RepeatedField(Operation, number=1)
    """Массив операций."""


class PortfolioResponse(proto.Message):
    """Текущий портфель по счёту."""

    total_amount_shares = proto.Field(common.MoneyValue, number=1)
    """Общая стоимость акций в портфеле в рублях."""

    total_amount_bonds = proto.Field(common.MoneyValue, number=2)
    """Общая стоимость облигаций в портфеле в рублях."""

    total_amount_etf = proto.Field(common.MoneyValue, number=3)
    """Общая стоимость фондов в портфеле в рублях."""

    total_amount_currencies = proto.Field(common.MoneyValue, number=4)
    """Общая стоимость валют в портфеле в рублях."""

    total_amount_futures = proto.Field(common.MoneyValue, number=5)
    """Общая стоимость фьючерсов в портфеле в рублях."""

    expected_yield = proto.Field(common.Quotation, number=6)
    """Текущая относительная доходность портфеля, в %."""

    positions = proto.RepeatedField(PortfolioPosition, number=7)
    """Список позиций портфеля."""

    account_id = proto.Field(proto.STRING, number=8)
    """Идентификатор счёта пользователя."""

    total_amount_options = proto.Field(common.MoneyValue, number=9)
    """Общая стоимость опционов в портфеле в рублях."""

    total_amount_sp = proto.Field(common.MoneyValue, number=10)
    """Общая стоимость структурных нот в портфеле в рублях"""

    total_amount_portfolio = proto.Field(common.MoneyValue, number=11)
    """Общая стоимость портфеля в рублях"""

    virtual_positions = proto.RepeatedField(VirtualPortfolioPosition, number=12)
    """Массив виртуальных позиций портфеля"""


class GetOperationsByCursorResponse(proto.Message):
    """Список операций по счёту с пагинацией."""

    has_next = proto.Field(proto.BOOL, number=1)
    """Признак, есть ли следующий элемент."""

    next_cursor = proto.Field(proto.STRING, number=2)
    """Следующий курсор."""

    items = proto.RepeatedField(OperationItem, number=6)
    """Список операций."""


class BrokerReportRequest(proto.Message):

    generate_broker_report_request = proto.Field(GenerateBrokerReportRequest, number=1, oneof="payload", optional=True)
    get_broker_report_request = proto.Field(GetBrokerReportRequest, number=2, oneof="payload", optional=True)

class BrokerReportResponse(proto.Message):

    generate_broker_report_response = proto.Field(GenerateBrokerReportResponse, number=1, oneof="payload", optional=True)
    get_broker_report_response = proto.Field(GetBrokerReportResponse, number=2, oneof="payload", optional=True)

class GetDividendsForeignIssuerRequest(proto.Message):

    generate_div_foreign_issuer_report = proto.Field(GenerateDividendsForeignIssuerReportRequest, number=1, oneof="payload", optional=True)
    """Объект запроса формирования отчёта."""

    get_div_foreign_issuer_report = proto.Field(GetDividendsForeignIssuerReportRequest, number=2, oneof="payload", optional=True)
    """Объект запроса сформированного отчёта."""


class GetDividendsForeignIssuerResponse(proto.Message):

    generate_div_foreign_issuer_report_response = proto.Field(GenerateDividendsForeignIssuerReportResponse, number=1, oneof="payload", optional=True)
    """Объект результата задачи запуска формирования отчёта."""

    div_foreign_issuer_report = proto.Field(GetDividendsForeignIssuerReportResponse, number=2, oneof="payload", optional=True)
    """Отчёт "Справка о доходах за пределами РФ"."""


class PortfolioStreamResponse(proto.Message):
    """Информация по позициям и доходностям портфелей."""

    subscriptions = proto.Field(PortfolioSubscriptionResult, number=1, oneof="payload", optional=True)
    """Объект результата подписки."""

    portfolio = proto.Field(PortfolioResponse, number=2, oneof="payload", optional=True)
    """Объект стриминга портфеля."""

    ping = proto.Field(common.Ping, number=3, oneof="payload", optional=True)
    """Проверка активности стрима."""


class PositionsStreamResponse(proto.Message):
    """Информация по изменению позиций портфеля."""

    subscriptions = proto.Field(PositionsSubscriptionResult, number=1, oneof="payload", optional=True)
    """Объект результата подписки."""

    position = proto.Field(PositionData, number=2, oneof="payload", optional=True)
    """Объект стриминга позиций."""

    ping = proto.Field(common.Ping, number=3, oneof="payload", optional=True)
    """Проверка активности стрима."""


class PositionsResponse(proto.Message):
    """Список позиций по счёту."""

    money = proto.RepeatedField(common.MoneyValue, number=1)
    """Массив валютных позиций портфеля."""

    blocked = proto.RepeatedField(common.MoneyValue, number=2)
    """Массив заблокированных валютных позиций портфеля."""

    securities = proto.RepeatedField(PositionsSecurities, number=3)
    """Список ценно-бумажных позиций портфеля."""

    limits_loading_in_progress = proto.Field(proto.BOOL, number=4)
    """Признак идущей в данный момент выгрузки лимитов."""

    futures = proto.RepeatedField(PositionsFutures, number=5)
    """Список фьючерсов портфеля."""

    options = proto.RepeatedField(PositionsOptions, number=6)
    """Список опционов портфеля."""


class PositionData(proto.Message):
    """Данные о позиции портфеля."""

    account_id = proto.Field(proto.STRING, number=1)
    """Идентификатор счёта."""

    money = proto.RepeatedField(PositionsMoney, number=2)
    """Массив валютных позиций портфеля."""

    securities = proto.RepeatedField(PositionsSecurities, number=3)
    """Список ценно-бумажных позиций портфеля."""

    futures = proto.RepeatedField(PositionsFutures, number=4)
    """Список фьючерсов портфеля."""

    options = proto.RepeatedField(PositionsOptions, number=5)
    """Список опционов портфеля."""

    date = proto.Field(timestamp_pb2.Timestamp, number=6)
    """Дата и время операции в формате UTC."""

