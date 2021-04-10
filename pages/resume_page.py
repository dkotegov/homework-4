import components
from pages.base_page import BasePage
from components.resume_form import ResumeForm


class ResumePage(BasePage):
    @property
    def form(self) -> components.resume_form:
        return ResumeForm(self.driver)
