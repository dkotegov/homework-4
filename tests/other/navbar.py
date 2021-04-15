import unittest


from pages.auth_page import AuthPage
from pages.chat_page import ChatPage
from pages.companies_page import CompaniesPage
from pages.create_resume_page import CreateResumePage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.registration_page import RegistrationPage
from pages.vacancies_page import VacanciesPage
from pages.resumes_page import ResumesPage
from pages.create_vacancy_page import CreateVacancyPage
from pages.create_company_page import CreateCompanyPage
from scenario.auth import setup_auth, auth_as_employer_has_comp, auth_as_employer_no_comp, auth_as_applicant
from tests.default_setup import default_setup


class Navbar(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)

        self.main_page = MainPage(self.driver)
        self.auth_page = AuthPage(self.driver)
        self.profile_page = ProfilePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_logout_link(self):
        setup_auth(self)
        self.main_page.click_logout()
        self.assertTrue(self.auth_page.is_open())

    def test_profile_link(self):
        setup_auth(self)
        self.main_page.click_profile_page()
        self.assertTrue(self.profile_page.is_open())

    def test_notification_link(self):
        setup_auth(self)
        self.main_page.click_notif_popup()
        notif = self.main_page.notification
        self.assertTrue(notif.is_open())

    def test_chats_link(self):
        setup_auth(self)
        self.main_page.click_chats_page()
        chat_page = ChatPage(self.driver)
        self.assertTrue(chat_page.is_open())

    def test_vacancy_link(self):
        self.main_page.open()
        self.main_page.click_vac_list()
        vac_list = VacanciesPage(self.driver)
        self.assertTrue(vac_list.is_open())

    def test_resume_link(self):
        self.main_page.open()
        self.main_page.click_res_list()
        res_list = ResumesPage(self.driver)
        self.assertTrue(res_list.is_open())

    def test_company_link(self):
        self.main_page.open()
        self.main_page.click_comp_list()
        comp_list = CompaniesPage(self.driver)
        self.assertTrue(comp_list.is_open())

    def test_mainpage_link(self):
        self.auth_page.open()
        self.main_page.click_mainpage()
        self.assertTrue(self.main_page.is_open())

    def test_registration_link(self):
        self.main_page.open()
        self.main_page.click_registration_page()
        reg_page = RegistrationPage(self.driver)
        self.assertTrue(reg_page.is_open())

    def test_auth_link(self):
        self.main_page.open()
        self.main_page.click_auth_page()
        self.assertTrue(self.auth_page.is_open())

    def test_create_vacancy(self):
        auth_as_employer_has_comp(self)
        self.main_page.click_create_vacancy()
        create_vac = CreateVacancyPage(self.driver)
        self.assertTrue(create_vac.is_open())

    def test_create_company(self):
        auth_as_employer_no_comp(self)
        self.main_page.click_create_company()
        create_comp = CreateCompanyPage(self.driver)
        self.assertTrue(create_comp.is_open())

    def test_create_resume(self):
        auth_as_applicant(self)
        self.main_page.click_create_resume()
        create_res = CreateResumePage(self.driver)
        self.assertTrue(create_res.is_open())
