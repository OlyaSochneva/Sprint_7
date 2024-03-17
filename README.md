## QA Sprint 7
#### Тесты для Яндекс.Самокат

Содержимое проекта:

**tests** - папка со всеми тестами:
- **tests_courier** - тесты для курьеров
- **tests_order** - тесты для заказов

**conftest.py** - фикстуры

**assistant_methods.py** - вспомогательные методы для генерации данных

**check_response_methods.py** - вспомогательные методы для проверки тела ответа

**allure_results** - отчёты

**requirements.txt** - внешние зависимости

## Тесты для курьеров (tests_courier)
### Cоздание курьера POST /api/v1/courier
**test_create_courier_success**

Проверка: курьера можно создать

Фикстура: new_courier_payload

ОР: код 201 и {"ok":true} в теле ответа

**test_create_courier_without_required_field_causes_400_error**

Проверка: если одно из обязательных полей отсутствует, вернётся ошибка 400

Фикстура: new_courier_payload

Параметр: удаляемое поле 

ОР: код 400 и "Недостаточно данных для создания учетной записи" в теле ответа

**test_create_two_same_couriers_causes_409_error**

Проверка: если попытаться создать курьера с данными, идентичными уже существующему, вернётся ошибка 409

Фикстура: new_courier_payload

ОР: код 409 

**test_create_two_same_login_couriers_causes_409_error**

Проверка: если попытаться создать курьера с таким же логином, как у уже существующего, вернётся ошибка 409

Фикстура: new_courier_payload

ОР: код 409 и "Этот логин уже используется" в теле ответа

### Удаление курьера DELETE /api/v1/courier/:id

**test_delete_courier_success**

Проверка: курьера можно удалить

Фикстура: login_new_courier_and_return_id

ОР: код 200 и {"ok":true} в теле ответа

**test_delete_courier_without_id_causes_400_error**

Проверка: если не передать id, вернётся ошибка 400

Фикстура: login_new_courier_and_return_id

ОР: код 400 и "Недостаточно данных для удаления курьера" в теле ответа

**test_delete_courier_with_invalid_id_causes_404_error**

Проверка: если передать несуществующий id, вернётся ошибка 404

ОР: код 404 и "Курьера с таким id нет" в теле ответа

### Логин курьера POST /api/v1/courier/login

**test_login_courier_success**

Проверка: курьера можно авторизовать

Фикстура: create_new_courier_and_return_login_password

ОР: код 200 и "id" в теле ответа

**test_login_without_required_field_causes_400_error**

Проверка: если одно из обязательных полей отсутствует, вернётся ошибка 400

Фикстура: create_new_courier_and_return_login_password

Параметр: удаляемое поле 

ОР: код 400 и "Недостаточно данных для входа" в теле ответа

**test_login_with_wrong_fields_causes_404_error**

Проверка: если одно из полей некорректное, вернётся ошибка 404

Фикстура: create_new_courier_and_return_login_password

Параметр: некорректное поле 

ОР: код 404 и "Учетная запись не найдена" в теле ответа

## Тесты для заказов (tests_order)
### Cоздание заказа POST /api/v1/orders

**test_create_order**

Проверка: заказ можно создать, указав один из двух цветов, оба цвета или никакой

Фикстура: order_payload

Параметр: значение по ключу "color"

ОР: код 201 и "track" в теле ответа

### Получить заказ по номеру GET /api/v1/orders/track

**test_get_order_by_track_success**

Проверка: заказ можно получить по треку

Фикстура: create_order_and_return_track

ОР: код 200 и "order" в теле ответа

**test_get_order_without_track_causes_400_error**

Проверка: если не передать query-параметр с треком, вернётся ошибка 400

ОР: код 400 и "Недостаточно данных для поиска" в теле ответа

**test_get_order_by_invalid_track_causes_404_error**

Проверка: если передать несуществующий трек, вернётся ошибка 404

ОР: код 404 и "Заказ не найден" в теле ответа

### Получить список заказов GET /api/v1/orders

Проверка: в теле ответа возвращается список заказов

Исп. метод: check_response

ОР: код 200 и метод check_response вернул 'OK'

### Фикстуры:
**order_payload** - возвращает словарь со сгенерированными данными для создания заказа (без указания цвета)

Вспомогательные методы: generate_random_string, choose_random_station, generate_phone_number, choose_random_rent_time, choose_random_delivery_date

**create_order_and_return_track(order_payload):** - создаёт заказ, возвращает трек и потом отменяет заказ 

API-методы: 
- POST /api/v1/orders
- PUT /api/v1/orders/cancel

**new_courier_payload** - возвращает словарь со сгенерированными данными для создания курьера, потом проверяет существование и удаляет его

Вспомогательные методы: generate_random_string

API-методы:

- POST /api/v1/courier/login
- DELETE /api/v1/courier/:id

**create_new_courier_and_return_login_password(new_courier_payload)** - создаёт курьера и возвращает логин и пароль

API-методы:
- POST /api/v1/courier

**login_new_courier_and_return_id(create_new_courier_and_return_login_password)** - авторизует созданного курьера и возвращает id

API-методы:

- POST /api/v1/courier/login
### Вспомогательные методы (assistant_methods):

- **generate_random_string** - рандомная lowercase строка, в к-ве аргумента принимает длину
- **choose_random_station** - случайное число от 1 до 237 (всего 237 станций в Самокате)
- **generate_phone_number** - случайная строка из 11 цифр формата "89**********"
- **choose_random_rent_time** - число от 1 до 7
- **choose_random_delivery_date** - случайная дата от 15 до 31 марта 2024
- **generate_random_id_or_track** - случайная строка из 7 цифр

### Методы для проверки тела ответа (check_response_methods):
Проверяем метод: получение списка заказов GET /api/v1/orders

**check_response(response)** - полная проверка структуры ответа

Аргумент: тело ответа после десереализации

Вызывает методы:
- check_orders(response) - проверяет наличие всех обязательных ключей в каждом заказе
- check_page_info(response) - проверяет наличие всех ключей
- check_available_stations(response) - проверяет наличие всех ключей в каждом элементе

Возвращает: 'OK', если все 3 метода вернули 'OK'











