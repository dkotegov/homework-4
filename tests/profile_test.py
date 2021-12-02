import os

from pages.profile import ProfilePage
from components.profile_form import ProfileForm
from tests.default_authorized import TestAuthorized
import constants


class ChangeToInvalidAvatarTest(TestAuthorized):
    PATH_OF_INVALID_AVATAR = os.getcwd() + constants.DEFAULT_AVATAR
    PATH_OF_DEFAULT_AVATAR = constants.DEFAULT_AVATAR

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_page.upload_new_avatar(self.PATH_OF_INVALID_AVATAR)
        profile_page.save_avatar()

        profile_page.open()

        self.assertEqual(
            self.PATH_OF_DEFAULT_AVATAR,
            profile_page.get_current_avatar()
        )


class ChangeToInvalidLoginTest(TestAuthorized):
    INVALID_LOGIN = constants.INVALID_SIGNUP_LOGIN

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_form = ProfileForm(self.driver)
        profile_form.set_login(self.INVALID_LOGIN)
        profile_form.submit()

        self.assertEqual(
            profile_form.get_login_error(),
            constants.ERROR_MSG_OF_INVALID_UPD_LOGIN
        )


class ChangeToEmptyLoginTest(TestAuthorized):
    EMPTY_LOGIN = ''

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_form = ProfileForm(self.driver)
        profile_form.set_login(self.EMPTY_LOGIN)
        profile_form.submit()

        self.assertEqual(
            profile_form.get_login_error(),
            constants.ERROR_MSG_OF_EMPTY_UPD_LOGIN
        )


class ChangeToInvalidEmailTest(TestAuthorized):
    INVALID_EMAIL = constants.INVALID_EMAIL

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_form = ProfileForm(self.driver)
        profile_form.set_email(self.INVALID_EMAIL)
        profile_form.submit()

        self.assertEqual(
            profile_form.get_email_error(),
            constants.ERROR_MSG_OF_INVALID_UPD_EMAIL
        )


class ChangeToEmptyEmailTest(TestAuthorized):
    EMPTY_EMAIL = ''

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_form = ProfileForm(self.driver)
        profile_form.set_email(self.EMPTY_EMAIL)
        profile_form.submit()

        self.assertEqual(
            profile_form.get_email_error(),
            constants.ERROR_MSG_OF_EMPTY_UPD_EMAIL
        )


class ChangeToInvalidEmailAndLoginTest(TestAuthorized):
    INVALID_LOGIN = constants.INVALID_SIGNUP_LOGIN
    INVALID_EMAIL = constants.INVALID_SIGNUP_EMAIL

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_form = ProfileForm(self.driver)
        profile_form.set_login(self.INVALID_LOGIN)
        profile_form.set_email(self.INVALID_EMAIL)
        profile_form.submit()

        self.assertEqual(
            profile_form.get_login_error(),
            constants.ERROR_MSG_OF_INVALID_UPD_LOGIN
        )


class ChangeToInvalidLoginAndValidEmailTest(TestAuthorized):
    INVALID_LOGIN = 'testqa@'
    NEW_VALID_EMAIL = 'newvalidemail@mail.ru'

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_form = ProfileForm(self.driver)
        profile_form.set_login(self.INVALID_LOGIN)
        profile_form.set_email(self.NEW_VALID_EMAIL)
        profile_form.submit()

        self.assertEqual(
            profile_form.get_login_error(),
            constants.ERROR_MSG_OF_INVALID_UPD_LOGIN
        )


class ChangeToValidAvatarTest(TestAuthorized):
    PATH_OF_DEFAULT_AVATAR = os.getcwd() + constants.PATH_OF_DEFAULT_AVATAR
    PATH_OF_VALID_AVATAR = os.getcwd() + constants.PATH_OF_VALID_AVATAR

    def tearDown(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()
        profile_page.upload_new_avatar(self.PATH_OF_DEFAULT_AVATAR)
        profile_page.save_avatar()
        self.driver.quit()

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        old_avatar = profile_page.get_current_avatar()
        profile_page.upload_new_avatar(self.PATH_OF_VALID_AVATAR)
        profile_page.save_avatar()

        self.assertNotEqual(
            old_avatar,
            profile_page.get_current_avatar()
        )


class ChangeToValidEmailTest(TestAuthorized):
    NEW_VALID_EMAIL = constants.NEW_VALID_EMAIL

    def tearDown(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()
        profile_form = ProfileForm(self.driver)
        profile_form.set_email(os.environ['LOGIN'])
        profile_form.submit()
        self.driver.quit()

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_form = ProfileForm(self.driver)
        profile_form.set_email(self.NEW_VALID_EMAIL)
        profile_form.submit()

        self.assertEqual(
            self.NEW_VALID_EMAIL,
            profile_form.get_email()
        )


class ChangeToValidLoginTest(TestAuthorized):
    NEW_VALID_LOGIN = constants.NEW_VALID_LOGIN

    def tearDown(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()
        profile_form = ProfileForm(self.driver)
        profile_form.set_login(self.old_login)
        profile_form.submit()
        self.driver.quit()

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_form = ProfileForm(self.driver)
        self.old_login = profile_form.get_login()
        profile_form.set_login(self.NEW_VALID_LOGIN)
        profile_form.submit()

        self.assertEqual(
            self.NEW_VALID_LOGIN,
            profile_form.get_login()
        )


class ChangeToValidLoginAndEmailTest(TestAuthorized):
    NEW_VALID_LOGIN = constants.NEW_VALID_LOGIN
    NEW_VALID_EMAIL = constants.NEW_VALID_EMAIL

    def tearDown(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()
        profile_form = ProfileForm(self.driver)
        profile_form.set_login(self.old_login)
        profile_form.set_email(os.environ['LOGIN'])
        profile_form.submit()
        self.driver.quit()

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_form = ProfileForm(self.driver)
        self.old_login = profile_form.get_login()
        profile_form.set_login(self.NEW_VALID_LOGIN)
        profile_form.set_email(self.NEW_VALID_EMAIL)
        profile_form.submit()

        self.assertEqual(
            self.NEW_VALID_LOGIN,
            profile_form.get_login()
        )

        self.assertEqual(
            self.NEW_VALID_EMAIL,
            profile_form.get_email()
        )


class ClickOnSubscriptionBtnTest(TestAuthorized):
    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_page.click_on_subscription_btn()

        self.assertTrue(profile_page.is_umoney_url())
