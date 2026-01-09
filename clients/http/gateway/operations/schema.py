from pydantic import BaseModel, Field, ConfigDict

from tools.fakers import fake
from enum import StrEnum


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_RPOGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """
    Описание структуры операций.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: str
    status: str
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationsSummarySchema(BaseModel):
    """
    Описание структуры статистики по операциям.
    """
    model_config = ConfigDict(populate_by_name=True)

    spent_amount: int = Field(alias="spentAmount")
    received_amount: int = Field(alias="receivedAmount")
    cashback_amount: int = Field(alias="cashbackAmount")


class OperationsReceiptSchema(BaseModel):
    """
    Описание структуры получения чека.
    """
    url: str
    document: str


class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка операций для определенного счета.
    """
    operations: list[OperationSchema]


class GetOperationsSummaryQuerySchema(GetOperationsQuerySchema):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Описание структуры ответа статистики по операциям для определенного счета.
    """
    summary: OperationsSummarySchema


class GetOperationsReceiptResponseSchema(BaseModel):
    """
    Описание структуры ответа получения чека по определенной операции.
    """
    receipt: OperationsReceiptSchema


class GetOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа получения информации об операции.
    """
    operation: OperationSchema


class MakeOperationRequestSchema(BaseModel):
    """
    Структура данных для POST методов по операциям.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: str = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции.
    """
    operation: OperationSchema


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции комиссии.
    """


class MakeFeeOperationResponseSchema(MakeOperationResponseSchema):
    """
    Описание структуры ответа операции комиссии.
    """


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции пополнения.
    """


class MakeTopUpOperationResponseSchema(MakeOperationResponseSchema):
    """
    Описание структуры ответа операции комиссии.
    """


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции кэшбэка.
    """


class MakeCashbackOperationResponseSchema(MakeOperationResponseSchema):
    """
    Описание структуры ответа операции кэшбека.
    """


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции перевода.
    """


class MakeTransferOperationResponseSchema(MakeOperationResponseSchema):
    """
    Описание структуры ответа операции перевода.
    """


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции покупки.
    """
    category: str = Field(default_factory=fake.category())


class MakePurchaseOperationResponseSchema(MakeOperationResponseSchema):
    """
    Описание структуры ответа операции покупки.
    """


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции оплаты по счету.
    """


class MakeBillPaymentOperationResponseSchema(MakeOperationResponseSchema):
    """
    Описание структуры ответа операции оплаты по счету.
    """


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции снятия наличных денег.
    """


class MakeCashWithdrawalOperationResponseSchema(MakeOperationResponseSchema):
    """
    Описание структуры ответа операции снятия наличных денег.
    """
