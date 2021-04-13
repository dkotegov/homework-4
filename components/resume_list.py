from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent


class ResumeListLocators:
    def __init__(self):
        self.root = '//div[@class="main-list"]'

        self.first_resume_title = '(//div[@class="list-row-description__name"])[1]/a'
        self.first_resume_description = '(//div[@class="list-row-description__specialism"])[1]'

        self.first_resume_container = '(//div[@class="list-row"])[1]'


class ResumeList(BaseComponent):
    def __init__(self, driver):
        super(ResumeList, self).__init__(driver)

        self.locators = ResumeListLocators()

    def get_first_resume_title(self) -> str:
        return self.get_field(self.locators.first_resume_title)

    def get_first_resume_description(self) -> str:
        return self.get_field(self.locators.first_resume_description)

    def go_first_resume_page(self):
        self.click_locator(self.locators.first_resume_container)