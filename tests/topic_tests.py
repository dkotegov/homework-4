# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import ShopForumPage
from tests.common import getDriver, Auth, Shop, Main, Topic
import time


class TopicTests(unittest.TestCase):
    TOPIC_TEXT = "my topic text"
    EDITED_TOPIC_TEXT = "edited topic text"
    SHOP_NAME = u'Shop'
    KEYWORD = u'keyword'
    COMMENT = u'comment'
    EDITED_COMMENT = u' edited'
    COMMENT_REMOVE_INFO = u"Комментарий удален"

    def setUp(self):
        self.driver = getDriver()

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

    # Очень связанные между собой удаление и добавление
    # ключевых слов
    # def test_set_remove_key_words(self):
    #
    #     shop_forum_page = ShopForumPage(self.driver)
    #
    #     topic_list_element = shop_forum_page.topic_list_element
    #     topic_list_element.open_keyword_field()
    #     topic_list_element.set_keyword(self.KEYWORD)
    #     topic_list_element.submit_keyword()
    #
    #     keyword = topic_list_element.get_keyword()
    #     self.assertEqual(self.KEYWORD, keyword)
    #
    #     topic_list_element.open_keyword_edit_field()
    #     topic_list_element.delete_keyword()
    #     topic_list_element.submit_keyword()
    #
    #     try:
    #         keyword = topic_list_element.get_keyword()
    #     except:
    #         keyword = None
    #     self.assertIsNone(keyword)

    # Очень связанные между собой удаление и добавление
    # хэштега
    # def test_set_remove_hashtag(self):
    #     shop_forum_page = ShopForumPage(self.driver)
    #
    #     topic_list_element = shop_forum_page.topic_list_element
    #     topic_list_element.open_keyword_field()
    #     topic_list_element.set_keyword(self.KEYWORD)
    #     topic_list_element.submit_keyword()
    #
    #     self.driver.refresh()
    #
    #     hashtag = topic_list_element.get_hashtag()
    #     self.assertEqual('#' + self.KEYWORD, hashtag)
    #     topic_list_element.open_keyword_field()
    #     topic_list_element.delete_keyword()
    #     topic_list_element.submit_keyword()
    #
    #     self.driver.refresh()
    #
    #     try:
    #         hashtag = topic_list_element.get_hashtag()
    #     except:
    #         hashtag = None
    #     self.assertIsNone(hashtag)

    # Очень связанные между собой удаление и добавление
    # лайка
    # def test_set_remove_class(self):
    #
    #     shop_forum_page = ShopForumPage(self.driver)
    #     topic_list_element = shop_forum_page.topic_list_element
    #
    #     topic_list_element.click_class()
    #     class_counter = topic_list_element.get_class_counter(active=True)
    #     self.assertEqual("1",class_counter)
    #
    #     topic_list_element.click_class()
    #     class_counter = topic_list_element.get_class_counter(active=False)
    #     self.assertEqual("0", class_counter)
    #
    # Очень связанные проверки создание-удаление-восстановление комментария
    # def test_create_remove_recover_comment(self):
    #     shop_forum_page = ShopForumPage(self.driver)
    #     topic_list_element = shop_forum_page.topic_list_element
    #     topic_list_element.open_topic_popup()
    #
    #     topic_popup = shop_forum_page.topic_popup
    #     topic_popup.set_comment(self.COMMENT)
    #     topic_popup.submit_comment()
    #
    #     comment_text = topic_popup.get_comment_text()
    #     self.assertEqual(self.COMMENT, comment_text)
    #     comment_author = topic_popup.get_comment_author()
    #     self.assertEqual(self.SHOP_NAME, comment_author)
    #
    #     topic_popup.remove_comment()
    #     remove_comment_info = topic_popup.remove_comment_info()
    #     self.assertEqual(self.COMMENT_REMOVE_INFO, remove_comment_info)
    #
    #     topic_popup.recover_comment()
    #     comment_text = topic_popup.get_comment_text()
    #     self.assertEqual(self.COMMENT, comment_text)
    #     comment_author = topic_popup.get_comment_author()
    #     self.assertEqual(self.SHOP_NAME, comment_author)
    #
    #     topic_popup.close_topic_popup()

    # def test_edit_comment(self):
    #     shop_forum_page = ShopForumPage(self.driver)
    #     topic_list_element = shop_forum_page.topic_list_element
    #     topic_list_element.open_topic_popup()
    #
    #     topic_popup = shop_forum_page.topic_popup
    #     topic_popup.set_comment(self.COMMENT)
    #     topic_popup.submit_comment()
    #
    #     topic_popup.open_edit_comment_field()
    #     topic_popup.clear_comment_field()
    #     topic_popup.set_comment(self.EDITED_COMMENT)
    #     topic_popup.submit_edit_coment()
    #     # TODO убрать слип
    #     time.sleep(1)
    #     comment_edited_text = topic_popup.get_comment_text()
    #     self.assertEqual(self.EDITED_COMMENT, comment_edited_text)
    #
    #     topic_popup.close_topic_popup()
    #
    #
    # def test_comment_counter(self):
    #     shop_forum_page = ShopForumPage(self.driver)
    #     topic_list_element = shop_forum_page.topic_list_element
    #     topic_list_element.open_topic_popup()
    #
    #     topic_popup = shop_forum_page.topic_popup
    #     topic_popup.set_comment(self.COMMENT)
    #     topic_popup.submit_comment()
    #
    #     comment_counter = topic_popup.get_comment_counter(empty=False)
    #     self.assertEqual("1", comment_counter)
    #
    #     topic_popup.remove_comment()
    #     self.driver.refresh()
    #     comment_counter = topic_popup.get_comment_counter(empty=True)
    #     self.assertEqual("0", comment_counter)
    #
    #     topic_popup.close_topic_popup()

    # TODO не работает совсем(((
    # def test_edit_topic_text(self):
    #     shop_forum_page = ShopForumPage(self.driver)
    #     topic_list_element = shop_forum_page.topic_list_element
    #     topic_list_element.open_topic_popup()
    #
    #     topic_popup = shop_forum_page.topic_popup
    #     topic_popup.open_right_menu()
    #     topic_popup.edit_topic()
    #
    #     topic_edit_popup = shop_forum_page.topic_creation_popup
    #     topic_edit_popup.clear_edit_field()
    #     topic_edit_popup.set_text(self.EDITED_TOPIC_TEXT)
    #     topic_edit_popup.submit()
    #     # TODO убрать слип
    #     time.sleep(10)
    #
    #     edited_topic_text = topic_popup.get_topic_text()
    #     print(edited_topic_text)
    #     self.assertEqual(self.EDITED_TOPIC_TEXT, edited_topic_text)
    #     time.sleep(2)
    #
    #     topic_popup.close_topic_popup()

    def test_add_photo(self):
        shop_forum_page = ShopForumPage(self.driver)
        topic_list_element = shop_forum_page.topic_list_element
        topic_list_element.open_topic_popup()

        topic_popup = shop_forum_page.topic_popup
        topic_popup.open_right_menu()
        topic_popup.edit_topic()

        topic_edit_popup = shop_forum_page.topic_creation_popup
        topic_edit_popup.add_photo()
        topic_edit_popup.add_photo_from_computer()



















