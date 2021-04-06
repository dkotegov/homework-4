import random
import string
import urllib.parse

from cases.base_case import BaseTest
from pages.meetings_page import MeetingsPage
from pages.people_page import PeoplePage
from steps.profile_steps import ProfileSteps
from utils.for_examples import for_examples


class ProfileTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.auth()
        self.profile_page = ProfileSteps(self.driver)
        self.profile_page.open_page()

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
