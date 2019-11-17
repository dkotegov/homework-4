# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tests.AskPage import AskPage

import os
import unittest

class AskTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.page = AskPage()
        super(AskTests, self).__init__(*args, **kwargs)

    def tearDown(self):
        self.page.quitDriver()

    def test_needThreeWords(self):
        self.page.clickLogin()
        self.page.login()
        self.page.setQuestionTheme('hello, world!')
        self.page.clickChooseAutosport()
        self.page.clickSendQuestion()
        self.page.checkAlert()

    def test_profile(self):
        self.page.clickLogin()
        self.page.login()
        self.page.clickAndWaitProfile()

    def test_notEmptyQuestion(self):
        shortQuestion = u'Why, man?'
        self.page.setQuestionTheme(shortQuestion)
        self.page.clearQuestionThemeByKeys()
        self.assertEqual(self.page.getAlertUnderQuestion(),
            u'Поле «Тема вопроса» обязательно для заполнения.')

    def test_mentionCountry(self):
        questionWithCountry = u'Россия'
        self.page.setQuestionTheme(questionWithCountry)
        self.page.autosettingSubcategory(u'Политика')
        self.assertEqual(self.page.getSubcategory(),
            u'Политика')

    def test_loginBtn(self):
        self.page.clickLogin()
        self.assertTrue(self.page.lofinFormIsVisible())

    def test_authorization(self):
        self.page.clickLogin()
        self.page.login()
        self.assertTrue(self.page.checkUrl())

    def test_tooBigQuestion(self):
        bigStr = u''
        for _ in range(122):
            bigStr = bigStr + u'a'
        self.page.setQuestionTheme(bigStr)
        self.assertEqual(self.page.getAlertUnderQuestion(),
            u'Поле «Тема вопроса» не может быть больше 120 символов.')