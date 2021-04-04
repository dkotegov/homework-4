from pages.base_component import Component


class LoginForm(Component):
    LOGIN = '//input[@name="login"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT_BTN = '//button[contains(text(),"Войти")]'
    REGISTER = '//a[contains(text(),"Зарегистрироваться")]'
    AUTH_MODAL = '//div[@id="authModal"]'
    MODAL_CLOSE = '//span[@class="modal__close"]'

    def wait_until_visible(self):
        self._wait_until_visible(self.AUTH_MODAL)

    def wait_until_invisible(self):
        self._wait_until_invisible(self.AUTH_MODAL)

    def set_login_text(self, text):
        self._find_element(self.LOGIN).send_keys(text)

    def set_password_text(self, text):
        self._find_element(self.PASSWORD).send_keys(text)

    def submit(self):
        self._find_element(self.SUBMIT_BTN).click()

    def click_register(self):
        self._find_element(self.REGISTER).click()

    def click_close(self):
        self._find_element(self.MODAL_CLOSE).click()
