import httpx
import time

create_user_payload = {
    "email": f"user{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
create_user_response = httpx.post(url="http://localhost:8003/api/v1/users", json=create_user_payload)

user_id = create_user_response.json()['user']['id']

open_credit_card_account_payload = {"userId": user_id}
open_credit_card_account_response = httpx.post(url="http://localhost:8003/api/v1/accounts/open-credit-card-account",
                                               json=open_credit_card_account_payload)

credit_card_account_id = open_credit_card_account_response.json()['account']['cards'][0]['accountId']
credit_card_card_id = open_credit_card_account_response.json()['account']['cards'][0]['id']

make_purchase_operation_payload = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "category": "taxi",
    "cardId": credit_card_card_id,
    "accountId": credit_card_account_id
}
make_purchase_operation_response = httpx.post(url="http://localhost:8003/api/v1/operations/make-purchase-operation",
                                              json=make_purchase_operation_payload)

make_purchase_operation_id = make_purchase_operation_response.json()['operation']['id']

get_operation_receipt_response = httpx.get(
    url=f"http://localhost:8003/api/v1/operations/operation-receipt/{make_purchase_operation_id}")

print(get_operation_receipt_response.json())
