def check_response(response):
    orders = ""
    page_info = ""
    stations = ""
    if "orders" in response:
        orders = check_orders(response)
    if "pageInfo" in response:
        page_info = check_page_info(response)
    if "availableStations" in response:
        stations = check_available_stations(response)
    if orders == "OK" and page_info == "OK" and stations == "OK":
        return "OK"
    else:
        return "NOT OK"


def check_orders(response):
    orders = response["orders"]  # это список orders
    checked_orders = 0  # счетчик проверенных заказов
    for order in orders:  # перебор элементов списка orders
        order_check = 0  # счетчик проверки ключей в заказе
        if "id" in order:
            order_check += 1
        if "courierId" in order:
            order_check += 1
        if "firstName" in order:
            order_check += 1
        if "lastName" in order:
            order_check += 1
        if "address" in order:
            order_check += 1
        if "metroStation" in order:
            order_check += 1
        if "phone" in order:
            order_check += 1
        if "rentTime" in order:
            order_check += 1
        if "deliveryDate" in order:
            order_check += 1
        if "track" in order:
            order_check += 1
        if "createdAt" in order:
            order_check += 1
        if "updatedAt" in order:
            order_check += 1
        if "status" in order:
            order_check += 1
        if order_check == 13:  # если все необходимые ключи есть, заказ проверен
            checked_orders += 1
    if checked_orders == len(orders):  # проверка, что все заказы правильные
        return "OK"


def check_page_info(response):
    if "pageInfo" in response:
        page_info = response["pageInfo"]
        page_check = 0
        if "page" in page_info:
            page_check += 1
        if "total" in page_info:
            page_check += 1
        if "limit" in page_info:
            page_check += 1
        if page_check == 3:
            return "OK"


def check_available_stations(response):
    if "availableStations" in response:
        available_stations = response["availableStations"]
        checked_stations = 0
        for station in available_stations:
            station_check = 0
            if "name" in station:
                station_check += 1
            if "number" in station:
                station_check += 1
            if "color" in station:
                station_check += 1
            if station_check == 3:
                checked_stations += 1
        if checked_stations == len(available_stations):
            return "OK"
