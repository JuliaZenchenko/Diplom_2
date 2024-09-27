import allure

from helper import Helper
from stellar_burgers_api import StellarBurgesApi
from data import *


class TestOrder:
    @allure.title("Проверка создания заказа c авторизацией с ингредиентами")
    def test_order_with_login_and_ingredients(self, new_body):
        response = StellarBurgesApi.create_user(new_body)
        token = response.json()['accessToken']
        ingredient = StellarBurgesApi.get_random_ingredients()
        created_order = (StellarBurgesApi.order_create(ingredient, token))
        assert created_order.status_code == 200 and created_order.json()['success'] is True
        delete_response = StellarBurgesApi.delete_user(token)
        assert delete_response.status_code == 202 and delete_response.json()["message"] == Messages.MESSAGE_SUCCESSFULLY_REMOVED

    @allure.title("Проверка создания заказа c авторизацией без ингредиентов")
    def test_order_with_login_without_ingredients(self, new_body):
        response = StellarBurgesApi.create_user(new_body)
        token = response.json()['accessToken']
        ingredient = []
        created_order = StellarBurgesApi.order_create(ingredient, token)
        assert created_order.status_code == 400 and created_order.json()['success'] is False
        delete_response = StellarBurgesApi.delete_user(token)
        assert delete_response.status_code == 202 and delete_response.json()["message"] == Messages.MESSAGE_SUCCESSFULLY_REMOVED

    @allure.title("Проверка создания заказа c авторизацией с неверным хэшем ингредиента")
    def test_order_with_login_and_incorrect_ingredients(self, new_body):
        response = StellarBurgesApi.create_user(new_body)
        token = response.json()['accessToken']
        invalid_ingredient = [ID.NON_EXISTENT_ID]
        created_order = StellarBurgesApi.order_create(invalid_ingredient, token)
        assert created_order.status_code == 500
        delete_response = StellarBurgesApi.delete_user(token)
        assert delete_response.status_code == 202 and delete_response.json()["message"] == Messages.MESSAGE_SUCCESSFULLY_REMOVED

    @allure.title("Проверка создания заказа без авторизации с ингредиентами")
    def test_order_without_login_with_ingredients(self):
        token = ''
        ingredient = Helper.get_random_ingredients()
        created_order = StellarBurgesApi.order_create(ingredient, token)
        assert created_order.status_code == 200 and created_order.json()['success'] is True

    @allure.title("Проверка создания заказа без авторизации без ингредиентов")
    def test_order_without_login_and_without_ingredients(self):
        token = ''
        ingredient = []
        created_order = StellarBurgesApi.order_create(ingredient, token)
        assert created_order.status_code == 400 and created_order.json()['success'] is False

    @allure.title("Проверка создания заказа без авторизации с неверным хэшем ингредиента")
    def test_order_without_login_and_incorrect_ingredients(self):
        token = ''
        invalid_ingredient = [ID.NON_EXISTENT_ID]
        created_order = StellarBurgesApi.order_create(invalid_ingredient, token)
        assert created_order.status_code == 500

