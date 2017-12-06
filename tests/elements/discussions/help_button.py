# coding=utf-8
from tests.elements.base import BaseElement
from selenium.webdriver.common.by import By


class HelpButton(BaseElement):
    SPAN = (By.XPATH, '//span[@uid="openHelpFeedbackForm"]')
