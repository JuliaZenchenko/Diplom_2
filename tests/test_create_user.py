import allure

from helper import Helper
from conftest import new_body
from data import Messages
from stellar_burgers_api import StellarBurgesApi


class TestCreateUser:
    @allure.title('Проверка, что можно создать пользователя c заполнением '
                  'всех обяз полей и запрос возвращает правильный ответ')
    def test_create_user(self, new_body):
        response = StellarBurgesApi.create_user(new_body)
        assert (response.status_code == 200 and 'accessToken' in response.json() and response.json()['success'] is True)
        token = response.json().get('accessToken')
        delete_response = StellarBurgesApi.delete_user(token)
        assert delete_response.status_code == 202 and delete_response.json()["message"] == "User successfully removed"

    @allure.title('Проверка, что нельзя создать пользователя, который уже зарегистрирован')
    def test_create_same_user(self, new_body):
        user_1 = StellarBurgesApi.create_user(new_body)
        user_2 = StellarBurgesApi.create_user(new_body)
        assert user_2.status_code == 403 and user_2.json()['message'] == Messages.ERROR_403_DUBLICATE
        token = user_1.json().get('accessToken')
        delete_response = StellarBurgesApi.delete_user(token)
        assert delete_response.status_code == 202 and delete_response.json()["message"] == "User successfully removed"

    @allure.title('Проверка, что нельзя создать пользователя и не заполнить одно из обязательных полей')
    def test_create_user_without_login(self):
        response = StellarBurgesApi.create_user(Helper.generate_create_user_without_one_field())
        message = response.json()
        assert response.status_code == 403 and message['message'] == Messages.ERROR_403_WITHOUT_DATE


