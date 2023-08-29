import time

from selenium import webdriver

from data import test_data
from pages.base.base_page import BasePage
from pages.login.login_page import LoginPage


class TestAdminLogin:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.base_page = BasePage(self.driver)
        self.login_page = LoginPage(self.base_page)

    """ Test case to validate Admin Login Page Title """

    def test_admin_pagetitle(self):
        self.base_page.visit(test_data.baseurl)
        time.sleep(2)
        self.login_page.fill_login_form(test_data.username, test_data.password)
        time.sleep(5)
        print("Current URL = ", self.driver.current_url)
        print("Page Title = ", self.driver.title)
        assert self.driver.title == 'OrangeHRM'

    def teardown_class(self):
        self.driver.close()
