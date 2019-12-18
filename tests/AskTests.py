# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities, Remote

import os
import time
import unittest

from tests.AskPage import AskPage

class AskTests(unittest.TestCase):
    DEBUG = False

    def __init__(self, *args, **kwargs):
        super(AskTests, self).__init__(*args, **kwargs)

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    # def test_needThreeWords(self):
    #     self.page = AskPage(self.driver)
    #     self.page.open()
        
    #     self.page.clickLogin()
    #     self.page.login()
    #     self.page.setQuestionTheme('hello, world!')
    #     self.page.clickChooseAnother()
    #     self.page.clickSendQuestion()
    #     self.page.checkAlert()

    # def test_profile(self):
    #     self.page = AskPage(self.driver)
    #     self.page.open()

    #     self.page.clickLogin()
    #     self.page.login()
    #     self.page.clickAndWaitProfile()

    def test_notEmptyQuestion(self):
        self.page = AskPage(self.driver)
        self.page.open()

        shortQuestion = u'Why, man?'
        self.page.setQuestionTheme(shortQuestion)
        self.page.clearQuestionThemeByKeys()
        self.assertEqual(self.page.getAlertUnderQuestion(),
            u'Поле «Тема вопроса» обязательно для заполнения.')

    # def test_mentionCountry(self):
    #     self.page = AskPage(self.driver)
    #     self.page.open()

    #     questionWithCountry = u'Россия'
    #     self.page.setQuestionTheme(questionWithCountry)
    #     self.page.autosettingSubcategory(u'Политика')
    #     self.assertEqual(self.page.getSubcategory(),
    #         u'Политика')

    # def test_loginBtn(self):
    #     self.page = AskPage(self.driver)
    #     self.page.open()

    #     self.page.clickLogin()
    #     self.assertTrue(self.page.lofinFormIsVisible())

    # def test_authorization(self):
    #     self.page = AskPage(self.driver)
    #     self.page.open()

    #     self.page.clickLogin()
    #     self.page.login()
    #     self.assertTrue(self.page.checkUrl())

    def test_tooBigQuestion(self):
        self.page = AskPage(self.driver)
        self.page.open()
        
        bigStr = u''
        for _ in range(122):
            bigStr = bigStr + u'a'
        self.page.setQuestionTheme(bigStr)
        self.assertEqual(self.page.getAlertUnderQuestion(),
            u'Поле «Тема вопроса» не может быть больше 120 символов.')

    # def test_photoVideoUploadTest(self):
    #     self.page = AskPage(self.driver)
    #     self.page.open()

    #     self.page.open_photo_upload_form()
    #     self.page.press_esc()

    #     self.page.open_video_upload_form()
    #     self.page.press_esc()

    #     if self.DEBUG:
    #         print('Photo/video upload test:.............PASSED\n')

    # def test_notValidTheme(self):
    #     self.page = AskPage(self.driver)
    #     self.page.open()
        
    #     self.page.clickLogin()
    #     self.page.login()
    #     self.page.setQuestionTheme(u'ыв ыва ыва 23')
    #     self.page.clickChooseAnother()
    #     self.page.clickSendQuestion()
    #     self.page.checkAlert()

    def test_tooBigQuestionBody(self):
        self.page = AskPage(self.driver)
        self.page.open()
        
        bigStr = u''
        for _ in range(3900):
            bigStr = bigStr + u'a'

        self.page.setQuestionAdditional(bigStr)
        self.assertEqual(self.page.getAlertUnderAdditional(),
            u'Поле «Текст вопроса» не может быть больше 3800 символов.')

    # def test_newQuestionEditTest(self):
    #     self.page = AskPage(self.driver)
    #     self.page.open()

    #     self.page.clickLogin()
    #     self.page.login()

    #     self.page.make_default_question()
    #     if self.DEBUG:
    #         print("make default question:........OK")

    #     self.page.check_edit_time()
    #     if self.DEBUG:
    #         print("check ediе time:..............OK")
    #         print("Question edit case test:.............PASSED\n")

    # def test_settingsTest(self):
    #     self.page = AskPage(self.driver)
    #     self.page.open()

    #     self.page.clickLogin()
    #     self.page.login()

    #     self.page.check_settings_page()
    #     if self.DEBUG:
    #         print("Login input:..................OK")
    #         print("Open settings:................OK")
    #         print("Settings open test:..................PASSED\n")

    # def test_pollOptionsTest(self):
    #     self.page = AskPage(self.driver)
    #     self.page.open()

    #     self.page.open_poll_form()
    #     if self.DEBUG:
    #         print("Poll page open:...............OK")

    #     self.page.check_poll_option_correct_add()
    #     if self.DEBUG:
    #         print("Settings open test:..................PASSED\n")