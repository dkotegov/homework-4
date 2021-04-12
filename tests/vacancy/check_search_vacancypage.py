import unittest

from pages.main_page import MainPage
from pages.vacancies_page import VacanciesPage
from pages.vacancy_page import VacancyPage
from scenario.default_setup import default_setup


class CheckSearchVacancyPage(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        self.KEYWORD = "Воспитатель"
        self.COLUMN = "Образование"
        self.mainPage = MainPage(self.driver)
        self.vacanciesPage = VacanciesPage(self.driver)
        self.vacancyPage = VacancyPage(self.driver)
        self.mainPage.open()

    def test_search_by_keyword(self):
        self.vacanciesPage.open()
        self.vacanciesPage.search_vacancy_by_keyword(self.KEYWORD)
        self.assertTrue(self.vacanciesPage.check_vacancy_exist_by_profession(self.KEYWORD))

    def test_search_by_checkbox(self):
        self.vacanciesPage.open()
        name = self.vacanciesPage.search_vacancy_by_checkbox()
        self.vacanciesPage.click_on_first_vacancy()

        self.assertTrue(self.vacancyPage.check_info_exist(name, self.COLUMN))

    def test_search_by_checkbox_and_keyword(self):
        self.vacanciesPage.open()
        name = self.vacanciesPage.search_vacancy_by_keyword_and_checkbox(self.KEYWORD)
        self.assertTrue(self.vacanciesPage.check_vacancy_exist_by_profession(self.KEYWORD))
        self.vacanciesPage.click_on_first_vacancy()
        self.assertTrue(self.vacancyPage.check_info_exist(name, self.COLUMN))

    def test_scroll_up_after_search(self):
        self.vacanciesPage.open()
        self.vacanciesPage.search_vacancy_by_keyword(self.KEYWORD)
        self.vacanciesPage.check_vacancy_exist_by_profession(self.KEYWORD)
        height = self.driver.execute_script("return window.pageYOffset")
        self.assertEqual(height, 0)

    def tearDown(self):
        self.driver.quit()
