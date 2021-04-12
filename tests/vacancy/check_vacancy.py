import unittest

from pages.create_vacancy_page import CreateVacancyPage
from scenario.auth import auth_as_employer_has_comp
from tests.default_setup import default_setup


# чек-лист: https://docs.google.com/document/d/1FHAfuOnQ-5DvYrhPhN8_B0CIfUrhWuT0EIDKHi73FYo/edit#heading=h.90kw3d5ydl9y

class Vacancy(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        auth_as_employer_has_comp(self)

        self.create_vacancy_page = CreateVacancyPage(self.driver)
        self.create_vacancy_form = self.create_vacancy_page.form

        self.create_vacancy_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_create_empty_vacancy(self):
        self.create_vacancy_form.submit()
        self.assertTrue(self.create_vacancy_form.is_title_error)
        self.assertTrue(self.create_vacancy_form.is_description_error)
        self.assertTrue(self.create_vacancy_form.is_skills_error)
        self.assertTrue(self.create_vacancy_form.is_requirements_error)
        self.assertTrue(self.create_vacancy_form.is_phone_error)
        self.assertTrue(self.create_vacancy_form.is_place_error)

    def test_create_vacancy_with_russian_letters_in_salary(self):
        self.create_vacancy_form.set_salary_min('a')
        self.create_vacancy_form.set_salary_max('b')
        self.create_vacancy_form.submit()
        self.assertTrue(self.create_vacancy_form.is_salary_error('Некорректное число и Некорректное число'))

    def test_create_vacancy_with_negative_salary(self):
        self.create_vacancy_form.set_salary_min('-1')
        self.create_vacancy_form.set_salary_max('-2')
        self.create_vacancy_form.submit()
        self.assertTrue(self.create_vacancy_form.is_salary_error('Поле не может принимать отрицательное значение. ' +
                                                                 'и Поле не может принимать отрицательное значение.'))

    def test_create_vacancy_with_invalid_chars_in_salary(self):
        self.create_vacancy_form.set_salary_min('!"№;%:?*()&^@\'\"`№$-+=~#')
        self.create_vacancy_form.submit()
        self.assertTrue(self.create_vacancy_form.is_salary_error('Некорректное число'))

    def test_create_vacancy_with_min_greater_max_in_salary(self):
        self.create_vacancy_form.set_salary_min('2')
        self.create_vacancy_form.set_salary_max('1')
        self.create_vacancy_form.submit()
        self.assertTrue(self.create_vacancy_form.is_salary_error('Минимальная зарплата не может быть' +
                                                                 ' больше максимальной'))

    def test_create_vacancy_with_min_equal_max_in_salary(self):
        self.create_vacancy_form.set_salary_min('1')
        self.create_vacancy_form.set_salary_max('1')
        self.create_vacancy_form.submit()
        self.assertTrue(self.create_vacancy_form.is_salary_error(''))

    def test_create_vacancy_with_zero_in_salary(self):
        self.create_vacancy_form.set_salary_min('0')
        self.create_vacancy_form.set_salary_max('0')
        self.create_vacancy_form.submit()
        self.assertTrue(self.create_vacancy_form.is_salary_error(''))

    # def test_create_vacancy_with_unlimited_salary(self):
    #     nmb = str(2 << 64)
    #     self.create_vacancy_form.set_salary_min(nmb)
    #     self.create_vacancy_form.set_salary_max(nmb)
    #     self.create_vacancy_form.submit()
    #     self.assertTrue(self.create_vacancy_form.is_salary_error('Некорректное число'))

