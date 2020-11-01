from base_classes.component import Component


class LoginForm(Component):
    LOGIN = '//input[@id="inputLogin"]'
    PASSWORD = '//input[@id="inputPassword"]'
    SUBMIT = '//div[@id="submit_button"]'
    REGISTER_BUTTON = '//a[text()="Регистрация"]'

    def set_login(self, login: str):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, password: str):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def open_registration(self):
        self.driver.find_element_by_xpath(self.REGISTER_BUTTON).click()
