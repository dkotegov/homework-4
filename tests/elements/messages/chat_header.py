# coding=utf-8

from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class ChatHeader(BaseElement):
    HEAD_NAME = (By.XPATH, "//span[@class='curPointer js-open-menu js-opponent-name']")
