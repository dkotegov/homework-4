import components
from pages.base_page import BasePage
from components.vacancy_create_form import VacancyCreateForm


class CreateVacancyPage(BasePage):
    PATH = 'createVacancy'

    def __init__(self, driver):
        self.vacancy_create_form = VacancyCreateForm(driver)
        super(CreateVacancyPage, self).__init__(driver, self.vacancy_create_form.locators.root)

    @property
    def form(self) -> components.vacancy_create_form:
        return VacancyCreateForm(self.driver)
