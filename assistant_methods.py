import string
import random
from datetime import date, timedelta


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def choose_random_station():
    return random.randint(1, 237)  # т.к. всего станций в списке Самоката 237


def generate_phone_number():
    phone_number = '89'  # чтобы номер был похож на настоящий
    for i in range(9):
        phone_number += random.choice(string.digits)
    return phone_number


def choose_random_rent_time():
    return random.randint(1, 7)


def choose_random_delivery_date():
    days = []
    d1 = date(2024, 3, 15)  # начальная дата
    d2 = date(2024, 3, 31)  # конечная дата
    delta = d2 - d1
    for i in range(delta.days + 1):
        days.append(str(d1 + timedelta(i)))
    return random.choice(days)


def generate_random_id_or_track():
    random_id = ''
    for i in range(7):
        random_id += random.choice(string.digits)
    return random_id


