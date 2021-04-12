import unittest


from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from scenario.auth import setup_auth
from scenario.default_setup import default_setup


class Navbar(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)

        self.main_page = MainPage(self.driver)
        self.auth_page = AuthPage(self.driver)
        self.profile_page = ProfilePage(self.driver)

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

    def test_chats_link(self):
        setup_auth(self)
        self.main_page.click_chats_page()

    def test_vacancy_link(self):
        self.main_page.open()
        self.main_page.click_vac_list()

    def test_resume_link(self):
        self.main_page.open()
        self.main_page.click_res_list()

    def test_company_link(self):
        self.main_page.open()
        self.main_page.click_comp_list()

    def test_mainpage_link(self):
        self.auth_page.open()
        self.main_page.click_mainpage()

    def test_registration_link(self):
        self.main_page.open()
        self.main_page.click_registration_page()

    def test_auth_link(self):
        self.main_page.open()
        self.main_page.click_auth_page()
        self.assertTrue(self.auth_page.is_open())



