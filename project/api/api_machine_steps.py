from project.config.api_endpoints import ApiEndpoints
from framework.base_api.base_api import BaseAPI
import allure


class ApiMachineSteps:
    """
    Class for working with BaseAPI
    """

    @staticmethod
    def update_pin(pin_id: int, voltage: float) -> dict:
        """
            Method "update_pin" that to make update pin
            @return: response - answer after post request
            @param: pin_id - if of pin
                   voltage - volts by pin
        """
        with allure.step("Use update_pin func id: {} voltage: {}.".format(pin_id, voltage)):
            end_point = ApiEndpoints.UPD_PIN.format(pin_id)
            response = BaseAPI.send_post_request(api_endpoint=end_point, body_data={"Voltage": voltage}).json()
            return response

    @staticmethod
    def update_pins(voltage_1: float, voltage_2: float) -> dict:
        """
           Method "update_pins" that to make update pins
           @return: response - answer after post request
           @param: voltage_1 - if of pin
                  voltage_2 - volts by pin
        """
        with allure.step("Use update_pins by {} volt and {} volt.".format(voltage_1, voltage_2)):
            end_point = ApiEndpoints.UPD_PINS
            json = {"Pins": [{"PinId": 1, "Voltage": voltage_1}, {"PinId": 2, "Voltage": voltage_2}]}
            response = BaseAPI.send_post_request(api_endpoint=end_point, body_json=json).json()
            return response

    @staticmethod
    def get_pin_state(pin_id: int) -> dict:
        """
            Method "get_pin_state" that to get pin state
            @return: response - answer after get request
            @param: pin_id - id of pin
        """
        with allure.step("Use get_pin_state func for id: {}.".format(pin_id)):
            end_point = ApiEndpoints.GET_PIN.format(pin_id)
            response = BaseAPI.send_get_request(end_point).json()
            return response

    @staticmethod
    def get_pins_state() -> dict:
        """
            Method "get_pins_state" that to get pins state
            @return: response - answer after get request
        """
        with allure.step("Use get_pins_state."):
            end_point = ApiEndpoints.PINS
            response = BaseAPI.send_get_request(end_point).json()
            return response

    @staticmethod
    def get_signal_state(sig_id: int) -> dict:
        """
           Method "get_signal_state" that get signal state
           @return: response - answer after get request
           @param: sig_id - id of signal
       """
        with allure.step("Use get_signal_state func for id: {}.".format(sig_id)):
            end_point = ApiEndpoints.GET_SIG.format(sig_id)
            response = BaseAPI.send_get_request(end_point).json()
            return response

    @staticmethod
    def get_signals_state() -> dict:
        """
            Method "get_signals_state" that to get signals state
            @return: response - answer after get request
        """
        with allure.step("Use get_signals_state."):
            end_point = ApiEndpoints.SIGNALS
            response = BaseAPI.send_get_request(end_point).json()
            return response
