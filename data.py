from helpers import generate_random_string
class User:
    my_login = 'witcher'
    my_courier_data = {'login': 'witcher1', 'password': '1234', 'firstName': 'herald'}
    my_courier_with_wrong_password = {'login': 'witcher', 'password': '1234'}


class Answer:
    NotFound = {
    'code': 404,
    'message': 'Учетная запись не найдена'
    }

    Сonflict = {
    'code': 409,
    'message': 'Этот логин уже используется. Попробуйте другой.'
    }

    BadRequest = {
    'code': 400,
    'message': 'Недостаточно данных для входа'
    }

    Created = {
    'ok': True
    }

    BadRequestCreat = {
    'code': 400,
    'message': 'Недостаточно данных для создания учетной записи'
    }

empty_filds = \
    {"login": '',
     "password": generate_random_string(10),
     "firstName": generate_random_string(10)
     },\
        {"login": generate_random_string(10),
     "password": '',
     "firstName": generate_random_string(10)
     },\
        {"login": '',
         "password": '',
         "firstName": ''
         }

order_filds ={
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}, \
    {
    "firstName": "Vi",
    "lastName": "Vinsent",
    "address": "Night-City",
    "metroStation": 4,
    "phone": "+7 923 422 12 54",
    "rentTime": 4,
    "deliveryDate": "2022-01-01",
    "comment": "Если надо убить — убивай. Если надо всё сжечь дотла... пусть горит",
    "color": [
        "GREY"
    ]
}, \
    {
    "firstName": "Vi",
    "lastName": "Vinsent",
    "address": "Night-City",
    "metroStation": 4,
    "phone": "+7 923 422 12 54",
    "rentTime": 4,
    "deliveryDate": "2022-01-01",
    "comment": "Если надо убить — убивай. Если надо всё сжечь дотла... пусть горит",
    "color": [
        "GREY",
        "BLACK"
    ]
}