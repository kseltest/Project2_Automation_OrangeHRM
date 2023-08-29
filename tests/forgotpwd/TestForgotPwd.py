import time

import pytest
from selenium import webdriver

from data import test_data
from pages.base.base_page import BasePage
from pages.forgotpwd.forgotpwd_page import ForgotPassword


class TestForgotPwd:
    def __int__(self):
        pass

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_page = BasePage(self.driver)
        self.forgetpwd_page = ForgotPassword(self.base_page)

    @pytest.mark.test_forgotpwd_link
    def test_forgotpwd_link(self):
        self.base_page.visit(test_data.baseurl)
        time.sleep(5)
        self.forgetpwd_page.forget_password_link()
        time.sleep(5)

    @pytest.mark.test_reset_password
    def test_reset_password(self):
        print("Forgot Password Link redirects to URL= ", self.driver.current_url)

        """ Negative scenario with blank username """
        self.forgetpwd_page.reset_username(test_data.resetnegative)
        self.forgetpwd_page.click_reset_button()
        time.sleep(5)

        """ Positive scenario with valid username """
        self.forgetpwd_page.reset_username(test_data.resetuser)
        self.forgetpwd_page.click_reset_button()
        time.sleep(5)

    def teardown_class(self):
        self.driver.close()
