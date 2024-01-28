import allure
from data import Urls
import requests


class TestGetOrders:

    @allure.title('Получение заказа авторизованного пользователя')
    def test_get_order_authorized_user_success(self, registered_user_return_token):
        access_token = registered_user_return_token
        response = requests.get(Urls.GET_ORDERS, headers={'Authorization': access_token})
        assert response.status_code == 200 and response.json().get('success')

    @allure.title('Получение заказа неавторизованного пользователя')
    def test_get_order_unauthorized_user_error(self):
        response = requests.get(Urls.GET_ORDERS)
        assert response.status_code == 401 and response.text == ('{"success":false,"message":"You should be '
                                                                 'authorised"}')

