import unittest

from pages.profile_page import ProfilePage

from scenario.auth import auth_as_applicant, auth_as_employer_no_comp, auth_as_employer_has_comp

from tests.default_setup import default_setup


class CheckProfile(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)

        self.profile_page = ProfilePage(self.driver)


    def tearDown(self):
        self.driver.quit()

    def test_link_to_my_resume(self):
        auth_as_applicant(self)
        self.assertTrue(self.profile_page.click_link_to_my_cards())

    def test_link_to_my_responses(self):
        auth_as_applicant(self)
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

    def test_check_open_resume_response(self):
        auth_as_applicant(self)
        self.profile_page.open()
        self.assertTrue(self.profile_page.click_link_to_myResponses())
        self.profile_page.open_resume_responses()
    
    def test_upload_avatar(self):
        auth_as_applicant(self)
        self.profile_page.open()
        self.profile_page.upload_avatar("/test_data/robot.png")

    def test_upload_big_avatar(self):
        auth_as_applicant(self)
        self.profile_page.open()
        self.profile_page.upload_avatar("/test_data/big_img.jpg")
        self.assertTrue(self.profile_page.check_error('Размеры изображения превышают допутимую высоту 2500px и ширину 2500px.'))



    def test_edit_name(self):
        auth_as_applicant(self)
        self.profile_page.open()
        self.profile_page.edit('margotmargot', 1)
        self.profile_page.edit('margot', 1)

    def test_edit_surname(self):
        auth_as_employer_no_comp(self)
        self.profile_page.open()
        self.profile_page.edit('margotmargot', 2)
        self.profile_page.edit('testEmployer', 2)

    def test_edit_email(self):
        auth_as_employer_has_comp(self)
        self.profile_page.open()
        self.profile_page.edit('margotmargot@mail.ru', 3)
        self.profile_page.edit('employer@employer.ru', 3)

    def test_edit_phone(self):
        auth_as_applicant(self)
        self.profile_page.open()
        self.profile_page.edit('12345678910', 4)

    def test_incorrect_name(self):
        auth_as_applicant(self)
        self.profile_page.open()
        self.profile_page.edit('margot1', 1)
        self.assertTrue(self.profile_page.check_error('Неправильные значения полей: имя должно содержать только буквы'))

    def test_incorrect_surname(self):
        auth_as_applicant(self)
        self.profile_page.open()
        self.profile_page.edit('margot1', 2)
        self.assertTrue(self.profile_page.check_error('Неправильные значения полей: фамилия должна содержать только буквы'))

    def test_incorrect_email(self):
        auth_as_applicant(self)
        self.profile_page.open()
        self.profile_page.edit('margot1', 3)
        self.assertTrue(
            self.profile_page.check_error('Email должен содержать "@" и латинские буквы, цифры, символы.'))

    def test_incorrect_phone(self):
        auth_as_applicant(self)
        self.profile_page.open()
        self.profile_page.edit('margot1', 4)
        self.assertTrue(
            self.profile_page.check_phone_error('Неверный номер телефона.'))
