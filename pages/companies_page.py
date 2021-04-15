import components
from pages.base_page import BasePage
from components.resume_list import ResumeList


class CompaniesPage(BasePage):
    PATH = 'companiesList'

    def __init__(self, driver):
        self.root_locator = '//div[@class="main-list"]'
        super(CompaniesPage, self).__init__(driver, self.root_locator)
