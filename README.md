## Дипломный проект. Задание 2: API-тесты

### API тесты для Stellar Burgers

### Структура проекта

- `tests` - пакет, содержащий тесты:
  - `test_create_order.py`
  - `test_create_user.py`
  - `test_get_user_orders.py`
  - `test_login.py`
  - `test_update_user_data.py`
- `allure-report` - папка с отчетом allure
- `conftest.py`
- `data.py`
- `helpers.py`
- `requirements.txt`
- `README.md`

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов**

>  `$pytest -v ./tests`