# coding=utf-8
from tests.elements.base import BaseElement
from selenium.webdriver.common.by import By

class MyPosts(BaseElement):
    BUTTON = (By.XPATH, u'//span[text()="Мои"]')