from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import BaseComponent


class ResumeFormLocators:
    def __init__(self):
        self.root = "//div[@class='main-content']"
        self.description = "//div[@class='job-description']/div[2]"
        self.place = "//div[@class='about-candidate']/div[2]"
        self.skills = "//div[@class='job-description']/div[5]"
        self.salary = "(//div[@class='inline-icon-desc__body'])[1]"


class ResumeForm(BaseComponent):
    def __init__(self, driver):
        super(ResumeForm, self).__init__(driver)
        self.wait = WebDriverWait(self.driver, 30, 0.1)
        self.locators = ResumeFormLocators()

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
