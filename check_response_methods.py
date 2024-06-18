from data import Sample


def check_response(response):
    orders = ""
    page_info = ""
    stations = ""
    if response.keys() == Sample.RESPONSE_SAMPLE.keys():
        orders = check_orders_list(response)
        page_info = check_page_info(response)
        stations = check_available_stations(response)
    if orders == "OK" and page_info == "OK" and stations == "OK":
        return "OK"


def check_orders_list(response):
    orders = response["orders"]
    checked_orders = 0
    for order in orders:
        if order.keys() == Sample.ORDER_SAMPLE.keys():
            checked_orders += 1
    if checked_orders == len(orders):
        return "OK"


def check_page_info(response):
    page_info = response["pageInfo"]
    if page_info.keys() == Sample.PAGE_INFO_SAMPLE.keys():
        return "OK"


def check_available_stations(response):
    available_stations = response["availableStations"]
    checked_stations = 0
    for station in available_stations:
        if station.keys() == Sample.STATION_SAMPLE.keys():
            checked_stations += 1
    if checked_stations == len(available_stations):
        return "OK"
