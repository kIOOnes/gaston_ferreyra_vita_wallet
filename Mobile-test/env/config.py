import os

class BaseConfig:
    # -------------------------
    # Screenshots folder
    # -------------------------
    SCREENSHOT_DIR = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    # -------------------------
    # General Appium capabilities
    # -------------------------
    PLATFORM_NAME = "Android"
    AUTOMATION_NAME = "UiAutomator2"
    NEW_COMMAND_TIMEOUT = 3600
    NO_RESET = True
    AUTO_GRANT_PERMISSIONS = True
    CONNECT_HARDWARE_KEYBOARD = True

# -------------------------
# Local Emulator / Appium
# -------------------------
class LocalConfig(BaseConfig):
    APPIUM_HOST = "127.0.0.1"
    APPIUM_PORT = 4723
    REMOTE_PATH = "/"

    DEVICE_NAME = "emulator-5554"
    PLATFORM_VERSION = "16.0"

    APP_PATH = r"C:\Users\pc\Downloads\VitaQA.apk"
    APP_PACKAGE = "com.vita_wallet"
    APP_ACTIVITY = "com.vita_wallet.MainActivity"

# -------------------------
# BrowserStack configuration
# -------------------------
class BrowserStackConfig(BaseConfig):
    APPIUM_HOST = "hub.browserstack.com"
    APPIUM_PORT = 443
    REMOTE_PATH = "/wd/hub"

    USERNAME = os.environ.get("BROWSERSTACK_USER")
    ACCESS_KEY = os.environ.get("BROWSERSTACK_KEY")

    DEVICE_NAME = "Google Pixel 7"
    PLATFORM_VERSION = "13.0"
    APP = "bs://<app-id>"  # App uploaded to BrowserStack
    PROJECT = "VitaQA"
    BUILD = "Build-001"
    NAME = "Test Gaston QA"
