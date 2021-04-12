from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


from components.base_component import BaseComponent


class ResumeFormLocators:
    def __init__(self):
        self.root = "//div[@class='cand-options']"

        self.description = "//div[text()='Подробная информация']/following-sibling::div"
        self.place = "//div[@class='about-candidate']/div[2]"
        self.skills = "//div[text()='Персональные навыки']/following-sibling::div"
        self.salary = "(//div[@class='inline-icon-desc__body'])[1]"
        self.position = '//span[@class="work-position"]'
        self.name_job = '//span[@class="name-company"]'


class ResumeForm(BaseComponent):
    def __init__(self, driver):
        super(ResumeForm, self).__init__(driver)
        self.wait = WebDriverWait(self.driver, 30, 0.1)
        self.locators = ResumeFormLocators()

    def wait_for_resume_page(self):
        self.wait.until(
            EC.url_matches("https://studhunt.ru/resume")
        )

    def get_description(self) -> str:
        return self.wait.until(
            lambda d: d.find_element_by_xpath(self.locators.description)
        ).text

    def get_place(self) -> str:
        return self.wait.until(
            lambda d: d.find_element_by_xpath(self.locators.place)
        ).text

    def get_skills(self) -> str:
        return self.wait.until(
            lambda d: d.find_element_by_xpath(self.locators.skills)
        ).text

    def get_salary(self) -> []:
        salary = self.wait.until(
            lambda d: d.find_element_by_xpath(self.locators.salary)
        ).text
        return salary.split('-')

    def get_position(self) -> []:
        return self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.position))
        )

    def get_name_job(self) -> []:
        return self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.name_job))
        )

