from components.vacancy_list import VacancyList
from pages.base_page import BasePage


class VacanciesPage(BasePage):
    """
    Страница Вакансий
    """

    def __init__(self, driver):
        super(VacanciesPage, self).__init__(driver)

        self.vacancy_list = VacancyList(self.driver)

    def check_vacancy_exist_by_profession(self, **kwargs):
        return self.vacancy_list.vacancies_exists_by_profession(**kwargs)

    def check_vacancy_exist_by_place(self, **kwargs):
        return self.vacancy_list.vacancies_exists_by_place(**kwargs)

    def check_vacancy_exist(self):
        return self.vacancy_list.vacancies_exists()
