from components.vacancy import Vacancy
from pages.base_page import BasePage


class VacancyPage(BasePage):
    """
    Страница Вакансии
    """

    def __init__(self, driver):
        self.vacancy = Vacancy(driver)
        super(VacancyPage, self).__init__(driver, self.vacancy.locators.root)

    def get_vacancy_name(self) -> str:
        return self.vacancy.get_vacancy_name()

    def check_education_exist(self,education:str,column:str) -> bool:
        return self.vacancy.education_exist(education,column)