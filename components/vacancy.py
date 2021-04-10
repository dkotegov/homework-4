from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent


class VacancyLocators:
    def __init__(self):
        self.root = '//div[@class="main-content"]'
        self.vacancy_name = '//div[@class="describe-employer__vac-name"]'
        self.job_overview_title = 'inline-icon-desc__title'
        self.job_overview_body = 'inline-icon-desc__body'
        self.job_overview = '//div[@class="job-overview-li"]'


class Vacancy(BaseComponent):
    def __init__(self, driver):
        super(Vacancy, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = VacancyLocators()

    def get_vacancy_name(self) -> str:
        element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.vacancy_name))
        )
        return element.get_attribute('innerText')

    def info_exist(self, search: str, column: str) -> bool:
        elements = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.job_overview))
        )

        for el in elements:
            body = el.find_element_by_class_name(self.locators.job_overview_body)
            title = el.find_element_by_class_name(self.locators.job_overview_title)
            if body.get_attribute('innerText') == search and title.get_attribute('innerText') == column:
                return True

        return False

