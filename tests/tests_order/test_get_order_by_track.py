import requests
from assistant_methods import generate_random_id_or_track
import allure
from data import Message
from data import URL


class TestGetOrderByTrack:
    @allure.title('Проверка: заказ можно получить по треку')
    def test_get_order_by_track_success(self, create_order_and_return_track):
        track = create_order_and_return_track
        response = requests.get(URL.GET_ORDER, params={'t': track})
        assert response.status_code == 200 and "order" in str(response.json())

    @allure.title('Проверка: если не передать query-параметр с треком, вернётся ошибка 400')
    def test_get_order_without_track_causes_400_error(self):
        response = requests.get(URL.GET_ORDER)
        assert (response.status_code == 400
                and Message.NOT_ENOUGH_DATA_FOR_SEARCH in str(response.json()))

    @allure.title('Проверка: если передать несуществующий трек, вернётся ошибка 404')
    def test_get_order_by_invalid_track_causes_404_error(self):
        track = generate_random_id_or_track()
        response = requests.get(URL.GET_ORDER, params={'t': track})
        assert (response.status_code == 404
                and Message.ORDER_NOT_FOUND in str(response.json()))
