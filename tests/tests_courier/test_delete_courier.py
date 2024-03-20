import requests
import allure

from data import Message
from data import URL
from assistant_methods import generate_random_id_or_track


class TestDeleteCourier:
    @allure.title('Проверка: курьера можно удалить')
    def test_delete_courier_success(self, login_new_courier_and_return_id):
        courier_id = login_new_courier_and_return_id
        response = requests.delete(URL.COURIER + '/' + courier_id, timeout=10)
        assert response.status_code == 200 and "True" == str((response.json())["ok"])

    @allure.title('Проверка: если не передать id, вернётся ошибка 400')
    @allure.description('(!)Тест падает, т.к. приходит ошибка 404, а не 400')
    def test_delete_courier_without_id_causes_400_error(self):
        response = requests.delete(URL.COURIER, timeout=10)
        assert (response.status_code == 400
                and Message.NOT_ENOUGH_DATA_FOR_DELETE in str(response.json()))

    @allure.title('Проверка: если передать несуществующий id, вернётся ошибка 404')
    def test_delete_courier_with_invalid_id_causes_404_error(self):
        courier_id = generate_random_id_or_track()
        response = requests.delete(URL.COURIER + '/' + courier_id, timeout=10)
        assert (response.status_code == 404
                and Message.ID_NOT_FOUND in str(response.json()))
