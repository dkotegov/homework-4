# coding=utf-8
from base import *
from tests.elements.show_topic import *


class ShowTopicPage(BasePage):
    def __init__(self, driver, topic_id):
        self.url = 'http://ftest.tech-mail.ru/blog/topic/view/' + str(topic_id) + '/'
        super(ShowTopicPage, self).__init__(driver)

    def get_topic_title(self):
        return TopicTitle(self.driver).wait_for_visible().get().text

    def get_topic_blog_name(self):
        return TopicBlog(self.driver).wait_for_visible().get().text

    def get_topic_content_el(self):
        return TopicContent(self.driver).wait_for_visible()

    def get_topic_poll_title(self):
        return TopicPoll(self.driver).get_title().wait_for_visible().get().text

    def get_topic_poll_answers(self):
        return TopicPoll(self.driver).get_answers().wait_for_visible().get_answers()

    def check_if_add_comment_button_is_not_exists(self):
        return TopicAddCommentButton(self.driver).is_existed() is False
