from selenium.webdriver.common.keys import Keys

from components.key_search_form import KeySearchForm
from components.vacancy_list import VacancyList
from pages.base_page import BasePage


class VacanciesPage(BasePage):
    """
    Страница Вакансий
    """
    PATH = 'employersList'

    PATH = 'employersList'

    def __init__(self, driver):
        self.vacancy_list = VacancyList(driver)
        self.vacancy_search = KeySearchForm(driver)
        super(VacanciesPage, self).__init__(driver, self.vacancy_list.locators.root)

    def check_vacancy_exist_by_profession(self, profession: str) -> bool:
        return self.vacancy_list.vacancies_exists_by_profession(profession)

    def check_vacancy_exist_by_place(self, place: str) -> bool:
        return self.vacancy_list.vacancies_exists_by_place(place)


    def check_vacancy_by_place_and_profession(self, place: str, profession: str) -> bool:
        res1 = self.vacancy_list.vacancies_exists_by_profession(profession)
        res2 = self.vacancy_list.vacancies_exists_by_place(place)
        return res1 & res2
      
    def get_sphere(self):
        return self.vacancy_list.get_sphere()


    def click_on_first_vacancy(self):
        self.vacancy_list.click_on_first_vacancy()


    def search_vacancy_by_keyword(self, keyword: str):
        self.vacancy_search.input_keyword(keyword)
        self.vacancy_search.click_on_search()

    def search_vacancy_by_checkbox(self) -> str:
        str = self.vacancy_search.click_on_search_checkbox()
        return str

    def search_vacancy_by_keyword_and_checkbox(self, keyword: str):
        str = self.vacancy_search.click_on_search_checkbox()
        self.vacancy_search.input_keyword(keyword)
        self.vacancy_search.click_on_search()
        return str

    def check_vacancies_exists_by_name(self, name: str) -> bool:
        return self.vacancy_list.vacancies_exists_by_name(name)

