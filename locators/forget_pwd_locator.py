from selenium.webdriver.common.by import By


class ForgetPwdLocators:
    """ Locator on Base Page """
    _forgetpwd_link = (By.XPATH, '//p[@class="oxd-text oxd-text--p orangehrm-login-forgot-header"]')

    """ Locator on Forgot Password Page """
    _reset_username = (By.XPATH, '//input[@name="username"]')
    _reset_button = (By.XPATH, '//button[@type="submit"]')
    _err_message = (By.TAG_NAME, 'span')
    _success_message = (By.XPATH, '//h6[@class = "oxd-text oxd-text--h6 orangehrm-forgot-password-title"]')
