from selenium.webdriver.support.wait import NoSuchElementException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def visit(self, base_url='https://www.google.com/'):
        return self.driver.get(base_url)

    def is_element_visible(self, *locator):
        try:
            return self.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    def get_text(self, *locator):
        """Return text from specific element"""
        try:
            return self.find_element(*locator).text
        except NoSuchElementException:
            return "INVALID"
