import pytest
from pages.login.login_page import LoginPage
from pages.home.home_page import HomePage
from pages.crypto.crypto_buy_page import CryptoBuyPage
from pages.crypto.crypto_confirm_page import CryptoConfirm
from pages.crypto.crypto_successful_page import CryptoSuccesfulPage
from data.users import UserData
import time

@pytest.mark.parametrize("user", UserData("data/users.csv").get_users())
def test_e2e_buy_crypto(driver, user):


    # -------------------------
    # A-A-A DESIGN PATTERN (Arrange, Act, Assert)
    # Arrange
    # -------------------------
    login_page = LoginPage(driver)
    
    # -------------------------
    # Act
    # -------------------------
    login_page.login(user["email"], user["password"])
    
    home_page = HomePage(driver)
    home_page.quit_pop_up()
    home_page.go_crypto()

    crypto_buy_page = CryptoBuyPage(driver)
    crypto_buy_page.select_crypto_to_sell()
    crypto_buy_page.enter_amount_to_sell(2000)
    crypto_buy_page.select_crypto_to_buy()
    crypto_buy_page.continue_operation()

    crypto_confirm_page = CryptoConfirm(driver)
    crypto_confirm_page.confirm()

    crypto_successful_page = CryptoSuccesfulPage(driver)
    crypto_successful_page.return_home()
    
    home_page.view_last_movements()
  
    # -------------------------
    # Assert
    # -------------------------
    
    status = home_page.get_status_operation()
    assert status == "Completada", f"Se esperaba 'Completada' pero se obtuvo '{status}'"