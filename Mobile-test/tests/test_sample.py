import pytest
from pages.login.login_page import LoginPage
from pages.home.home_page import HomePage
from pages.crypto.crypto_buy_page import CryptoBuyPage
from data.users import UserData

@pytest.mark.parametrize("user", UserData("data/users.csv").get_users())
def test_login(driver, user):


    # -------------------------
    # A-A-A DESIGN PATTERN
    # Arrange 1
    # -------------------------
    login_page = LoginPage(driver)
    
    # -------------------------
    # Act 2
    # -------------------------
    login_page.login(user["email"], user["password"])
    
    # -------------------------
    # Assert 3
    # -------------------------
    #welcome_text_locator = ('xpath', '//android.widget.TextView[@text="Welcome"]')
    #assert login_page.el.find_element(welcome_text_locator).is_displayed(), "Login failed for user: {}".format(user["email"])
    
    home_page = HomePage(driver)
    home_page.quit_pop_up(driver)
    home_page.go_crypto(driver)

    crypto_buy_page = crypto_buy_page(driver)
    crypto_buy_pagehome_page.quit_pop_up(driver)
    home_page.go_crypto(driver)