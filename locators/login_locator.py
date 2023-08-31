from selenium.webdriver.common.by import By


class LoginLocator:
    """ Locators for Base Page """
    _msg = (By.XPATH, '//p[text()="Invalid credentials"]')

    """ Locators for Admin Page """
    _username_field = (By.NAME, 'username')
    _password_field = (By.NAME, 'password')
    _login_button = (By.XPATH, '//button[@type="submit"]')
