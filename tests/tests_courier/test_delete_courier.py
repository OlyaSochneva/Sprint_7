import requests
from assistant_methods import generate_random_id_or_track
import allure


class TestDeleteCourier:
    @allure.title('Проверка: курьера можно удалить')
    def test_delete_courier_success(self, login_new_courier_and_return_id):
        courier_id = login_new_courier_and_return_id
        response = requests.delete('https://qa-scooter.praktikum-services.ru/api/v1/courier/' + courier_id,
                                   timeout=10)
        assert response.status_code == 200 and "True" == str((response.json())["ok"])

    @allure.title('Проверка: если не передать id, вернётся ошибка 400')
    @allure.description('(!)Тест падает, т.к. приходит ошибка 404, а не 400')
    def test_delete_courier_without_id_causes_400_error(
            self, login_new_courier_and_return_id):
        response = requests.delete('https://qa-scooter.praktikum-services.ru/api/v1/courier', timeout=10)
        assert (response.status_code == 400
                and "Недостаточно данных для удаления курьера" in str(response.json()))

    @allure.title('Проверка: если передать несуществующий id, вернётся ошибка 404')
    def test_delete_courier_with_invalid_id_causes_404_error(self):
        courier_id = generate_random_id_or_track()
        response = requests.delete('https://qa-scooter.praktikum-services.ru/api/v1/courier/' + courier_id,
                                   timeout=10)
        assert (response.status_code == 404
                and "Курьера с таким id нет" in str(response.json()))
