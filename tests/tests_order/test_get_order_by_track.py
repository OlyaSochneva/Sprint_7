import requests
from assistant_methods import generate_random_id_or_track
import allure


class TestGetOrderByTrack:
    @allure.title('Проверка: заказ можно получить по треку')
    def test_get_order_by_track_success(
            self, create_order_and_return_track):
        track = create_order_and_return_track
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders/track',
                                params={'t': track})
        assert response.status_code == 200 and "order" in str(response.json())

    @allure.title('Проверка: если не передать query-параметр с треком, вернётся ошибка 400')
    def test_get_order_without_track_causes_400_error(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders/track')
        assert (response.status_code == 400
                and "Недостаточно данных для поиска" in str(response.json()))

    @allure.title('Проверка: если передать несуществующий трек, вернётся ошибка 404')
    def test_get_order_by_invalid_track_causes_404_error(self):
        track = generate_random_id_or_track()
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders/track',
                                params={'t': track})
        assert (response.status_code == 404
                and "Заказ не найден" in str(response.json()))
