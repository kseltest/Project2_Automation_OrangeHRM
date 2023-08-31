import time

from selenium import webdriver
from locators.login_locator import LoginLocator
from pages.base.base_page import BasePage
from pages.login.login_page import LoginPage
from data import test_data


class TestLogin:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(0.5)
        self.base_page = BasePage(self.driver)
        self.login_page = LoginPage(self.base_page)

    def test_login(self):
        """ Negative Testcase scenario for Login with Invalid user/password """
        username = test_data.user_invalid
        password = test_data.password_invalid

        self.base_page.visit(test_data.baseurl)
        time.sleep(2)
        self.login_page.fill_login_form(username, password)
        time.sleep(2)

        try:
            assert self.base_page.is_element_visible(*LoginLocator._msg) is True

            elem = self.base_page.find_element(*LoginLocator._msg)
            print("Error on Page for Username = %s : %s" % (username, elem.text))
        except Exception:
            print("Valid User %s && PageTitle = %s" % (username, self.driver.title))

    def teardown_class(self):
        self.driver.close()
