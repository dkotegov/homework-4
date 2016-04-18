# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class BlockFindNewObraz:
    def __init__(self, driver):
        self.driver = driver

    def get_message_no_success(self):
        message = self.driver.find_element_by_class_name("article__text")
        return message.text

    def message_is_success(self, msg, obraz):
        return msg.find(obraz + u" найдено") != -1 or msg.find(obraz + u" / Толкование образа") != -1


    def message_is_no_success(self, msg):
        return msg.find(u"не найдено") != -1

    def get_message_success(self):
        str1 = self._get_message1_success()
        if str1 != None:
            return str1
        else:
            return self._get_message2_success()

    def _get_message1_success(self):
        try:
            message = self.driver.find_element_by_class_name("hdr_search")
            return message.text
        except NoSuchElementException:
            return None

    def _get_message2_success(self):
        try:
            message = self.driver.find_element_by_class_name("hdr__inner")
            return message.text
        except NoSuchElementException:

            return None

    def find(self, obraz):
        input = self.driver.find_element_by_name("q")
        input.send_keys(obraz)

        self.driver.find_element_by_name("clb11934144").click()



