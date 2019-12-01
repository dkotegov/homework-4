import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

from LoginPage import LoginPage

import time

class LoginTest(unittest.TestCase):

    LOGIN_URL = 'https://m.calendar.mail.ru/login'
    BASE_URL = 'https://m.calendar.mail.ru/'
    login = os.environ.get('LOGIN')
    password = os.environ.get('PASSWORD')

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        login_page = LoginPage(self.driver)
        login_page.open(self.LOGIN_URL)
        login_page.enter_login(self.login)
        login_page.enter_password(self.password)
        login_page.login()
        login_page.wait_redirect(self.BASE_URL)

    def test_create_event(self):
        page = LoginPage(self.driver)
        page.open(self.BASE_URL)
        page.open_menu_plus()
        count_of_childs_before = page.get_count_of_events()
        page.enter_event_name('New event 1')
        page.click_on_ok_btn()
        page.wait_redirect('https://m.calendar.mail.ru/event/new/')
        count_of_childs_after = page.get_count_of_events()
        print('before: %d, after: %d'  % (count_of_childs_before, count_of_childs_after))
        self.assertEqual(count_of_childs_before, count_of_childs_after - 1)


    def test_jump_to_edit_event(self):
        page = LoginPage(self.driver)
        page.open(self.BASE_URL)
        page.click_on_event()
        page.click_on_edit_btn()
        page.wait_redirect('https://m.calendar.mail.ru/event/new/')


    def test_edit_event(self):
        page = LoginPage(self.driver)
        page.open(self.BASE_URL)
        page.click_on_event()
        page.click_on_edit_btn()
        self.event_name = 'New event 3'
        page.enter_event_name(self.event_name)
        page.click_on_ok_btn()
        page.click_on_back_btn()
        event = page.get_event()
        self.assertEqual(event.text, "New event 3")
    
    # def test_remove_event(self):
    #     page = LoginPage(self.driver)
    #     page.open(self.BASE_URL)
    #     page.click_on_event()
    #     page.click_on_remove_btn()
    #     # Repeat to click on a remove button to confirm
    #     page.click_on_remove_btn()
    #     time.sleep(2)
    #     self.assertEqual(page.get_count_of_events(), 0)

    def tearDown(self):
        self.driver.quit()
