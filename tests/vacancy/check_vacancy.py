import unittest

from pages.create_vacancy_page import CreateVacancyPage
from pages.profile_page import ProfilePage
from pages.vacancies_page import VacanciesPage
from scenario.auth import auth_as_employer_has_comp
from scenario.default_setup import default_setup
from scenario.vacancy import VacancyScenario


class Vacancy(unittest.TestCase):
    def setUp(self) -> None:
        default_setup(self)
        auth_as_employer_has_comp(self)
        self.profile_page = ProfilePage(self.driver)
        self.vac_page = CreateVacancyPage(self.driver)
        self.vac_list = VacanciesPage(self.driver)
        self.vac_form = self.vac_page.form
        self.vac_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_create_empty_vacancy(self):
        self.vac_form.submit()
        self.assertTrue(self.vac_form.is_title_error)
        self.assertTrue(self.vac_form.is_description_error)
        self.assertTrue(self.vac_form.is_skills_error)
        self.assertTrue(self.vac_form.is_requirements_error)
        self.assertTrue(self.vac_form.is_phone_error)
        self.assertTrue(self.vac_form.is_place_error)

    def test_create_vacancy_with_russian_letters_in_salary(self):
        self.vac_form.set_salary_min('a')
        self.vac_form.set_salary_max('b')
        self.vac_form.submit()
        self.assertTrue(self.vac_form.is_salary_error('Некорректное число и Некорректное число'))

    def test_create_vacancy_with_negative_salary(self):
        self.vac_form.set_salary_min('-1')
        self.vac_form.set_salary_max('-2')
        self.vac_form.submit()
        self.assertTrue(self.vac_form.is_salary_error('Поле не может принимать отрицательное значение. ' +
                                                                 'и Поле не может принимать отрицательное значение.'))

    def test_create_vacancy_with_invalid_chars_in_salary(self):
        self.vac_form.set_salary_min('!"№;%:?*()&^@\'\"`№$-+=~#')
        self.vac_form.submit()
        self.assertTrue(self.vac_form.is_salary_error('Некорректное число'))

    def test_create_vacancy_with_min_greater_max_in_salary(self):
        self.vac_form.set_salary_min('2')
        self.vac_form.set_salary_max('1')
        self.vac_form.submit()
        self.assertTrue(self.vac_form.is_salary_error('Минимальная зарплата не может быть' +
                                                                 ' больше максимальной'))

    def test_create_vacancy_with_min_equal_max_in_salary(self):
        self.vac_form.set_salary_min('1')
        self.vac_form.set_salary_max('1')
        self.vac_form.submit()
        self.assertTrue(self.vac_form.is_salary_error(''))

    def test_create_vacancy_with_zero_in_salary(self):
        self.vac_form.set_salary_min('0')
        self.vac_form.set_salary_max('0')
        self.vac_form.submit()
        self.assertTrue(self.vac_form.is_salary_error(''))

    def test_create_vacancy_without_contacts(self):
        vacancy = VacancyScenario(form=self.vac_form)
        vacancy.fill_vacancy()
        self.vac_form.set_email('')
        self.vac_form.submit()
        self.assertTrue(self.vac_form.is_email_error)

    def test_delete_vacancy_success(self):
        vacancy = VacancyScenario(test=self)
        vacancy.create_vacancy()
        existed_title = self.vac_form.get_title
        vacancy.delete_vacancy()
        self.profile_page.open()
        self.profile_page.profile_form.click_to_my_cards()
        self.assertFalse(self.vac_form.check_vacancy_exist(existed_title))

    def test_create_vacancy_success(self):
        vacancy = VacancyScenario(test=self)
        vacancy.create_vacancy()
        existed_title = self.vac_form.get_title
        vacancy.delete_vacancy()
        self.assertTrue(vacancy.vacancy_uniq_title, existed_title)

    def test_create_vacancy_with_unlimited_salary(self):
        nmb = str(2 << 64)
        vacancy = VacancyScenario(form=self.vac_form)
        vacancy.fill_vacancy()
        self.vac_form.set_salary_min(nmb)
        self.vac_form.set_salary_max(nmb)
        self.vac_form.submit()
        self.assertTrue(self.vac_form.is_server_error('Обязательные поля не заполнены.'))

    def test_update_vacancy_success(self):
        vacancy = VacancyScenario(test=self, form=self.vac_form)
        vacancy.create_vacancy()
        vacancy.open_update_page()
        self.vac_form.set_salary_min('1')
        self.vac_form.set_salary_max('10')
        self.vac_form.submit()
        vacancy.delete_vacancy()

    def test_view_vacancy_in_list(self):
        vacancy = VacancyScenario(test=self)
        vacancy.create_vacancy()
        existed_title = self.vac_form.get_title
        uri_to_delete = vacancy.get_vacancy_uri
        self.vac_list.open()
        vacancy_titles = self.vac_form.get_vacancies_in_list_titles()
        vacancy.delete_vacancy(uri_to_delete)
        self.assertTrue(existed_title in vacancy_titles)

    def test_redirect_vacancy_from_list(self):
        vacancy = VacancyScenario(test=self)
        vacancy.create_vacancy()
        existed_title_on_create = self.vac_form.get_title
        uri_to_delete = vacancy.get_vacancy_uri
        self.vac_list.open()
        self.vac_form.open_by_title(existed_title_on_create)
        title_clicked = self.vac_form.get_title
        vacancy.delete_vacancy(uri_to_delete)
        self.assertTrue(title_clicked == existed_title_on_create)
