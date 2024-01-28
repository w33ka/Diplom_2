import pytest
import requests
import allure

import helpers
from data import Urls


class TestCreateUser:
    @allure.title('Регистрация нового пользователя')
    def test_register_user_success(self, registered_user_return_response):
        response = registered_user_return_response
        assert response.status_code == 200 and response.json().get('success')

    @allure.title('Регистрация уже существующего пользователя')
    def test_register_existing_user_error(self, registered_user_return_log_pass):
        payload = registered_user_return_log_pass
        response = requests.post(Urls.REGISTER_USER, json=payload)
        assert response.status_code == 403 and response.text == '{"success":false,"message":"User already exists"}'

    @allure.title('Регистрация пользователя без обязательного поля')
    @pytest.mark.parametrize("field_to_remove", ["email", "password", "name"])
    def test_register_user_without_required_field_error(self, field_to_remove):
        payload = helpers.payload.copy()
        payload.pop(field_to_remove)
        response = requests.post(Urls.REGISTER_USER, json=payload)
        assert response.status_code == 403 and response.text == ('{"success":false,"message":"Email, password and name '
                                                                 'are required fields"}')