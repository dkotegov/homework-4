import components
from pages.base_page import BasePage
from components.resume_create_form import ResumeCreateForm
from components.experience_create_form import ExperienceCreateForm


class CreateResumePage(BasePage):
    PATH = 'createResume'

    def __init__(self, driver):
        self.resume_create_form = ResumeCreateForm(driver)
        super(CreateResumePage, self).__init__(driver, self.resume_create_form.locators.root)

    @property
    def create_form(self) -> components.resume_create_form:
        return ResumeCreateForm(self.driver)

    @property
    def create_experience_form(self) -> components.experience_create_form:
        return ExperienceCreateForm(self.driver)
