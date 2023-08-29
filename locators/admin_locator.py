from selenium.webdriver.common.by import By


class AdminLocator:
    """ Locators for Admin Page """
    _username_field = (By.NAME, 'username')
    _password_field = (By.NAME, 'password')
    _login_button = (By.XPATH, '//button[@type="submit"]')

    """ Locators for Admin Header """
    admin = (By.XPATH, '//a[@href="/web/index.php/admin/viewAdminModule"]')
    user_management = (By.XPATH, '//span[text()="User Management "]')
    job = (By.XPATH, '//span[text()="Job "]')
    organization = (By.XPATH, '//span[text()="Organization "]')
    qualification = (By.XPATH, '// span[text() = "Qualifications "]')
    nationalities = (By.XPATH, '//a[text()="Nationalities"]')
    corporate_banking = (By.XPATH, '//a[text()="Corporate Branding"]')
    configuration = (By.XPATH, '//span[text()="Configuration "]')  # Value in Chrome - Configuration

    """ Locators for Admin Menu """
    pim = (By.XPATH, '//a[@href="/web/index.php/pim/viewPimModule"]')
    leave = (By.XPATH, '//a[@href="/web/index.php/leave/viewLeaveModule"]')
    time = (By.XPATH, '//span[text()="Time"]')
    recruitment = (By.XPATH, '//span[text()="Recruitment"]')
    my_info = (By.XPATH, '//span[text()="My Info"]')
    performance = (By.XPATH, '//span[text()="Performance"]')
    dashboard = (By.XPATH, '//span[text()="Dashboard"]')
    directory = (By.XPATH, '//span[text()="Directory"]')
    maintenance = (By.XPATH, '//span[text()="Maintenance"]')
    buzz = (By.XPATH, '//a[@href="/web/index.php/buzz/viewBuzz"]')
