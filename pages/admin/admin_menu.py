from locators.admin_locator import AdminLocator
from pages.login.login_page import LoginPage


class AdminMenuPage(LoginPage):

    def __init__(self, driver):
        super().__init__(driver)

    def goto_page(self):
        self.find_element(*AdminLocator.admin).click()

    def find_admin(self):
        return self.is_element_visible(*AdminLocator.admin)

    def find_pim(self):
        return self.is_element_visible(*AdminLocator.pim)

    def find_leave(self):
        return self.is_element_visible(*AdminLocator.leave)

    def find_time(self):
        return self.is_element_visible(*AdminLocator.time)

    def find_recruitment(self):
        return self.is_element_visible(*AdminLocator.recruitment)

    def find_myinfo(self):
        return self.is_element_visible(*AdminLocator.my_info)

    def find_performance(self):
        return self.is_element_visible(*AdminLocator.performance)

    def find_dashboard(self):
        return self.is_element_visible(*AdminLocator.dashboard)

    def find_directory(self):
        return self.is_element_visible(*AdminLocator.directory)

    def find_maintenance(self):
        return self.is_element_visible(*AdminLocator.maintenance)

    def find_buzz(self):
        return self.is_element_visible(*AdminLocator.buzz)
