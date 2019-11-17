# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities, Remote

import os
import unittest

from tests.AskPage import AskPage

class AskTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(AskTests, self).__init__(*args, **kwargs)

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.page.quitDriver()

    def test_needThreeWords(self):
        self.page = AskPage(self.driver)
        self.page.open()
        
        self.page.clickLogin()
        self.page.login()
        self.page.setQuestionTheme('hello, world!')
        self.page.clickChooseAutosport()
        self.page.clickSendQuestion()
        self.page.checkAlert()

    def test_profile(self):
        self.page = AskPage(self.driver)
        self.page.open()

        self.page.clickLogin()
        self.page.login()
        self.page.clickAndWaitProfile()

    def test_notEmptyQuestion(self):
        self.page = AskPage(self.driver)
        self.page.open()

        shortQuestion = u'Why, man?'
        self.page.setQuestionTheme(shortQuestion)
        self.page.clearQuestionThemeByKeys()
        self.assertEqual(self.page.getAlertUnderQuestion(),
            u'Поле «Тема вопроса» обязательно для заполнения.')

    def test_mentionCountry(self):
        self.page = AskPage(self.driver)
        self.page.open()

        questionWithCountry = u'Россия'
        self.page.setQuestionTheme(questionWithCountry)
        self.page.autosettingSubcategory(u'Политика')
        self.assertEqual(self.page.getSubcategory(),
            u'Политика')

    def test_loginBtn(self):
        self.page = AskPage(self.driver)
        self.page.open()

        self.page.clickLogin()
        self.assertTrue(self.page.lofinFormIsVisible())

    def test_authorization(self):
        self.page = AskPage(self.driver)
        self.page.open()

        self.page.clickLogin()
        self.page.login()
        self.assertTrue(self.page.checkUrl())

    def test_tooBigQuestion(self):
        self.page = AskPage(self.driver)
        self.page.open()
        
        bigStr = u''
        for _ in range(122):
            bigStr = bigStr + u'a'
        self.page.setQuestionTheme(bigStr)
        self.assertEqual(self.page.getAlertUnderQuestion(),
            u'Поле «Тема вопроса» не может быть больше 120 символов.')