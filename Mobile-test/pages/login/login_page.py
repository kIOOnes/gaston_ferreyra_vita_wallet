from core.gestures import Gestures
from core.elements import Elements
from core.waits import Waits
from appium.webdriver.common.appiumby import AppiumBy

# -------------------------
# LOCATORS
# -------------------------

START_SESSION_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Iniciar sesión")')
EMAIL_INPUT = (AppiumBy.XPATH, '(//android.widget.EditText)[1]')
PASSWORD_INPUT = (AppiumBy.XPATH, '(//android.widget.EditText)[2]')
LOGIN_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@text="Ingresar"]')

# -------------------------
# PAGE OBJECT
# -------------------------
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.elm = Elements(driver)
        self.gestures = Gestures(driver)
        self.waits = Waits(driver)

    def login(self, email, password):
        self.elm.click(START_SESSION_BUTTON)
        self.elm.click(EMAIL_INPUT)
        self.elm.send_keys(EMAIL_INPUT,email)
        self.elm.click(PASSWORD_INPUT)
        self.elm.send_keys(PASSWORD_INPUT,password)
        self.elm.click(LOGIN_BUTTON)

