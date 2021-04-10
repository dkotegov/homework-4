from components.registration_form import RegistrationForm
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    """
    Страница регистрации
    """

    PATH = 'reg'

    def __init__(self, driver):
        self.registration_form = RegistrationForm(driver)
        super(RegistrationPage, self).__init__(driver, self.registration_form.locators.root)


    def go_to_auth(self):
        self.registration_form.click_to_auth_href()

    def select_company(self):
        self.registration_form.click_select_company_btn()
        self.registration_form.choose_company()

    def set_data(self, data):
        self.registration_form.set_name(data['name'])
        self.registration_form.set_surname(data['surname'])
        self.registration_form.set_email(data['email'])
        self.registration_form.set_password(data['password'])
        self.registration_form.set_confirm_password(data['confirm_password'])