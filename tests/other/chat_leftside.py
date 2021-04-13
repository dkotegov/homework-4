import unittest

from pages.chat_page import ChatPage
from pages.main_page import MainPage
from pages.vacancies_page import VacanciesPage
from pages.vacancy_page import VacancyPage
from scenario.auth import setup_auth, auth_as_employer_has_comp
from scenario.create_resume import create_resume
from scenario.default_setup import default_setup
from scenario.registration_applicant import RegistrationApplicantScenario


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

    def tearDown(self):
        self.driver.quit()

    def test_chat_exist_after_response(self):
        setup_auth(self)
        create_resume(self)
        self.vacanciesPage.open()
        self.vacanciesPage.click_on_first_vacancy()
        self.vacancyPage.click_on_response()
        self.vacancyPage.click_on_first_resume()
        self.chatPage.open()
        self.assertTrue(self.chatPage.is_open())

class ChatLeftSideWithCreate(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        self.VACANCY_NAME = "Программист 1С"
        self.TEST_MSG = "привет"
        self.STATUS_TEST = "Новый статус заявки"

        self.vacanciesPage = VacanciesPage(self.driver)
        self.vacancyPage = VacancyPage(self.driver)
        self.chatPage = ChatPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.Applicant = RegistrationApplicantScenario(self)
        self.data = self.Applicant.registration_applicant()

    def tearDown(self):
        self.main_page.open()
        self.main_page.click_logout()
        logData = {'EMAIL': self.data["EMAIL"], 'PASSWORD': self.data["PASSWORD"]}
        setup_auth(self, logData)
        self.Applicant.delete_applicant()
        self.driver.quit()

    def test_check_new_chat_after_request(self):
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
        self.assertEqual(firstAndLastName[0], self.data["NAME"])
        self.assertEqual(firstAndLastName[1], self.data["SURNAME"])

    def test_check_new_message_after_request(self):
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
        logData = {'EMAIL': self.data["EMAIL"], 'PASSWORD': self.data["PASSWORD"]}
        setup_auth(self, logData)
        self.chatPage.open()
        self.chatPage.click_on_another_chat(0)
        text = self.chatPage.get_last_msg()
        self.assertEqual(text, self.TEST_MSG)


