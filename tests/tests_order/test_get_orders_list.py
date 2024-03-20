import requests
from check_response_methods import check_response
import allure
from data import URL


class TestGetOrdersList:
    @allure.title('Проверка: в теле ответа возвращается список заказов')
    @allure.description('(!) В параметр передан лимит в два заказа, чтобы сократить время теста')
    def test_get_orders_list_without_id_success(self):
        response = requests.get(URL.ORDER, params={'limit': 2}, timeout=30)
        result = check_response(response.json())
        assert response.status_code == 200 and result == "OK"
