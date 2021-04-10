import unittest

from pages.main_page import MainPage
from pages.vacancies_page import VacanciesPage
from tests.default_setup import default_setup


class CheckSearch(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        self.PROFESSION = "Воспитатель"
        self.PLACE = "Москва"
        self.mainPage = MainPage(self.driver)
        self.vacanciesPage = VacanciesPage(self.driver)
        self.mainPage.open()

    def test_search_by_profession(self):
        self.mainPage.search_by_profession(profession=self.PROFESSION)
        self.assertTrue(self.vacanciesPage.check_vacancy_exist_by_profession(profession=self.PROFESSION))

    def test_search_by_place(self):
        self.mainPage.search_by_place(place=self.PLACE)
        self.assertTrue(self.vacanciesPage.check_vacancy_exist_by_place(place=self.PLACE))

    def test_vacancies_page_move(self):
        self.mainPage.search_by_place(place=self.PLACE)
        self.assertTrue(self.vacanciesPage.is_open())

    def tearDown(self):
        self.driver.quit()
