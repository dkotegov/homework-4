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

        self.errors_arr = ['Поле обязательно для заполнения.', 'Поле обязательно для заполнения.', 'Укажите email.', 'Укажите пароль.', 'Пароли не совпадают']


    def go_to_auth(self):
        self.registration_form.click_to_auth_href()

    def select_company(self):
        self.registration_form.click_select_company_btn()
        self.registration_form.choose_company()

    def set_data(self, data):
        self.registration_form.set_name(data['NAME'])
        self.registration_form.set_surname(data['SURNAME'])
        self.registration_form.set_email(data['EMAIL'])
        self.registration_form.set_password(data['PASSWORD'])
        self.registration_form.set_confirm_password(data['CONFIRM_PASSWORD'])
        self.registration_form.submit()

    def click_to_checkbox(self):
        self.registration_form.select_checkbox()

    def click_checkout_btn(self):
        self.registration_form.click_checkout_btn()

    def wait_for_reg_is_done(self):
        self.registration_form.wait_for_mainpage()

    def errors_empty_data(self):
        tmpBool = True
        errors = self.registration_form.all_errors()
        for i in range(0, len(errors) - 1):
            if errors[i].text != self.errors_arr[i]:
                tmpBool = False
        return tmpBool

    def top_error(self, error_text):
        error = self.registration_form.top_error()
        return error.text == error_text

    def error_email(self):
        errors = self.registration_form.all_errors()
        return errors[2].text == 'Email должен содержать "@" и латинские буквы, цифры, символы.'

    def errors_in_passwords(self):
        errors = self.registration_form.all_errors()
        return errors[3].text == errors[3].text == 'Пароли не совпадают'

    def wait_for_page_open(self):
        self.registration_form.wait_for_page_open()