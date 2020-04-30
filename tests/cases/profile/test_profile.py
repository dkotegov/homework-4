import os

from tests.conftest import accessor, open_user_profile, create_review
from tests.steps.profile.steps import Steps


class TestProfileEditing:
    def test_edit_name_success(self, user_profile, user_restore_default, logout):
        name = 'new'
        Steps.open_modal()
        Steps.enter_name(name)
        Steps.save_profile()
        assert accessor.find_element_by_css_selector('.list__item div.title').get_text().lower() == name.lower()

    def test_edit_description_success(self, user_profile, user_restore_default, logout):
        description = 'new description'
        Steps.open_modal()
        Steps.enter_description(description)
        Steps.save_profile()
        assert accessor.find_elements_by_css_selector('.list__item div')[1] \
                   .get_text().lower() == description.lower()

    def test_edit_name_too_short(self, user_profile, logout):
        name = '2'
        Steps.open_modal()
        Steps.enter_name(name)
        Steps.save_profile_no_wait()
        assert accessor.find_element_by_id('error-js-username-input') is not None

    def test_edit_name_invalid_symbols(self, user_profile, logout):
        name = 'русские буковки'
        Steps.open_modal()
        Steps.enter_name(name)
        Steps.save_profile_no_wait()
        assert accessor.find_element_by_id('error-js-username-input') is not None

    def test_edit_description_too_long(self, user_profile, logout):
        description = 'a' * 500
        Steps.open_modal()
        Steps.enter_description(description)
        Steps.save_profile_no_wait()
        assert accessor.find_element_by_id('error-js-save-button') is not None

    def test_upload_avatar(self, user_profile, user_restore_default, logout):
        original_avatar_name = accessor.find_element_by_css_selector('.profile__photo').element.get_attribute('src')
        Steps.open_modal()
        Steps.upload_avatar(f'{os.getcwd()}/../../test_data/test.jpg')
        Steps.save_profile()
        assert original_avatar_name != accessor.find_element_by_css_selector('.profile__photo') \
            .element.get_attribute('src')

    def test_review_in_profile(self, user):
        create_review()
        open_user_profile()
        Steps.check_date_correctness()
