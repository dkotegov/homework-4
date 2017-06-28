# -*- coding: utf-8 -*-

import os
import unittest
import re

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.by import By

from event_list import EventListPage
from auth_page import authenticate
from utils import wait_for_element_load

class Test1(unittest.TestCase):
    '''Check if header redirects to event page'''

    REGISTRATION_CLOSED = u'Регистрация закрыта'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')
        print browser
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        authenticate(self.driver)
        event_list_page = EventListPage(self.driver)
        event_list_page.open()
        wait_for_element_load(self.driver, (By.XPATH, '//h2[@class="page-header"][text()="Мероприятия"]'))
        event = event_list_page.event
        event.open_event()
        is_url_correct = re.match(r'^http://ftest\.tech-mail\.ru/blog/topic/view/[0-9]+/$',
                                  self.driver.current_url) is not None
        self.assertTrue(is_url_correct)
