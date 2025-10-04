import time

class Waits:
    def __init__(self, driver):
        self.driver = driver

    def seconds_sleep(self, seconds):
        time.sleep(seconds)

