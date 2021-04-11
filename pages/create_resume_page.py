import components
from pages.base_page import BasePage
from components.resume_create_form import ResumeCreateForm


class CreateResumePage(BasePage):
    PATH = 'createResume'

    def __init__(self, driver):
        self.resume_create_form = ResumeCreateForm(driver)
        super(CreateResumePage, self).__init__(driver, self.resume_create_form.locators.root)

    @property
    def form(self) -> components.resume_create_form:
        return ResumeCreateForm(self.driver)
