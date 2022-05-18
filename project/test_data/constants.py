class BatteryConsts:
    DEFAULT_VOLTAGE = 800
    READY_STATE = 'Ready'
    NOT_READY_STATE = 'NotReady'


class GearsConsts:
    PARK_GEAR1 = 0.67
    NEUTRAL_GEAR1 = 1.48
    REVERSE_GEAR1 = 2.28
    DRIVE_GEAR1 = 3.12

    PARK_GEAR2 = 3.12
    NEUTRAL_GEAR2 = 2.28
    REVERSE_GEAR2 = 1.48
    DRIVE_GEAR2 = 0.67


class BrakePedalConsts:
    PRESSED = 1
    RELEASED = 2


class AccPedalConsts:
    ACC_ZERO = 1
    ACC_THIRSTY = 2
    ACC_FIFTY = 2.5
    ACC_HUNDRED = 3

    STR_THIRSTY = "30 %"
    STR_FIFTY = "50 %"
    STR_HUNDRED = "100 %"
    STR_ZERO_NM = "0 Nm"


class LimitConsts:
    FIVE_HUNDRED = 500
    ALMOST_EIGHT_HUNDRED = 799
    TWO_HUNDRED = 200
    FOUR_HUNDRED = 400


class DefaultConsts:
    DEFAULT_ZERO = 0.0
    DEFAULT_ONE = 1
