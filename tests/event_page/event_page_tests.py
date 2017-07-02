# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidElementStateException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.auth import authenticate, logout
from tests.create_page.create_page import CreatePage
from tests.event_page.event_page import EventPage, Notification
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

class VoteTests(Test):
    TOPIC_TITLE = 'title'
    TOPIC_TEXT = 'text'

    def _create_topic(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        form = create_page.topic_options
        form.set_title(self.TOPIC_TITLE)
        form.set_main_text(self.TOPIC_TEXT)
        form.submit()
        wait_for_element_load(self.driver, (By.XPATH, EventPage.UNIQUE))
        self.temp_topic_url = self.driver.current_url

    def setUp(self):
        super(VoteTests, self).setUp()
        authenticate(self.driver, another=True)
        self.create_page = CreatePage(self.driver)
        self.create_page.open()
        wait_for_element_load(self.driver, (By.XPATH, CreatePage.UNIQUE))
        self._create_topic()
        logout(self.driver)
        authenticate(self.driver)
        self.event_page = EventPage(self.driver)
        self.event_page.open(self.temp_topic_url)
        wait_for_element_load(self.driver, (By.XPATH, EventPage.UNIQUE))

    def tearDown(self):
        logout(self.driver)
        authenticate(self.driver, another=True)
        self.event_page = EventPage(self.driver)
        self.event_page.open(self.temp_topic_url)
        self.event_page.topic_actions_block.delete_topic()
        self.driver.quit()

    def _test_vote(self, vote):
        topic_footer = self.event_page.topic_footer
        self.assertTrue(topic_footer.are_all_vote_buttons_visible(), 'Not all vote buttons are visible by default')
        if vote == '+':
            topic_footer.vote_up()
        elif vote == '0':
            topic_footer.vote_zero()
        elif vote == '-':
            topic_footer.vote_down()
        WebDriverWait(self.driver, 10).until(
            lambda d: Notification(d).is_notification_present()
        )
        WebDriverWait(self.driver, 10).until(
            lambda d: not Notification(d).is_notification_present()
        )
        self.assertFalse(topic_footer.are_all_vote_buttons_visible(), 'Vote up: All vote buttons visible after voting')
        return topic_footer.get_voted_class()

    def test_vote_up(self):
        '''Vote up'''
        voted_class = self._test_vote('+')
        self.assertIn('voted-up', voted_class, 'Voted class doesn\'t contain right value (vote up)')
        self.assertNotIn('voted-down', voted_class, 'Voted class contains wrong value')
        self.assertNotIn('voted-zero', voted_class, 'Voted class contains wrong value')

    def test_vote_down(self):
        '''Vote down'''
        voted_class = self._test_vote('-')
        self.assertIn('voted-down', voted_class, 'Voted class doesn\'t contain right value (vote down)')
        self.assertNotIn('voted-up', voted_class, 'Voted class contains wrong value')
        self.assertNotIn('voted-zero', voted_class, 'Voted class contains wrong value')

    def test_vote_zero(self):
        '''Vote zero'''
        voted_class = self._test_vote('0')
        self.assertIn('voted-zero', voted_class, 'Voted class doesn\'t contain right value (vote zero)')
        self.assertNotIn('voted-down', voted_class, 'Voted class contains wrong value')
        self.assertNotIn('voted-up', voted_class, 'Voted class contains wrong value')

    # def test_vote_up_twice(self):
    #     '''Vote second time'''
    #     topic_footer = self.event_page.topic_footer
    #     if topic_footer.are_all_vote_buttons_visible():
    #         topic_footer.vote_down()
    #     topic_footer.vote_up()
    #     self.assertFalse(topic_footer.are_all_vote_buttons_visible(),
    #                      'Vote twice: All vote buttons visible after voting')

