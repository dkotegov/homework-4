from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent


class VacancyLocators:
    def __init__(self):
        self.root = '//div[@class="main-content"]'
        self.vacancy_name = '//div[@class="describe-employer__vac-name"]'


class Vacancy(BaseComponent):
    def __init__(self, driver):
        super(Vacancy, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = VacancyLocators()

    def get_vacancy_name(self) -> str:
        element = self.wait.until(
            EC.presence_of_element_located((By.XPATH,self.locators.vacancy_name))
        )
        return element.get_attribute('innerText')





