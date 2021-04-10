from pages.create_resume_page import CreateResumePage


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
    create_resume_form.set_title(data['title'])
    create_resume_form.set_description(data['description'])
    create_resume_form.set_place(data['place'])
    create_resume_form.set_skills(data['skills'])

    create_resume_form.submit()
    create_resume_form.wait_for_resume_page()
