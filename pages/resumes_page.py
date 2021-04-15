import components
from pages.base_page import BasePage
from components.resume_list import ResumeList


class ResumesPage(BasePage):
    PATH = 'candidatesList'

    def __init__(self, driver):
        self.resume_list = ResumeList(driver)
        super(ResumesPage, self).__init__(driver, self.resume_list.locators.root)

    @property
    def list(self) -> components.resume_list:
        return ResumeList(self.driver)
