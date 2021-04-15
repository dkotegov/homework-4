import os
import random
import string
import urllib.parse

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.color import Color

from cases.base_case import BaseTest
from pages.login_form import LoginForm
from pages.meetings_page import MeetingsPage
from pages.people_page import PeoplePage
from steps.profile_steps import ProfileSteps
from utils.for_examples import for_examples


class ProfileTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.profile_page = ProfileSteps(self.driver)

        auth_token = os.environ.get('AUTH_TOKEN', None)
        if auth_token is not None:
            self.profile_page.open_page()
            self.driver.add_cookie({'name': 'authToken', 'value': auth_token})
            self.profile_page.open_page()
        else:
            self.auth()
            self.profile_page.open_page()
            self.profile_page.open_page('/profile')

    @for_examples(*list(ProfileSteps.Fields))
    def test_skills_editing(self, field):
        new_text = ''.join(random.choice(string.ascii_letters) for i in range(32))
        self.profile_page.edit_field(field, new_text)
        self.profile_page.update_field(field)
        actual = self.profile_page.get_field_value(field)
        self.assertEqual(new_text, actual, f'{field.name} value {actual} doesn\'t match {new_text}')

    @for_examples(*list(ProfileSteps.Fields))
    def test_skills_cancel_editing(self, field):
        old_text = self.profile_page.get_field_value(field)
        self.profile_page.edit_field(field, ''.join(random.choice(string.ascii_letters) for i in range(32)))
        self.profile_page.cancel_editing(field)
        actual = self.profile_page.get_field_value(field)
        self.assertEqual(old_text, actual, f'{field.name} value {actual} doesn\'t match {old_text}')

    def test_meetings_page_redirect(self):
        self.profile_page.open_meetings_page()
        actual_url = self.profile_page.get_page_url()
        expected_url = MeetingsPage.get_default_url()
        self.assertEqual(expected_url, actual_url, f'Meetings page url {actual_url} doesn\'t match {expected_url}')

    def test_people_redirect(self):
        self.profile_page.open_people_page()
        actual_url = self.profile_page.get_page_url()
        expected_url = PeoplePage.get_default_url()
        self.assertEqual(expected_url, actual_url, f'People page url {actual_url} doesn\'t match {expected_url}')

    def test_vk_redirect(self):
        self.profile_page.open_vk_link()
        actual_url = self.profile_page.get_page_url()
        expected_url = 'https://vk.com/mxtest'
        self.assertEqual(expected_url, actual_url, f'Vk url {actual_url} doesn\'t match {expected_url}')

    def test_tg_redirect(self):
        self.profile_page.open_tg_link()
        actual_url = self.profile_page.get_page_url()
        expected_url = 'https://t.me/mxtest'
        self.assertEqual(expected_url, actual_url, f'Telegram url {actual_url} doesn\'t match {expected_url}')

    def test_meeting_redirect(self):
        self.profile_page.open_test_meeting()
        actual_url = self.profile_page.get_page_url()
        expected_url = urllib.parse.urljoin(MeetingsPage.BASE_URL, '/meeting?meetId=29')
        self.assertEqual(expected_url, actual_url, f'Meeting url {actual_url} doesn\'t match {expected_url}')

    def test_subscribe_btn_stranger_visibility(self):
        self.profile_page.open_stranger_profile()
        self.assertTrue(self.profile_page.check_subscribe_btn_visibility())

    def test_subscribe_btn_my_profile_visibility(self):
        self.profile_page.open_page()
        self.assertFalse(self.profile_page.check_subscribe_btn_visibility())

    def test_subscribe_btn_signed_out(self):
        self.profile_page.sign_out()
        self.profile_page.open_stranger_profile()
        self.profile_page.subscribe()
        try:
            LoginForm(self.driver).wait_until_visible()
            self.assertTrue(LoginForm(self.driver).is_visible())
        except TimeoutException:
            self.fail('Auth modal does not show up')

    def test_subscribe_btn_signed_in(self):
        self.profile_page.open_stranger_profile(1)
        self.profile_page.subscribe()
        self.profile_page.handle_sub_confirmation()
        new_text = 'Отменить подписку'
        actual = self.profile_page.get_subscribe_btn_text()
        self.profile_page.unsubscribe()
        self.profile_page.handle_unsub_confirmation()
        self.assertEqual(new_text, actual, f'Subscribe button text {actual} doesn\'t match {new_text}')

    def test_unsubscribe_btn(self):
        self.profile_page.open_stranger_profile(2)
        self.profile_page.unsubscribe()
        self.profile_page.handle_unsub_confirmation()
        new_text = 'Подписаться'
        actual = self.profile_page.get_subscribe_btn_text()
        self.profile_page.subscribe()
        self.profile_page.handle_sub_confirmation()
        self.assertEqual(new_text, actual, f'Subscribe button text {actual} doesn\'t match {new_text}')

    def test_avatar_overlay_visibility(self):
        self.profile_page.hover_on_avatar()
        actual_text = self.profile_page.get_avatar_overlay_text()
        expected_text = 'Выберите файл'
        self.assertEqual(expected_text, actual_text,
                         f'Avatar overlay text {actual_text} doesn\'t match {expected_text}')

    def test_avatar_update(self):
        test_avatar = os.path.join('', os.getcwd(), 'resources/test_image.jpeg')
        self.profile_page.hover_on_avatar()
        self.profile_page.choose_new_avatar(test_avatar)
        actual_text = self.profile_page.get_avatar_button_text()
        expected_text = 'Сохранить'
        self.assertEqual(expected_text, actual_text,
                         f'Avatar button text {actual_text} doesn\'t match {expected_text}')

    def test_tags_selection(self):
        self.profile_page.open_tags_modal()
        bg_color = self.profile_page.select_golang_tag()
        actual = Color.from_string(bg_color).hex
        expected = '#9cbdb6'
        self.assertEqual(expected, actual,
                         f'Selected tag background color {actual} doesn\'t match {expected}')

    def test_tags_addition(self):
        self.profile_page.open_tags_modal()
        self.profile_page.select_cpp_tag()
        self.profile_page.update_tags()
        profile_tags = self.profile_page.get_tags()
        self.profile_page.open_tags_modal()
        self.profile_page.select_cpp_tag()
        self.profile_page.update_tags()
        cpp_tag = "C++"
        self.assertIn(cpp_tag, profile_tags, f'Tag {cpp_tag} is not in profile tags: {profile_tags}')

    def test_tags_modal_closing(self):
        self.profile_page.open_tags_modal()
        self.profile_page.close_tags_modal()
        self.assertFalse(self.profile_page.is_tags_modal_visible())
