import allure
import requests
import pytest
import data
import json
from urls import *
class TestCreatOrder:
    @allure.title('Проверка создания заказа при разных параметрах цвета')
    @allure.description('Проверка статус-кода и тела ответа')
    @pytest.mark.parametrize('order_filds', data.order_filds)
    def test_creat_order(self, order_filds):
        order_data = json.dumps(order_filds)
        response = requests.post(CREAT_ORDER_URL, order_data)
        assert response.status_code == 201 and 'track' in response.text