import allure
import requests
import random

from data import Urls


class StellarBurgesApi:
    @allure.step('Создание пользователя')
    def create_user(body) -> object:
        return requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=body)

    @staticmethod
    @allure.step('Авторизация пользователя')
    def auth_user(body):
        StellarBurgesApi.create_user(body)
        response = requests.post(Urls.BASE_URL + Urls.LOGIN_USER, json=body)
        return response

    @allure.step("Метод для внесения изменений в данные пользователя")
    def remove_user_data(body, token):
        header = {"Authorization": token}
        return requests.patch(Urls.BASE_URL + Urls.DATA_USER, json=body, headers=header)

    @staticmethod
    @allure.step('Возвращаем ответ на запрос (удаление пользователя)')
    def delete_user(token):
        response = requests.delete(Urls.BASE_URL+Urls.DATA_USER, headers={'Authorization': token})
        return response

    @staticmethod
    @allure.step("Метод для получения списка ингредиентов")
    def ingredients_get_method():
        return requests.get(Urls.BASE_URL + Urls.INGRIDIENTS_URL)

    @allure.step('Создать заказ')
    def order_create(ingredients, token):
        payload = {"ingredients": ingredients}
        header = {"Authorization": token}
        return requests.post(Urls.BASE_URL + Urls.ORDER, json=payload, headers=header)

    @allure.step("Метод для получения списка заказов")
    def list_of_orders(token):
        header = {"Authorization": token}
        return requests.get(Urls.BASE_URL + Urls.ORDER, headers=header)

    @allure.step("Генерируем рандомный список ингредиентов")
    def get_random_ingredients():
        response = StellarBurgesApi.ingredients_get_method()
        # Получаем список id ингредиентов
        ingredients = [ingredient['_id'] for ingredient in response.json()['data']]
        # Выбираем 3 случайных ингредиента
        random_ingredients_list = random.sample(ingredients, k=3)
        return random_ingredients_list

