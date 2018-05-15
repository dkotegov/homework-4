# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import ShopForumPage
from tests.common import getDriver, Auth, Shop, Main


class CreateDeleteTopicTest(unittest.TestCase):
    SHOP_NAME = u'Shop'
    TOPIC_TEXT = u'my topic text'
    REMOVE_TOPIC_INFO = u"Тема удалена"
    REMOVE_TOPIC_MSG = u"Этот объект уже удалён или заблокирован."

    def setUp(self):
        self.driver = getDriver()

        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()

        shop = Shop(self.driver)
        shop.create(self.SHOP_NAME)
        shop.open_forum_page()

    def tearDown(self):
        Shop(self.driver).remove()
        self.driver.quit()

    def test(self):
        shop_forum_page = ShopForumPage(self.driver)
        topic_creation_popup = shop_forum_page.topic_creation_popup
        topic_creation_popup.open_popup()
        topic_creation_popup.set_text(self.TOPIC_TEXT)
        topic_creation_popup.submit()

        topic_list_element = shop_forum_page.topic_list_element

        topic_text = topic_list_element.get_topic_text()
        self.assertEqual(topic_text, self.TOPIC_TEXT)

        topic_owner = topic_list_element.get_topic_owner()
        self.assertEqual(topic_owner, self.SHOP_NAME)

        topic_list_element.open_topic_popup()

        topic_popup = shop_forum_page.topic_popup
        topic_popup.open_right_menu()
        topic_popup.remove_topic()

        remove_topic_info = topic_popup.remove_topic_info()
        self.assertEqual(self.REMOVE_TOPIC_INFO, remove_topic_info)

        topic_popup.close_topic_popup()
        topic_list_element.open_topic_popup()

        notify_panel = shop_forum_page.notify_panel
        message = notify_panel.get_message()

        self.assertEqual(self.REMOVE_TOPIC_MSG, message)

        notify_panel.close_panel()

#         TODO проверить то что топика нет на странице
