import configuration
import requests
import data
import json


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


def get_new_user_token():
    response = post_new_user(data.user_body)
    response_data = response.json()
    return response_data['authToken']


response1 = get_new_user_token()
print(response1)


def post_new_client_kit(body):
    token = get_new_user_token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=body,
                         headers=headers)
