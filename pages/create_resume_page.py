import components
from pages.base_page import BasePage
from components.resume_create_form import ResumeCreateForm


class CreateResumePage(BasePage):
    BASE_URL = 'https://studhunt.ru/'
    PATH = 'createResume'

    @property
    def form(self) -> components.resume_create_form:
        return ResumeCreateForm(self.driver)
