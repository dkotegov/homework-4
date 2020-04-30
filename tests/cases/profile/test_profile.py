import os

from tests.conftest import accessor, open_user_profile, create_review
from tests.steps.profile.steps import Steps


class TestProfileEditing:
    def test_edit_name_success(self, user_profile, user_restore_default, logout):
        name = 'new'
        Steps.open_modal()
        Steps.enter_name(name)
        Steps.save_profile()
        Steps.check_name_equality(name)

    def test_edit_description_success(self, user_profile, user_restore_default, logout):
        description = 'new description'
        Steps.open_modal()
        Steps.enter_description(description)
        Steps.save_profile()
        Steps.check_description_equality(description)

    def test_edit_name_too_short(self, user_profile, logout):
        name = '2'
        Steps.open_modal()
        Steps.enter_name(name)
        Steps.save_profile_no_wait()
        Steps.check_username_error_existence()

    def test_edit_name_invalid_symbols(self, user_profile, logout):
        name = 'русские буковки'
        Steps.open_modal()
        Steps.enter_name(name)
        Steps.save_profile_no_wait()
        Steps.check_username_error_existence()

    def test_edit_description_too_long(self, user_profile, logout):
        description = 'a' * 500
        Steps.open_modal()
        Steps.enter_description(description)
        Steps.save_profile_no_wait()
        Steps.check_description_error_existence()

    def test_upload_avatar(self, user_profile, user_restore_default, logout):
        original_avatar_name = Steps.get_avatar_src()
        Steps.open_modal()
        Steps.upload_avatar(f'{os.getcwd()}/tests/test_data/test.jpg')
        Steps.save_profile()
        Steps.check_avatar_update(original_avatar_name)


class TestProfileReview:
    def test_review_in_profile(self, user):
        create_review()
        open_user_profile()
        Steps.check_date_correctness()
