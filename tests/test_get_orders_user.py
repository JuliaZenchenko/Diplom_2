import allure

from helper import Helper
from stellar_burgers_api import StellarBurgesApi
from data import *


class TestGetOrdersUser:
    @allure.title("Проверка получения заказов конкретного авторизованного пользователя")
    def test_get_order_list_for_login_user(self, new_body):
        response = StellarBurgesApi.create_user(new_body)
        token = response.json()['accessToken']
        ingredient = Helper.get_random_ingredients()
        StellarBurgesApi.order_create(ingredient, token)
        order_list = StellarBurgesApi.list_of_orders(token)
        assert order_list.status_code == 200 and order_list.json()['success'] is True
        token = response.json().get('accessToken')
        delete_response = StellarBurgesApi.delete_user(token)
        assert delete_response.status_code == 202 and delete_response.json()["message"] == "User successfully removed"

    @allure.title("Проверка получения списка заказов неавторизованного пользователя")
    def test_get_order_list_without_login_user(self):
        token = ''
        ingredient = Helper.get_random_ingredients()
        StellarBurgesApi.order_create(ingredient, token)
        order_list = StellarBurgesApi.list_of_orders(token)
        assert order_list.status_code == 401 and order_list.json()['success'] is False and order_list.json()[
            'message'] == Messages.ERROR_401_AUTHORIZED_FOR_ORDER_LIST

