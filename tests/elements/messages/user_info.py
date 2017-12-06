# coding=utf-8

from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class UserInfo(BaseElement):
    HEAD_NAME = (By.XPATH, "//div[@class='chat_column_hd_name']")
    DO_NOT_DISTURB_BUTTON = (By.CSS_SELECTOR, ".chat_column_menu > ul:nth-child(1) > li:nth-child(5) > a:nth-child(1)")
