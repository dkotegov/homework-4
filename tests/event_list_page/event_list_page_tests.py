# -*- coding: utf-8 -*-

import re

from selenium.common.exceptions import InvalidElementStateException
from selenium.webdriver.common.by import By

from tests.event_list_page.event_list_page import EventListPage
from tests.auth import authenticate
from tests.create_page.create_page import CreatePage
from tests.utils import Test, wait_for_element_load


class EventListTest(Test):

    def test(self):
        authenticate(self.driver)
        self.event_list_page = EventListPage(self.driver)
        self.event_list_page.open()
        wait_for_element_load(self.driver, (By.XPATH, EventListPage.UNIQUE))

class Test1(EventListTest):
    '''Check if header redirects to event page'''

    def test(self):
        super(Test1, self).test()
        event = self.event_list_page.event
        event.open_event()
        is_url_correct = re.match(r'^http://ftest\.tech-mail\.ru/blog/topic/view/[0-9]+/$',
                                  self.driver.current_url) is not None
        self.assertTrue(is_url_correct, 'Header doesn\'t redirect to event page')


class Test2(EventListTest):
    '''Check if registration button doesn't change its text on click when registration is closed'''

    def test(self):
        super(Test2, self).test()
        event = self.event_list_page.event
        old_text = event.get_button_text()
        try:
            event.participate()
        except InvalidElementStateException:
            pass
        new_text = event.get_button_text()
        self.assertEqual(old_text, new_text, 'Registration button text changed')


class Test3(EventListTest):
    '''Check if registration button doesn't change its color on click when registration is closed'''

    def test(self):
        super(Test3, self).test()
        event = self.event_list_page.event
        old_color = event.get_button_color()
        try:
            event.participate()
        except InvalidElementStateException:
            pass
        new_color = event.get_button_color()
        self.assertEqual(old_color, new_color, 'Registration button color changed')


class Test4(EventListTest):
    '''Check if subheader redirects to event list'''

    def test(self):
        super(Test4, self).test()
        event = self.event_list_page.event
        event.open_blog()
        self.assertEqual(self.driver.current_url, EventListPage.get_url(), 'Subheader link is incorrect')


class Test5(EventListTest):
    '''Check if Читать дальше redirects to event page'''

    def test(self):
        super(Test5, self).test()
        event = self.event_list_page.event
        event.read_further()
        is_url_correct = re.match(r'^http://ftest\.tech-mail\.ru/blog/topic/view/[0-9]+/#cut$',
                                  self.driver.current_url) is not None
        self.assertTrue(is_url_correct, 'Read further url incorrect')


class Test6(EventListTest):
    '''Check if Создать топик redirects to create topic page'''

    def test(self):
        super(Test6, self).test()
        blog_menu = self.event_list_page.blog_menu
        blog_menu.create()
        self.assertEqual(self.driver.current_url, CreatePage.get_url(), 'Create page url is incorrect')