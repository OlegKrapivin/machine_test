import pytest

from project.config.ids import PinIds
from project.test_data.constants import *
import allure


@pytest.mark.xfail
def test_all_pins_have_zero_volt(api_terminal):
    with allure.step("--> №1 step: (BatteryState == Error)"):
        api_terminal.update_pin(PinIds.BATTERY_VOLTAGE, DefaultConsts.DEFAULT_ZERO)

    with allure.step("--> №2 step: Gear_1 (Voltage == 0.01V)"):
        assert api_terminal.get_pin_state(PinIds.GEAR_1)['Voltage'] == DefaultConsts.DEFAULT_ZERO,\
            "Volts value is not correct."

    with allure.step("--> №3 step: Gear_2 (Voltage == 0.01V)"):
        assert api_terminal.get_pin_state(PinIds.GEAR_2)['Voltage'] == DefaultConsts.DEFAULT_ZERO, \
            "Volts value is not correct."

    with allure.step("--> №4 step: AccPedal (Voltage == 0.01V)"):
        assert api_terminal.get_pin_state(PinIds.ACC_PEDAL)['Voltage'] == DefaultConsts.DEFAULT_ZERO,\
            "Volts value is not correct."

    with allure.step("--> №5 step: BreakPedal (Voltage == 0.01V)"):
        assert api_terminal.get_pin_state(PinIds.BRAKE_PEDAL)['Voltage'] == DefaultConsts.DEFAULT_ZERO, \
            "Volts value is not correct."

    with allure.step("--> №6 step: BatteryVoltage (Voltage == 0.0V)"):
        assert api_terminal.get_pin_state(PinIds.BATTERY_VOLTAGE)['Value'] == DefaultConsts.DEFAULT_ZERO,\
            "Volts value is not correct."
