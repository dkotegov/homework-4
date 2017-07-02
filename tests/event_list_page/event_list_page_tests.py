# -*- coding: utf-8 -*-

import re

from selenium.common.exceptions import InvalidElementStateException, TimeoutException
from selenium.webdriver.common.by import By

from tests.event_list_page.event_list_page import EventListPage
from tests.auth import authenticate
from tests.create_page.create_page import CreatePage
from tests.event_page.event_page import EventPage
from tests.utils import Test, wait_for_element_load


class EventListTests(Test):

    def setUp(self):
        super(EventListTests, self).setUp()
        authenticate(self.driver)
        self.event_list_page = EventListPage(self.driver)
        self.event_list_page.open()
        wait_for_element_load(self.driver, (By.XPATH, EventListPage.UNIQUE))

    def test_header_link(self):
        '''Check if header redirects to event page'''
        event = self.event_list_page.event
        event.open_event()
        is_url_correct = re.match(r'^http://ftest\.tech-mail\.ru/blog/topic/view/[0-9]+/$',
                                  self.driver.current_url) is not None
        self.assertTrue(is_url_correct, 'Header doesn\'t redirect to event page')

    def test_registration_closed_button_text(self):
        '''Check if registration button doesn't change its text on click when registration is closed'''
        event = self.event_list_page.event
        old_text = event.get_button_text()
        try:
            event.participate()
        except InvalidElementStateException:
            self.driver.execute_script('var xpath=\'' + event.SUBMIT_BUTTON_PATH + '\';' +
                                       'document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()')
        new_text = event.get_button_text()
        self.assertEqual(old_text, new_text, 'Registration button text changed')

    def test_registration_closed_button_color(self):
        '''Check if registration button doesn't change its color on click when registration is closed'''
        event = self.event_list_page.event
        old_color = event.get_button_color()
        try:
            event.participate()
        except InvalidElementStateException:
            self.driver.execute_script('var xpath=\'' + event.SUBMIT_BUTTON_PATH + '\';' +
                                       'document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()')
        new_color = event.get_button_color()
        self.assertEqual(old_color, new_color, 'Registration button color changed')

    def test_subheader_link(self):
        '''Check if subheader redirects to event list'''
        event = self.event_list_page.event
        event.open_blog()
        try:
            wait_for_element_load(self.driver, (By.XPATH, EventListPage.UNIQUE))
        except TimeoutException:
            self.fail('Subheader link is incorrect')

    def test_read_further_link(self):
        '''Check if Читать дальше redirects to event page'''
        event = self.event_list_page.event
        event.read_further()
        try:
            wait_for_element_load(self.driver, (By.XPATH, EventPage.UNIQUE))
        except TimeoutException:
            self.fail('Read further link is incorrect')
        finally:
            self.assertRegexpMatches(self.driver.current_url,
                                 r'^http://ftest\.tech-mail\.ru/blog/topic/view/[0-9]+/#cut$',
                                 'Read further link doesn\'t scroll')

    def test_create_topic_link(self):
        '''Check if Создать топик redirects to create topic page'''
        blog_menu = self.event_list_page.blog_menu
        blog_menu.create()
        try:
            wait_for_element_load(self.driver, (By.XPATH, CreatePage.UNIQUE))
        except TimeoutException:
            self.fail('Create topic link is incorrect')
