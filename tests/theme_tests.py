# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import ShopForumPage
from tests.common import getDriver, Auth, Shop, Main
import time

class PostTests(unittest.TestCase):
    SHOP_NAME = u'Магазин'
    KEYWORD = u'keyword'
    COMMENT = u'comment'
    ADD_TO_COMMENT = u' edited'

    def setUp(self):
        self.driver = getDriver()

        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()

        shop = Shop(self.driver)
        shop.create(self.SHOP_NAME)
        shop.open_forum_page()

        shop_forum_page = ShopForumPage(self.driver)
        topic_creation_popup = shop_forum_page.topic_creation_popup
        topic_creation_popup.open_popup()
        topic_creation_popup.set_text()
        topic_creation_popup.submit()


    def tearDown(self):
        # TODO Element <a ...> is not clickable
        import time
        time.sleep(1)

        Shop(self.driver).remove()
        self.driver.quit()

    # TODO убрать куда нибудь так как это в сетапе
    # def test_create_delete_theme(self):
    #     shop_forum_page = ShopForumPage(self.driver)
    #     topic_creation_popup = shop_forum_page.topic_creation_popup
    #     topic_creation_popup.open_popup()
    #     topic_creation_popup.set_text()
    #     topic_creation_popup.submit()

    # def test_set_key_words_to_theme(self):
    #
    #     shop_forum_page = ShopForumPage(self.driver)
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

    # def test_set_remove_class(self):
    #
    #     shop_forum_page = ShopForumPage(self.driver)
    #
    #
    #     topic_list = shop_forum_page.topic_list
    #
    #
    #     topic_list.click_class()
    #     class_counter = topic_list.get_class_counter(active=True)
    #     self.assertEqual("1",class_counter)
    #
    #     topic_list.click_class()
    #     class_counter = topic_list.get_class_counter(active=False)
    #     self.assertEqual("0", class_counter)

    # TODO возможно проверять юзера
    # Тут слишком связанные проверки, поэтому они входят в один тест
    # def test_create_delete_recover_comment(self):
    #     shop_forum_page = ShopForumPage(self.driver)
    #     topic_list = shop_forum_page.topic_list
    #     topic_list.open_topic_popup()
    #
    #     topic_popup = shop_forum_page.topic_popup
    #     topic_popup.set_comment(self.COMMENT)
    #     topic_popup.submit_comment()
    #
    #     comment_text = topic_popup.get_comment_text()
    #     self.assertEqual(self.COMMENT, comment_text)
    #
    #     topic_popup.remove_comment()
    #     remove_comment_info = topic_popup.remove_comment_info()
    #     self.assertEqual(u"Комментарий удален", remove_comment_info)
    #
    #     topic_popup.recover_comment()
    #     comment_text = topic_popup.get_comment_text()
    #     self.assertEqual(self.COMMENT, comment_text)
    #
    #     topic_popup.close_topic_popup()

    # def test_edit_comment(self):
    #     shop_forum_page = ShopForumPage(self.driver)
    #     topic_list = shop_forum_page.topic_list
    #     topic_list.open_topic_popup()
    #
    #     topic_popup = shop_forum_page.topic_popup
    #     topic_popup.set_comment(self.COMMENT)
    #     topic_popup.submit_comment()
    #
    #     topic_popup.open_edit_comment_field()
    #     topic_popup.set_comment(self.ADD_TO_COMMENT)
    #     topic_popup.submit_edit_coment()
    #     # TODO убрать слип
    #     time.sleep(1)
    #     comment_text = topic_popup.get_comment_text()
    #     self.assertEqual(self.COMMENT + self.ADD_TO_COMMENT, comment_text)
    #
    #     topic_popup.close_topic_popup()


    # TODO пока не сделано
    # def test_comment_counter(self):
    #     shop_forum_page = ShopForumPage(self.driver)
    #     topic_list = shop_forum_page.topic_list
    #     topic_list.open_topic_popup()
    #
    #     topic_popup = shop_forum_page.topic_popup
    #     topic_popup.set_comment(self.COMMENT)
    #     topic_popup.submit_comment()
    #
    #     comment_counter = topic_popup.get_comment_counter(empty=False)
    #     self.assertEqual("1", comment_counter)
    #
    #     comment_text = topic_popup.get_comment_text()
    #     self.assertEqual(self.COMMENT, comment_text)
    #
    #     topic_popup.remove_comment()
    #
    #     remove_comment_info = topic_popup.remove_comment_info()
    #     print(remove_comment_info)
    #     self.assertEqual(u"Комментарий удален", remove_comment_info)
    #
    #     time.sleep(2)
    #
    #     topic_popup.close_topic_popup()
    #
    #     time.sleep(2)




