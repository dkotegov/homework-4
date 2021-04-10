from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent


class VacancyListLocators:
    def __init__(self):
        self.vacancy_list = '//div[@class="list-row"]'
        self.vacancy_list_names = '//div[@class="list-row-description__name"]'
        self.vacancy_list_location = '//div[@class="list-row-description__location"]'


class VacancyList(BaseComponent):
    def __init__(self, driver):
        super(VacancyList, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = VacancyListLocators()

    def vacancies_exists_by_profession(self, profession: str):
        elements = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.vacancy_list_names)))

        for el in elements:
            elem = el.find_element_by_tag_name("a")
            print(str.lower(elem.get_attribute('text')), str.lower(profession))
            if not str.lower(elem.get_attribute('text')).__contains__(str.lower(profession)):
                return False

        return True

    def vacancies_exists_by_place(self, place: str):
        elements = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.vacancy_list_location)))

        for el in elements:
            print(str.lower(el.get_attribute('text')), str.lower(place))
            if not str.lower(el.get_attribute('text')).__contains__(str.lower(place)):
                return False

        return True
