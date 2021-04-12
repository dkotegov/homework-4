from pages.create_resume_page import CreateResumePage


def create_experience(test, data=None) -> None:
    if data is None:
        data = {
            'position': 'Developer',
            'name_job': 'Mail.ru Group',
            'start_date': '01.02.2010',
            'end_date': '01.02.2020',
        }
    create_resume_page = CreateResumePage(test.driver)
    create_experience_form = create_resume_page.create_experience_form

    create_experience_form.set_position(data['position'])
    create_experience_form.set_name_job(data['name_job'])
    create_experience_form.set_date_start(data['start_date'])
    create_experience_form.set_date_end(data['end_date'])
    create_experience_form.submit_exp()