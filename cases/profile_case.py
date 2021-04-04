import random
import string

from cases.base_case import BaseTest
from steps.profile_steps import ProfileSteps


class ProfileTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.auth()
        self.profile_page = ProfileSteps(self.driver)
        self.profile_page.open_page()

    def test_skills_edit(self):
        skills_text = ''.join(random.choice(string.ascii_letters) for i in range(32))
        self.profile_page.edit_skills(skills_text)
        actual = self.profile_page.get_skills()
        self.assertEqual(skills_text, actual, f'Skills value {actual} doesn\'t match {skills_text}')
