import random
import string

from cases.base_case import BaseTest
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
