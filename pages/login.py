from pages.defaultPage import Page, Component


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    # @property
    # def top_menu(self):
    #     return TopMenu(self.driver)


# loginBtn: '[id="loginModal"]',
# loginUser: '[id="loginUser"]',
# pass: '[id="passUser"]',
# submitButton: '[id="sendLogin"]',
# modalCloseInfo: '[id="closeInfo"]',


class AuthForm(Component):
    LOGIN_MODAL = '//[id="loginModal"]'
    LOGIN = '//input[id="loginUser"]'
    PASSWORD = '//input[id="passUser"]'
    SUBMIT = '//button[id="sendLogin"]'
    LOGIN_CLOSE_INFO = '//[id="closeInfo"]'

    # LOGIN_BUTTON = '//a[text()="Вход для участников"]'

    def open_form(self):
        self.driver.find_element_by_xpath(self.LOGIN_MODAL).click()

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
