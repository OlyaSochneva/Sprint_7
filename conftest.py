import pytest
import json
import requests

from assistant_methods import order_payload
from assistant_methods import new_courier_payload
from data import URL


@pytest.fixture(scope="function")
def create_order_and_return_track():
    payload = json.dumps(order_payload())
    response = requests.post(URL.ORDER, data=payload)
    track = str((response.json())["track"])
    yield track
    requests.put(URL.CANCEL_ORDER, params={"track": track})


@pytest.fixture(scope="function")
def create_new_courier_and_return_login_password():
    login_pass = {}
    payload = new_courier_payload()
    requests.post(URL.COURIER, data=payload)
    login_pass['login'] = payload['login']
    login_pass['password'] = payload['password']
    yield login_pass
    response = requests.post(URL.COURIER_LOGIN, data=login_pass)
    if response.status_code == 200:
        courier_id = str((response.json())["id"])
        requests.delete(URL.COURIER + '/' + courier_id)


@pytest.fixture(scope="function")
def login_new_courier_and_return_id(create_new_courier_and_return_login_password):
    payload = create_new_courier_and_return_login_password
    response = requests.post(URL.COURIER_LOGIN, data=payload)
    courier_id = str((response.json())["id"])
    return courier_id
