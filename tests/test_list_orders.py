import requests
from urls import *
import allure

class TestListsOrders:
    @allure.title('Получение списка заказов')
    @allure.description('Проверка статус-кода и тела ответа')
    def test_all_lists_orders(self):
        response = requests.get(LIST_ORDERS_URL)
        assert response.status_code == 200 and type(response.json()['orders']) == list