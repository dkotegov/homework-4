from enum import Enum

from pages.profile_page import ProfilePage
from steps.base_steps import Steps


class ProfileSteps(Steps):
    class Fields(Enum):
        SKILLS = 0
        INTERESTS = 1
        EDUCATION = 2
        JOB = 3
        AIMS = 4

    def __init__(self, driver):
        super().__init__(driver)
        self.page = ProfilePage(driver)
        self.__fields = [self.page.right_column.SKILLS,
                         self.page.right_column.INTERESTS,
                         self.page.right_column.EDUCATION,
                         self.page.right_column.JOB,
                         self.page.right_column.AIMS]

    def edit_field(self, field, text):
        print(field.value)
        self.page.right_column.click_edit(self.__fields[field.value])
        self.page.right_column.fill_textfield(self.__fields[field.value], text)

    def cancel_editing(self, field):
        self.page.right_column.click_cross_mark(self.__fields[field.value])

    def update_field(self, field):
        self.page.right_column.click_check_mark(self.__fields[field.value])
        self.page.right_column.wait_for_update_confirmation()

    def get_field_value(self, field):
        return self.page.right_column.get_value(self.__fields[field.value])
