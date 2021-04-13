import unittest


from tests.default_setup import default_setup
from scenario.auth import setup_auth
from scenario.create_resume import create_resume
from pages.create_resume_page import CreateResumePage
from pages.resume_page import ResumePage
from scenario.auth import setup_auth
from scenario.delete_resume import delete_resume
from scenario.create_resume import create_resume, create_resume_without_submit


class CreateResumeWrong(unittest.TestCase):
    data = {
        'title': 'My Title',
        'description': 'My cool resume',
        'place': 'I very good',
        'skills': 'My great skills',
    }

    def setUp(self) -> None:
        default_setup(self)
        setup_auth(self)

        self.create_resume_page = CreateResumePage(self.driver)
        self.create_resume_form = self.create_resume_page.create_form

        self.resume_page = ResumePage(self.driver)
        self.resume = self.resume_page.form

        self.create_resume_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_create_empty_resume(self):
        self.create_resume_form.submit_resume()
        self.assertTrue(self.create_resume_form.is_title_error())
        self.assertTrue(self.create_resume_form.is_description_error())
        self.assertTrue(self.create_resume_form.is_place_error())
        self.assertTrue(self.create_resume_form.is_skills_error())

    def test_enter_salary_in_letters(self):
        self.create_resume_form.set_salary_min("letters")
        self.create_resume_form.submit_resume()
        self.assertTrue(self.create_resume_form.is_salary_error('Некорректное число'))

    def test_enter_negative_salary(self):
        self.create_resume_form.set_salary_min(-123)
        self.create_resume_form.submit_resume()
        self.assertTrue(self.create_resume_form.is_salary_error('Поле не может принимать отрицательное значение.'))

    def test_enter_salary_in_symbol(self):
        self.create_resume_form.set_salary_min('(!"№;%:?*()')
        self.create_resume_form.submit_resume()
        self.assertTrue(self.create_resume_form.is_salary_error('Некорректное число'))

    def test_enter_salary_min_greater_max(self):
        self.create_resume_form.set_salary_min(12)
        self.create_resume_form.set_salary_max(3)
        self.create_resume_form.submit_resume()
        self.assertTrue(
            self.create_resume_form.is_salary_error('Минимальная зарплата не может быть больше максимальной'))

    def test_enter_salary_is_zero(self):
        create_resume_without_submit(self.create_resume_form, self.data)
        self.create_resume_form.set_salary_min(0)
        self.create_resume_form.set_salary_max(1)
        self.create_resume_form.submit_resume()

        self.assertTrue(self.create_resume_form.is_salary_error('Поле не может принимать отрицательное значение.'))

    def test_create_resume_with_empty_contect_data(self):
        create_resume_without_submit(self.create_resume_form, self.data)
        self.create_resume_form.clear_contact_data()
        self.create_resume_form.submit_resume()
        self.assertTrue(self.create_resume_form.is_surname_error())
        self.assertTrue(self.create_resume_form.is_name_error())
        self.assertTrue(self.create_resume_form.is_email_error())

    def test_enter_very_big_salary(self):
        # Ошибка при вводе зарплаты >999999999
        create_resume_without_submit(self.create_resume_form, self.data)
        self.create_resume_form.set_salary_min(1)
        self.create_resume_form.set_salary_max(9999999999999)
        self.create_resume_form.submit_resume()
        self.assertTrue(self.create_resume_form.is_common_error())

    def test_load_image_error(self):
        create_resume_without_submit(self.create_resume_form, self.data)
        self.create_resume_form.load_image()
        self.create_resume_form.submit_resume()
        self.assertTrue(self.create_resume_form.is_common_error(
            'Превышен максимальный размер изображения. Максимальный размер: 2 mB.'))


class CreateResume(unittest.TestCase):
    data = {
        'title': 'My Title',
        'description': 'My cool resume',
        'place': 'I very good',
        'skills': 'My great skills',
    }

    def setUp(self) -> None:
        default_setup(self)
        setup_auth(self)

        self.create_resume_page = CreateResumePage(self.driver)
        self.create_resume_form = self.create_resume_page.create_form

        self.resume_page = ResumePage(self.driver)
        self.resume = self.resume_page.form

        self.create_resume_page.open()

    def tearDown(self):
        delete_resume(self)
        self.driver.quit()

    def test_create_resume(self):
        create_resume(self)

        place = self.resume.get_place()
        description = self.resume.get_description()
        skills = self.resume.get_skills()

        self.assertEqual(self.data['place'], place)
        self.assertEqual(self.data['description'], description)
        self.assertEqual(self.data['skills'], skills)

    def test_enter_equal_salary(self):
        create_resume_without_submit(self.create_resume_form, self.data)
        salary = 5
        self.create_resume_form.set_salary_min(salary)
        self.create_resume_form.set_salary_max(salary)
        self.create_resume_form.submit_resume()
        self.resume.wait_for_resume_page()

        page_salary = self.resume.get_salary()
        self.assertEqual(salary, int(page_salary[0]))
        self.assertEqual(salary, int(page_salary[1]))

