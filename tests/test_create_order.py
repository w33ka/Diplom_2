import allure
from data import Ingredients
from data import Urls
import requests


class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_authorization_success(self, registered_user_return_token):
        access_token = registered_user_return_token
        payload = Ingredients.INGREDIENT
        response = requests.post(Urls.CREATE_ORDER, headers={'Authorization': access_token}, json=payload)
        assert response.status_code == 200 and response.json().get('success')

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_authorization_success(self):
        payload = Ingredients.INGREDIENT
        response = requests.post(Urls.CREATE_ORDER, json=payload)
        assert response.status_code == 200 and response.json().get('success')

    @allure.title('Создание заказа без ингредиента')
    def test_create_order_without_ingredients_error(self):
        payload = []
        response = requests.post(Urls.CREATE_ORDER, json=payload)
        assert response.status_code == 400 and response.text == ('{"success":false,"message":"Ingredient ids must be '
                                                                 'provided"}')

    @allure.title('Создание заказа с неверным хешем ингредиента')
    def test_create_order_with_invalid_hash_error(self):
        payload = Ingredients.INVALID_INGREDIENTS
        response = requests.post(Urls.CREATE_ORDER, json=payload)
        assert response.status_code == 500
