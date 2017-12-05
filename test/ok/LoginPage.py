from Page import Page

from selenium.webdriver.common.keys import Keys

class LoginPage(Page):
    INPUT_LOGIN     = "field_email"
    INPUT_PASSWORD  = "field_password"

    def __init__(self, driver, login, password):
        super(LoginPage, self).__init__(driver, "login_page")

        self.login = login
        self.password = password

    def auth(self):
        login_field = self.driver.find_element_by_id(self.INPUT_LOGIN)
        password_field = self.driver.find_element_by_id(self.INPUT_PASSWORD)

        login_field.send_keys(self.login)
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.ENTER)
