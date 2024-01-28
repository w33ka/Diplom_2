import requests
import allure
from data import Urls


class TestLogInUser:

    @allure.title('Проверка логина под существующим пользователем')
    def test_login_success(self, registered_user_return_log_pass):
        payload = registered_user_return_log_pass
        response = requests.post(Urls.LOGIN_USER, json=payload)
        assert response.status_code == 200 and response.json().get('success')

    @allure.title('Проверка логина с неверным логином и паролем')
    def test_login_with_incorrect_log_and_pass_error(self):
        payload = {
            "email": "incorrect_email@yandex.ru",
            "password": "123456"
        }

        response = requests.post(Urls.LOGIN_USER, json=payload)
        assert response.status_code == 401 and response.text == ('{"success":false,"message":"email or password are '
                                                                 'incorrect"}')
