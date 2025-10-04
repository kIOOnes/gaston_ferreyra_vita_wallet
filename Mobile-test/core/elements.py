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
        locator = (by_tuple, value) if value else by_tuple
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, by_tuple, text, value=None):
        self.find_element(by_tuple).send_keys(text)

    def is_present(self, by_tuple, value=None, timeout=5):
        locator = (by_tuple, value) if value else by_tuple
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
        
    def wait_for_enabled(self, by_tuple, timeout=30, poll_frequency=0.5):
        locator = by_tuple
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                lambda driver: self.driver.find_element(*locator).is_enabled()
            )
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        
        except TimeoutException:
            print(f"[WARN] El elemento {locator} no se habilito en {timeout} segundos.")
            return False