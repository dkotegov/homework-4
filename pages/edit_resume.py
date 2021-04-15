import components
from pages.base_page import BasePage
from components.resume_edit_form import ResumeEditForm


class EditResumePage(BasePage):
    PATH = 'createResume'

    def __init__(self, driver):
        self.resume_edit_form = ResumeEditForm(driver)
        super(EditResumePage, self).__init__(driver, self.resume_edit_form.locators.root)

    @property
    def edit_form(self) -> components.resume_edit_form:
        return ResumeEditForm(self.driver)
