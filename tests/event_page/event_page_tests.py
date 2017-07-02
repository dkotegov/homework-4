# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidElementStateException

from tests.auth import authenticate
from tests.event_page.event_page import EventPage
from tests.utils import Test, wait_for_element_load


class EventPageTests(Test):
    ALERT_TEXT = u'Вы действительно хотите перейти к другому комментарию?'
    SOME_TEXT = 'some text'

    def setUp(self):
        super(EventPageTests, self).setUp()
        authenticate(self.driver)
        self.event_page = EventPage(self.driver)
        self.event_page.open()
        wait_for_element_load(self.driver, (By.XPATH, EventPage.UNIQUE))

    def test_registration_closed_button_text(self):
        '''Check the text of "registration closed" button'''
        participation_block = self.event_page.participation_block
        old_text = participation_block.get_button_text()
        try:
            participation_block.participate()
        except InvalidElementStateException:
            self.driver.execute_script('var xpath=\'' + participation_block.SUBMIT_BUTTON_PATH + '\';' +
                                       'document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()')
        new_text = participation_block.get_button_text()
        self.assertEqual(old_text, new_text, 'Text of participation button has changed')

    def test_registration_closed_button_color(self):
        '''Check the color of "registration closed" button'''
        participation_block = self.event_page.participation_block
        old_color = participation_block.get_button_color()
        try:
            participation_block.participate()
        except InvalidElementStateException:
            self.driver.execute_script('var xpath=\'' + participation_block.SUBMIT_BUTTON_PATH + '\';' +
                                       'document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()')
        new_color = participation_block.get_button_color()
        self.assertEqual(old_color, new_color, 'Color of participation button has changed')

    def test_comments_button_link_test(self):
        '''Click go to comments button'''
        topic_footer = self.event_page.topic_footer
        old_url = self.driver.current_url
        topic_footer.go_to_commments()
        new_url = self.driver.current_url
        self.assertEqual(new_url, old_url + '#comments', 'Go to comments wrong url')

    def test_vote_up(self):
        '''Vote up'''
        topic_footer = self.event_page.topic_footer
        topic_footer.vote_up()
        self.assertFalse(topic_footer.are_all_vote_buttons_visible(),
                         'Vote up: All vote buttons visible after voting')


    def test_vote_up_twice(self):
        '''Vote second time'''
        topic_footer = self.event_page.topic_footer
        if topic_footer.are_all_vote_buttons_visible():
            topic_footer.vote_down()
        topic_footer.vote_up()
        self.assertFalse(topic_footer.are_all_vote_buttons_visible(),
                         'Vote twice: All vote buttons visible after voting')

    def test_add_comment(self):
        '''Add comment'''
        comments_block = self.event_page.comments_block
        comments_block.add_comment()
        self.assertTrue(comments_block.is_textarea_visible(), 'Textarea is not visible - adding a comment')

    def test_click_twice_on_add_comment(self):
        '''Click add comment twice'''
        comments_block = self.event_page.comments_block
        comments_block.add_comment()
        comments_block.type_to_textarea(self.SOME_TEXT)
        comments_block.add_comment()
        self.assertTrue(self.event_page.is_alert_shown(), 'Alert not shown - adding a comment twice')
        self.assertEqual(self.event_page.get_alert_text(),
                         self.ALERT_TEXT,
                         'Alert text is wrong - adding a comment twice')
        self.event_page.confirm_alert()
        self.assertEqual(comments_block.get_text_from_textarea(), '',
                         'Text in textarea haven\'t disappear - adding a comment twice')


