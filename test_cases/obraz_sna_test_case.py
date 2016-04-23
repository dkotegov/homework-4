# coding=utf-8
import unittest
from time import sleep
import os

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.obraz_sna_page import BlockFindNewObraz, BlockRepostToSocialNet
from test_cases.main_page_test_case import tune_driver

mypage = "https://horo.mail.ru/sonnik/nostradamus/edinorog/"
vk_login = os.environ['HW4LOGIN_VK']
vk_password = os.environ['HW4PASSWORD_VK']


class BlockFindNewObrazTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver(mypage)
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

class BlockRepostToSocialNetTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver(mypage)
        self.block = BlockRepostToSocialNet(self.driver, mypage)

    def tearDown(self):
        self.driver.quit()

    # на странице баг, авторизация не проходит из-за длинного урла (> 2000 апи вк не разрешает)
    # def testShareToVkNotYetAuth(self):
    #     before = self.block.getCountReposts()
    #     self.block.postToVkWithAuth(vk_login, vk_password)
    #     after = self.block.getCountReposts()
    #     self.assertEqual(before + 1, after)

    def testShareToVkAlreadyAuth(self):
        before = self.block.getCountReposts()

        self.block.authVK(vk_login, vk_password)
        # WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.driver.find_element_by_id('main_feed')))
        sleep(2)
        self.driver.get(mypage)

        self.block.postToVkAlreadyAuth()
        after = self.block.getCountReposts()
        self.assertEqual(before + 1, after)


