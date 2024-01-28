import allure
import helpers
import requests
from data import Urls


class TestUpdateUser:

    @allure.title('Изменение данных пользователя с авторизацией')
    def test_update_user_data_with_authorization_success(self, registered_user_return_token):
        access_token = registered_user_return_token
        new_data = helpers.payload
        response = requests.patch(Urls.UPDATE_USER, headers={'Authorization': access_token}, json=new_data)
        assert response.status_code == 200 and response.json().get('success')

    @allure.title('Изменение данных пользователя без авторизации')
    def test_update_user_data_without_authorization_error(self):
        payload = helpers.payload
        response = requests.patch(Urls.UPDATE_USER, json=payload)
        assert response.status_code == 401 and response.text == ('{"success":false,"message":"You should be '
                                                                 'authorised"}')
