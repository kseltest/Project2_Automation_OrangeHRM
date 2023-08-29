import time

from selenium import webdriver

from data import test_data
from pages.admin.admin_header import AdminHeaderPage
from pages.base.base_page import BasePage
from pages.login.login_page import LoginPage


class TestAdminHeader:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.base_page = BasePage(self.driver)
        self.login_page = LoginPage(self.base_page)
        self.admin_header_page = AdminHeaderPage(self.login_page)

    def test_admin_header(self):
        self.base_page.visit(test_data.baseurl)
        self.login_page.fill_login_form(test_data.username, test_data.password)
        time.sleep(2)

        self.admin_header_page.goto_page()
        time.sleep(5)

        assert self.driver.title == 'OrangeHRM'
        assert self.admin_header_page.find_header() is True
        assert self.admin_header_page.find_usermanagement() is True
        assert self.admin_header_page.find_job() is True
        assert self.admin_header_page.find_organisation() is True
        assert self.admin_header_page.find_qualification() is True
        assert self.admin_header_page.find_nationalities() is True
        assert self.admin_header_page.find_corporatebanking() is True
        assert self.admin_header_page.find_configuration() is True

        print("All Admin Headers are present in Admin Page")

    def teardown_class(self):
        self.driver.close()
