import pytest
import requests
import allure

from assistant_methods import generate_random_string
from data import Message
from data import URL


class TestLoginCourier:
    @allure.title('Проверка: курьера можно авторизовать')
    def test_login_courier_success(self, create_new_courier_and_return_login_password):
        payload = create_new_courier_and_return_login_password
        response = requests.post(URL.COURIER_LOGIN, data=payload, timeout=10)
        assert response.status_code == 200 and "id" in str(response.json())

    @allure.title('Проверка: если одно из полей некорректное, вернётся ошибка 404')
    @pytest.mark.parametrize(
        "wrong_field", [
            'login',
            'password'
        ])
    def test_login_with_wrong_fields_causes_404_error(
            self, create_new_courier_and_return_login_password, wrong_field):
        payload = create_new_courier_and_return_login_password
        payload[wrong_field] = generate_random_string(5)
        response = requests.post(URL.COURIER_LOGIN, data=payload, timeout=10)
        assert (response.status_code == 404
                and Message.ACCOUNT_NOT_FOUND in str(response.json()))

    @allure.title('Проверка: если одно из обязательных полей отсутствует, вернётся ошибка 400')
    @allure.description('(!)Тест падает, если не передать пароль, т.к. не приходит ответ '
                        '(та же проблема воспроизводится вручную в Postman).')
    @pytest.mark.parametrize(
        "deleted_field", [
            'login',
            'password'
        ])
    def test_login_without_required_field_causes_400_error(
            self, create_new_courier_and_return_login_password, deleted_field):
        payload = create_new_courier_and_return_login_password
        payload.pop(deleted_field)
        response = requests.post(URL.COURIER_LOGIN, data=payload, timeout=10)
        assert (response.status_code == 400
                and Message.NOT_ENOUGH_DATA_FOR_LOGIN in str(response.json()))
