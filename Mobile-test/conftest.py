import os
import time
import pytest
import allure
from appium import webdriver
from appium.webdriver import Remote
from appium.options.android import UiAutomator2Options
from env.config import LocalConfig

# -------------------------
# Carpeta para screenshots
# -------------------------

SCREENSHOT_DIR = os.path.join(os.getcwd(), "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# -------------------------
# Fixture driver
# -------------------------

@pytest.fixture(scope="function")
def driver():
    
    config = LocalConfig()

    opts = UiAutomator2Options()
    opts.set_capability("platformName", config.PLATFORM_NAME)
    opts.set_capability("automationName", config.AUTOMATION_NAME)
    opts.set_capability("deviceName", config.DEVICE_NAME)
    opts.set_capability("platformVersion", config.PLATFORM_VERSION)
    opts.set_capability("app", config.APP_PATH)
    opts.set_capability("appPackage", config.APP_PACKAGE)
    opts.set_capability("appActivity", config.APP_ACTIVITY)
    opts.set_capability("noReset", config.NO_RESET)
    opts.set_capability("autoGrantPermissions", config.AUTO_GRANT_PERMISSIONS)
    opts.set_capability("newCommandTimeout", config.NEW_COMMAND_TIMEOUT)
    opts.set_capability("connectHardwareKeyboard", True)
    command_executor = f"http://{config.APPIUM_HOST}:{config.APPIUM_PORT}"
    
    # Inicializar driver
    driver_instance = webdriver.Remote(command_executor=command_executor, options=opts)
    
    # Espera para asegurarse que la app arrancó
    time.sleep(2)

    yield driver_instance

    # Cerrar app al finalizar test
   # driver_instance.terminate_app(config.APP_PACKAGE)
   # driver_instance.quit()