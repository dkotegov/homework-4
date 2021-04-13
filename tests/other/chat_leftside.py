import unittest

from pages.chat_page import ChatPage
from pages.main_page import MainPage
from pages.vacancies_page import VacanciesPage
from pages.vacancy_page import VacancyPage
from scenario.auth import setup_auth, auth_as_employer_has_comp
from scenario.create_resume import create_resume
from scenario.default_setup import default_setup
from scenario.registration_applicant import registration_applicant


class ChatLeftSide(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        self.VACANCY_NAME = "Программист 1С"
        self.TEST_MSG = "привет"
        self.STATUS_TEST = "Новый статус заявки"

        self.vacanciesPage = VacanciesPage(self.driver)
        self.vacancyPage = VacancyPage(self.driver)
        self.chatPage = ChatPage(self.driver)
        self.main_page = MainPage(self.driver)

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
        name1 = self.chatPage.get_current_chat_name()
        time1 = self.chatPage.get_chat_info_time(0)
        self.chatPage.click_on_another_chat(1)
        name2 = self.chatPage.get_current_chat_name()
        time2 = self.chatPage.get_chat_info_time(1)
        if name1 != name2:
            self.assertTrue(self.chatPage.is_open())
        else:
            self.assertNotEqual(time1, time2)

    def test_check_new_chat_after_request(self):
        data = registration_applicant(self)
        create_resume(self)
        self.vacanciesPage.open()
        self.vacanciesPage.search_vacancy_by_keyword(self.VACANCY_NAME)
        self.vacanciesPage.click_on_first_vacancy()
        self.vacancyPage.click_on_response()
        self.vacancyPage.click_on_first_resume()
        self.chatPage.open()
        self.main_page.open()
        self.main_page.click_logout()

        auth_as_employer_has_comp(self)
        self.chatPage.open()
        name = self.chatPage.get_first_chat_name()
        firstAndLastName = name.split(" ")
        self.assertEqual(firstAndLastName[0], data["NAME"])
        self.assertEqual(firstAndLastName[1], data["SURNAME"])

    def test_check_new_message_after_request(self):
        data = registration_applicant(self)
        create_resume(self)
        self.vacanciesPage.open()
        self.vacanciesPage.search_vacancy_by_keyword(self.VACANCY_NAME)
        self.vacanciesPage.click_on_first_vacancy()
        self.vacancyPage.click_on_response()
        self.vacancyPage.click_on_first_resume()

        self.main_page.open()
        self.main_page.click_logout()

        auth_as_employer_has_comp(self)
        self.chatPage.open()
        self.chatPage.click_on_another_chat(0)
        self.chatPage.click_on_send_msg(self.TEST_MSG)

        self.main_page.open()
        self.main_page.click_logout()
        logData = {'EMAIL': data["EMAIL"], 'PASSWORD': data["PASSWORD"]}
        setup_auth(self, logData)
        self.chatPage.open()
        self.chatPage.click_on_another_chat(0)
        text = self.chatPage.get_last_msg()
        self.assertEqual(text, self.TEST_MSG)

    def test_check_new_status_after_msg(self):
        data = registration_applicant(self)
        create_resume(self)
        self.vacanciesPage.open()
        self.vacanciesPage.search_vacancy_by_keyword(self.VACANCY_NAME)
        self.vacanciesPage.click_on_first_vacancy()
        self.vacancyPage.click_on_response()
        self.vacancyPage.click_on_first_resume()

        self.main_page.open()
        self.main_page.click_logout()

        auth_as_employer_has_comp(self)
        self.chatPage.open()
        self.chatPage.click_on_another_chat(0)
        status = self.chatPage.get_chat_status()
        self.assertEqual(status, self.STATUS_TEST)
        self.chatPage.click_on_send_msg(self.TEST_MSG)
        last = self.chatPage.get_chat_info_last_msg()
        self.assertEqual(last, self.TEST_MSG)

    def tearDown(self):
        self.driver.quit()
