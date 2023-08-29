from locators.admin_locator import AdminLocator
from pages.base.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_login_form(self, username, password):
        self.find_element(*AdminLocator._username_field).send_keys(username)
        self.find_element(*AdminLocator._password_field).send_keys(password)
        self.find_element(*AdminLocator._login_button).click()
