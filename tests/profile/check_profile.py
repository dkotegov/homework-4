import unittest

from selenium.webdriver import Remote

from pages.profile_page import ProfilePage
from scenario.default_setup import default_setup
from scenario.auth import setup_auth
from pages.resume_page import ResumePage
from scenario.auth import auth_as_employer_no_comp, auth_as_applicant, auth_as_employer_has_comp


class CheckProfile(unittest.TestCase):

    driver: Remote

    def setUp(self) -> None:
        default_setup(self)

        self.profile_page = ProfilePage(self.driver)
        self.resume_page = ResumePage(self.driver)


    def tearDown(self):
        self.driver.quit()

    def test_link_to_my_resume(self):
        auth_as_applicant(self)
        self.profile_page.open()
        self.assertTrue(self.profile_page.click_link_to_my_cards())

    def test_link_to_my_responses(self):
        auth_as_applicant(self)
        self.profile_page.open()
        self.assertTrue(self.profile_page.click_link_to_myResponses())

    def test_link_to_my_fav_as_empl(self):
        auth_as_employer_has_comp(self)
        self.profile_page.open()
        self.assertTrue(self.profile_page.click_to_link_myFavorite())

    def test_open_vac(self):
        auth_as_employer_has_comp(self)
        self.profile_page.open()
        self.assertTrue(self.profile_page.click_link_to_my_cards())
        self.profile_page.view_card()
        # TODO проверить открытие вакансии

    def test_edit_vac(self):
        auth_as_employer_has_comp(self)
        self.profile_page.open()
        self.assertTrue(self.profile_page.click_link_to_my_cards())
        self.profile_page.edit_card()
        # TODO проверить открытие вакансии на редактирование


    def test_check_open_vacancy_response(self):
        auth_as_applicant(self)
        self.profile_page.open()
        self.assertTrue(self.profile_page.click_link_to_myResponses())
        self.profile_page.open_vacancy_responses()

    def test_check_open_company_response(self):
        auth_as_applicant(self)
        self.profile_page.open()
        self.assertTrue(self.profile_page.click_link_to_myResponses())
        self.profile_page.open_company_responses()

    def test_upload_big_avatar(self):
        auth_as_applicant(self)
        self.profile_page.open()
        self.profile_page.upload_avatar("/test_data/big_img.jpg")
        self.assertTrue(self.profile_page.check_error('Размеры изображения превышают допутимую высоту 2500px и ширину 2500px.'))

    def test_upload_avatar(self):
        auth_as_applicant(self)
        self.profile_page.open()
        self.profile_page.upload_avatar("/test_data/robot.png")
        self.assertFalse(self.profile_page.check_error('Размеры изображения превышают допутимую высоту 2500px и ширину 2500px.'))


    def test_check_open_resume_response(self):
        auth_as_applicant(self)
        self.profile_page.open()
        self.assertTrue(self.profile_page.click_link_to_myResponses())
        self.profile_page.open_resume_responses()
        self.assertTrue(self.resume_page.is_open())



    def test_edit_name(self):
        check_value = 'margotmargot'
        auth_as_applicant(self)
        self.profile_page.open()
        self.profile_page.edit(check_value, 1)
        self.driver.refresh()
        self.assertTrue(self.profile_page.get_text(check_value, 0))
        self.profile_page.edit('margot', 1)


    def test_edit_surname(self):
        check_value = 'margotmargot'
        auth_as_employer_no_comp(self)
        self.profile_page.open()
        self.profile_page.edit(check_value, 2)
        self.driver.refresh()
        self.assertTrue(self.profile_page.get_text(check_value, 1))
        self.profile_page.edit('testEmployer', 2)


    def test_edit_email(self):
        check_value = 'margotmargot@mail.ru'
        auth_as_employer_has_comp(self)
        self.profile_page.open()
        self.profile_page.edit(check_value, 3)
        self.driver.refresh()
        self.assertTrue(self.profile_page.get_text(check_value, 2))
        self.profile_page.edit('employer@employer.ru', 3)

    def test_edit_phone(self):
        check_value = '12345678910'
        auth_as_applicant(self)
        self.profile_page.open()
        self.profile_page.edit(check_value, 4)
        self.driver.refresh()
        self.assertTrue(self.profile_page.get_text(check_value, 3))

    def test_incorrect_name(self):
        check_data = auth_as_applicant(self)
        self.profile_page.open()
        self.profile_page.edit('margot1', 1)
        self.assertTrue(self.profile_page.check_error('Неправильные значения полей: имя должно содержать только буквы'))
        self.driver.refresh()
        self.assertTrue(self.profile_page.get_text(check_data['NAME'], 0))

    def test_incorrect_surname(self):
        check_data = auth_as_applicant(self)
        self.profile_page.open()
        self.profile_page.edit('margot1', 2)
        self.assertTrue(self.profile_page.check_error('Неправильные значения полей: фамилия должна содержать только буквы'))
        self.driver.refresh()
        self.assertTrue(self.profile_page.get_text(check_data['SURNAME'], 1))

    def test_incorrect_email(self):
        check_data = auth_as_applicant(self)
        self.profile_page.open()
        self.profile_page.edit('margot1', 3)
        self.assertTrue(
            self.profile_page.check_span_error('Email должен содержать "@" и латинские буквы, цифры, символы.'))
        self.driver.refresh()
        self.assertTrue(self.profile_page.get_text(check_data['EMAIL'], 2))

    def test_incorrect_phone(self):
        check_data = auth_as_applicant(self)
        self.profile_page.open()
        self.profile_page.edit('margot1', 4)
        self.assertTrue(
            self.profile_page.check_span_error('Неверный номер телефона.'))
        self.driver.refresh()
        self.assertTrue(self.profile_page.get_text(check_data['PHONE'], 3))
