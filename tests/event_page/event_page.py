# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException, TimeoutException
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

    def is_alert_shown(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(), 'Timed out waiting alert')
        except TimeoutException:
            return False
        else:
            return True

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

    def get_voted_class(self):
        class_list = self.driver.find_element_by_xpath(self.VOTE_CONTAINER_PATH).get_attribute('class')
        return class_list

    def are_all_vote_buttons_visible(self):
        return self.driver.find_element_by_xpath(self.VOTE_UP_BUTTON_PATH).is_displayed() \
            and self.driver.find_element_by_xpath(self.VOTE_DOWN_BUTTON_PATH).is_displayed() \
            and self.driver.find_element_by_xpath(self.VOTE_INDIFFERENT_PATH).is_displayed()


class Notification(Component):
    NOTIFICATION_PATH = '//div[@class="n-box n-error"]/div'

    def is_being_shown(self):
        try:
            self._wait_for_xpath(self.NOTIFICATION_PATH)
            return True
        except TimeoutException:
            return False

    def get_text(self):
        if self.is_being_shown():
            return self.driver.find_element_by_xpath(self.NOTIFICATION_PATH).text
        return None


class CommentsBlock(Component):
    ADD_COMMENT_PATH = '//a[text()="Оставить комментарий"]'
    TEXTAREA_PATH = '//textarea[@id="id_text"]'

    def add_comment(self):
        self._clicker(self.ADD_COMMENT_PATH)

    def is_textarea_visible(self):
        self._wait_for_xpath(self.TEXTAREA_PATH)
        return self.driver.find_element_by_xpath(self.TEXTAREA_PATH).is_displayed()

    def type_to_textarea(self, text):
        self.driver.find_element_by_xpath(self.TEXTAREA_PATH).send_keys(text)

    def get_text_from_textarea(self):
        return self.driver.find_element_by_xpath(self.TEXTAREA_PATH).text
