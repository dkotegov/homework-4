from components.resume_popup import ResumePopup
from components.vacancy import Vacancy
from pages.base_page import BasePage


class VacancyPage(BasePage):
    """
    Страница Вакансии
    """

    def __init__(self, driver):
        self.vacancy = Vacancy(driver)
        self.resume_popup = ResumePopup(driver)
        super(VacancyPage, self).__init__(driver, self.vacancy.locators.root)

    def get_vacancy_name(self) -> str:
        return self.vacancy.get_vacancy_name()

    def check_info_exist(self, info: str, column: str) -> bool:
        return self.vacancy.info_exist(info, column)

    def click_on_response(self) -> str:
        return self.vacancy.click_on_response()

    def click_on_first_resume(self) -> None:
        return self.resume_popup.click_on_resume()
