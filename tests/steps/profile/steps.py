from tests.pages.profile.pages import Pages
from tests.steps.base.base_steps import BaseSteps


class Steps(BaseSteps):
    @staticmethod
    def open_edit_page():
        Pages.click_open_editing_page_button()

    @staticmethod
    def open_modal():
        Pages.click_open_editing_modal_button()

    @staticmethod
    def enter_name(name):
        Pages.enter_name(name)

    @staticmethod
    def enter_description(description):
        Pages.enter_description(description)

    @staticmethod
    def save_profile():
        Pages.save_profile()

    @staticmethod
    def save_profile_no_wait():
        Pages.save_profile_no_wait()

    @staticmethod
    def enter_profile_info(name, description):
        Pages.enter_name(name)
        Pages.enter_description(description)
