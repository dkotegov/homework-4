# coding=utf-8

from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class SettingsButton(BaseElement):
    BUTTON = (By.XPATH, u'//a[@title="Настройки"]')
