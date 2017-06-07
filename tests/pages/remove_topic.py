# coding=utf-8
from base import BasePage
from tests.elements.remove_topic import RemoveButtons


class RemoveTopicPage(BasePage):
    def __init__(self, driver, topic_id):
        self.url = 'http://ftest.tech-mail.ru/blog/topic/delete/' + str(topic_id) + '/'
        super(RemoveTopicPage, self).__init__(driver)

    def submit_remove(self):
        RemoveButtons(self.driver).submit_remove_button().wait_for_visible().get().click()

    def cancel_remove(self):
        RemoveButtons(self.driver).cancel_remove_button().wait_for_visible().get().click()
