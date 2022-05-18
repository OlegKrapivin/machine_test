import allure
import pytest

from project.config.ids import PinIds, SignalIds
from project.test_data.constants import *


@pytest.mark.parametrize("value, state", [(LimitConsts.FIVE_HUNDRED, BatteryConsts.READY_STATE),
                                          (LimitConsts.ALMOST_EIGHT_HUNDRED, BatteryConsts.READY_STATE),
                                          (BatteryConsts.DEFAULT_VOLTAGE, BatteryConsts.READY_STATE),
                                          (DefaultConsts.DEFAULT_ONE, BatteryConsts.NOT_READY_STATE),
                                          (LimitConsts.TWO_HUNDRED, BatteryConsts.NOT_READY_STATE),
                                          (LimitConsts.FOUR_HUNDRED, BatteryConsts.NOT_READY_STATE)])
def test_battery_component_boundary_values(api_terminal, value, state):
    with allure.step("--> №1 step: (BatteryState == Ready)"):
        api_terminal.update_pin(PinIds.BATTERY_VOLTAGE, value)

    with allure.step("--> Expected result."):
        assert api_terminal.get_signal_state(SignalIds.BATTERY_STATE)['Value'] == state, \
            "Battery state is not correct"
