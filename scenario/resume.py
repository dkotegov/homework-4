from pages.create_resume_page import CreateResumePage
from pages.edit_resume import EditResumePage
from pages.profile_page import ProfilePage


class ResumeScenario:
    def __init__(self, test, form, experience_form=None):
        self.data = {
            'title': 'My Title',
            'description': 'My cool resume',
            'place': 'I very good',
            'skills': 'My great skills',

            'position': 'Developer',
            'name_job': 'Mail.ru Group',
            'start_date': '01.02.2010',
            'end_date': '01.02.2020',
        }
        self.form = form
        self.experience_form = experience_form
        self.test = test

    def create_resume(self, data=None) -> None:
        if data is None:
            data = self.data
        create_resume_page = CreateResumePage(self.test.driver)
        create_resume_page.open()
        self.form = create_resume_page.create_form

        create_resume_form = self.fill_resume(data)
        create_resume_form.submit_resume()
        create_resume_form.wait_for_resume_page()

    def fill_resume(self, data=None):
        if data is None:
            data = self.data

        self.form.set_title(data['title'])
        self.form.set_description(data['description'])
        self.form.set_place(data['place'])
        self.form.set_skills(data['skills'])
        return self.form

    def create_resume_with_experience(self, data=None):
        if data is None:
            data = self.data
        create_resume_page = CreateResumePage(self.test.driver)
        create_resume_page.open()
        self.form = create_resume_page.create_form

        create_resume_form = self.fill_resume(create_resume_page.create_form, data)
        create_resume_form.open_popup_add_experience()
        self.create_experience(data)
        create_resume_form.submit_resume()
        create_resume_form.wait_for_resume_page()

    def create_experience(self, data=None) -> None:
        if data is None:
            data = {
                'position': 'Developer',
                'name_job': 'Mail.ru Group',
                'start_date': '01.02.2010',
                'end_date': '01.02.2020',
            }
        create_resume_page = CreateResumePage(self.test.driver)
        self.experience_form = create_resume_page.create_experience_form

        self.experience_form.set_position(data['position'])
        self.experience_form.set_name_job(data['name_job'])
        self.experience_form.set_date_start(data['start_date'])
        self.experience_form.set_date_end(data['end_date'])
        self.experience_form.submit_exp()

    def delete_resume(self):
        profile_page = ProfilePage(self.test.driver)
        edit_resume_page = EditResumePage(self.test.driver)
        edit_resume_form = edit_resume_page.edit_form

        profile_page.open()
        profile_page.click_my_first_resume_edit()
        edit_resume_form.delete_resume()
