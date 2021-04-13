from pages.create_resume_page import CreateResumePage
from scenario.create_experience import create_experience


def create_resume(test, data=None) -> None:
    if data is None:
        data = {
            'title': 'My Title',
            'description': 'My cool resume',
            'place': 'I very good',
            'skills': 'My great skills',
        }
    create_resume_page = CreateResumePage(test.driver)
    create_resume_page.open()

    create_resume_form = create_resume_page.form
    create_resume_form = create_resume_without_submit(create_resume_page.create_form, data)
    create_resume_form.submit_resume()
    create_resume_form.wait_for_resume_page()


def create_resume_without_submit(create_resume_form, data):

    create_resume_form.set_title(data['title'])
    create_resume_form.set_description(data['description'])
    create_resume_form.set_place(data['place'])
    create_resume_form.set_skills(data['skills'])
    create_resume_form.submit()
    return create_resume_form


def create_resume_with_experience(test, data=None):
    if data is None:
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
    create_resume_page = CreateResumePage(test.driver)
    create_resume_page.open()
    create_resume_form = create_resume_without_submit(create_resume_page.create_form, data)
    create_resume_form.open_popup_add_experience()
    create_experience(test, data)
    create_resume_form.submit_resume()
    create_resume_form.wait_for_resume_page()
