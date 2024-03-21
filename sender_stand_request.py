import configuration
import requests
import data


def post_new_user(body):#esta función da de alta al nuevo usuario
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


# response = post_new_user(data.user_body)
# print(response.status_code)
# print(response.json())  # incluyendo esto ya me da 201 y un authToken


def get_new_user_token():  # esta función me proporciona el token
    response = post_new_user(data.user_body)
    response_data = response.json()
    return response_data["authToken"]


# response1 = get_new_user_token()
# print(response1)


def post_new_client_kit(body): # esta función crea el kit del usuario y responde con el nombre
    token = get_new_user_token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=body,
                         headers=headers)


response = post_new_client_kit(data.tests[0])

# print(response.status_code)
# print(response.json())
# print(response)

