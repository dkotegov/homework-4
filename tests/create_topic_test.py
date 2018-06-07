# -*- coding: utf-8 -*-
import unittest

from tests.common import get_driver, Auth, Shop, Main, Topic


class CreateTopicTest(unittest.TestCase):
    SHOP_NAME = u'Shop'
    USERNAME = u'Феофан Лампер'
    TOPIC_TEXT = u'My topic text'

    def setUp(self):
        self.driver = get_driver()

        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()

        self.shop = Shop(self.driver)
        self.shop.create(self.SHOP_NAME)
        self.shop.open_forum_page()

    def tearDown(self):
        self.shop.remove()
        self.driver.quit()

    def test_create_topic(self):
        topic = Topic(self.driver)
        topic.create(self.TOPIC_TEXT)

        topic_text = topic.get_text()
        self.assertEqual(self.TOPIC_TEXT, topic_text)

        topic_shop_name = topic.get_shop_name()
        self.assertEqual(self.SHOP_NAME, topic_shop_name)

        topic_author = topic.get_author()
        self.assertEqual(self.USERNAME, topic_author)
