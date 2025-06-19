import requests
import pytest
import data
from urls import *
from data import *
import allure
from conftest import delet_curier
class TestCreatingCurier:
    @allure.title('Создание курьера с валидными данными')
    @allure.description('Проверка статус-кода и тела ответа')
    def test_creat_curier(self):
        payload = {"login": generate_random_string(10),
                   "password": generate_random_string(10),
                   "firstName": generate_random_string(10)
                   }
        response = requests.post(CREAT_CURIER_URL, payload)
        assert response.status_code == 201
        assert response.json() == Answer.Created
        assert response.json()['ok'] == True

        courier_id = response.json().get("id")
        if courier_id:
            delet_curier.append(courier_id)

    @allure.title('Создание курьера с уже существующим логином')
    @allure.description('Проверка статус-кода и тела ответа')
    def test_dont_creat_same_curier(self):
        payload = {"login": User.my_login,
                   "password": generate_random_string(10),
                   "firstName": generate_random_string(10)
                   }
        response = requests.post(CREAT_CURIER_URL, payload)
        assert response.status_code == 409
        assert response.json() == Answer.Сonflict

    @allure.title('Создание курьера без заполнения обязательных полей')
    @allure.description('Проверка статус-кода и тела ответа')
    @pytest.mark.parametrize('empty_filds', data.empty_filds)
    def test_no_required_fields(self, empty_filds):
        response = requests.post(CREAT_CURIER_URL, data=empty_filds)
        assert response.status_code == 400
        assert response.json() == Answer.BadRequestCreat
