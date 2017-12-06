# coding=utf-8

from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class HomeButton(BaseElement):
    BUTTON = (By.XPATH, u'//div[@title="На главную"]')
