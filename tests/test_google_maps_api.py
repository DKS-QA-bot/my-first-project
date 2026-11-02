import json
import allure
from utils.api import GoogleMapsApi
from requests import Response

from utils.cheking import Checking

"""Создание изменение и удалени новой локации"""
@allure.epic("Test create place")
class Test_create_place():

    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):

        print('\nMethod Post')
        result_post = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post,200)
        Checking.checking_json_token(result_post,['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post,'status','OK')



        print("\nМетод Get POST")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get,200)
        Checking.checking_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')




        print("\nМетод Put")
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put,200)
        Checking.checking_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("\nМетод Get PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get,200)
        Checking.checking_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website','language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("\nМетод Delete")
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete,200)
        Checking.checking_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')



        print("\nМетод Get Delete")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get,404)
        Checking.checking_json_token(result_get,['msg'])
        Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")



        print("Тестирование создание, изменение и удаления новой локации прошло успешно")
