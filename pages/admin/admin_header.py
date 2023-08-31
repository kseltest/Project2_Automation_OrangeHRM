from locators.admin_locator import AdminLocator
from pages.login.login_page import LoginPage


class AdminHeaderPage(LoginPage):

    def __init__(self, driver):
        super().__init__(driver)

    def goto_page(self):
        """ Select Admin on Page """
        self.find_element(*AdminLocator.admin).click()

    def find_header(self):
        return self.is_element_visible(*AdminLocator.admin)

    def find_usermanagement(self):
        return self.is_element_visible(*AdminLocator.user_management)

    def find_job(self):
        return self.is_element_visible(*AdminLocator.job)

    def find_organisation(self):
        return self.is_element_visible(*AdminLocator.organization)

    def find_qualification(self):
        return self.is_element_visible(*AdminLocator.qualification)

    def find_nationalities(self):
        return self.is_element_visible(*AdminLocator.nationalities)

    def find_corporatebanking(self):
        return self.is_element_visible(*AdminLocator.corporate_banking)

    def find_configuration(self):
        return self.is_element_visible(*AdminLocator.configuration)
