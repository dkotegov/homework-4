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

    def hover_on_avatar(self):
        self.page.left_column.hover_on_avatar()

    def get_avatar_overlay_text(self):
        return self.page.left_column.get_avatar_overlay_text()

    def choose_new_avatar(self, filename):
        self.page.left_column.choose_avatar_file(filename)

    def get_avatar_button_text(self):
        return self.page.left_column.get_avatar_button_text()

    def open_tags_modal(self):
        self.page.tags.open_tags_modal()
        self.page.tags.wait_for_tags_modal()

    def select_cpp_tag(self):
        self.page.tags.click_cpp_tag()
        return self.page.tags.get_cpp_tag_bg_color()

    def update_tags(self):
        self.page.tags.click_commit_tags_update()
        self.page.tags.close_update_confirmation()

    def get_tags(self):
        return self.page.tags.get_tags()

    def close_tags_modal(self):
        self.page.tags.click_close_modal()
        self.page.tags.wait_for_modal_closing()

    def is_tags_modal_visible(self):
        return self.page.tags.get_modal_visibility()
