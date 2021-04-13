import unittest

from pages.main_page import MainPage
from pages.vacancies_page import VacanciesPage
from pages.vacancy_page import VacancyPage
from scenario.default_setup import default_setup


class CheckSearch(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        self.PROFESSION = "Воспитатель"
        self.PLACE = "Москва"
        self.KEYWORD = "Воспитатель"
        self.COLUMN = "Направление"
        self.mainPage = MainPage(self.driver)
        self.vacanciesPage = VacanciesPage(self.driver)
        self.vacancyPage = VacancyPage(self.driver)
        self.mainPage.open()

    def test_search_by_profession(self):
        self.mainPage.search_by_profession(self.PROFESSION)
        self.assertTrue(self.vacanciesPage.check_vacancy_exist_by_profession(self.PROFESSION))

    def test_search_by_place(self):
        self.mainPage.search_by_place(self.PLACE)
        self.assertTrue(self.vacanciesPage.check_vacancy_exist_by_place(self.PLACE))

    def test_search_by_place_and_profession(self):
        self.mainPage.search_by_place_and_profession(self.PLACE, self.PROFESSION)
        self.assertTrue(self.vacanciesPage.check_vacancy_by_place_and_profession(self.PLACE, self.PROFESSION))

    def test_search_by_category(self):
        name = self.mainPage.click_on_category()
        self.vacanciesPage.click_on_first_vacancy()
        self.assertTrue(self.vacancyPage.check_info_exist(name, self.COLUMN))

    def tearDown(self):
        self.driver.quit()
