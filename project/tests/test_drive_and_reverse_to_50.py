import pytest
import allure

from project.config.ids import PinIds, SignalIds
from project.test_data.constants import *


@pytest.mark.parametrize("result, gear1, gear2", [('Drive', GearsConsts.DRIVE_GEAR1, GearsConsts.DRIVE_GEAR2),
                                                  ('Reverse', GearsConsts.REVERSE_GEAR1, GearsConsts.REVERSE_GEAR2)])
def test_drive_and_reverse_to_50(api_terminal, result, gear1, gear2):
    with allure.step("--> №1 step: (BatteryState == Ready)"):
        api_terminal.update_pin(PinIds.BATTERY_VOLTAGE, BatteryConsts.DEFAULT_VOLTAGE)

    with allure.step("--> №2 step: (BrakePedalState == Pressed)"):
        api_terminal.update_pin(PinIds.BRAKE_PEDAL, BrakePedalConsts.PRESSED)

    with allure.step(f"--> №3 step: (Dear Shifter == {result})"):
        api_terminal.update_pins(gear1, gear2)

    with allure.step("--> №4 step: (AccPedalPos == 0%)"):
        api_terminal.update_pin(PinIds.ACC_PEDAL, AccPedalConsts.ACC_ZERO)

    with allure.step("--> №5 step: (BrakePedalState == Released)"):
        api_terminal.update_pin(PinIds.BRAKE_PEDAL, BrakePedalConsts.RELEASED)

    with allure.step("--> №6 step: (AccPedalPos == 30%)"):
        api_terminal.update_pin(PinIds.ACC_PEDAL, AccPedalConsts.ACC_THIRSTY)

    with allure.step("--> №7 step: (AccPedalPos == 50%)"):
        api_terminal.update_pin(PinIds.ACC_PEDAL, AccPedalConsts.ACC_FIFTY)

    with allure.step("--> Expected result."):
        assert api_terminal.get_signal_state(SignalIds.ACC_PEDAL_POS)['Value'] == AccPedalConsts.STR_FIFTY, \
            "AccPedalPos is not correct."
        assert api_terminal.get_signal_state(SignalIds.GEAR_POSITION)['Value'] == result, \
            "GearPosition is not correct."
