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
    
    NEW_COMMAND_TIMEOUT = 3600
    NO_RESET = False
    AUTO_GRANT_PERMISSIONS = True
    CONNECT_HARDWARE_KEYBOARD = True

# -------------------------
# Local Emulator 
# -------------------------
class LocalConfig(BaseConfig):
    APPIUM_HOST = "127.0.0.1"
    APPIUM_PORT = 4723
    REMOTE_PATH = "/"
    AUTOMATION_NAME = "UiAutomator2"
    DEVICE_NAME = "Pixel_9"
    PLATFORM_VERSION = "16.0"
    APP_PATH = r"C:\Users\pc\Downloads\VitaQA.apk"
    APP_PACKAGE = "com.vita_wallet"
    APP_ACTIVITY = "com.vita_wallet.MainActivity"

# -------------------------
# BrowserStack Emulator configuration
# -------------------------
class BrowserStackConfig(BaseConfig):
    APPIUM_HOST = "hub.browserstack.com"
    APPIUM_PORT = 443
    REMOTE_PATH = "/wd/hub"

    USERNAME = "username"
    ACCESS_KEY = "access_key"

    DEVICE_NAME = "Google Pixel 7"
    PLATFORM_VERSION = "13.0"
    APP = "bs://app-id" 
    PROJECT = "VitaQA"
    BUILD = "Build-ChallengeQA"
    NAME = "Name Gaston QA"