from project.config.ids import PinIds, SignalIds
from project.test_data.constants import *
import allure


def test_press_brake_after_acc_30(api_terminal):
    with allure.step("--> №1 step: (BatteryState == Ready)"):
        api_terminal.update_pin(PinIds.BATTERY_VOLTAGE, BatteryConsts.DEFAULT_VOLTAGE)

    with allure.step("--> №2 step: (BrakePedalState == Pressed)"):
        api_terminal.update_pin(PinIds.BRAKE_PEDAL, BrakePedalConsts.PRESSED)

    with allure.step("--> №3 step: (Dear Shifter == Drive)"):
        api_terminal.update_pins(GearsConsts.DRIVE_GEAR1, GearsConsts.DRIVE_GEAR2)

    with allure.step("--> №4 step: (AccPedalPos == 0%)"):
        api_terminal.update_pin(PinIds.ACC_PEDAL, AccPedalConsts.ACC_ZERO)

    with allure.step("--> №5 step: (BrakePedalState == Released)"):
        api_terminal.update_pin(PinIds.BRAKE_PEDAL, BrakePedalConsts.RELEASED)

    with allure.step("--> №6 step: (AccPedalPos == 30%)"):
        api_terminal.update_pin(PinIds.ACC_PEDAL, AccPedalConsts.ACC_THIRSTY)

    with allure.step("--> №7 step: (BrakePedalState == Pressed)"):
        api_terminal.update_pin(PinIds.BRAKE_PEDAL, BrakePedalConsts.PRESSED)

    with allure.step("--> Expected result."):
        assert api_terminal.get_signal_state(SignalIds.REQ_TORQUE)['Value'] == AccPedalConsts.STR_ZERO_NM, \
            "ReqTorque value is not correct"
