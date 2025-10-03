from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        self.find_element(by_tuple, value).send_keys(text)

