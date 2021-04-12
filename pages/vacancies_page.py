from components.vacancy_list import VacancyList
from pages.base_page import BasePage


class VacanciesPage(BasePage):
    """
    Страница Вакансий
    """
    PATH = "employersList"

    def __init__(self, driver):
        self.vacancy_list = VacancyList(driver)
        super(VacanciesPage, self).__init__(driver, self.vacancy_list.locators.root)

    def check_vacancy_exist_by_profession(self, profession: str):
        return self.vacancy_list.vacancies_exists_by_profession(profession)

    def check_vacancy_exist_by_place(self, place: str):
        return self.vacancy_list.vacancies_exists_by_place(place)
