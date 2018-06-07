# -*- coding: utf-8 -*-
import time
import unittest

from PageObjects.page_objects import ShopForumPage
from tests.common import get_driver, Auth, Shop, Main, Topic


class HashTagTests(unittest.TestCase):
    """Набор тестов на разные варианты создания ключевого слова"""
    TOPIC_TEXT = "my topic text"
    SHOP_NAME = u'Shop'

    SIMPLE_HASHTAG = u"хэштег"
    HASHTAG_WITH_SPACE_CASE = {
        'keyword': u'хэштег с пробелом',
        'hashtag': u'#ХэштегСПробелом'}
    HASHTAG_WITH_DOTS_CASE = {
        'keyword': u'...хэштег///',
        'hashtag': u'#Хэштег'}

    def setUp(self):
        self.driver = get_driver()

        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()

        shop = Shop(self.driver)
        shop.create(self.SHOP_NAME)
        shop.open_forum_page()

        Topic(self.driver).create(text=self.TOPIC_TEXT)

    def tearDown(self):
        # Topic(self.driver).remove()
        # # TODO Element <a ...> is not clickable
        # import time
        time.sleep(1)

        Shop(self.driver).remove()
        self.driver.quit()

    def test_simple_keyword_creation_and_delete(self):
        """Позитивный тест на создание и удаление простого хэштега"""
        keyword_component = ShopForumPage(self.driver).keyword_component
        keyword_component.open_keyword_field()
        keyword_component.set_keyword(self.SIMPLE_HASHTAG)
        keyword_component.submit_keyword()

        self.driver.refresh()

        hashtag = keyword_component.get_hashtag()
        self.assertEqual('#' + self.SIMPLE_HASHTAG, hashtag)

        keyword_component.open_keyword_field()
        keyword_component.delete_keyword()
        keyword_component.submit_keyword()

        self.driver.refresh()

        self.assertFalse(keyword_component.is_hashtag_exists())

    def test_hashtag_with_space_creation(self):
        """Позитивный тест на создание хэштега из ключевого слова с пробелом"""
        keyword_component = ShopForumPage(self.driver).keyword_component
        keyword_component.open_keyword_field()
        keyword_component.set_keyword(self.HASHTAG_WITH_SPACE_CASE['keyword'])
        keyword_component.submit_keyword()

        self.driver.refresh()

        hashtag = keyword_component.get_hashtag()
        self.assertEqual(self.HASHTAG_WITH_SPACE_CASE['hashtag'], hashtag)

    def test_hashtag_with_dots_creation(self):
        """Позитивный тест на создание хэштега из ключевого слова с точками и слешами"""
        keyword_component = ShopForumPage(self.driver).keyword_component
        keyword_component.open_keyword_field()
        keyword_component.set_keyword(self.HASHTAG_WITH_DOTS_CASE['keyword'])
        keyword_component.submit_keyword()

        self.driver.refresh()

        hashtag = keyword_component.get_hashtag()
        self.assertEqual(self.HASHTAG_WITH_DOTS_CASE['hashtag'], hashtag)

    def test_some_hashtag_creation(self):
        """Позитивный тест на создание хэштега из ключевого слова с точками и слешами"""
        keyword_component = ShopForumPage(self.driver).keyword_component
        keyword_component.open_keyword_field()
        keyword_component.set_keyword(self.HASHTAG_WITH_DOTS_CASE['keyword'])
        keyword_component.submit_keyword()

        self.driver.refresh()

        hashtag = keyword_component.get_hashtag()
        self.assertEqual(self.HASHTAG_WITH_DOTS_CASE['hashtag'], hashtag)
