import unittest

from pages.resumes_page import ResumesPage
from pages.resume_page import ResumePage
from scenario.auth import setup_auth
from scenario.create_resume import create_resume, create_resume_without_submit
from scenario.default_setup import default_setup


class ListResume(unittest.TestCase):
    data = {
        'title': 'My Title',
        'description': 'My cool resume',
        'place': 'I very good',
        'skills': 'My great skills',
    }

    def setUp(self) -> None:
        default_setup(self)
        setup_auth(self)
        create_resume(self, self.data)

        self.resume_page = ResumePage(self.driver)
        self.resume = self.resume_page.form

        self.resume_list = ResumesPage(self.driver)
        self.resume_list_form = self.resume_list.list

        self.resume_list.open()

    def tearDown(self):
        self.driver.quit()

    def test_created_resume_in_list(self):
        title = self.resume_list_form.get_first_resume_title()
        description = self.resume_list_form.get_first_resume_description()
        self.assertEqual(title, self.data['title'])
        self.assertEqual(description, self.data['description'])

    def test_resume_click(self):
        self.resume_list_form.go_first_resume_page()
        self.assertTrue(self.resume_page.is_open())

        resume_data = self.resume_page.get_resume_data()
        self.assertDictEqual(resume_data, {
            'description': self.data['description'],
            'place': self.data['place'],
            'skills': self.data['skills'],
        })
