from core.gestures import Gestures
from core.elements import Elements
from core.waits import Waits
from appium.webdriver.common.appiumby import AppiumBy

# -------------------------
# LOCATORS
# -------------------------

CONFIRM_OPERATION_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Confirmar")')

# -------------------------
# PAGE OBJECT
# -------------------------

class CryptoConfirm:
    def __init__(self, driver):
        self.driver = driver
        self.elm = Elements(driver)
        self.gestures = Gestures(driver)
        self.waits = Waits(driver)

    def confirm(self):
        self.elm.wait_for_enabled(CONFIRM_OPERATION_BUTTON)
        self.elm.click(CONFIRM_OPERATION_BUTTON)