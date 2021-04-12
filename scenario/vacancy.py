import uuid

from pages.create_vacancy_page import CreateVacancyPage


def create_vacancy(test, data=None) -> None:
    if data is None:
        data = {
            'title': 'TEST-vacancy-№' + str(uuid.uuid4()),
            'description': 'Some descriptions',
            'skills': 'Some skills',
            'requirements': 'Some requirements',
            'responsibilities': 'Some responsibilities',
            'phone': '88888888888',
            'address': 'some address'
        }
    create_vacancy_page = CreateVacancyPage(test.driver)
    create_vacancy_page.open()

    create_vacancy_form = create_vacancy_without_submit(create_vacancy_page.form, data)
    create_vacancy_form.submit()
    create_vacancy_form.wait_for_vacancy_page()


def create_vacancy_without_submit(create_vacancy_form, data):
    create_vacancy_form.set_title(data['title'])
    create_vacancy_form.set_description(data['description'])
    create_vacancy_form.set_skills(data['skills'])
    create_vacancy_form.set_requirements(data['requirements'])
    create_vacancy_form.set_responsibilities(data['responsibilities'])
    create_vacancy_form.set_phone(data['phone'])
    create_vacancy_form.set_address(data['address'])
    return create_vacancy_form
