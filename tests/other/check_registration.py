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

    def setUp(self) -> None:
        default_setup(self)

        self.incorrect_name = 'name123'
        self.incorrect_surname = 'surname123'
        self.incorrect_email = 'margot.ru'
        self.correct_name = 'margotName'
        self.correct_surname = 'margotSurname'
        self.correct_email = 'test@test.ru'
        self.correct_password = self.PASSWORD_APPL

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
        empty_form = {
            'NAME': '',
            'SURNAME': '',
            'EMAIL': '',
            'PASSWORD': '',
            'CONFIRM_PASSWORD': ''
        }
        self.reg_page.open()
        self.reg_page.set_data(empty_form)
        self.assertTrue(self.reg_page.errors_empty_data())

    def test_empty_form_empl(self):
        empty_form = {
            'NAME': '',
            'SURNAME': '',
            'EMAIL': '',
            'PASSWORD': '',
            'CONFIRM_PASSWORD': ''
        }
        self.reg_page.open()
        self.reg_page.click_checkout_btn()
        self.reg_page.set_data(empty_form)
        self.assertTrue(self.reg_page.errors_empty_data())

    def test_incorrect_name_appl(self):
        incorrect_name_data = {
            'NAME': self.incorrect_name,
            'SURNAME': self.correct_surname,
            'EMAIL': self.correct_email,
            'PASSWORD': self.correct_password,
            'CONFIRM_PASSWORD': self.correct_password
        }
        self.reg_page.open()
        self.reg_page.set_data(incorrect_name_data)
        self.assertTrue(self.reg_page.top_error('Неправильные значения полей: имя должно содержать только буквы'))

    def test_incorrect_name_empl(self):
        incorrect_name_data = {
            'NAME': self.incorrect_name,
            'SURNAME': self.correct_surname,
            'EMAIL': self.correct_email,
            'PASSWORD': self.correct_password,
            'CONFIRM_PASSWORD': self.correct_password
        }
        self.reg_page.open()
        self.reg_page.click_checkout_btn()
        self.reg_page.select_company()
        self.reg_page.set_data(incorrect_name_data)
        self.assertTrue(self.reg_page.top_error('Неправильные значения полей: имя должно содержать только буквы'))

    def test_incorrect_surname_appl(self):
        incorrect_surname_data = {
            'NAME': self.correct_name,
            'SURNAME': self.incorrect_surname,
            'EMAIL': self.correct_email,
            'PASSWORD': self.correct_password,
            'CONFIRM_PASSWORD': self.correct_password
        }
        self.reg_page.open()
        self.reg_page.set_data(incorrect_surname_data)
        self.assertTrue(self.reg_page.top_error('Неправильные значения полей: фамилия должна содержать только буквы'))

    def test_incorrect_surname_empl(self):
        incorrect_surname_data = {
            'NAME': self.correct_name,
            'SURNAME': self.incorrect_surname,
            'EMAIL': self.correct_email,
            'PASSWORD': self.correct_password,
            'CONFIRM_PASSWORD': self.correct_password
        }
        self.reg_page.open()
        self.reg_page.click_checkout_btn()
        self.reg_page.click_to_checkbox()
        self.reg_page.set_data(incorrect_surname_data)
        self.assertTrue(self.reg_page.top_error('Неправильные значения полей: фамилия должна содержать только буквы'))

    def test_incorrect_email_appl(self):
        incorrect_email_data = {
            'NAME': self.correct_name,
            'SURNAME': self.correct_surname,
            'EMAIL': self.incorrect_email,
            'PASSWORD': self.correct_password,
            'CONFIRM_PASSWORD': self.correct_password
        }
        self.reg_page.open()
        self.reg_page.set_data(incorrect_email_data)
        self.assertTrue(self.reg_page.error_email())

    def test_not_equal_passwords(self):
        different_password_data = {
            'NAME': self.correct_name,
            'SURNAME': self.correct_surname,
            'EMAIL': self.correct_email,
            'PASSWORD': self.correct_password,
            'CONFIRM_PASSWORD': '123123'
        }
        self.reg_page.open()
        self.reg_page.set_data(different_password_data)
        self.assertTrue(self.reg_page.errors_in_passwords())

    def test_existing_account(self):
        existing_data = {
            'NAME': 'testReg',
            'SURNAME': 'testReg',
            'EMAIL': self.EMAIL_EMPL_COMP,
            'PASSWORD': self.PASSWORD_EMPL_COMP,
            'CONFIRM_PASSWORD': self.PASSWORD_EMPL_COMP
        }
        registration_applicant(self, existing_data)
        self.main_page.click_logout()
        self.reg_page.open()
        self.reg_page.set_data(existing_data)
        self.assertTrue(self.reg_page.top_error('Пользователь уже существует.'))
        setup_auth(self, existing_data)
        self.profile_page.open()
        self.profile_page.delete_account()

