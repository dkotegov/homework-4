import components
from pages.base_page import BasePage
from components.resume_form import ResumeForm


class ResumePage(BasePage):

    def __init__(self, driver):
        self.resume_form = ResumeForm(driver)
        super(ResumePage, self).__init__(driver, self.resume_form.ROOT)

    @property
    def form(self) -> components.resume_form:
        return ResumeForm(self.driver)
