import components

from pages.base_page import BasePage
from components.vacancy_update_form import VacancyUpdateForm


class UpdateVacancyPage(BasePage):
    PATH = 'updateVacancy'

    def __init__(self, driver, vacancy_uniq_title):
        self.vacancy_uniq_title = vacancy_uniq_title
        self.vacancy_update_form = VacancyUpdateForm(driver)
        super(UpdateVacancyPage, self).__init__(driver, self.vacancy_update_form.locators.root)

    @property
    def get_current_url(self):
        return self.driver.current_url

    @property
    def form(self) -> components.vacancy_update_form:
        return VacancyUpdateForm(self.driver)

