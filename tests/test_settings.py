import os
import unittest

import requests
from selenium.webdriver import DesiredCapabilities, Remote

from pages.auth_page import AuthPage
from pages.group_page import GroupPage
from pages.my_groups_components import AgeRestriction, GroupSubcategory
from pages.settings_components import GeneralForm, Role, RoleRadioButtons, WhoCanLeaveComments


class TestsChangeNameAndDescriptions(unittest.TestCase):
    LOGIN_1 = os.environ['LOGIN_1']
    PASSWORD_1 = os.environ['PASSWORD_1']

    def setUp(self):
        self.driver_1 = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver_1.implicitly_wait(10)

        auth_page = AuthPage(self.driver_1)
        auth_page.open()

        profile_page = auth_page.sign_in(self.LOGIN_1, self.PASSWORD_1)

        desc = {
            'description': 'group about shit',
            'title': 'pulp fiction',
            'subcategory': GroupSubcategory.CINEMA_TV,
            'age_restriction': AgeRestriction.NO_RESTRICTION
        }

        group_page = profile_page.to_groups_page().create_public_page(desc)
        profile_page.open()
        group_page.open()

        setting_page = group_page.to_settings_page()

        self.group_page = group_page
        self.setting_page = setting_page

    def tearDown(self):
        self.group_page.delete_group()
        self.driver_1.quit()

    def test_change_name_and_descriptions(self):
        general_page = self.setting_page.to_general_page()
        general_page.change_name_and_description('kill bill', "this group about bill's death")
        self.group_page.open()
        self.assertEqual(self.group_page.get_name(), 'kill bill')
        self.assertEqual(self.group_page.get_description(), "this group about bill's death")


class TestsAddAPIKey(unittest.TestCase):
    LOGIN_1 = os.environ['LOGIN_1']
    PASSWORD_1 = os.environ['PASSWORD_1']

    def setUp(self):
        self.driver_1 = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver_1.implicitly_wait(10)

        auth_page = AuthPage(self.driver_1)
        auth_page.open()

        profile_page = auth_page.sign_in(self.LOGIN_1, self.PASSWORD_1)

        desc = {
            'description': 'group about shit',
            'title': 'pulp fiction',
            'subcategory': GroupSubcategory.CINEMA_TV,
            'age_restriction': AgeRestriction.NO_RESTRICTION
        }

        group_page = profile_page.to_groups_page().create_public_page(desc)

        setting_page = group_page.to_settings_page()

        setting_page.open()

        self.group_page = group_page
        self.setting_page = setting_page

    def tearDown(self):
        self.group_page.delete_group()
        self.driver_1.quit()

    def test_get_api_key(self):
        key = self.setting_page.open().to_management_page().generate_access_key()
        self.assertIsNotNone(key)
        response = self.get_test_request(key)
        self.assertNotIn("error_code", response.keys())

    @staticmethod
    def get_test_request(key):
        r = requests.get("https://api.ok.ru/graph/me/chats?access_token={}".format(key))
        return r.json()


class TestsAddApp(unittest.TestCase):
    LOGIN_1 = os.environ['LOGIN_1']
    PASSWORD_1 = os.environ['PASSWORD_1']

    def setUp(self):
        self.driver_1 = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver_1.implicitly_wait(10)

        auth_page = AuthPage(self.driver_1)
        auth_page.open()

        profile_page = auth_page.sign_in(self.LOGIN_1, self.PASSWORD_1)

        desc = {
            'description': 'group about shit',
            'title': 'pulp fiction',
            'subcategory': GroupSubcategory.CINEMA_TV,
            'age_restriction': AgeRestriction.NO_RESTRICTION
        }

        group_page = profile_page.to_groups_page().create_public_page(desc)

        setting_page = group_page.to_settings_page()

        setting_page.open()

        self.group_page = group_page
        self.setting_page = setting_page

    def tearDown(self):
        self.group_page.delete_group()
        self.driver_1.quit()

    def test_add_app(self):
        app_page = self.setting_page.to_application_page()
        app_page.open()
        name = app_page.add_app()
        self.group_page.open()
        self.assertTrue(self.group_page.is_app_added(name))


