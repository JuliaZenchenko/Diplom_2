import allure
import random

from faker import Faker
from stellar_burgers_api import StellarBurgesApi
from random import choice


class Helper:
    @allure.step('Генерация почты пароля имени для юзера')
    def generate_create_user():
        fake = Faker()
        body = {
            "email": fake.email(domain="yandex.ru"),
            "password": fake.password(),
            "name": fake.first_name()
        }
        return body

    @allure.step('Генерация почты пароля имени для юзера без одного поля')
    def generate_create_user_without_one_field():
        user_body = Helper.generate_create_user()
        field_to_delete = random.choice(list(user_body.keys()))
        del user_body[field_to_delete]
        return user_body

    @allure.step('Генерация почты пароля имени для несуществующего юзера')
    def generate_user():
        fake = Faker()
        body = {
            "email": fake.email(domain="yandex.ru"),
            "password": fake.password()
        }
        return body

    @allure.step('Генерация почты, пароля и имени для юзера с изменением одного поля')
    def generate_create_user_with_modified_field():
        user_body = Helper.generate_create_user()
        field_to_modify = random.choice(list(user_body.keys()))  # Выбираем поле для изменения
        if field_to_modify == 'email':    # Изменяем значение выбранного поля
            user_body[field_to_modify] = "modified_email@yandex.ru"
        elif field_to_modify == 'name':
            user_body[field_to_modify] = "Modified Name"
        elif field_to_modify == 'password':
            user_body[field_to_modify] = "NewPassword123"
        return user_body

    @allure.step("Генерируем рандомный список ингредиентов")
    def get_random_ingredients():
        response = StellarBurgesApi.ingredients_get_method()
        ingredients = []

        for ingredient in response.json()['data']:
            ingredients.append(ingredient['_id'])

        random_ingredients_list = []
        for ingredient in range(3):
            random_ingredients_list.append(choice(ingredients))

        return random_ingredients_list
