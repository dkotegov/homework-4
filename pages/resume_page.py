import components
from pages.base_page import BasePage
from components.resume import ResumeForm


class ResumePage(BasePage):

    def __init__(self, driver):
        self.resume_form = ResumeForm(driver)
        super(ResumePage, self).__init__(driver, self.resume_form.locators.root)

    @property
    def form(self) -> components.resume:
        return ResumeForm(self.driver)
