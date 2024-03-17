import pytest
import requests
import allure


class TestCreateCourier:
    @allure.title('Проверка: курьера можно создать')
    def test_create_courier_success(self, new_courier_payload):
        payload = new_courier_payload
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier',
                                 data=payload, timeout=10)
        assert response.status_code == 201 and "True" == str((response.json())["ok"])

    @allure.title('Проверка: если одно из обязательных полей отсутствует, вернётся ошибка 400')
    @allure.description('(!)Тест падает с параметром firstName, т.к. фактически это поле необязательное '
                        'и его отсутствие не вызывает ошибку (баг?)')
    @pytest.mark.parametrize(
        "deleted_field", [
            'login',
            'password',
            'firstName'
        ])
    def test_create_courier_without_required_field_causes_400_error(
            self, new_courier_payload, deleted_field):
        payload = new_courier_payload
        payload.pop(deleted_field)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier',
                                 data=payload, timeout=10)
        assert (response.status_code == 400
                and "Недостаточно данных для создания учетной записи" in str(response.json()))

    @allure.title('Проверка: если попытаться создать курьера с данными, идентичными уже существующему, '
                  'вернётся ошибка 409')
    @allure.description('(!)В тестовой документации указан только текст для ошибки с одинаковым логином '
                        '«Этот логин уже используется», в случае если у курьеров совпадают ВСЕ данные, '
                        'фактически возвращается ошибка с таким же сообщением. Это серая зона в требованиях '
                        '(как мне кажется), поэтому в тесте проверяем только код ошибки')
    def test_create_two_same_couriers_causes_409_error(
            self, new_courier_payload):
        payload = new_courier_payload
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier',
                      data=payload, timeout=10)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier',
                                 data=payload, timeout=10)
        assert response.status_code == 409

    @allure.title('Проверка: если попытаться создать курьера с таким же логином, как у уже существующего, '
                  'вернётся ошибка 409')
    def test_create_two_same_login_couriers_causes_409_error(
            self, new_courier_payload):
        payload_1 = new_courier_payload
        same_login = payload_1['login']
        payload_2 = new_courier_payload
        payload_2['login'] = same_login
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier',
                      data=payload_1, timeout=10)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier',
                                 data=payload_2, timeout=10)
        assert response.status_code == 409 and "Этот логин уже используется" in str(response.json())
