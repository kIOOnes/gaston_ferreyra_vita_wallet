import pytest
from pages.login.login_page import LoginPage
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
 
