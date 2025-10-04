from core.gestures import Gestures
from core.elements import Elements
from core.waits import Waits
from appium.webdriver.common.appiumby import AppiumBy

# -------------------------
# LOCATORS
# -------------------------

TYPE_SELL_SELECT = (AppiumBy.XPATH, '//android.view.ViewGroup[@index="12"]')
TYPE_BUY_SELECT = (AppiumBy.XPATH, '//android.view.ViewGroup[@index="16"]')
SELL_AMOUNT_INPUT = (AppiumBy.XPATH, '(//android.widget.EditText)[1]')
ARS_SELECT = (AppiumBy.ACCESSIBILITY_ID, "ARS,   -  Peso Argentino")
USDT_SELECT = (AppiumBy.ACCESSIBILITY_ID, "USDT,   -  USD Tether")
CONTINUE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Continuar")

# -------------------------
# PAGE OBJECT
# -------------------------

class CryptoBuyPage:
    def __init__(self, driver):
            self.driver = driver
            self.elm = Elements(driver)
            self.gestures = Gestures(driver)
            self.waits = Waits(driver)
    
    def select_crypto_to_sell(self):
            self.elm.click(TYPE_SELL_SELECT)
            self.elm.click(ARS_SELECT)
            return
    
    def select_crypto_to_buy(self):
            self.elm.click(TYPE_BUY_SELECT)
            self.elm.click(USDT_SELECT)
            return
    
    def enter_amount_to_sell(self, amount):
            self.elm.click(SELL_AMOUNT_INPUT)
            self.elm.send_keys(SELL_AMOUNT_INPUT,amount)
            return
    
    def continue_operation(self):
            self.elm.click(CONTINUE_BUTTON)
            return