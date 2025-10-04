from core.gestures import Gestures
from core.elements import Elements
from core.waits import Waits
from appium.webdriver.common.appiumby import AppiumBy

# -------------------------
# LOGIN LOCATORS
# -------------------------

TYPE_SEND_SELECT = (AppiumBy.XPATH, '//android.view.ViewGroup[@index="12"]')
TYPE_BUY_SELECT = (AppiumBy.XPATH, '//android.view.ViewGroup[@index="16"]')
SELL_AMOUNT_INPUT = (AppiumBy.XPATH, '(//android.widget.EditText)[1]')
BUY_AMOUNT_INPUT =(AppiumBy.XPATH, '(//android.widget.EditText)[2]')
ARS_SELECT = (AppiumBy.ACCESSIBILITY_ID, "ARS,   -  Peso Argentino")
BTC_SELECT = (AppiumBy.ACCESSIBILITY_ID, "BTC,   -  Bitcoin")
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
    
    def select_crypto_to_send(self, driver, crypto_type):
            self.elm.click()
            return
    
    def select_crypto_to_buy(self, driver, crypto_type):
            return
    
    def enter_amount_to_sell(self, driver, amount):
            
            return
    
    def enter_amount_to_buy(self, driver, amount):
            return

    
    