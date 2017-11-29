# coding=utf-8

from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class UserInfo(BaseElement):
    HEAD_NAME = (By.XPATH, "//div[@class='chat_column_hd_name']")
