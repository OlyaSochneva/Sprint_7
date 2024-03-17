import pytest
import json
import requests
import allure


@allure.title('Проверка: заказ можно создать, указав один из двух цветов, оба цвета или никакой')
class TestCreateOrder:
    test_orders = []

    @pytest.mark.parametrize(
        "color",
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GRAY"],
            []
        ])
    def test_create_order(self, order_payload, color):
        payload = order_payload
        payload["color"] = color
        payload_string = json.dumps(payload)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders',
                                 data=payload_string, timeout=10)
        self.test_orders.append(str((response.json())["track"]))
        assert response.status_code == 201 and "track" in response.json()

    @classmethod
    def teardown_class(cls):
        for track in cls.test_orders:
            requests.put('https://qa-scooter.praktikum-services.ru/api/v1/orders/cancel/',
                         params={"track": track}, timeout=10)
