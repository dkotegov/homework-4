import unittest

from pages.main_page import MainPage
from pages.resumes_page import ResumesPage
from pages.resume_page import ResumePage
from pages.profile_page import ProfilePage
from scenario.vacancy import VacancyScenario
from scenario.auth import auth_as_employer_has_comp, setup_auth
from tests.default_setup import default_setup
from scenario.registration_employer import RegistrationEmployerScenario


class Favorite(unittest.TestCase):
    data = {
        'title': 'My Title',
        'description': 'My cool resume',
        'place': 'I very good',
        'skills': 'My great skills',
    }

    def setUp(self) -> None:
        default_setup(self)
        scen = RegistrationEmployerScenario(self)
        scen.registration_employer(True)

        self.resume_page = ResumePage(self.driver)
        self.resume = self.resume_page.form

        self.resume_list = ResumesPage(self.driver)
        self.resume_list_form = self.resume_list.list

        self.profile_page = ProfilePage(self.driver)
        self.profile_form = self.profile_page.profile_form

        self.resume_list.open()
        self.resume_list_form.go_first_resume_page()

    def tearDown(self):
        self.profile_page.delete_account()
        self.driver.quit()

    def test_add_to_favorite(self):
        self.assertEqual(self.resume.get_text_favorite_btn(), 'Добавить в избранное')
        self.resume.add_to_favorite()
        self.resume.wait_to_add_favorite()
        self.assertEqual(self.resume.get_text_favorite_btn(), 'Убрать из избранного')
        self.profile_page.open()

    def test_check_added_favorite_in_profile(self):
        self.assertEqual(self.resume.get_text_favorite_btn(), 'Добавить в избранное')
        self.resume.add_to_favorite()
        self.resume.wait_to_add_favorite()
        self.profile_page.open()
        page_data = self.profile_page.get_my_favorite()
        self.assertDictEqual(page_data, {
            'title': self.data['title'],
            'description': self.data['description'],
        })
        self.profile_page.click_my_profile_info()


class Response(unittest.TestCase):
    data = {
        'title': 'My Title',
        'description': 'My cool resume',
        'place': 'I very good',
        'skills': 'My great skills',
    }

    def setUp(self) -> None:
        default_setup(self)
        auth_as_employer_has_comp(self)
        self.vacancy = VacancyScenario(test=self)
        self.vacancy.create_vacancy()
        self.uri_to_delete = self.vacancy.get_vacancy_uri

        self.resume_page = ResumePage(self.driver)
        self.resume = self.resume_page.form

        self.resume_list = ResumesPage(self.driver)
        self.resume_list_form = self.resume_list.list

        self.profile_page = ProfilePage(self.driver)
        self.profile_form = self.profile_page.profile_form

        self.resume_list.open()
        self.resume_list_form.go_first_resume_page()

    def tearDown(self):
        self.vacancy.delete_vacancy(self.uri_to_delete)
        self.driver.quit()

    def test_create_response(self):
        self.resume.response()
        self.assertEqual(self.resume.get_response_done(), 'Ваш отклик успешно отправлен!')

    def test_check_created_response_in_profile(self):
        data = self.resume.response()
        parsed = data.split('\n')
        title = parsed[0]
        self.profile_page.open()
        self.profile_page.click_link_to_myResponses()
        self.assertTrue(self.profile_page.find_vacancy_in_responses(title))


class Pdf(unittest.TestCase):
    def setUp(self) -> None:
        default_setup(self)
        setup_auth(self)

        self.resume_page = ResumePage(self.driver)
        self.resume = self.resume_page.form

        self.resume_list = ResumesPage(self.driver)
        self.resume_list_form = self.resume_list.list

        self.main_page = MainPage(self.driver)

        self.resume_list.open()
        self.resume_list_form.go_first_resume_page()

    def tearDown(self):
        self.main_page.click_logout()
        self.driver.quit()

    def test_create_pdf(self):
        self.resume.click_to_create_pdf()
        self.assertEqual(len(self.driver.window_handles), 2)
