import uuid

from pages.create_vacancy_page import CreateVacancyPage
from pages.update_vacancy_page import UpdateVacancyPage


class VacancyScenario:

    def __init__(self, test=None, form=None):
        self.vacancy_uniq_title = 'TEST-vacancy-№' + str(uuid.uuid4())
        self.data = {
            'title': self.vacancy_uniq_title,
            'description': 'Some descriptions',
            'skills': 'Some skills',
            'requirements': 'Some requirements',
            'responsibilities': 'Some responsibilities',
            'phone': '88888888888',
            'address': 'some address'
        }
        self.form = form
        self.test = test

    def create_vacancy(self, data=None) -> None:
        if data is None:
            data = self.data
        create_vacancy_page = CreateVacancyPage(self.test.driver)
        self.form = create_vacancy_page.form
        create_vacancy_page.open()

        create_vacancy_form = self.create_vacancy_without_submit(data)
        create_vacancy_form.submit()
        create_vacancy_form.wait_for_vacancy_page()

    def create_vacancy_without_submit(self, data=None):
        if data is None:
            data = self.data
        self.form.set_title(data['title'])
        self.form.set_description(data['description'])
        self.form.set_skills(data['skills'])
        self.form.set_requirements(data['requirements'])
        self.form.set_responsibilities(data['responsibilities'])
        self.form.set_phone(data['phone'])
        self.form.set_address(data['address'])
        return self.form

    def delete_vacancy(self):
        delete_vacancy_page = UpdateVacancyPage(self.test.driver, self.vacancy_uniq_title)
        vac_id = '?' + delete_vacancy_page.get_current_url.split('?')[1].split('&')[0]
        delete_vacancy_page.open(vac_id)
        delete_vacancy_page.form.submit_delete()