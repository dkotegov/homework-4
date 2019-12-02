import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

from EventPage import EventPage

import time

class EventTest(unittest.TestCase):

    LOGIN_URL = 'https://m.calendar.mail.ru/login'
    BASE_URL = 'https://m.calendar.mail.ru/'
    login = os.environ.get('LOGIN')
    password = os.environ.get('PASSWORD')

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        login_page = EventPage(self.driver)
        login_page.open(self.LOGIN_URL)
        login_page.enter_login(self.login)
        login_page.enter_password(self.password)
        login_page.login()
        login_page.wait_redirect(self.BASE_URL)

    def test_create_event(self):
        page = EventPage(self.driver)
        page.open(self.BASE_URL)
        page.open_menu_plus()
        count_of_childs_before = page.get_count_of_events()
        page.enter_event_name('New event')
        page.click_on_ok_btn()
        page.wait_redirect('https://m.calendar.mail.ru/event/new/')
        self.driver.refresh()
        count_of_childs_after = page.get_count_of_events()
        self.assertNotEqual(count_of_childs_before, count_of_childs_after)

    def test_jump_to_edit_event(self):
        page = EventPage(self.driver)
        page.open(self.BASE_URL)
        page.create_event('New event')
        page.click_on_first_event()
        page.click_on_edit_btn()
        page.wait_redirect('https://m.calendar.mail.ru/event/new/')

    def test_edit_event(self):
        page = EventPage(self.driver)
        page.open(self.BASE_URL)
        page.create_event('New event')
        page.click_on_first_event()
        page.click_on_edit_btn()
        self.event_name = 'New event 3'
        page.enter_event_name(self.event_name)
        page.click_on_ok_btn()
        page.click_on_back_btn()
        event = page.get_first_event()
        self.assertEqual(event.text, "New event 3")
    
    def test_remove_event(self):
        page = EventPage(self.driver)
        page.open(self.BASE_URL)
        page.create_event('New event')
        self.driver.refresh()
        count_of_childs_before = page.get_count_of_events()
        page.click_on_first_event()
        page.click_on_remove_btn()
        # Repeat to click on a remove button to confirm
        page.click_on_remove_btn()
        page.wait_redirect('https://m.calendar.mail.ru')
        self.driver.refresh()
        count_of_childs_after = page.get_count_of_events()
        self.assertNotEqual(count_of_childs_before, count_of_childs_after)

    def tearDown(self):
        self.driver.quit()
