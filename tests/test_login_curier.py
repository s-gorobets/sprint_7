import requests
import pytest
import data
from helpers import generate_random_string
from urls import *
from data import *
import allure
class TestLoginCurier:
    @allure.title('Успешная авторизация с существующими данными')
    @allure.description('Проверка статус-кода и тела ответа')
    def test_login(self):
        response = requests.post(LOGIN_CURIER_URL, data=User.my_courier_data)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Неуспешная авторизация при вводе невалидных данных')
    @allure.description('Проверка статус-кода и тела ответа')
    @pytest.mark.parametrize('empty_filds', data.empty_filds)
    def test_login_error_in_icorrect_data(self, empty_filds):
        response = requests.post(LOGIN_CURIER_URL, data=empty_filds)
        print(response.status_code)
        assert response.status_code == 400
        assert response.json() == Answer.BadRequest

    @allure.title('Неуспешная авторизация при вводе не всех обязательных полей')
    @allure.description('Проверка статус-кода и тела ответа')
    def test_login_with_unreal_data(self):
        payload = {"login": generate_random_string(10),
                   "password": generate_random_string(10),
                   "firstName": generate_random_string(10)
                   }
        response = requests.post(LOGIN_CURIER_URL, payload)
        assert response.status_code == 404
        assert response.json() == Answer.NotFound