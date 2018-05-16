from src.auth_factory import AuthFactory
from src.components.forms.auth_form import AuthForm
from src.pages.base_page import BasePage


class AuthPage(BasePage):

    def __init__(self, driver):
        super(AuthPage, self).__init__(driver)
        self._url = 'http://ok.ru'
        self._logout_url = "https://www.ok.ru/dk?st.cmd=anonymMain&st.lgn=on&st.fflo=off"
        self._auth = AuthFactory.create()

    def open_and_sign_in(self):
        self.driver.maximize_window()
        self.driver.get(self._url)
        self._login(self._auth.username, self._auth.password)

    def open(self):
        self.driver.maximize_window()
        self.driver.get(self._url)

    def sign_in(self, login, password):
        self.driver.get(self._url)
        self._login(login, password)
    
    def _login(self, login, password):
        auth_form = AuthForm(self.driver)
        auth_form.get_login_input().send_keys(login)
        auth_form.get_password_input().send_keys(password)
        auth_form.get_submit_button().click()


