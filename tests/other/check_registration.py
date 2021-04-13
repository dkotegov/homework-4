import unittest

from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.registration_page import RegistrationPage
from scenario.auth import setup_auth
from scenario.default_setup import default_setup
from scenario.registration_applicant import registration_applicant
from scenario.registration_employer import RegistrationEmployerScenario


class CheckRegistration(unittest.TestCase):

    incorrect_name = 'name123'
    incorrect_surname = 'surname123'
    incorrect_email = 'margot.ru'
    incorrect_password = 'q'
    correct_name = 'margotName'
    correct_surname = 'margotSurname'
    correct_email = 'test@test.ru'
    correct_password = 'margot'

    incorrect_name_data = {
        'NAME': incorrect_name,
        'SURNAME': correct_surname,
        'EMAIL': correct_email,
        'PASSWORD': correct_password,
        'CONFIRM_PASSWORD': correct_password
    }

    incorrect_surname_data = {
        'NAME': correct_name,
        'SURNAME': incorrect_surname,
        'EMAIL': correct_email,
        'PASSWORD': correct_password,
        'CONFIRM_PASSWORD': correct_password
    }

    incorrect_email_data = {
        'NAME': correct_name,
        'SURNAME': correct_surname,
        'EMAIL': incorrect_email,
        'PASSWORD': correct_password,
        'CONFIRM_PASSWORD': correct_password
    }

    different_password_data = {
        'NAME': correct_name,
        'SURNAME': correct_surname,
        'EMAIL': correct_email,
        'PASSWORD': correct_password,
        'CONFIRM_PASSWORD': '123123'
    }

    empty_form = {
        'NAME': '',
        'SURNAME': '',
        'EMAIL': '',
        'PASSWORD': '',
        'CONFIRM_PASSWORD': ''
    }

    existing_data = {
        'NAME': 'testReg',
        'SURNAME': 'testReg',
        'EMAIL': 'testReg@testReg.ru',
        'PASSWORD': 'testReg',
        'CONFIRM_PASSWORD': 'testReg'
    }

    def setUp(self) -> None:
        default_setup(self)

        self.auth_page = AuthPage(self.driver)
        self.reg_page = RegistrationPage(self.driver)
        self.profile_page = ProfilePage(self.driver)
        self.main_page = MainPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_to_auth(self):
        self.reg_page.open()
        self.reg_page.go_to_auth()
        self.auth_page.check_open_page()

    def test_correct_registration_applicant_and_delete(self):
        data = registration_applicant(self)
        self.main_page.click_profile_page()
        self.profile_page.is_open()
        self.assertTrue(self.profile_page.check_profile_data(data))
        self.profile_page.delete_account()


    def test_correct_reg_empl_and_del(self):
        scen = RegistrationEmployerScenario(self)
        data = scen.registration_employer(True)
        self.main_page.click_profile_page()
        self.profile_page.is_open()
        self.assertTrue(self.profile_page.check_profile_data(data))
        self.profile_page.delete_account()

    def test_correct_reg_empl_with_company_and_del(self):
        scen = RegistrationEmployerScenario(self)
        data = scen.registration_employer(True)
        self.main_page.click_profile_page()
        self.profile_page.is_open()
        self.assertTrue(self.profile_page.check_profile_data(data))
        self.profile_page.delete_account()

    def test_empty_form_apl(self):
        self.reg_page.open()
        self.reg_page.set_data(self.empty_form)
        self.assertTrue(self.reg_page.errors_empty_data())

    def test_empty_form_empl(self):
        self.reg_page.open()
        self.reg_page.click_checkout_btn()
        self.reg_page.set_data(self.empty_form)
        self.assertTrue(self.reg_page.errors_empty_data())

    def test_incorrect_name_appl(self):
        self.reg_page.open()
        self.reg_page.set_data(self.incorrect_name_data)
        self.assertTrue(self.reg_page.top_error('Неправильные значения полей: имя должно содержать только буквы'))

    def test_incorrect_name_empl(self):
        self.reg_page.open()
        self.reg_page.click_checkout_btn()
        self.reg_page.select_company()
        self.reg_page.set_data(self.incorrect_name_data)
        self.assertTrue(self.reg_page.top_error('Неправильные значения полей: имя должно содержать только буквы'))

    def test_incorrect_surname_appl(self):
        self.reg_page.open()
        self.reg_page.set_data(self.incorrect_surname_data)
        self.assertTrue(self.reg_page.top_error('Неправильные значения полей: фамилия должна содержать только буквы'))

    def test_incorrect_surname_empl(self):
        self.reg_page.open()
        self.reg_page.click_checkout_btn()
        self.reg_page.click_to_checkbox()
        self.reg_page.set_data(self.incorrect_surname_data)
        self.assertTrue(self.reg_page.top_error('Неправильные значения полей: фамилия должна содержать только буквы'))

    def test_incorrect_email_appl(self):
        self.reg_page.open()
        self.reg_page.set_data(self.incorrect_email_data)
        self.assertTrue(self.reg_page.error_email())

    def test_not_equal_passwords(self):
        self.reg_page.open()
        self.reg_page.set_data(self.different_password_data)
        self.assertTrue(self.reg_page.errors_in_passwords())

    def test_existing_accaunt(self):
        registration_applicant(self, self.existing_data)
        self.main_page.click_logout()
        self.reg_page.open()
        self.reg_page.set_data(self.existing_data)
        self.assertTrue(self.reg_page.top_error('Пользователь уже существует.'))
        setup_auth(self, self.existing_data)
        self.profile_page.open()
        self.profile_page.delete_account()

