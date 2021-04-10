import unittest

from pages.main_page import MainPage
from pages.vacancies_page import VacanciesPage
from pages.vacancy_page import VacancyPage
from setup.auth import setup_auth
from setup.default_setup import default_setup


class CheckRecommendations(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        self.PROFESSION = "Воспитатель"
        self.mainPage = MainPage(self.driver)
        self.vacanciesPage = VacanciesPage(self.driver)
        self.vacancyPage = VacancyPage(self.driver)
        self.mainPage.open()

    def test_vacancy_open_on_click(self):
        setup_auth(self)
        self.mainPage.click_recommendations()
        self.assertTrue(self.vacanciesPage.is_open())
        self.vacanciesPage.click_on_first_vacancy()
        self.assertTrue(self.vacancyPage.is_open())

    def test_vacancy_equiv_on_click(self):
        setup_auth(self)
        self.mainPage.search_by_profession(self.PROFESSION)
        self.vacanciesPage.click_on_first_vacancy()
        name = self.vacancyPage.get_vacancy_name()
        self.assertTrue(self.vacanciesPage.check_vacancy_exist_by_profession(name))

    def tearDown(self):
        self.driver.quit()

