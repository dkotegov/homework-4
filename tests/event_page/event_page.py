# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.utils import Page, Component


class EventPage(Page):
    PATH = 'blog/topic/view/8532/'
    UNIQUE = '//span[@id="count-comments"]'

    @property
    def participation_block(self):
        return ParticipationBlock(self.driver)

    @property
    def topic_footer(self):
        return TopicFooter(self.driver)

    @property
    def notification(self):
        return Notification(self.driver)

    @property
    def comments_block(self):
        return CommentsBlock(self.driver)

    @property
    def topic_actions_block(self):
        return TopicActionsBlock(self.driver)

    def is_alert_shown(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(), 'Timed out waiting alert')
            return True
        except TimeoutException:
            return False

    def get_alert_text(self):
        if self.is_alert_shown():
            return self.driver.switch_to.alert.text
        return None

    def confirm_alert(self):
        if self.is_alert_shown():
            self.driver.switch_to.alert.accept()


class ParticipationBlock(Component):
    SUBMIT_BUTTON_PATH = '//button[text()="Регистрация закрыта"]'

    def participate(self):
        self._clicker(self.SUBMIT_BUTTON_PATH)

    def get_button_text(self):
        self._wait_for_xpath(self.SUBMIT_BUTTON_PATH)
        return self.driver.find_element_by_xpath(self.SUBMIT_BUTTON_PATH).text

    def get_button_color(self):
        self._wait_for_xpath(self.SUBMIT_BUTTON_PATH)
        return self.driver.find_element_by_xpath(self.SUBMIT_BUTTON_PATH).value_of_css_property('background-color')

    def is_button_clickable(self):
        return self._wait_for_xpath(self.SUBMIT_BUTTON_PATH).is_enabled()


class TopicFooter(Component):
    COMMENTS_BUTTON_PATH = '//a[@title="читать комментарии"]'
    VOTE_UP_BUTTON_PATH = '//div[@class="vote-item vote-up"]'
    VOTE_DOWN_BUTTON_PATH = '//div[@class="vote-item vote-down"]'
    VOTE_INDIFFERENT_PATH = '//div[@class="vote-item vote-count"]'
    VOTE_CONTAINER_PATH = '//li[@class="topic-info-vote"]/div'

    def go_to_commments(self):
        self._clicker(self.COMMENTS_BUTTON_PATH)

    def vote_up(self):
        self._clicker(self.VOTE_UP_BUTTON_PATH)

    def vote_down(self):
        self._clicker(self.VOTE_DOWN_BUTTON_PATH)

    def vote_zero(self):
        self._clicker(self.VOTE_INDIFFERENT_PATH)

    def get_voted_class(self):
        class_list = self.driver.find_element_by_xpath(self.VOTE_CONTAINER_PATH).get_attribute('class')
        return class_list

    def are_all_vote_buttons_visible(self):
        return self.driver.find_element_by_xpath(self.VOTE_UP_BUTTON_PATH).is_displayed() \
            and self.driver.find_element_by_xpath(self.VOTE_DOWN_BUTTON_PATH).is_displayed() \
            and self.driver.find_element_by_xpath(self.VOTE_INDIFFERENT_PATH).is_displayed()


class Notification(Component):
    NOTIFICATION_PATH = '//div[contains(@class, "n-box")]/p'
    CONTAINER_PATH = '//div[@id="notifier"]'

    def is_being_shown(self):
        try:
            self._wait_for_xpath(self.NOTIFICATION_PATH)
            return True
        except TimeoutException:
            return False

    def get_text(self):
        if self.is_notification_present():
            return self.driver.find_element_by_xpath(self.NOTIFICATION_PATH).text
        return None

    def is_notification_present(self):
        return self._wait_for_xpath(self.CONTAINER_PATH).text != ''


class CommentsBlock(Component):
    ADD_COMMENT_PATH = u'//a[text()="Оставить комментарий"]'
    TEXTAREA_PATH = '//textarea[@id="id_text"]'
    SUBMIT_COMMENT_PATH = u'//button[text()="добавить"]'
    COMMENT_PATH = '//div[@class="comment-rendered"]'
    COMMENT_CONTAINER_PATH = '//div[@class="comment-content "]'
    DELETE_COMMENT_PATH = '//a[@class="comment-delete link-dotted comment-deletable"]'

    def add_comment(self):
        self._clicker(self.ADD_COMMENT_PATH)

    def is_textarea_visible(self):
        return self._wait_for_xpath(self.TEXTAREA_PATH).is_displayed()

    def type_to_textarea(self, text):
        self.driver.find_element_by_xpath(self.TEXTAREA_PATH).send_keys(text)

    def get_text_from_textarea(self):
        return self.driver.find_element_by_xpath(self.TEXTAREA_PATH).text

    def submit_comment(self):
        self._clicker(self.SUBMIT_COMMENT_PATH)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.COMMENT_PATH))
        )

    def get_comment_text(self):
        return self._wait_for_xpath(self.COMMENT_PATH).text.strip()

    def get_comment_container_text(self):
        return self._wait_for_xpath(self.COMMENT_CONTAINER_PATH).text.strip()

    def delete_comment(self):
        self._clicker(self.DELETE_COMMENT_PATH)
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), 'Deleting comment: alert didn\'t appear')
        alert = self.driver.switch_to.alert
        alert.accept()
        WebDriverWait(self.driver, 10).until(
            lambda d: Notification(d).is_notification_present()
        )
        WebDriverWait(self.driver, 10).until(
            lambda d: not Notification(d).is_notification_present()
        )

class TopicActionsBlock(Component):
    DELETE_LINK_PATH = '//a[@class="actions-delete"]'
    DELETE_BUTTON_CONFIRM = '//input[@value="Удалить"]'

    def delete_topic(self):
        self._clicker(self.DELETE_LINK_PATH)
        confirm_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DELETE_BUTTON_CONFIRM)
        )
        confirm_button.click()
