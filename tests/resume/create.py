import unittest

from default_setup import default_setup
from scenario.auth import setup_auth
from scenario.create_resume import create_resume

from pages.resume_page import ResumePage


class CreateResume(unittest.TestCase):
    data = {
        'title': 'My Title',
        'description': 'My cool resume',
        'place': 'I very good',
        'skills': 'My great skills',
    }

    def setUp(self) -> None:
        default_setup(self)
        setup_auth(self)

    def test_create_resume(self):
        create_resume(self)

        resume_page = ResumePage(self.driver)
        resume_form = resume_page.form

        place = resume_form.get_place()
        description = resume_form.get_description()
        skills = resume_form.get_skills()

        self.assertEqual(self.data['place'], place)
        self.assertEqual(self.data['description'], description)
        self.assertEqual(self.data['skills'], skills)

    def tearDown(self):
        self.driver.quit()
