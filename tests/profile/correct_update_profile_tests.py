import os

from pages.profile import ProfilePage
from components.profile_form import ProfileForm
from tests.default_authorized import TestAuthorized


class ChangeToValidAvatarTest(TestAuthorized):
    PATH_OF_DEFAULT_AVATAR = os.getcwd() + '/resources/default_avatar.webp'
    PATH_OF_VALID_AVATAR = os.getcwd() + '/resources/valid_avatar.webp'

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
    NEW_VALID_EMAIL = 'newvalidemail@mail.ru'

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
    NEW_VALID_LOGIN = 'newvalidlogin'

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
    NEW_VALID_LOGIN = 'newvalidlogin'
    NEW_VALID_EMAIL = 'newvalidemail@mail.ru'

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
