import random
import allure
import requests

from data import Urls

@allure.step('Создание тестового пользователя и возврат данных для авторизации')
def create_and_return_user():
    email = f'{random.randint(100, 1000000)}@testdomain.com'
    password = f'{random.randint(100000, 1000000)}'
    name = f'{random.randint(100, 1000000)}'
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    url = f'{Urls.BASE_URL}{Urls.CREATE_USER_URL}'
    requests.post(url=url, json=payload)
    return payload

@allure.step('Удаление тестового пользователя')
def login_and_delete_user(payload):
    url = f'{Urls.BASE_URL}{Urls.LOGIN_USER_URL}'
    token = requests.post(url=url, json=payload).json().get('accessToken')
    headers = {'Authorization': token}
    url = f'{Urls.BASE_URL}{Urls.USER_URL}'
    requests.delete(url=url, headers=headers)