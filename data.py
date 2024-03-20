class Sample:
    RESPONSE_SAMPLE = {
        "orders": "",
        "pageInfo": "",
        "availableStations": ""
    }

    ORDER_SAMPLE = {
        "id": "",
        "courierId": "",
        "firstName": "",
        "lastName": "",
        "address": "",
        "metroStation": "",
        "phone": "",
        "rentTime": "",
        "deliveryDate": "",
        "track": "",
        "color": "",
        "comment": "",
        "createdAt": "",
        "updatedAt": "",
        "status": ""
    }
    PAGE_INFO_SAMPLE = {
        "page": "",
        "total": "",
        "limit": ""
    }
    STATION_SAMPLE = {
        "name": "",
        "number": "",
        "color": ""
    }


class Message:
    NOT_ENOUGH_DATA_FOR_REG = "Недостаточно данных для создания учетной записи"
    LOGIN_ALREADY_EXISTS = "Этот логин уже используется"
    NOT_ENOUGH_DATA_FOR_DELETE = "Недостаточно данных для удаления курьера"
    ID_NOT_FOUND = "Курьера с таким id нет"
    NOT_ENOUGH_DATA_FOR_LOGIN = "Недостаточно данных для входа"
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    NOT_ENOUGH_DATA_FOR_SEARCH = "Недостаточно данных для поиска"
    ORDER_NOT_FOUND = "Заказ не найден"


class URL:
    ORDER = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'  # (создать, получить все заказы)
    CANCEL_ORDER = 'https://qa-scooter.praktikum-services.ru/api/v1/orders/cancel/' # отменить заказ
    GET_ORDER = 'https://qa-scooter.praktikum-services.ru/api/v1/orders/track' # получить заказ по треку

    COURIER_LOGIN = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login' # авторизовать курьера
    COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'  # создать, удалить курьера
