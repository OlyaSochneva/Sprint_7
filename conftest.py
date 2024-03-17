import pytest
import json
import requests

from assistant_methods import choose_random_station
from assistant_methods import generate_phone_number
from assistant_methods import choose_random_delivery_date
from assistant_methods import choose_random_rent_time
from assistant_methods import generate_random_string


@pytest.fixture(scope="function")
def order_payload():  # без указания цвета
    payload = {
        "firstName": generate_random_string(5),
        "lastName": generate_random_string(5),
        "address": generate_random_string(5),
        "metroStation": choose_random_station(),
        "phone": generate_phone_number(),
        "rentTime": choose_random_rent_time(),
        "deliveryDate": choose_random_delivery_date(),
        "comment": generate_random_string(5)
    }
    return payload


@pytest.fixture(scope="function")
def create_order_and_return_track(order_payload):
    payload = json.dumps(order_payload)
    track = ""
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
    if response.status_code == 201:
        track = str((response.json())["track"])
    yield track
    requests.put('https://qa-scooter.praktikum-services.ru/api/v1/orders/cancel/',
                 params={"track": track})


@pytest.fixture(scope="function")
def new_courier_payload():
    login = generate_random_string(5)
    password = generate_random_string(5)
    first_name = generate_random_string(5)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    yield payload
    login_pass = {"login": login, "password": password}
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=login_pass)
    if response.status_code == 200:
        courier_id = str((response.json())["id"])
        requests.delete('https://qa-scooter.praktikum-services.ru/api/v1/courier/' + courier_id)


@pytest.fixture(scope="function")
def create_new_courier_and_return_login_password(new_courier_payload):
    login_pass = {}
    payload = new_courier_payload
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    if response.status_code == 201:
        login_pass["login"] = payload["login"]
        login_pass["password"] = payload["password"]
    return login_pass


@pytest.fixture(scope="function")
def login_new_courier_and_return_id(create_new_courier_and_return_login_password):
    payload = create_new_courier_and_return_login_password
    courier_id = ""
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
    if response.status_code == 200:
        courier_id = str((response.json())["id"])
    return courier_id