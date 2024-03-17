import requests
from check_response_methods import check_response
import allure


class TestGetOrdersList:
    @allure.title('Проверка: в теле ответа возвращается список заказов')
    @allure.description('(!) В параметр передан лимит в два заказа, чтобы сократить время теста')
    def test_get_orders_list_without_id_success(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders',
                                params={'limit': 2}, timeout=30)
        response_body = response.json()
        result = check_response(response_body)
        assert response.status_code == 200 and result == "OK"
