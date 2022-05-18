from project.config.urls import Urls


class ApiEndpoints:
    URL = Urls.URL
    API = URL + 'api/'
    PINS = API + 'pins'
    GET_PIN = PINS + '/{}'
    SIGNALS = API + 'signals'
    GET_SIG = SIGNALS + '/{}'
    UPD_PIN = PINS + '/{}/update_pin'
    UPD_PINS = PINS + '/update_pins'
