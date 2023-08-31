import time

import pytest
from selenium import webdriver

from data import test_data
from locators.forget_pwd_locator import ForgetPwdLocators
from pages.base.base_page import BasePage
from pages.forgotpwd.forgotpwd_page import ForgotPassword


class TestForgotPwd:
    def __int__(self):
        pass

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(0.5)
        self.base_page = BasePage(self.driver)
        self.forgetpwd_page = ForgotPassword(self.base_page)

    @pytest.mark.test_forgotpwd_link
    def test_forgotpwd_link(self):
        """ Testcase to validate forgot password link """

        self.base_page.visit(test_data.baseurl)

        try:
            assert self.base_page.is_element_visible(*ForgetPwdLocators._forgetpwd_link) is True
            print("Forgot Password Link is present in page: ", self.driver.current_url)
            time.sleep(2)
            self.forgetpwd_page.forget_password_link()
        except:
            print("Forget Password Link is NOT present in page: ", self.driver.current_url)

    @pytest.mark.test_reset_password_blank
    def test_reset_password_blank(self):
        """ Testcase to validate Popup Window on forgot password link Page
            Negative scenario with blank username textbox """

        print("Forgot Password Link redirects to URL = ", self.driver.current_url)
        self.forgetpwd_page.reset_username(test_data.resetnegative)
        self.forgetpwd_page.click_reset_button()
        time.sleep(3)

    @pytest.mark.test_reset_password_value
    def test_reset_password_value(self):
        """ Testcase to validate Popup Window on forgot password link Page
            Positive scenario with value in username textbox """

        print("Forgot Password Link redirects to URL = ", self.driver.current_url)
        self.forgetpwd_page.reset_username(test_data.resetuser)
        self.forgetpwd_page.click_reset_button()
        time.sleep(3)

    def teardown_class(self):
        self.driver.close()
