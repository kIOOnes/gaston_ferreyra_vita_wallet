from core.gestures import Gestures
from core.elements import Elements
from core.waits import Waits
from appium.webdriver.common.appiumby import AppiumBy

# -------------------------
# LOGIN LOCATORS
# -------------------------

ACCEPT_BUTTON_POP_UP = (AppiumBy.ACCESSIBILITY_ID, "Entendido")

# -------------------------
# PAGE OBJECT
# -------------------------

class HomePage:
    def __init__(self, driver):
            self.driver = driver
            self.elm = Elements(driver)
            self.gestures = Gestures(driver)
            self.waits = Waits(driver)

    def quit_pop_up(self, driver):
            self.elm.click(ACCEPT_BUTTON_POP_UP)
