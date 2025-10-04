from core.gestures import Gestures
from core.elements import Elements
from core.waits import Waits
from appium.webdriver.common.appiumby import AppiumBy

# -------------------------
# LOGIN LOCATORS
# -------------------------

ACCEPT_BUTTON_POP_UP = (AppiumBy.ACCESSIBILITY_ID, "Entendido")
CRYPTO_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Cripto")
LAST_MOVEMENTS_BUTTON = (AppiumBy.XPATH, '(//android.view.ViewGroup[@clickable="true" and contains(@content-desc, "Intercambio")])[1]')

# -------------------------
# PAGE OBJECT
# -------------------------

class HomePage:
    def __init__(self, driver):
            self.driver = driver
            self.elm = Elements(driver)
            self.gestures = Gestures(driver)
            self.waits = Waits(driver)

    def quit_pop_up(self):
        if(self.elm.is_present):
            self.elm.click(ACCEPT_BUTTON_POP_UP)
        return
    
    def go_crypto(self):
        self.elm.click(CRYPTO_BUTTON)

    def view_last_movements(self):
        self.waits.seconds_sleep(5)
        self.elm.click(LAST_MOVEMENTS_BUTTON)