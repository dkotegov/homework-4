import unittest

from pages.create_resume_page import CreateResumePage
from pages.resume_page import ResumePage
from pages.edit_resume import EditResumePage
from pages.profile_page import ProfilePage
from scenario.auth import setup_auth
from scenario.delete_resume import delete_resume
from scenario.create_resume import create_resume_without_submit, create_resume_with_experience
from scenario.create_experience import create_experience
from scenario.default_setup import default_setup


class EditResume(unittest.TestCase):
    data = {
        'title': 'My Title',
        'description': 'My cool resume',
        'place': 'I very good',
        'skills': 'My great skills',

        'position': 'Developer',
        'name_job': 'Mail.ru Group',
        'start_date': '01.02.2010',
        'end_date': '01.02.2020',
    }

    other_data = {
        'title': 'other My Title',
        'description': 'other My cool resume',
        'place': 'other I very good',
        'skills': 'other My great skills',
    }

    def setUp(self) -> None:
        default_setup(self)

        self.create_resume_page = CreateResumePage(self.driver)
        self.create_resume_form = self.create_resume_page.create_form

        self.resume_page = ResumePage(self.driver)
        self.resume = self.resume_page.form

        self.edit_resume_page = EditResumePage(self.driver)
        self.edit_resume_form = self.edit_resume_page.edit_form

        self.profile_page = ProfilePage(self.driver)

        setup_auth(self)
        create_resume_with_experience(self, self.data)

        self.profile_page.open()
        self.profile_page.click_my_first_resume_edit()
        self.assertTrue(self.edit_resume_page.is_open())

    def test_save_without_changes(self):
        self.edit_resume_form.submit_resume()
        self.resume.wait_for_resume_page()
        self.assertTrue(self.resume_page.is_open())

        self.assertEqual(self.data['place'], self.resume.get_place())
        self.assertEqual(self.data['description'], self.resume.get_description())
        self.assertEqual(self.data['skills'], self.resume.get_skills())

    def test_save_with_changes(self):
        self.edit_resume_form.clear_inputs()
        create_resume_without_submit(self.edit_resume_form, self.other_data)

        self.edit_resume_form.submit_resume()
        self.resume.wait_for_resume_page()
        self.assertTrue(self.resume_page.is_open())

        self.assertEqual(self.other_data['place'], self.resume.get_place())
        self.assertEqual(self.other_data['description'], self.resume.get_description())
        self.assertEqual(self.other_data['skills'], self.resume.get_skills())

    def test_add_experience(self):
        self.edit_resume_form.open_popup_add_experience()
        create_experience(self, self.data)
        self.edit_resume_form.submit_resume()
        self.edit_resume_form.wait_for_resume_page()
        position = self.resume.get_position()
        name_job = self.resume.get_name_job()
        self.assertEqual(self.data['position'], position[1].text)
        self.assertEqual(self.data['name_job'], name_job[1].text)

    def test_delete_experience(self):
        self.edit_resume_form.delete_experience()
        self.assertFalse(self.edit_resume_form.check_experience_exist())

    def tearDown(self):
        delete_resume(self)
        self.driver.quit()
