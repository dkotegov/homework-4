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