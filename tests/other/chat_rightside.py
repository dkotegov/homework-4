import unittest

from pages.chat_page import ChatPage
from pages.vacancies_page import VacanciesPage
from pages.vacancy_page import VacancyPage
from scenario.auth import setup_auth
from scenario.create_resume import create_resume
from scenario.default_setup import default_setup
from scenario.registration_applicant import registration_applicant


class ChatRightSide(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)

        self.vacanciesPage = VacanciesPage(self.driver)
        self.vacancyPage = VacancyPage(self.driver)
        self.chatPage = ChatPage(self.driver)

    def test_check_clear_chats_info(self):
        registration_applicant(self)
        self.chatPage.open()

    def tearDown(self):
        self.driver.quit()
