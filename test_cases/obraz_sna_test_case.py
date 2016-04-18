# coding=utf-8
import unittest
import time
import datetime

from selenium import webdriver

from pages.obraz_sna_page import BlockFindNewObraz


def tune_driver():
    # self.driver = webdriver.Chrome('./chromedriver')
    driver = webdriver.Firefox()
    driver.get("https://horo.mail.ru/sonnik/nostradamus/edinorog/")
    driver.implicitly_wait(10)
    return driver


class BlockFindNewObrazTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver()
        self.block = BlockFindNewObraz(self.driver)

    def tearDown(self):
        self.driver.quit()

    def testExistingObraz(self):
        obrazs = [u"Кот", u"Собака"]

        for i in range(len(obrazs)):

            self.block.find(obrazs[i])
            msg = self.block.get_message_success()
            self.assertTrue(self.block.message_is_success(msg, obrazs[i]))

    def testNoExistingObraz(self):
        obraz = u"Котопёс"

        self.block.find(obraz)
        msg = self.block.get_message_no_success()
        self.assertTrue(self.block.message_is_no_success(msg))