class TestsAddGroupLinks(unittest.TestCase):
    LOGIN_1 = os.environ['LOGIN_1']
    PASSWORD_1 = os.environ['PASSWORD_1']

    def setUp(self):
        self.driver_1 = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver_1.implicitly_wait(10)

        auth_page = AuthPage(self.driver_1)
        auth_page.open()

        profile_page = auth_page.sign_in(self.LOGIN_1, self.PASSWORD_1)

        desc = {
            'description': 'group about shit',
            'title': 'pulp fiction',
            'subcategory': GroupSubcategory.CINEMA_TV,
            'age_restriction': AgeRestriction.NO_RESTRICTION
        }

        group_page = profile_page.to_groups_page().create_public_page(desc)

        setting_page = group_page.to_settings_page()

        setting_page.open()

        self.group_page = group_page
        self.setting_page = setting_page

    def tearDown(self):
        self.group_page.delete_group()
        self.driver_1.quit()

    def test_add_group_links(self):
        group_name = self.setting_page.add_group_links().add()
        name = self.group_page.open().is_group_added(group_name)
        self.assertIsNotNone(name)
        self.assertEqual(name, group_name)


class TestsForbiddenComments(unittest.TestCase):
    LOGIN_1 = os.environ['LOGIN_1']
    PASSWORD_1 = os.environ['PASSWORD_1']
    LOGIN_2 = os.environ['LOGIN_2']
    PASSWORD_2 = os.environ['PASSWORD_2']

    def setUp(self):
        self.driver_1 = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver_1.implicitly_wait(10)

        self.driver_2 = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver_2.implicitly_wait(10)
        auth_page = AuthPage(self.driver_1)
        auth_page.open()

        profile_page = auth_page.sign_in(self.LOGIN_1, self.PASSWORD_1)

        desc = {
            'description': 'group about shit',
            'title': 'pulp fiction',
            'subcategory': GroupSubcategory.CINEMA_TV,
            'age_restriction': AgeRestriction.NO_RESTRICTION
        }

        group_page = profile_page.to_groups_page().create_public_page(desc)
        group_page.open()

        auth_page_user2 = AuthPage(self.driver_2)
        auth_page_user2.open()

        profile_user_2 = auth_page_user2.sign_in(self.LOGIN_2, self.PASSWORD_2)
        group_page_user2 = GroupPage(self.driver_2, path=group_page.path).open()

        setting_page = group_page.to_settings_page()

        self.group_page = group_page
        self.group_page_user_2 = group_page_user2
        self.setting_page = setting_page
        self.profile_user_2 = profile_user_2

    def tearDown(self):
        self.group_page.delete_group()
        self.driver_1.quit()
        self.driver_2.quit()

    def test_forbidden_comments_nobody(self):
        self.setting_page.open().to_management_page().forbid_leave_comments(WhoCanLeaveComments.NOBODY)
        self.group_page.open().create_post('Pica-boo')
        self.assertTrue(self.group_page.comment_popup().is_disabled_leave_comment_at_all())

    def test_forbidden_comments_members(self):
        self.setting_page.open().to_management_page().forbid_leave_comments(WhoCanLeaveComments.MEMBERS)
        self.group_page.open().create_post("OK")
        self.assertTrue(self.group_page_user_2.open().comment_popup().is_disabled_leave_comments_not_members())

    def test_forbidden_comments_everybody(self):
        self.setting_page.open().to_management_page().forbid_leave_comments(WhoCanLeaveComments.EVERYBODY)
        self.group_page.open().create_post("BURDA")
        self.assertFalse(self.group_page_user_2.open().comment_popup().is_disabled_leave_comment_at_all())


class TestsHideSections(unittest.TestCase):
    LOGIN_1 = os.environ['LOGIN_1']
    PASSWORD_1 = os.environ['PASSWORD_1']

    def setUp(self):
        self.driver_1 = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver_1.implicitly_wait(10)

        auth_page = AuthPage(self.driver_1)
        auth_page.open()

        profile_page = auth_page.sign_in(self.LOGIN_1, self.PASSWORD_1)

        desc = {
            'description': 'group about shit',
            'title': 'pulp fiction',
            'subcategory': GroupSubcategory.CINEMA_TV,
            'age_restriction': AgeRestriction.NO_RESTRICTION
        }

        group_page = profile_page.to_groups_page().create_public_page(desc)

        setting_page = group_page.to_settings_page()

        setting_page.open()

        self.group_page = group_page
        self.setting_page = setting_page

    def tearDown(self):
        self.group_page.delete_group()
        self.driver_1.quit()

    def test_hide_section_photo(self):
        self.setting_page.open().to_management_page().hide_photo_section()
        self.assertFalse(self.group_page.open().check_presence_section("Фото "))

    def test_hide_section_video(self):
        self.setting_page.open().to_management_page().hide_video_section()
        self.assertFalse(self.group_page.open().check_presence_section("Видео "))

    def test_hide_section_goods(self):
        self.setting_page.open().to_management_page().show_goods_section()
        self.assertTrue(self.group_page.open().check_presence_section("Товары "))


