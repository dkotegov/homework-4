import unittest

from pages.main_page import MainPage
from pages.vacancies_page import VacanciesPage
from setup.default_setup import default_setup


class CheckSearchVacancyPage(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        self.KEYWORD = "Воспитатель"
        self.mainPage = MainPage(self.driver)
        self.vacanciesPage = VacanciesPage(self.driver)
        self.mainPage.open()

    def test_search_by_keyword(self):
        self.vacanciesPage.open()
        self.vacanciesPage.search_vacancy_by_keyword(self.KEYWORD)
        self.vacanciesPage.check_vacancy_exist_by_profession(self.KEYWORD)

    def tearDown(self):
        self.driver.quit()
