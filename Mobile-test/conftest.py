import pytest
import os
import time
import allure
from appium import webdriver
from env.config import LocalConfig, BrowserStackConfig

# -------------------------
# Screenshots folder
# -------------------------
SCREENSHOT_DIR = os.path.join(os.getcwd(), "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# -------------------------
# Select environment config
# -------------------------
def get_config():
    env = os.environ.get("TEST_ENV", "local").lower()
    if env == "browserstack":
        return BrowserStackConfig
    return LocalConfig

# -------------------------
# Driver fixture
# -------------------------
@pytest.fixture(scope="function")
def driver():
    config = get_config()

    desired_caps = {
        "platformName": config.PLATFORM_NAME,
        "automationName": getattr(config, "AUTOMATION_NAME", "UiAutomator2"),
        "deviceName": config.DEVICE_NAME,
        "platformVersion": getattr(config, "PLATFORM_VERSION", None),
        "app": getattr(config, "APP_PATH", getattr(config, "APP", None)),
        "appPackage": getattr(config, "APP_PACKAGE", None),
        "appActivity": getattr(config, "APP_ACTIVITY", None),
        "noReset": config.NO_RESET,
        "autoGrantPermissions": config.AUTO_GRANT_PERMISSIONS,
        "newCommandTimeout": config.NEW_COMMAND_TIMEOUT,
        "connectHardwareKeyboard": config.CONNECT_HARDWARE_KEYBOARD
    }

    if getattr(config, "USERNAME", None):
        # BrowserStack authentication
        command_executor = f"https://{config.USERNAME}:{config.ACCESS_KEY}@{config.APPIUM_HOST}:{config.APPIUM_PORT}{config.REMOTE_PATH}"
    else:
        command_executor = f"http://{config.APPIUM_HOST}:{config.APPIUM_PORT}{config.REMOTE_PATH}"

    driver_instance = webdriver.Remote(command_executor=command_executor, desired_capabilities=desired_caps)

    yield driver_instance
    driver_instance.quit()

# -------------------------
# Hook: capture screenshot on failure
# -------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Captures screenshot if a test fails and attaches it to Allure.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver_fixture = item.funcargs.get("driver", None)
        if driver_fixture:
            try:
                # Capture screenshot in memory
                screenshot_png = driver_fixture.get_screenshot_as_png()

                # Unique filename
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                test_name = item.name
                screenshot_file = os.path.join(SCREENSHOT_DIR, f"{test_name}_{timestamp}.png")

                # Save locally
                driver_fixture.save_screenshot(screenshot_file)
                print(f"\n[Screenshot saved] {screenshot_file}")

                # Attach to Allure
                allure.attach(screenshot_png, name=f"{test_name}_{timestamp}",
                              attachment_type=allure.attachment_type.PNG)

            except Exception as e:
                print(f"\n[Error capturing screenshot] {e}")
