import unittest
from selenium import webdriver
from pages.auth_page import AuthPage
from pages.userinfo_page import UserInfoPage

class UserInfoTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_correct_input(self):
        auth_page = AuthPage(self.driver)
        auth_page.authorize()

        userinfo_page = UserInfoPage(self.driver)

        userinfo_page.input_firstname('fname')
        userinfo_page.input_lastname('lname')
        userinfo_page.input_nickname('nname')

        userinfo_page.click_submit_button()
        userinfo_page.wait_for_ok_after_submit()



    def test_image_upload(self):
        auth_page = AuthPage(self.driver)
        auth_page.authorize()

        userinfo_page = UserInfoPage(self.driver)
        userinfo_page.input_test_image()

        userinfo_page.click_submit_button()
        userinfo_page.wait_for_ok_after_submit()



    def test_logout(self):
        auth_page = AuthPage(self.driver)
        auth_page.authorize()

        userinfo_page = UserInfoPage(self.driver)
        userinfo_page.open_settings_in_new_window()
        userinfo_page.wait_for_ok_after_submit()

        userinfo_page.click_logout_button()
        userinfo_page.wait_for_logout()

        userinfo_page.switch_to_window(0)
        userinfo_page.resresh_page()
        userinfo_page.match_to_login_URI()


    def test_date_lists(self):
        auth_page = AuthPage(self.driver)
        auth_page.authorize()

        userinfo_page = UserInfoPage(self.driver)

        userinfo_page.click_on_day_input()
        userinfo_page.click_on_day_child_input()
        userinfo_page.click_on_month_input()
        userinfo_page.click_on_month_child_input()
        userinfo_page.click_on_year_input()
        userinfo_page.click_on_year_child_input()

        userinfo_page.click_submit_button()
        userinfo_page.wait_for_ok_after_submit()




    def test_open_help(self):
        auth_page = AuthPage(self.driver)
        auth_page.authorize()

        userinfo_page = UserInfoPage(self.driver)

        userinfo_page.click_on_help()
        userinfo_page.switch_to_window(1)
        userinfo_page.wait_for_help()