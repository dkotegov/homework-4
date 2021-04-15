import unittest

from pages.main_page import MainPage
from pages.resume_page import ResumePage
from pages.resumes_page import ResumesPage
from pages.vacancies_page import VacanciesPage
from pages.recommendation_page import RecommendationPage
from pages.profile_page import ProfilePage
from scenario.resume import ResumeScenario
from scenario.vacancy import VacancyScenario
from tests.default_setup import default_setup
from scenario.registration_applicant import RegistrationApplicantScenario
from scenario.registration_employer import RegistrationEmployerScenario
from scenario.auth import auth_as_employer_has_comp, setup_auth


class Notification(unittest.TestCase):
    def setUp(self) -> None:
        default_setup(self)

        self.main_page = MainPage(self.driver)
        self.vacancies = VacanciesPage(self.driver)
        self.rec_page = RecommendationPage(self.driver)
        self.profile = ProfilePage(self.driver)
        self.resume_page = ResumePage(self.driver)
        self.resume = self.resume_page.form
        self.resume_list = ResumesPage(self.driver)
        self.resume_list_form = self.resume_list.list
        self.scenario = ResumeScenario(self, self.resume)
        self.Applicant = RegistrationApplicantScenario(self)
        self.reg_data = self.Applicant.registration_applicant()

    def tearDown(self):
        self.main_page.open()
        self.main_page.click_logout()
        logData = {'EMAIL': self.reg_data["EMAIL"], 'PASSWORD': self.reg_data["PASSWORD"]}
        setup_auth(self, logData)
        self.Applicant.delete_applicant()
        self.driver.quit()

    def test_empty_notification(self):
        self.main_page.click_notif_popup()
        self.main_page.wait_notif_open()
        self.assertEqual(self.main_page.get_text_empty_notif(), 'У вас нет новых уведомлений')

    def test_recommended_vacancies(self):
        self.vacancies.open()
        self.vacancies.click_on_first_vacancy()
        self.main_page.click_notif_popup()
        self.main_page.wait_notif_open()
        self.assertTrue(self.main_page.check_notif_recommendations())

    def test_recommended_vacancies_page(self):
        self.vacancies.open()
        self.vacancies.click_on_first_vacancy()
        self.main_page.click_notif_popup()
        self.main_page.wait_notif_open()
        self.main_page.notification.click_notif_recommendation()
        self.assertTrue(self.rec_page.is_open())
        self.main_page.click_notif_popup()
        self.main_page.wait_notif_open()
        self.assertEqual(self.main_page.get_text_recommendation(), '')

    def test_response(self):
        self.scenario.create_resume()
        self.main_page.click_logout()

        auth_as_employer_has_comp(self)
        vacancy = VacancyScenario(test=self)
        vacancy.create_vacancy()
        self.resume_list.open()
        self.resume_list_form.go_first_resume_page()
        self.resume.response()
        self.resume.get_response_done()

        self.vacancies.open()
        self.vacancies.click_on_first_vacancy()
        vacancy.delete_vacancy()
        self.main_page.click_logout()

        setup_auth(self, self.reg_data)
        self.main_page.click_notif_popup()
        self.main_page.wait_notif_open()
        self.assertTrue(self.main_page.check_response())
        self.main_page.delete_response()
        self.scenario.delete_resume()


