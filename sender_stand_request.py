import configuration
import requests
import data
import json


def post_new_user(body):#esta función agrega un nuevo usuario
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


def get_new_user_token():# esta función se utiliza para generar el authToken
    response = post_new_user(data.user_body)#este user body es el nombre del cliente
    response_data = response.json()
    return response_data['authToken']


response1 = get_new_user_token()
print(response1)


def post_new_client_kit(body):#esta función se utiliza para generar un kit por un nuevo cliente
    token = get_new_user_token()#el token es la validación de que se creó un usuario
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=body,
                         headers=headers)
