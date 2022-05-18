import allure
import requests


class BaseAPI:
    @staticmethod
    def send_get_request(api_endpoint, header_dict=None):
        with allure.step('Send GET request'):
            response = requests.get(api_endpoint, headers=header_dict)
            response.raise_for_status()
            return response

    @staticmethod
    def send_post_request(api_endpoint, body_data=None, body_json=None):
        with allure.step('Send POST request'):
            response = requests.post(api_endpoint, data=body_data, json=body_json)
            response.raise_for_status()
            return response

    @staticmethod
    def send_delete_request(api_endpoint):
        with allure.step('Send Delete request'):
            response = requests.delete(api_endpoint)
            response.raise_for_status()
            return response

    @staticmethod
    def send_put_request(api_endpoint, data=None):
        with allure.step('Send Put request'):
            response = requests.put(api_endpoint, data=data)
            response.raise_for_status()
            return response
