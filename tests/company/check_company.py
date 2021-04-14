import unittest

from pages.create_company_page import CreateCompanyPage
from scenario.auth import auth_as_employer_no_comp
from scenario.create_company import create_company_without_submit
from scenario.default_setup import default_setup


class Company(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        auth_as_employer_no_comp(self)

        self.create_company_page = CreateCompanyPage(self.driver)
        self.create_company_form = self.create_company_page.form

        self.create_company_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_create_empty_company(self):
        self.create_company_form.submit()
        self.assertTrue(self.create_company_form.is_title_error())
        self.assertTrue(self.create_company_form.is_description_error)

    def test_create_short_title_company(self):
        self.create_company_form.set_title("<3")
        self.create_company_form.set_description("a")
        self.create_company_form.submit()
        self.assertTrue(self.create_company_form.is_title_error('Неправильные значения полей: ' +
                                                                'название компании должно быть от 4 до 30 символов.'))

    def test_create_with_big_logo_company(self):
        create_company_without_submit(self.create_company_form, None)
        self.create_company_form.load_image()
        self.create_company_form.submit()
        self.assertTrue(self.create_company_form.is_img_size_error)
