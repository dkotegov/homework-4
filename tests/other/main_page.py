import unittest

from pages.vacancies_page import VacanciesPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from pages.create_resume_page import CreateResumePage
from tests.default_setup import default_setup
from scenario.auth import setup_auth


class PopularCategory(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        self.sphere = 'Государственные организации'
        self.main_page = MainPage(self.driver)
        self.vacancies_page = VacanciesPage(self.driver)
        self.reg_page = RegistrationPage(self.driver)
        self.create_resume_page = CreateResumePage(self.driver)
        self.main_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_check_vacancy_by_sphere(self):
        self.main_page.click_on_sphere(self.sphere)
        self.assertTrue(self.vacancies_page.is_open())
        self.vacancies_page.click_on_first_vacancy()
        self.assertEqual(self.vacancies_page.get_sphere(), self.sphere)

    def test_check_footer_btn_not_auth(self):
        text = self.main_page.click_footer_btn()
        self.assertEqual(text, 'Создать аккаунт')
        self.reg_page.wait_for_page_open()
        self.assertTrue(self.reg_page.is_open())

    def test_check_footer_btn_auth(self):
        setup_auth(self)
        text = self.main_page.click_footer_btn()
        self.assertEqual(text, 'Создать резюме')
        self.create_resume_page.wait_for_page_open()
        self.assertTrue(self.create_resume_page.is_open())


