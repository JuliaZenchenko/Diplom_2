import allure
import pytest
import requests

from helper import Helper
from stellar_burgers_api import StellarBurgesApi
from data import *


class TestChangeDataUser:
    @allure.title('Проверка изменения данных у авторизованного пользователя')
    def test_change_data_auth_user(self, new_body):
        response = StellarBurgesApi.auth_user(new_body)
        token = response.json().get('accessToken')
        modified_data = Helper.generate_create_user_with_modified_field()
        response = StellarBurgesApi.remove_user_data(modified_data, token)
        assert response.status_code in (200, 403)
        if response.status_code == 403:
            assert response.json().get('success') is False and response.json().get(
                'message') == Messages.ERROR_403_EMAIL_ALREADY_EXISTS
        else:  # Если статус 200
            assert response.json()['success'] is True

        delete_response = StellarBurgesApi.delete_user(token)
        assert delete_response.status_code == 202 and delete_response.json()["message"] == "User successfully removed"

    @pytest.mark.parametrize("new_user_body", [
        {"email": "", "name": "Name", "password": "Password"},  # Пустой email
        {"email": "test@yandex.ru", "name": "", "password": "Password"},  # Пустое имя
        {"email": "test@yandex.ru", "name": "Name", "password": ""}  # Пустой пароль
    ])
    @allure.title("Проверка сохранения изменений у пользователя без авторизации")
    def test_change_data_no_auth_user(self, new_user_body):
        response = requests.patch(Urls.BASE_URL + Urls.DATA_USER, json=new_user_body)
        assert response.status_code == 401 and response.json()[
            'message'] == Messages.ERROR_401_AUTHORIZED_FOR_ORDER_LIST
