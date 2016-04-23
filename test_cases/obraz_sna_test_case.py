# coding=utf-8
import unittest
import os
from selenium import webdriver
from pages.obraz_sna_page import BlockFindNewObraz, BlockRepostToSocialNet

mypage = "https://horo.mail.ru/sonnik/nostradamus/edinorog/"

vk_login = os.environ['HW4LOGIN_VK']
vk_password = os.environ['HW4PASSWORD_VK']

def tune_driver(mypage):
    driver = webdriver.Firefox()
    if os.environ['HW4LOGIN'] == "CHROME":
        driver = webdriver.Chrome('./chromedriver')
    driver.get(mypage)
    driver.implicitly_wait(3)
    return driver


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
        self.block.authVK(vk_login, vk_password)
        self.driver.get(mypage)

        before = self.block.getCountReposts()
        self.block.postToVkAlreadyAuth()
        after = self.block.getCountReposts()
        self.assertEqual(before + 1, after)


