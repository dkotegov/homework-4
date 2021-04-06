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
        self.page.right_column.click_edit(self.__fields[field.value])
        self.page.right_column.fill_textfield(self.__fields[field.value], text)

    def cancel_editing(self, field):
        self.page.right_column.click_cross_mark(self.__fields[field.value])

    def update_field(self, field):
        self.page.right_column.click_check_mark(self.__fields[field.value])
        self.page.right_column.wait_for_update_confirmation()

    def get_field_value(self, field):
        return self.page.right_column.get_value(self.__fields[field.value])

    def open_meetings_page(self):
        self.page.navbar.click_meetings()

    def open_people_page(self):
        self.page.navbar.click_people()

    def open_stranger_profile(self, user_id=1):
        self.open_page(f'/profile?userId={user_id}')

    def check_subscribe_btn_visibility(self):
        return self.page.left_column.is_subscribe_btn_visible()

    def get_subscribe_btn_text(self):
        return self.page.left_column.get_sub_btn_text()

    def open_vk_link(self):
        self.page.left_column.click_vk()

    def open_tg_link(self):
        self.page.left_column.click_telegram()

    def open_test_meeting(self):
        self.page.left_column.click_test_meeting()

    def sign_out(self):
        self.page.navbar.click_menu()
        self.page.navbar.click_sign_out()

    def subscribe(self):
        self.page.left_column.click_subscribe_btn()

    def handle_sub_confirmation(self):
        self.page.left_column.wait_for_sub_confirmation()
        self.page.left_column.click_close_confirmation()

    def unsubscribe(self):
        self.page.left_column.click_subscribe_btn()

    def handle_unsub_confirmation(self):
        self.page.left_column.wait_for_unsub_confirmation()
        self.page.left_column.click_close_confirmation()
