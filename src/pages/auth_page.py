from src.components.forms.auth_form import AuthForm
from src.pages.base_page import BasePage


class AuthPage(BasePage):

    def __init__(self, driver):
        super(AuthPage, self).__init__(driver)
        self.MAIN_URL = 'http://ok.ru'
        self.LOG_OUT_URL = "https://www.ok.ru/dk?st.cmd=anonymMain&st.lgn=on&st.fflo=off"
   
    def open(self):
        self.driver.get(self.MAIN_URL)
        self.driver.maximize_window()

    def sign_in(self, login, password):
        self.driver.get(self.MAIN_URL)
        self.login(login, password)
    
    def login(self, login, password):
        auth_form = AuthForm(self.driver)
        auth_form.get_login_input().send_keys(login)
        auth_form.get_password_input().send_keys(password)
        auth_form.get_submit_button().click()


