# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidElementStateException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.auth import authenticate, logout, switch_to_user2, switch_to_user1
from tests.create_page.create_page import CreatePage
from tests.event_page.event_page import EventPage, Notification
from tests.utils import Test, wait_for_element_load


class TestsRequiringTopicCreate(Test):
    '''Contains create topic function'''

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
        super(TestsRequiringTopicCreate, self).setUp()
        authenticate(self.driver)
        self._create_topic()
        self.event_page = EventPage(self.driver)
        self.event_page.open(self.temp_topic_url)
        wait_for_element_load(self.driver, (By.XPATH, EventPage.UNIQUE))

    def tearDown(self):
        switch_to_user1(self.driver)
        self.event_page = EventPage(self.driver)
        self.event_page.open(self.temp_topic_url)
        self.event_page.topic_actions_block.delete_topic()
        self.driver.quit()


class TestsRequiringTwoPersons(Test):
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
        super(TestsRequiringTwoPersons, self).setUp()
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


class EventPageTests(Test):
    ALERT_TEXT = u'Вы действительно хотите перейти к другому комментарию?'
    SOME_TEXT = 'some text'

    def setUp(self):
        super(EventPageTests, self).setUp()
        authenticate(self.driver)
        self.event_page = EventPage(self.driver)
        self.event_page.open()
        wait_for_element_load(self.driver, (By.XPATH, EventPage.UNIQUE))

    def test_registration_closed_button(self):
        '''Check the text of "registration closed" button'''
        participation_block = self.event_page.participation_block
        self.assertFalse(participation_block.is_button_clickable())

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


class CommentTests(TestsRequiringTopicCreate):
    SOME_TEXT = 'some text'
    COMMENT_DELETED = u'комментарий удален'
    COMMENT_DELETED_COLOR = '#c5c5c5'

    def comment(self):
        comments_block = self.event_page.comments_block
        comments_block.add_comment()
        if comments_block.is_textarea_visible():
            comments_block.type_to_textarea(self.SOME_TEXT)
            comments_block.submit_comment()

    def test_leaving_comment(self):
        self.comment()
        comment_text = self.event_page.comments_block.get_comment_text()
        self.assertEqual(comment_text, self.SOME_TEXT, 'Comment adding failed!')

    def test_deleting_comment(self):
        self.comment()
        self.event_page.comments_block.delete_comment()
        switch_to_user2(self.driver)
        self.event_page.open(self.temp_topic_url)
        comment_text = self.event_page.comments_block.get_comment_container_text()
        self.assertEqual(comment_text, self.COMMENT_DELETED, 'Comment deleting failed')


class VoteTests(TestsRequiringTwoPersons):
    OUT_OF_TIME = u'Время истекло'

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

    def test_vote_up_twice(self):
        '''Vote second time'''

        self._test_vote('+')
        self.event_page.topic_footer.vote_up()
        notification = self.event_page.notification
        WebDriverWait(self.driver, 10).until(lambda d: notification.is_notification_present())
        self.assertEqual(notification.get_text(), self.OUT_OF_TIME, 'Vote twice: notification wrong text')
        WebDriverWait(self.driver, 10).until(lambda d: not notification.is_notification_present())

    def test_vote_down_twice(self):
        '''Vote second time'''

        self._test_vote('-')
        self.event_page.topic_footer.vote_up()
        notification = self.event_page.notification
        WebDriverWait(self.driver, 10).until(lambda d: notification.is_notification_present())
        self.assertEqual(notification.get_text(), self.OUT_OF_TIME, 'Vote twice: notification wrong text')
        WebDriverWait(self.driver, 10).until(lambda d: not notification.is_notification_present())
