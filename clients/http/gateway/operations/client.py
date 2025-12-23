from typing import TypedDict
from httpx import Response, QueryParams
from clients.http.client import HTTPClient


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    accountId: str


class GetOperationsSummaryQueryDict(GetOperationsQueryDict):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """


class MakeOperationRequestDict(TypedDict):
    """
    Структура данных для POST методов по операциям.
    """
    status: str
    amount: int
    cardId: str
    accountId: str


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции комиссии.
    """


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции пополнения.
    """


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции кэшбэка.
    """


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции перевода.
    """


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции покупки.
    """
    category: str


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции оплаты по счету.
    """


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции снятия наличных денег.
    """


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-operations.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение информации об операции.

        :param operation_id: ID операции
        :return: Объект httpx.Response с информацией об операции.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operations_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение чека по операции.

        :param operation_id: ID операции
        :return: Объект httpx.Response с информацией о чеке по операции.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response со списком операций для определенного счета.
        """
        return self.get(f"/api/v1/operations", params=QueryParams(**query))

    def get_operations_api_summary(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response со статистикой по операциям для определенного счета.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Словарь со status, amount, cardId и accountId
        :return: Объект httpx.Response с результатом по созданию операции комиссии.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param request: Словарь со status, amount, cardId и accountId
        :return: Объект httpx.Response с результатом по созданию операции пополнения.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь со status, amount, cardId и accountId
        :return: Объект httpx.Response с результатом по созданию операции кэшбэка.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь со status, amount, cardId и accountId
        :return: Объект httpx.Response с результатом по созданию операции перевода.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь со status, amount, cardId, accountId и category
        :return: Объект httpx.Response с результатом по созданию операции покупки.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :param request: Словарь со status, amount, cardId и accountId
        :return: Объект httpx.Response с результатом по созданию операции оплаты по счету.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных денег.

        :param request: Словарь со status, amount, cardId и accountId
        :return: Объект httpx.Response с результатом по созданию операции снятия наличных денег.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)
