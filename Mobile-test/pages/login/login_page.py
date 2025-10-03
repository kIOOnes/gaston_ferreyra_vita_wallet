from core.gestures import Gestures
from core.elements import Elements
from core.waits import Waits
from selenium.webdriver.common.by import By

# -------------------------
# LOGIN LOCATORS
# -------------------------
START_SESSION_BUTTON = (By.XPATH, "")
EMAIL_INPUT = (By.XPATH, "//android.widget.TextView[@text='Correo electrónico']/following-sibling::android.widget.EditText")
PASSWORD_INPUT = (By.XPATH, '//android.widget.TextView[@text="Contraseña"]')
LOGIN_BUTTON = (By.XPATH, '//android.widget.TextView[@text="Ingresar"]')

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
        self.elm.click(EMAIL_INPUT)
        self.elm.send_keys(EMAIL_INPUT,email)
        self.elm.click(PASSWORD_INPUT)
        self.elm.send_keys(PASSWORD_INPUT,password)
        self.elm.click(LOGIN_BUTTON)

