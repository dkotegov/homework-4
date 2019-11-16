from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tests.pages.AskPage import AskPage

import os
import unittest

class notEmptyQuestionTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.page = AskPage()
        super(notEmptyQuestionTestCase, self).__init__(*args, **kwargs)

    def test_01(self):
        shortQuestion = 'Why, man?'
        self.page.setQuestionTheme(shortQuestion)
        self.page.clearQuestionThemeByKeys()
        self.assertEqual(self.page.getAlertUnderQuestion(),
            'Поле «Тема вопроса» обязательно для заполнения.')

    def tearDown(self):
        self.page.quitDriver()