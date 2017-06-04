# coding=utf-8
from base import *
from tests.elements.remove_topic import *


class RemoveTopicPage(BasePage):
    def __init__(self, driver, topic_id):
        self.url = 'http://ftest.tech-mail.ru/blog/topic/delete/' + str(topic_id) + '/'
        super(RemoveTopicPage, self).__init__(driver)

    def submit_remove(self):
        SubmitRemoveButton(self.driver).wait_for_visible().get().click()

    def cancel_remove(self):
        CancelRemoveButton(self.driver).wait_for_visible().get().click()
