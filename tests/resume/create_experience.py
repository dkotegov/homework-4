import unittest

from pages.create_resume_page import CreateResumePage
from pages.resume_page import ResumePage
from tests.default_setup import default_setup
from scenario.auth import setup_auth
from scenario.create_resume import create_resume_without_submit


class CreateExperience(unittest.TestCase):
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

    def setUp(self) -> None:
        default_setup(self)
        setup_auth(self)

        self.create_resume_page = CreateResumePage(self.driver)
        self.create_resume_form = self.create_resume_page.create_form
        self.create_experience_form = self.create_resume_page.create_experience_form

        self.resume_page = ResumePage(self.driver)
        self.resume = self.resume_page.form

        self.create_resume_page.open()
        create_resume_without_submit(self.create_resume_form, self.data)
        self.create_resume_form.open_popup_add_experience()

    # def test_create_empty_experience(self):
    #     self.create_experience_form.submit_exp()
    #     self.assertTrue(self.create_experience_form.is_date_error('Укажите дату'))
    #     self.assertTrue(self.create_experience_form.is_position_error())
    #     self.assertTrue(self.create_experience_form.is_name_job_error())

    # def test_enter_date_start_greater_end(self):
    #     self.create_experience_form.set_position(self.data['position'])
    #     self.create_experience_form.set_name_job(self.data['name job'])
    #     self.create_experience_form.set_date_start('01.01.2010')
    #     self.create_experience_form.set_date_end('01.01.2000')
    #     self.create_experience_form.submit_exp()
    #     self.assertTrue(self.create_experience_form.is_date_error('Некорректная дата.'))

    # def test_close_popup(self):
    #     self.create_experience_form.close_popup()
    #     self.assertFalse(self.create_experience_form.form_is_open())

    def test_create_experience(self):
        self.create_experience_form.set_position(self.data['position'])
        self.create_experience_form.set_name_job(self.data['name_job'])
        self.create_experience_form.set_date_start(self.data['start_date'])
        self.create_experience_form.set_date_end(self.data['end_date'])
        self.create_experience_form.submit_exp()

        page_date = self.create_resume_form.get_job_date()
        for i in range(len(page_date)):
            page_date[i] = page_date[i].replace('\n', '')
            parsed = page_date[i].split('-')
            # parsed[2] = parsed[2].split("\n")[0]
            page_date[i] = f'{parsed[1]}.{parsed[2]}.{parsed[0]}'
        self.assertEqual(page_date[0], self.data['start_date'])
        self.assertEqual(page_date[1], self.data['end_date'])
        self.assertEqual(self.create_resume_form.get_job_name(), self.data['name_job'])
        self.assertEqual(self.create_resume_form.get_job_position(), self.data['position'])



    def tearDown(self):
        self.driver.quit()


