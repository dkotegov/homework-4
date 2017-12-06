# coding=utf-8

from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class ChatHeader(BaseElement):
    HEAD_NAME = (By.XPATH, "//span[@class='curPointer js-open-menu js-opponent-name']")
    CALL_BUTTON = (By.CSS_SELECTOR, "a.video-chat-buttons_i:nth-child(2)")
