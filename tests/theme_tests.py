# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import ShopForumPage
from tests.common import getDriver, Auth, Shop, Main
import time

class PostTests(unittest.TestCase):
    SHOP_NAME = u'Магазин'
    KEYWORD = u'keyword'

    def setUp(self):
        self.driver = getDriver()

        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()

        shop = Shop(self.driver)
        shop.create(self.SHOP_NAME)
        shop.open_forum_page()

    def tearDown(self):
        # TODO Element <a ...> is not clickable
        import time
        time.sleep(1)

        Shop(self.driver).remove()
        self.driver.quit()

    # def test_create_delete_theme(self):
    #     shop_forum_page = ShopForumPage(self.driver)
    #     topic_popup = shop_forum_page.topic_popup
    #     topic_popup.open_popup()
    #     topic_popup.set_text()
    #     topic_popup.submit()

    # def test_set_key_words_to_theme(self):
    #
    #     shop_forum_page = ShopForumPage(self.driver)
    #     topic_popup = shop_forum_page.topic_popup
    #     topic_popup.open_popup()
    #     topic_popup.set_text()
    #     topic_popup.submit()
    #
    #     topic_list = shop_forum_page.topic_list
    #     topic_list.open_keyword_field()
    #     topic_list.set_keyword(self.KEYWORD)
    #     topic_list.submit_keyword()
    #
    #     keyword = topic_list.get_keyword()
    #     self.assertEqual(self.KEYWORD, keyword)
    #
    #     topic_list.open_keyword_edit_field()
    #     topic_list.delete_keyword()
    #     topic_list.submit_keyword()
    #     # TODO проверить удаление


    # def test_set_hashtag_to_theme(self):
    #     shop_forum_page = ShopForumPage(self.driver)
    #     topic_popup = shop_forum_page.topic_popup
    #     topic_popup.open_popup()
    #     topic_popup.set_text()
    #     topic_popup.submit()
    #
    #     topic_list = shop_forum_page.topic_list
    #     topic_list.open_keyword_field()
    #     topic_list.set_keyword(self.KEYWORD)
    #     topic_list.submit_keyword()
    #
    #     self.driver.refresh()
    #
    #     hashtag = topic_list.get_hashtag()
    #     self.assertEqual('#' + self.KEYWORD, hashtag)
    #     topic_list.open_keyword_field()
    #     topic_list.delete_keyword()
    #     topic_list.submit_keyword()
    #
    #     self.driver.refresh()
    #     # TODO проверить удаление

    def test_set_class(self):

        shop_forum_page = ShopForumPage(self.driver)
        topic_popup = shop_forum_page.topic_popup
        topic_popup.open_popup()
        topic_popup.set_text()
        topic_popup.submit()

        topic_list = shop_forum_page.topic_list

        topic_list.click_class()
        class_counter = topic_list.get_class_counter(active=True)
        self.assertEqual("1",class_counter)

        topic_list.click_class()
        class_counter = topic_list.get_class_counter(active=False)
        self.assertEqual("0", class_counter)





