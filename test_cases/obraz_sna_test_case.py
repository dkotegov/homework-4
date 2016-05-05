# coding=utf-8
import unittest
import os

from pages.obraz_sna_page import BlockFindNewObraz, RepostBlock
from pages.vk_page import VKPage
from helpers import tune_driver

PAGE = "https://horo.mail.ru/sonnik/nostradamus/edinorog/"

VK_LOGIN = os.environ['HW4LOGIN_VK']
VK_PASSWORD = os.environ['HW4PASSWORD_VK']
BROWSER = os.environ['HW4BROWSER']


class BlockFindNewObrazTestCase(unittest.TestCase):
    @staticmethod
    def _message_is_success(msg, obraz):
        return msg.find(u" / Толкование образа") != -1 and msg.find(obraz) != -1

    @staticmethod
    def _message_is_success_search(msg, obraz):
        return msg.find(obraz + u" найдено") != -1

    @staticmethod
    def _message_is_not_success_search(msg):
        return msg.find(u"не найдено") != -1

    def setUp(self):
        self.driver = tune_driver()
        self.page = BlockFindNewObraz(self.driver, PAGE)

    def tearDown(self):
        self.driver.quit()

    def test_existing_obraz(self):
        self.page.open()

        obraz = u"Кот"
        self.page.find(obraz)
        msg = self.page.get_text_header_article()
        self.assertTrue(self._message_is_success(msg, obraz))

    def test_existing_obraz_search(self):
        self.page.open()

        obraz = u"собака"
        self.page.find(obraz)
        msg = self.page.get_text_header_search()
        self.assertTrue(self._message_is_success_search(msg, obraz))

    def test_no_existing_obraz(self):
        self.page.open()

        obraz = u"Котопёс"
        self.page.find(obraz)
        msg = self.page.get_text_article()
        self.assertTrue(self._message_is_not_success_search(msg))


class RepostBlockTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver()
        self.page = RepostBlock(self.driver, PAGE)
        self.vk_page = VKPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    ## на странице баг, авторизация не проходит из-за длинного урла (> 2000 апи вк не разрешает)
    # def test_vk_repost_with_auth(self):
    #     self.page.open()
    #
    #     before = self.page.get_count_reposts()
    #
    #     self.page.share()
    #     self.vk_page.auth(VK_LOGIN, VK_PASSWORD)
    #     self.vk_page.post()
    #
    #     self.page.open()
    #
    #     after = self.page.get_count_reposts()
    #     self.assertEqual(after, before + 1)

    def test_vk_repost(self):
        self.vk_page.open()
        self.vk_page.auth(VK_LOGIN, VK_PASSWORD)

        self.page.open()

        before = self.page.get_count_reposts()

        self.page.share()
        self.vk_page.post()

        self.page.open()

        after = self.page.get_count_reposts()
        self.assertEqual(after, before + 1)


