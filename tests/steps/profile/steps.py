from datetime import datetime

from tests.conftest import accessor
from tests.pages.profile.pages import Pages
from tests.steps.base.base_steps import BaseSteps


class Steps(BaseSteps):
    @staticmethod
    def open_edit_page():
        Pages.click_open_editing_page_button()

    @staticmethod
    def check_username_error_existence():
        assert accessor.find_element_by_id('error-js-username-input') is not None

    @staticmethod
    def check_description_error_existence():
        assert accessor.find_element_by_id('error-js-save-button') is not None

    @staticmethod
    def get_avatar_src():
        return accessor.find_element_by_css_selector('.profile__photo').element.get_attribute('src')

    @staticmethod
    def open_modal():
        Pages.click_open_editing_modal_button()

    @staticmethod
    def enter_name(name):
        Pages.enter_name(name)

    @staticmethod
    def check_name_equality(name):
        assert accessor.find_element_by_css_selector('.list__item div.title').get_text().lower() == name.lower()

    @staticmethod
    def check_description_equality(description):
        assert accessor.find_elements_by_css_selector('.list__item div')[1] \
                   .get_text().lower() == description.lower()

    @staticmethod
    def enter_description(description):
        Pages.enter_description(description)

    @staticmethod
    def save_profile():
        Pages.save_profile()

    @staticmethod
    def check_avatar_update(original_name):
        assert original_name != Steps.get_avatar_src()

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
