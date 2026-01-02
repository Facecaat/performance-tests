from typing import TypedDict
from httpx import Response, QueryParams
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """
    Описание структуры операций.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationsSummaryDict(TypedDict):
    """
    Описание структуры статистики по операциям.
    """
    spentAmount: int
    receivedAmount: int
    cashbackAmount: int


class OperationsReceiptDict(TypedDict):
    """
    Описание структуры получения чека.
    """
    url: str
    document: str


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    accountId: str


class GetOperationsResponseDict(TypedDict):
    """
    Описание структуры ответа получения списка операций для определенного счета.
    """
    operations: list[OperationDict]


class GetOperationsSummaryQueryDict(GetOperationsQueryDict):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """


class GetOperationsSummaryResponseDict(TypedDict):
    """
    Описание структуры ответа статистики по операциям для определенного счета.
    """
    summary: OperationsSummaryDict


class GetOperationsReceiptResponseDict(TypedDict):
    """
    Описание структуры ответа получения чека по определенной операции.
    """
    receipt: OperationsReceiptDict


class GetOperationResponseDict(TypedDict):
    """
    Описание структуры ответа получения информации об операции.
    """
    operation: OperationDict


class MakeOperationRequestDict(TypedDict):
    """
    Структура данных для POST методов по операциям.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции.
    """
    operation: OperationDict


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции комиссии.
    """


class MakeFeeOperationResponseDict(MakeOperationResponseDict):
    """
    Описание структуры ответа операции комиссии.
    """


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции пополнения.
    """


class MakeTopUpOperationResponseDict(MakeOperationResponseDict):
    """
    Описание структуры ответа операции комиссии.
    """


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции кэшбэка.
    """


class MakeCashbackOperationResponseDict(MakeOperationResponseDict):
    """
    Описание структуры ответа операции кэшбека.
    """


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции перевода.
    """


class MakeTransferOperationResponseDict(MakeOperationResponseDict):
    """
    Описание структуры ответа операции перевода.
    """


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции покупки.
    """
    category: str


class MakePurchaseOperationResponseDict(MakeOperationResponseDict):
    """
    Описание структуры ответа операции покупки.
    """


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции оплаты по счету.
    """


class MakeBillPaymentOperationResponseDict(MakeOperationResponseDict):
    """
    Описание структуры ответа операции оплаты по счету.
    """


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции снятия наличных денег.
    """


class MakeCashWithdrawalOperationResponseDict(MakeOperationResponseDict):
    """
    Описание структуры ответа операции снятия наличных денег.
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

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id=operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationsReceiptResponseDict:
        response = self.get_operations_receipt_api(operation_id=operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_api_summary(query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
            category="string"
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
