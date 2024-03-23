import sender_stand_request
import data


def get_user_body():# función para obtener el nombre del usuario
    current_body = data.user_body.copy()
    first_name = current_body["firstName"]
    return first_name


# print(get_user_body())


def get_kit_body(name):#función para obtener el nombre del kit
    response = sender_stand_request.post_new_client_kit(name)
    dato = response.json()
    return dato


def positive_assert(kit_body):#función para la evaluación de las pruebas positivas
    user_body = kit_body
    user_response = sender_stand_request.post_new_client_kit(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["name"] == user_body["name"]


def negative_assert_code_400(kit_body): #función para la evaluación de las pruebas negativas
    user_body = kit_body
    response = sender_stand_request.post_new_client_kit(user_body)
    assert response.status_code == 400


def test_kit_1_letter_in_name_success_response():
    dato =  data.tests[0]
    positive_assert(dato)
#prueba positiva con una letra en nombre del kit


def test_create_kit_511_letters_new_kit():
    dato = data.tests[1]
    positive_assert(dato)
#prueba positiva con 511 letras en el nombre del kit


def test_create_kit_0_character_new_kit():
    dato = data.tests[2]
    negative_assert_code_400(dato)
#prueba negativa sin nombre


def test_create_kit_512_letter_new_kit():
    dato = data.tests[3]
    negative_assert_code_400(dato)
#prueba negativa con 512 letras en el nombre del kit


def test_create_kit_special_characters_new_kit():
    dato = data.tests[4]
    positive_assert(dato)
#prueba positiva con caracteres especiales en el nombre del kit


def test_create_kit_space_new_kit():
    dato = data.tests[5]
    positive_assert(dato)
#prueba positiva con espacios en el nombre del kit


def test_create_kit_number_new_kit():
    dato = data.tests[6]
    positive_assert(dato)
#prueba positiva con string de números en el nombre del kit


def test_create_kit_no_parameter_new_kit():
    dato = data.tests[7]
    negative_assert_code_400(dato)
#prueba negativa sin ningún parámetro


def test_create_kit_different_parameter_new_kit():
    dato = data.tests[8]
    negative_assert_code_400(dato)
#prueba negativa con parámetros diferentes a sting en el nombre del kit
