import time

from locators.forget_pwd_locator import ForgetPwdLocators
from pages.base.base_page import BasePage


class ForgotPassword(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.reset_user = ""

    def forget_password_link(self):
        self.find_element(*ForgetPwdLocators._forgetpwd_link).click()

    def reset_username(self, resetusername):
        self.reset_user = resetusername
        self.find_element(*ForgetPwdLocators._reset_username).send_keys(resetusername)

    def click_reset_button(self):
        self.find_element(*ForgetPwdLocators._reset_button).click()
        time.sleep(2)

        if self.reset_user == "":
            print("Reset Password with Username = [blank]")
            print("ERROR = ", self.get_text(*ForgetPwdLocators._err_message))
        else:
            print("Reset Password with Username = ", self.reset_user)
            print("SUCCESS = ", self.get_text(*ForgetPwdLocators._success_message))
