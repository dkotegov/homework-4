import unittest

from pages.chat_page import ChatPage
from pages.vacancies_page import VacanciesPage
from pages.vacancy_page import VacancyPage
from setup.auth import setup_auth
from setup.create_resume import create_resume
from setup.default_setup import default_setup


class ChatLeftSide(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        self.PROFESSION = "Воспитатель"

        self.vacanciesPage = VacanciesPage(self.driver)
        self.vacancyPage = VacancyPage(self.driver)
        self.chatPage = ChatPage(self.driver)

    def test_chat_exist_after_response(self):
        setup_auth(self)
        create_resume(self)
        self.vacanciesPage.open()
        self.vacanciesPage.click_on_first_vacancy()
        self.vacancyPage.click_on_response()
        self.vacancyPage.click_on_first_resume()
        self.chatPage.open()
        self.assertTrue(self.chatPage.is_open())

    def test_click_another_chat(self):
        setup_auth(self)
        self.chatPage.open()
        self.chatPage.click_on_another_chat(0)
        chat_name1 = self.chatPage.click_on_another_chat(1)
        chat_name2 = self.chatPage.get_current_chat_name()
        self.assertEqual(chat_name1, chat_name2)

    def tearDown(self):
        self.driver.quit()
