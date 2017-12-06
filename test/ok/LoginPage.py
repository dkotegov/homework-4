from Page import Page


class LoginPage(Page):
    FORM_CLASS = "js-login-form"

    INPUT_LOGIN = "field_email"
    INPUT_PASSWORD = "field_password"
    BUTTON_CLASS = "button-pro"

    def __init__(self, driver, login, password):
        super(LoginPage, self).__init__(driver, "login_page")

        self.login = login
        self.password = password

    def auth(self):
        login_field = self.driver.find_element_by_id(self.INPUT_LOGIN)
        password_field = self.driver.find_element_by_id(self.INPUT_PASSWORD)

        login_field.send_keys(self.login)
        password_field.send_keys(self.password)

        # for Chrome
        # password_field.send_keys(Keys.ENTER)

        base = self.getElementByClass(self.driver, self.FORM_CLASS)
        self.getElementByClass(base, self.BUTTON_CLASS).click()
