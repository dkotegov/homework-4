import unittest

from pages.main_page import MainPage
from pages.vacancies_page import VacanciesPage
from pages.recommendation_page import RecommendationPage
from pages.profile_page import ProfilePage
from tests.default_setup import default_setup
from scenario.registration_applicant import registration_applicant
from scenario.registration_employer import registration_employer


class Notification(unittest.TestCase):
    def setUp(self) -> None:
        default_setup(self)

        self.main_page = MainPage(self.driver)
        self.vacancies = VacanciesPage(self.driver)
        self.rec_page = RecommendationPage(self.driver)
        self.profile = ProfilePage(self.driver)

    def tearDown(self):
        self.profile.open()
        self.profile.delete_account()
        self.driver.quit()

    def test_empty_notification(self):
        registration_employer(self, False)
        self.main_page.click_notif_popup()
        self.main_page.wait_notif_open()
        self.assertEqual(self.main_page.get_text_empty_notif(), 'У вас нет новых уведомлений')

    def test_recommended_vacancies(self):
        registration_applicant(self)
        self.vacancies.open()
        self.vacancies.click_on_first_vacancy()
        self.main_page.click_notif_popup()
        self.main_page.wait_notif_open()
        self.assertTrue(self.main_page.check_notif_recommendations())


    def test_recommended_vacancies_page(self):
        registration_applicant(self)
        self.vacancies.open()
        self.vacancies.click_on_first_vacancy()
        self.main_page.click_notif_popup()
        self.main_page.wait_notif_open()
        self.main_page.notification.click_notif_recommendation()
        self.assertTrue(self.rec_page.is_open())
        self.main_page.click_notif_popup()
        self.main_page.wait_notif_open()
        a = self.main_page.get_text_recommendation()
        self.assertEqual(a, '')


