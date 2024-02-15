import sender_stand_request
import data


def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


def get_kit_body(name):
    response = sender_stand_request.post_new_client_kit(data.kit_body)
    json = response.json()
    json["name"] = name
    return json["name"]


def positive_assert(kit_body):
    user_response = sender_stand_request.post_new_client_kit(kit_body)

    assert user_response.status_code == 201


def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)

    assert response.status_code == 400
    assert response.json()["No se han aprobado todos los parámetros requeridos"]


# primero quiero definir todas las funciones para luego realizar las pruebas

def test_create_kit_1_letter_in_name_kit_get_success_response():
    positive_assert("a")


def test_create_kit_511_letters_in_name_kit_get_success_response():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("№%@")


def test_create_kit_has_space_in_name_get_success_response():  # porque no se resaltan de azul??
    positive_assert("A Aaa")


def test_crete_kit_has_number_in_name_get_success_response():
    positive_assert("123")


def test_create_kit_has_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)


def test_create_kit_has_512_letters_in_name_kit_get_error_response():
    negative_assert_code_400(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


def test_create_kit_has_no_parameter_get_error_response():
    negative_assert_code_400()


def test_create_kit_has_different_parameter_in_name_kit_get_error_response():
    negative_assert_code_400(123)
