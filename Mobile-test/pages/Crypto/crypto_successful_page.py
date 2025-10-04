from core.gestures import Gestures
from core.elements import Elements
from core.waits import Waits
from appium.webdriver.common.appiumby import AppiumBy

# -------------------------
# LOCATORS
# -------------------------

RETURN_HOME_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ir al inicio")')

# -------------------------
# PAGE OBJECT
# -------------------------

class CryptoSuccesfulPage:
    def __init__(self, driver):
            self.driver = driver
            self.elm = Elements(driver)
            self.gestures = Gestures(driver)
            self.waits = Waits(driver)

    def return_home(self):
            self.elm.click(RETURN_HOME_BUTTON)