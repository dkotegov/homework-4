from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent


class VacancyListLocators:
    def __init__(self):
        self.root = '//div[@class="main-list"]'
        self.vacancy_list = '//div[@class="list-row"]'
        self.vacancy_list_names = '//div[@class="list-row-description__name"]'
        self.vacancy_list_location = '//div[@class="list-row-description__location"]'


class VacancyList(BaseComponent):
    def __init__(self, driver):
        super(VacancyList, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = VacancyListLocators()

    def vacancies_exists_by_profession(self, profession: str) -> bool:
        try:
            elements = WebDriverWait(self.driver, 1).until(
                EC.presence_of_all_elements_located((By.XPATH, self.locators.vacancy_list_names)))
        except TimeoutException:
            return True

        for el in elements:
            elem = el.find_element_by_tag_name("a")
            if not str.lower(elem.get_attribute('text')).__contains__(str.lower(profession)):
                return False

        return True

    def vacancies_exists_by_place(self, place: str) -> bool:
        try:
            elements = WebDriverWait(self.driver, 1).until(
                EC.presence_of_all_elements_located((By.XPATH, self.locators.vacancy_list_location)))
        except TimeoutException:
            return True

        for el in elements:
            if not str.lower(el.get_attribute('innerText')).__contains__(str.lower(place)):
                return False

        return True

    def click_on_first_vacancy(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.vacancy_list)))

        element.click()

    def vacancies_exists_by_name(self, name: str) -> bool:
        try:
            elements = WebDriverWait(self.driver, 1).until(
                EC.presence_of_all_elements_located((By.XPATH, self.locators.vacancy_list_names)))
        except TimeoutException:
            return True

        for el in elements:
            elem = el.find_element_by_tag_name("a")
            if not str.lower(elem.get_attribute('text')).__contains__(str.lower(name)):
                return True

        return False