class TestsChangeType(unittest.TestCase):
    LOGIN_1 = os.environ['LOGIN_1']
    PASSWORD_1 = os.environ['PASSWORD_1']

    def setUp(self):
        self.driver_1 = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver_1.implicitly_wait(10)

        auth_page = AuthPage(self.driver_1)
        auth_page.open()

        profile_page = auth_page.sign_in(self.LOGIN_1, self.PASSWORD_1)

        desc = {
            'description': 'group about shit',
            'title': 'pulp fiction',
            'subcategory': GroupSubcategory.CINEMA_TV,
            'age_restriction': AgeRestriction.NO_RESTRICTION
        }

        group_page = profile_page.to_groups_page().create_public_page(desc)
        profile_page.open()

        setting_page = group_page.open().to_settings_page()

        self.group_page = group_page
        self.setting_page = setting_page

    def tearDown(self):
        self.group_page.delete_group()
        self.driver_1.quit()

    def test_change_type(self):
        general_page = self.setting_page.to_general_page()
        general_page.change_type()
        general_page.change_category_of_group()
        form = general_page.form
        type = form.type
        category = form.category
        self.group_page.open()
        self.assertEqual("{}, {}".format(type, category), self.group_page.get_category())

    def test_change_groups_category(self):
        general_page = self.setting_page.to_general_page()
        general_page.change_category_of_group(GeneralForm.Category.STAR, GeneralForm.Subcategory.HUMORIST)
        form = general_page.form
        type = form.type
        category = form.category
        self.group_page.open()
        self.assertRegex(self.group_page.get_category(), "^{},.*{}".format(type, category))


class TestsAddStuff(unittest.TestCase):
    LOGIN_1 = os.environ['LOGIN_1']
    PASSWORD_1 = os.environ['PASSWORD_1']
    LOGIN_2 = os.environ['LOGIN_2']
    PASSWORD_2 = os.environ['PASSWORD_2']

    def setUp(self):
        self.driver_1 = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver_1.implicitly_wait(10)

        self.driver_2 = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver_2.implicitly_wait(10)
        auth_page = AuthPage(self.driver_1)
        auth_page.open()

        profile_page = auth_page.sign_in(self.LOGIN_1, self.PASSWORD_1)

        desc = {
            'description': 'group about shit',
            'title': 'pulp fiction',
            'subcategory': GroupSubcategory.CINEMA_TV,
            'age_restriction': AgeRestriction.NO_RESTRICTION
        }

        group_page = profile_page.to_groups_page().create_public_page(desc)
        profile_page.open()

        auth_page_user2 = AuthPage(self.driver_2)
        auth_page_user2.open()

        profile_user_2 = auth_page_user2.sign_in(self.LOGIN_2, self.PASSWORD_2)
        group_page_user2 = GroupPage(self.driver_2, path=group_page.path).open()
        group_page_user2.join()

        setting_page = group_page.open().to_settings_page()

        self.group_page = group_page
        self.group_page_user_2 = group_page_user2
        self.setting_page = setting_page
        self.profile_user_2 = profile_user_2

    def tearDown(self):
        self.group_page.delete_group()
        self.driver_1.quit()
        self.driver_2.quit()

    def test_add_moderator(self):
        admin_page = self.setting_page.to_admin_page()
        admin_page.add_moderator(self.profile_user_2.name, RoleRadioButtons.MODERATOR)
        admin_page.to_administration_list()
        self.assertTrue(admin_page.is_moder_added(self.profile_user_2.name, Role.MODERATOR))

    def test_add_super_moderator(self):
        admin_page = self.setting_page.to_admin_page()
        admin_page.add_moderator(self.profile_user_2.name, Role.SUPERMODERATOR)
        admin_page.to_administration_list()
        self.assertTrue(admin_page.is_moder_added(self.profile_user_2.name, Role.SUPERMODERATOR))

    def test_add_editor(self):
        admin_page = self.setting_page.to_admin_page()
        admin_page.add_moderator(self.profile_user_2.name, RoleRadioButtons.EDITOR)
        admin_page.to_administration_list()
        self.assertTrue(admin_page.is_moder_added(self.profile_user_2.name, Role.EDITOR))

    def test_add_analyst(self):
        admin_page = self.setting_page.to_admin_page()
        admin_page.add_moderator(self.profile_user_2.name, RoleRadioButtons.ANALYST)
        admin_page.to_administration_list()
        self.assertTrue(admin_page.is_moder_added(self.profile_user_2.name, Role.ANALYST))


