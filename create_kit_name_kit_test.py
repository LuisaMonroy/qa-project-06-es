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


def test_create_kit_1_letter_in_name_kit_get_success_response():#prueba positiva con una letra en nombre del kit
    dato =  data.tests[0]
    positive_assert(dato)


def test_create_kit_511_letters_in_name_get_success_response():#prueba positiva con 511 letras en el nombre del kit
    dato = data.tests[1]
    positive_assert(dato)


def tests_create_kit_has_special_symbol_in_name_get_success_response():#prueba positiva con caracteres especiales en el nombre del kit
    dato = data.tests[2]
    positive_assert(dato)


def test_create_kit_has_space_in_name_get_success_response():#prueba positiva con espacios en el nombre del kit
    dato = data.tests[3]
    positive_assert(dato)


def test_create_kit_has_number_in_name_get_success_response():##prueba positiva con string de números en el nombre del kit
    dato = data.tests[4]
    positive_assert(dato)


def test_create_kit_has_no_name_get_error_response():#prueba negativa sin nombre
    dato = data.tests[5]
    negative_assert_code_400(dato)


def test_create_hit_has_512_letters_in_name_kit_get_error_response():#prueba negativa con 512 letras en el nombre del kit
    dato = data.tests[6]
    negative_assert_code_400(dato)


def test_create_kit_has_no_parameter_in_name_get_error_response():#prueba negativa con ningún parámetro
    dato = data.tests[7]
    negative_assert_code_400(dato)


def test_create_kit_has_different_parameter_in_name_kit_get_error_response():#prueba negativa con parámetros diferentes a sting en el nombre del kit
    dato = data.tests[8]
    negative_assert_code_400(dato)

