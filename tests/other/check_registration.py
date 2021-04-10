import unittest

from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.registration_page import RegistrationPage
from scenario.registration_applicant import registration_applicant
from scenario.registration_employer import registration_employer
from tests.default_setup import default_setup


class CheckRegistration(unittest.TestCase):
    select_company = True

    def setUp(self) -> None:
        default_setup(self)

        self.auth_page = AuthPage(self.driver)
        self.reg_page = RegistrationPage(self.driver)
        self.profile_page = ProfilePage(self.driver)
        self.main_page = MainPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    # def test_checkout_to_auth(self):
    #     self.reg_page.open()
    #     self.reg_page.go_to_auth()
    #     self.auth_page.is_open()

    # def test_correct_registration_applicant_and_delete(self):
    #     data = registration_applicant(self)
    #     self.main_page.click_profile_page()
    #     self.profile_page.is_open()
    #     self.assertTrue(self.profile_page.check_profile_data(data))
    #     self.profile_page.delete_account()

    def test_correct_registration_employer_and_delete(self):
        data = registration_employer(self, self.select_company)
        self.main_page.click_profile_page()
        self.profile_page.is_open()
        self.assertTrue(self.profile_page.check_profile_data(data))
        self.profile_page.delete_account()

