from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Waits:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, by_tuple, value=None):
        locator = (by_tuple, value) if value else by_tuple
        return self.wait.until(EC.presence_of_element_located(locator))

