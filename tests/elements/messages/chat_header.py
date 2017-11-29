# coding=utf-8

from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class ChatHeader(BaseElement):
    HEAD_NAME = (By.XPATH, "//span[@class='curPointer js-open-menu js-opponent-name']")
    CALL_BUTTON = (By.CSS_SELECTOR,
                   "#hook_Block_ConversationHeader > div.chat_toolbar_cnt > div.chat_toolbar_ac > div.video-chat-buttons > a.video-chat-buttons_i.__audiocall")
