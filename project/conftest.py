import allure
import pytest

from project.api.api_machine_steps import ApiMachineSteps
from project.test_data.constants import DefaultConsts
from project.config.ids import PinIds


@pytest.fixture(scope="session")
def api_terminal():
    api_terminal = ApiMachineSteps
    yield api_terminal


@pytest.fixture(autouse=True)
def clear_fields():
    with allure.step("Сlear input fields."):
        ApiMachineSteps.update_pin(PinIds.BATTERY_VOLTAGE, DefaultConsts.DEFAULT_ZERO)
