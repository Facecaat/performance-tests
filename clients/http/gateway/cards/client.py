from clients.http.client import HTTPClient
from httpx import Response
from typing import TypedDict


class CreateCardRequestDict(TypedDict):
    """
    Структура данных для создания новой карты
    """
    userId: str
    accountId: str


class CardGatewayHTTPClient(HTTPClient):
    def issue_virtual_card_api(self, request: CreateCardRequestDict) -> Response:
        """
        Создание виртуальной карты.

        :param request: Словарь с данными новой виртуальной карты.
        :return: Объект от свервера (объект httpx.Response)
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: CreateCardRequestDict) -> Response:
        """
        Создание физической карты.

        :param request: Словарь с данными новой физической карты.
        :return: Объект от свервера (объект httpx.Response)
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)
