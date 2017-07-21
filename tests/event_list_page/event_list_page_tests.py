# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

from tests.event_list_page.event_list_page import EventListPage
from tests.auth import TestWithAuth
from tests.create_page.create_page import CreatePage
from tests.event_page.event_page import EventPage
from tests.utils import wait_for_element_load, Header


class EventListTests(TestWithAuth):

    def setUp(self):
        super(EventListTests, self).setUp()
        self.event_list_page = EventListPage(self.driver)
        self.event_list_page.open()
        wait_for_element_load(self.driver, (By.XPATH, EventListPage.UNIQUE))

    def test_header_link(self):
        """Check if header redirects to event page"""
        event = self.event_list_page.event
        event.open_event()
        wait_for_element_load(self.driver, (By.XPATH, EventPage.UNIQUE))
        self.assertRegexpMatches(self.driver.current_url,
                                 r'^http://ftest\.tech-mail\.ru/blog/topic/view/[0-9]+/',
                                 'Header doesn\'t redirect to event page')

    def test_registration_closed_button_text(self):
        """Check if registration button doesn't change its text on click when registration is closed"""
        event = self.event_list_page.event
        self.assertFalse(event.is_button_clickable())

    def test_subheader_link(self):
        """Check if subheader redirects to event list"""
        event = self.event_list_page.event
        header = Header(self.driver).get_header_text()
        event.open_blog()
        self.assertEqual(header, EventListPage.HEADER_TEXT)

    def test_read_further_link(self):
        """Check if Читать дальше redirects to event page"""
        event = self.event_list_page.event
        event.read_further()
        wait_for_element_load(self.driver, (By.XPATH, EventPage.UNIQUE))
        self.assertRegexpMatches(self.driver.current_url,
                                 r'^http://ftest\.tech-mail\.ru/blog/topic/view/[0-9]+/#cut$',
                                 'Read further link doesn\'t scroll')

    def test_create_topic_link(self):
        """Check if Создать топик redirects to create topic page"""

        blog_menu = self.event_list_page.blog_menu
        blog_menu.create()
        header = Header(self.driver).get_header_text().strip()
        self.assertEqual(CreatePage.HEADER_TEXT, header)
