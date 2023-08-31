import time

from selenium import webdriver

from data import test_data
from pages.admin.admin_menu import AdminMenuPage
from pages.base.base_page import BasePage
from pages.login.login_page import LoginPage


class TestAdminMenu:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.base_page = BasePage(self.driver)
        self.login_page = LoginPage(self.base_page)
        self.admin_menu_page = AdminMenuPage(self.login_page)

    def test_admin_menu(self):
        """Test case to validate main menu options displaying on the Admin page"""

        self.base_page.visit(test_data.baseurl)
        self.login_page.fill_login_form(test_data.adminuser, test_data.adminpwd)
        time.sleep(5)

        self.admin_menu_page.goto_page()
        time.sleep(5)

        assert self.driver.title == 'OrangeHRM'
        assert self.admin_menu_page.find_admin() is True
        assert self.admin_menu_page.find_pim() is True
        assert self.admin_menu_page.find_leave() is True
        assert self.admin_menu_page.find_time() is True
        assert self.admin_menu_page.find_recruitment() is True
        assert self.admin_menu_page.find_myinfo() is True
        assert self.admin_menu_page.find_performance() is True
        assert self.admin_menu_page.find_dashboard() is True
        assert self.admin_menu_page.find_directory() is True
        assert self.admin_menu_page.find_maintenance() is True
        assert self.admin_menu_page.find_buzz() is True

        print("The title of Admin page is :", self.driver.title)
        print("All Main Menu are present in Admin Page")

    def teardown_class(self):
        self.driver.close()
