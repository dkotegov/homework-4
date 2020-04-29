from time import sleep

from tests.conftest import accessor
from tests.steps.profile.steps import Steps


class TestProfileEditing:
    def test_edit_name_success(self, test_user_profile, test_user_restore_default, logout):
        name = 'new'
        Steps.open_modal()
        Steps.enter_name(name)
        Steps.save_profile()
        assert accessor.find_element_by_css_selector('.list__item div.title').get_text().lower() == name.lower()
        test_user_restore_default()

    def test_edit_description_success(self, test_user_profile, test_user_restore_default, logout):
        description = 'new description'
        Steps.open_modal()
        Steps.enter_description(description)
        Steps.save_profile()
        assert accessor.find_elements_by_css_selector('.list__item div')[1] \
                   .get_text().lower() == description.lower()
        test_user_restore_default()

    def test_edit_name_too_short(self, test_user_profile, logout):
        name = '2'
        Steps.open_modal()
        Steps.enter_name(name)
        Steps.save_profile_no_wait()
        assert accessor.find_element_by_id('error-js-username-input') is not None

    def test_edit_name_invalid_symbols(self, test_user_profile, logout):
        name = 'русские буковки'
        Steps.open_modal()
        Steps.enter_name(name)
        Steps.save_profile_no_wait()
        assert accessor.find_element_by_id('error-js-username-input') is not None

    def test_edit_description_too_long(self, test_user_profile, logout):
        description = 'a' * 500
        Steps.open_modal()
        Steps.enter_description(description)
        Steps.save_profile_no_wait()
        assert accessor.find_element_by_id('error-js-save-button') is not None
