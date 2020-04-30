from datetime import datetime

from tests.conftest import accessor
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
    def upload_avatar(file: str):
        Pages.upload_avatar(file)

    @staticmethod
    def save_profile_no_wait():
        Pages.save_profile_no_wait()

    @staticmethod
    def enter_profile_info(name, description):
        Pages.enter_name(name)
        Pages.enter_description(description)

    @staticmethod
    def check_date_correctness():
        selector = '.review__likes'
        accessor.wait_for_load(css_locator=selector)
        date = datetime.now()
        review_date = accessor.find_element_by_css_selector(selector).get_text()
        assert review_date[:review_date.rfind(':')] == f'{date.day}.{date.month - 1}.120 {date.hour}'
