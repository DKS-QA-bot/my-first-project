"""Методы для проверки ответов наших запросов"""
import json

from requests import Response


class Checking:

    @staticmethod
    def check_status_code(response : Response, status_code ):
        """Метод для проверки статус кода"""
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f"Успешно !! Статус код = {response.status_code}")
        else:
            print(f"Провал !! Статус код = {response.status_code}")

    @staticmethod
    def checking_json_token(response: Response, expected_value):
        """Метод для проверки наличия обязательных полей в ответе запроса"""
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")


    @staticmethod
    def check_json_value(response , field_name, expected_value):
        """Метод для проверки """
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f"{field_name} верен!!")
