import sender_stand_request
import data


def get_user_body(first_name):  # esta función extrae al usuario, me sirve esta función para generar el kit?
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


def get_kit_body(
        name):  # esta función  extrae del cuerpo de la solicitud, aquí esta lo que contiene el kit pero el nombre también?
    response = sender_stand_request.post_new_client_kit(data.kit_body_name)
    json = response.json()
    json["name"] = name
    return json["name"]  # siento que esta función no es necesaria


def positive_assert(kit_body):  # función para evaluar las pruebas positivas
    user_response = sender_stand_request.post_new_client_kit(data.kit_body_name)
    assert user_response.status_code == 201
    assert user_response.json()["kit_body_name"] == kit_body

    # aqui se evalua la respuesta de la función de creacion del kit
    # cómo evalúo el nombre


def negative_assert_code_400(kit_body):  # función para evaluar las pruebas negativas
    response = sender_stand_request.post_new_client_kit(data.kit_body_name)
    response.json()["kit_body_name"] == kit_body
    assert response.status_code == 400
    assert response.json()["No se han aprobado todos los parámetros requeridos"]


def test_create_kit_1_letter_in_name_kit_get_success_response():  # prueba con una caracter en el campo nombre
    positive_assert(data.kit_body_name[0])


def test_create_kit_511_letters_in_name_kit_get_success_response():  # prueba con 511 caracteres en el campo nombre
    positive_assert(data.kit_body_name[1])


def test_create_kit_has_no_parameter_get_error_response():  # prueba sin parámetro en el campo nombre
    negative_assert_code_400(data.kit_body_name[2])


def test_create_kit_has_512_letters_in_name_kit_get_error_response():  # prueba con 512 caracteres en el campo nombre
    negative_assert_code_400(data.kit_body_name[3])


def test_create_kit_has_special_symbol_in_name_get_success_response():  # prueba con símbolos especiales en el campo nombre
    positive_assert(data.kit_body_name[4])


def test_create_kit_has_space_in_name_get_success_response():  # prueba con espacio en el campo nombre
    positive_assert(data.kit_body_name[5])


def test_crete_kit_has_number_in_name_get_success_response():  # prueba con un string de números en el campo nombre
    positive_assert(data.kit_body_name[6])


def test_create_kit_has_no_name_get_error_response():  # prueba con el campo nombre vacío
    kit_body = data.kit_body_name.copy()
    kit_body.pop("name")
    negative_assert_code_400(data.kit_body_name[7])


def test_create_kit_has_different_parameter_in_name_kit_get_error_response():  # prueba con valores numéricos en el campo nombre
    negative_assert_code_400(data.kit_body_name[8])
