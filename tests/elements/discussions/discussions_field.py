# coding=utf-8
from tests.elements.base import BaseElement
from selenium.webdriver.common.by import By


class DiscussionsField(BaseElement):
    DIV = (By.XPATH, '//div[@class="mdialog_list_conversations custom-scrolling"]')
