import unittest

from pages.resumes_page import ResumesPage
from pages.resume_page import ResumePage
from pages.profile_page import ProfilePage
from tests.default_setup import default_setup
from scenario.registration_employer import registration_employer


class Favorite(unittest.TestCase):
    data = {
        'title': 'My Title',
        'description': 'My cool resume',
        'place': 'I very good',
        'skills': 'My great skills',
    }

    def setUp(self) -> None:
        default_setup(self)
        registration_employer(self, False)

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
        self.assertEqual(self.resume.get_text_favorite_btn(), 'Убрать из избранного')
        self.profile_page.open()

    def test_check_added_favorite_in_profile(self):
        self.assertEqual(self.resume.get_text_favorite_btn(), 'Добавить в избранное')
        self.resume.add_to_favorite()
        self.profile_page.open()
        page_data = self.profile_page.get_my_favorite()
        self.assertDictEqual(page_data, {
            'title': self.data['title'],
            'description': self.data['description'],
        })
        self.profile_page.click_my_profile_info()


