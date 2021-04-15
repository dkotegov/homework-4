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

    def get_resume_data(self):
        self.resume_form.wait_for_resume_page()
        assert self.is_open() is True, "resume page is not open"
        return {
            'description': self.resume_form.get_description(),
            'place': self.resume_form.get_place(),
            'skills': self.resume_form.get_skills(),
        }
