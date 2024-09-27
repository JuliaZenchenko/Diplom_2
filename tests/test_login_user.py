import allure

from helper import Helper
from stellar_burgers_api import StellarBurgesApi
from data import Messages


class TestLoginUser:
    @allure.title('Проверка авторизации существующего пользователя')
    def test_login_user_positive(self, new_body):
        response = StellarBurgesApi.auth_user(new_body)
        assert response.status_code == 200
        token = response.json().get('accessToken')
        delete_response = StellarBurgesApi.delete_user(token)
        assert delete_response.status_code == 202 and delete_response.json()["message"] == Messages.MESSAGE_SUCCESSFULLY_REMOVED

    allure.title("Проверка авторизации несуществующего пользователя")
    def test_login_user_negativ(self):
        login_user = StellarBurgesApi.auth_user(Helper.generate_user())
        assert login_user.status_code == 401 and login_user.json()['message'] == Messages.ERROR_401_AUTHORIZED

