from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tests.pages.AskPage import AskPage

import os
import time
import unittest

class AskTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.page = AskPage()
        super(AskTests, self).__init__(*args, **kwargs)

    def tearDown(self):
        self.page.quitDriver()

    def test_notEmptyQuestion(self):
        shortQuestion = 'Why, man?'
        self.page.setQuestionTheme(shortQuestion)
        self.page.clearQuestionThemeByKeys()
        self.assertEqual(self.page.getAlertUnderQuestion(),
            'Поле «Тема вопроса» обязательно для заполнения.')

    def test_tooBigQuestion(self):
        bigStr = ''
        for _ in range(122):
            bigStr = bigStr + 'a'
        self.page.setQuestionTheme(bigStr)
        self.assertEqual(self.page.getAlertUnderQuestion(),
            'Поле «Тема вопроса» не может быть больше 120 символов.')

    def test_mentionCountry(self):
        questionWithCountry = 'Россия'
        self.page.setQuestionTheme(questionWithCountry)
        # Пока не понятно как этот костыль решать
        time.sleep(5)
        self.assertEqual(self.page.getSubcategory(),
            'Политика')

    def test_loginBtn(self):
        self.page.clickLogin()
        self.assertTrue(self.page.lofinFormIsVisible())

    def test_authorization(self):
        self.page.clickLogin()
        self.page.login()
        self.assertTrue(self.page.checkUrl())

    def test_profile(self):
        self.page.clickLogin()
        self.page.login()
        self.page.clickAndWaitProfile()
