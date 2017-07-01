# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidElementStateException

from tests.auth import authenticate
from tests.event_page.event_page import EventPage
from tests.utils import Test, wait_for_element_load


class EventPageTest(Test):

    def test(self):
        authenticate(self.driver)
        self.event_page = EventPage(self.driver)
        self.event_page.open()
        wait_for_element_load(self.driver, (By.XPATH, EventPage.UNIQUE))

class Test1(EventPageTest):
    '''Check the text of "registration closed" button'''

    def test(self):
        super(Test1, self).test()
        participation_block = self.event_page.participation_block
        old_text = participation_block.get_button_text()
        try:
            participation_block.participate()
        except InvalidElementStateException:
            pass
        new_text = participation_block.get_button_text()
        self.assertEqual(old_text, new_text, 'Text of participation button has changed')


class Test2(EventPageTest):
    '''Check the color of "registration closed" button'''

    def test(self):
        super(Test2, self).test()
        participation_block = self.event_page.participation_block
        old_color = participation_block.get_button_color()
        try:
            participation_block.participate()
        except InvalidElementStateException:
            pass
        new_color = participation_block.get_button_color()
        self.assertEqual(old_color, new_color, 'Color of participation button has changed')


class Test3(EventPageTest):
    '''Click go to comments button'''

    def test(self):
        super(Test3, self).test()
        topic_footer = self.event_page.topic_footer
        old_url = self.driver.current_url
        topic_footer.go_to_commments()
        new_url = self.driver.current_url
        self.assertEqual(new_url, old_url + '#comments', 'Go to comments wrong url')


class Test4(EventPageTest):
    '''Vote up'''

    def test(self):
        super(Test4, self).test()
        topic_footer = self.event_page.topic_footer
        topic_footer.vote_up()
        self.assertFalse(topic_footer.are_all_vote_buttons_visible(),
                         'Vote up: All vote buttons visible after voting')


class Test5(EventPageTest):
    '''Vote second time'''

    def test(self):
        super(Test5, self).test()
        topic_footer = self.event_page.topic_footer
        notification = self.event_page.notification
        if topic_footer.are_all_vote_buttons_visible():
            topic_footer.vote_down()
        topic_footer.vote_up()
        self.assertFalse(topic_footer.are_all_vote_buttons_visible(),
                         'Vote twice: All vote buttons visible after voting')


class Test6(EventPageTest):
    '''Add comment'''

    def test(self):
        super(Test6, self).test()
        comments_block = self.event_page.comments_block
        comments_block.add_comment()
        self.assertTrue(comments_block.is_textarea_visible(), 'Textarea is not visible - adding a comment')


class Test7(EventPageTest):
    '''Click add comment twice'''

    def test(self):
        super(Test7, self).test()
        comments_block = self.event_page.comments_block
        comments_block.add_comment()
        comments_block.add_comment()
        self.assertTrue(self.event_page.is_alert_shown(), 'Alert not shown - adding a comment twice')