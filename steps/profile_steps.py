from pages.profile_page import ProfilePage
from steps.base_steps import Steps


class ProfileSteps(Steps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = ProfilePage(driver)

    def edit_skills(self, text):
        self.page.right_column.click_edit(self.page.right_column.SKILLS)
        self.page.right_column.fill_textfield(self.page.right_column.SKILLS, text)
        self.page.right_column.click_check_mark(self.page.right_column.SKILLS)
        self.page.right_column.wait_for_update_confirmation()

    def get_skills(self):
        return self.page.right_column.get_value(self.page.right_column.SKILLS)