class TestsHideObsceneLanguage(unittest.TestCase):
    LOGIN_1 = os.environ['LOGIN_1']
    PASSWORD_1 = os.environ['PASSWORD_1']
    LOGIN_2 = os.environ['LOGIN_2']
    PASSWORD_2 = os.environ['PASSWORD_2']

    def setUp(self):
        self.driver_1 = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver_1.implicitly_wait(10)

        self.driver_2 = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver_2.implicitly_wait(10)
        auth_page = AuthPage(self.driver_1)
        auth_page.open()

        profile_page = auth_page.sign_in(self.LOGIN_1, self.PASSWORD_1)

        desc = {
            'description': 'group about shit',
            'title': 'pulp fiction',
            'subcategory': GroupSubcategory.CINEMA_TV,
            'age_restriction': AgeRestriction.NO_RESTRICTION
        }

        group_page = profile_page.to_groups_page().create_public_page(desc)
        profile_page.open()
        group_page.open()

        auth_page_user2 = AuthPage(self.driver_2)
        auth_page_user2.open()

        profile_user_2 = auth_page_user2.sign_in(self.LOGIN_2, self.PASSWORD_2)
        group_page_user2 = GroupPage(self.driver_2, path=group_page.path).open()
        group_page_user2.join()

        setting_page = group_page.to_settings_page()

        self.group_page = group_page
        self.group_page_user_2 = group_page_user2
        self.setting_page = setting_page
        self.profile_user_2 = profile_user_2

    def tearDown(self):
        self.group_page.delete_group()
        self.driver_1.quit()
        self.driver_2.quit()

    def test_hide_obscene_language_english_simple(self):
        self.setting_page.open().to_management_page().hide_obscene_language()
        self.group_page.open().create_post('Make America Great Again')
        self.group_page.create_comment("FUCK")
        group_page_user2 = GroupPage(self.driver_2, path=self.group_page.path).open()
        self.assertRegex(group_page_user2.get_comment_message(), "^[*\ ]*$")

    def test_hide_obscene_language_russian_simple(self):
        self.setting_page.open().to_management_page().hide_obscene_language()
        self.group_page.open().create_post('Make Russia Great Again')
        self.group_page.create_comment("Блять")
        group_page_user2 = GroupPage(self.driver_2, path=self.group_page.path).open()
        self.assertRegex(group_page_user2.get_comment_message(), "^[*\ ]*$")

    def test_hide_obscene_language_english_many(self):
        self.setting_page.open().to_management_page().hide_obscene_language()
        self.group_page.open().create_post('Make America Great Again')
        self.group_page.create_comment("FUCK FUCK")
        group_page_user2 = GroupPage(self.driver_2, path=self.group_page.path).open()
        self.assertRegex(group_page_user2.get_comment_message(), "^[*\ ]*$")

    def test_hide_obscene_language_russian_many(self):
        self.setting_page.open().to_management_page().hide_obscene_language()
        self.group_page.open().create_post('Make Russia Great Again')
        self.group_page.create_comment("ебаный хуй")
        group_page_user2 = GroupPage(self.driver_2, path=self.group_page.path).open()
        self.assertRegex(group_page_user2.get_comment_message(), "^[*\ ]*$")

    def test_hide_obscene_language_english_context(self):
        self.setting_page.open().to_management_page().hide_obscene_language()
        self.group_page.open().create_post('Make America Great Again')
        self.group_page.create_comment("FUCK YOU")
        group_page_user2 = GroupPage(self.driver_2, path=self.group_page.path).open()
        self.assertRegex(group_page_user2.get_comment_message(), "^[*\ ]*YOU$")

    def test_hide_obscene_language_russian_context(self):
        self.setting_page.open().to_management_page().hide_obscene_language()
        self.group_page.open().create_post('Make Russia Great Again')
        self.group_page.create_comment("ТЕБЕ ПИЗДЕЦ")
        group_page_user2 = GroupPage(self.driver_2, path=self.group_page.path).open()
        self.assertRegex(group_page_user2.get_comment_message(), "^ТЕБЕ[*\ ]*$")
