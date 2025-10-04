from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import time

class Elements:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, by_tuple, value=None):
        locator = (by_tuple, value) if value else by_tuple
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, by_tuple, value=None):
        self.find_element(by_tuple, value).click()

    def send_keys(self, by_tuple, text, value=None):
        print(f"[DEBUG] Buscando elemento con locator: {by_tuple} con {text}")
        self.find_element(by_tuple).send_keys(text)

    def is_present(self, by_tuple, value=None, timeout=5):
        """Devuelve True si el elemento está presente, False si no"""
        locator = (by_tuple, value) if value else by_tuple
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    #def adb_send_keys(self, text: str):
    #    """Usa ADB a través del driver, no necesita device_name"""
    #    escaped_text = text.replace(" ", "%s").replace("+", "%2B")
    #    self.driver.execute_script("mobile: shell", {
    #        "command": f'input text "{escaped_text}"'
    #    })
    #    time.sleep(0.5)
