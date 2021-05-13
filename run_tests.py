# -*- coding: utf-8 -*-

import unittest
import argparse
import sys

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from config import Config


class EmailEmptyTestCase(unittest.TestCase):

    def loginWithEmptyEmail(self):
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      config.selectors['enter'])))
        enter.click()
        self.assertIn('Войти', self.browser.title)

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testEmailEmpty(self):
        self.loginWithEmptyEmail()


class PasswordEmptyTestCase(unittest.TestCase):

    def loginWithEmptyPassword(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,  config.selectors['email'])))
        email.send_keys('name')
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      config.selectors['enter'])))
        enter.click()
        self.assertIn('Войти', self.browser.title)

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testPasswordEmpty(self):
        self.loginWithEmptyPassword()

class EmailMistakeTestCase(unittest.TestCase):

    def fillWrongUsername(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      config.selectors['email'])))
        email.send_keys('name')
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         config.selectors['password'])))
        password.send_keys('pass')
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      config.selectors['enter'])))
        enter.click()

    def checkErrorMessage(self):
        error = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'p#emailError')))
        self.assertIn('Do not find this user in db', error.get_attribute('innerText'))

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testEmailMistake(self):
       self.fillWrongUsername()
       self.checkErrorMessage()

class SuccessLoginTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      config.selectors['enter'])))
        enter.click()

    def checkLogin(self):
        header = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['header'])))
        self.assertIn('Письма', header.get_attribute('innerText'))

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testSuccessLogin(self):
        self.auth()
        self.checkLogin()

class SendLetterTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      config.selectors['enter'])))
        enter.click()

    def openSendPage(self):
        sendPage = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['send_page'])))
        sendPage.click()

    def fillAndSendMessage(self):
        to = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, config.selectors['to'])))
        to.send_keys('mark@mailer.ru.com')
        theme = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, config.selectors['theme'])))
        theme.send_keys('Тема')
        message = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, config.selectors['message'])))
        message.send_keys('Сообщение')

        button = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, config.selectors['button'])))
        button.click()

    def checkIfSend(self):
        if config.browser == 'Firefox':
            self.assertIn('Письма', self.browser.title)
        if config.browser == 'Chrome':
            self.assertIn('Отправить письмо', self.browser.title)

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testSendLetter(self):
        self.auth()
        self.openSendPage()
        self.fillAndSendMessage()
        self.checkIfSend()

class SendLetterWrongEmailTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      config.selectors['enter'])))
        enter.click()

    def openSendPage(self):
        sendPage = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['send_page'])))
        sendPage.click()

    def fillAndSendMessage(self):
        to = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, config.selectors['to'])))
        to.send_keys('1212121212')
        theme = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, config.selectors['theme'])))
        theme.send_keys('Тема')
        message = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, config.selectors['message'])))
        message.send_keys('Сообщение')

        button = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, config.selectors['button'])))
        button.click()

    def checkIfNotSend(self):
        titlePage = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, config.selectors['titlePage'])))
        self.assertIn('Написать', titlePage.get_attribute('innerText'))

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testSendLetterWrongEmail(self):
        self.auth()
        self.openSendPage()
        self.fillAndSendMessage()
        self.checkIfNotSend()

class SendLetterBigThemeTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      config.selectors['enter'])))
        enter.click()

    def openSendPage(self):
        sendPage = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['send_page'])))
        sendPage.click()

    def fillAndSendMessage(self):
        to = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, config.selectors['to'])))
        to.send_keys('mark@mailer.ru.com')
        theme = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, config.selectors['theme'])))
        theme.send_keys('Темаааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа')
        message = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, config.selectors['message'])))
        message.send_keys('Сообщение')

        button = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, config.selectors['button'])))
        button.click()

    def checkIfSend(self):
        if config.browser == 'Firefox':
            self.assertIn('Письма', self.browser.title)
        if config.browser == 'Chrome':
            self.assertIn('Отправить письмо', self.browser.title)

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testSendLetterBigTheme(self):
        self.auth()
        self.openSendPage()
        self.fillAndSendMessage()
        self.checkIfSend()

class SendLetterBigTextTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      config.selectors['enter'])))
        enter.click()

    def openSendPage(self):
        sendPage = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['send_page'])))
        sendPage.click()

    def fillAndSendMessage(self):
        to = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, config.selectors['to'])))
        to.send_keys('mark@mailer.ru.com')
        theme = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, config.selectors['theme'])))
        theme.send_keys('Тема')
        message = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, config.selectors['message'])))
        message.send_keys('Сообщение\nСообщение\nСообщение\nСообщение\nСообщение')

        button = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, config.selectors['button'])))
        button.click()

    def checkIfSend(self):
        if config.browser == 'Firefox':
            self.assertIn('Письма', self.browser.title)
        if config.browser == 'Chrome':
            self.assertIn('Отправить письмо', self.browser.title)

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testSendLetterBigText(self):
        self.auth()
        self.openSendPage()
        self.fillAndSendMessage()
        self.checkIfSend()

class OpenLetterTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['enter'])))
        enter.click()

    def openLetter(self):
        letter = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['letter'])))
        letter.click()

    def checkIfNotRead(self):
        notReadButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['not_read_button'])))
        self.assertIn('Не прочитать', notReadButton.get_attribute('innerText'))

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testOpenLetter(self):
        self.auth()
        self.openLetter()
        self.checkIfNotRead()

class ModalCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['enter'])))
        enter.click()

    def openLetter(self):
        letter = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['letter'])))
        letter.click()

    def checkIfOpen(self):
        notReadButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['not_read_button'])))
        self.assertIn('Не прочитать', notReadButton.get_attribute('innerText'))

    def checkIfModal(self):
        addButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['add_button'])))
        addButton.click()
        submitButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['submit_button'])))
        self.assertIn('ДОБАВИТЬ', submitButton.get_attribute('innerText'))

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testModal(self):
        self.auth()
        self.openLetter()
        self.checkIfOpen()
        self.checkIfModal()

class CloseModalCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['enter'])))
        enter.click()

    def openLetter(self):
        letter = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['letter'])))
        letter.click()

    def checkIfOpen(self):
        notReadButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['not_read_button'])))
        self.assertIn('Не прочитать', notReadButton.get_attribute('innerText'))

    def closeModal(self):
        addButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['add_button'])))
        addButton.click()
        submitButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['submit_button'])))
        self.assertIn('ДОБАВИТЬ', submitButton.get_attribute('innerText'))
        crossButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['cross'])))
        crossButton.click()

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testCloseModal(self):
        self.auth()
        self.openLetter()
        self.checkIfOpen()
        self.closeModal()

class LetterToSpamTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['enter'])))
        enter.click()

    def openLetter(self):
        letter = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['letter'])))
        letter.click()

    def checkIfNotRead(self):
        notReadButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['not_read_button'])))
        self.assertIn('Не прочитать', notReadButton.get_attribute('innerText'))

    def toSpam(self):
        addButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['add_button'])))
        addButton.click()

        submitButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['submit_button'])))
        submitButton.click()

    def checkIfSpam(self):
        emptyLetter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['empty_letter'])))
        self.assertIn('', emptyLetter.get_attribute('innerText'))

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testLetterToSpam(self):
        self.auth()
        self.openLetter()
        self.checkIfNotRead()
        self.toSpam()
        self.checkIfSpam()

class LetterFromSpamTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['enter'])))
        enter.click()

    def toSpamSection(self):
        spam = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['spamUn'])))
        spam.click()
        _ = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['letter'])))

    def openLetter(self):
        letter = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['letter'])))
        letter.click()

    def checkIfNotRead(self):
        notReadButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['not_read_button'])))
        self.assertIn('Не прочитать', notReadButton.get_attribute('innerText'))

    def fromSpam(self):
        addButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['add_button'])))
        addButton.click()

        submitButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['submit_button'])))
        submitButton.click()

    def checkIfNotSpam(self):
        emptyLetter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['empty_letter'])))
        self.assertIn('', emptyLetter.get_attribute('innerText'))

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testLetterFromSpam(self):
        self.auth()
        self.toSpamSection()
        self.openLetter()
        self.checkIfNotRead()
        self.fromSpam()
        self.checkIfNotSpam()

class DeleteLetterFromSpamTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['enter'])))
        enter.click()

    def toSpamSection(self):
        spam = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['spamUn'])))
        spam.click()
        _ = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['letter'])))

    def openLetter(self):
        letter = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['letter'])))
        letter.click()

    def checkIfNotRead(self):
        notReadButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['not_read_button'])))
        self.assertIn('Не прочитать', notReadButton.get_attribute('innerText'))

    def deleteLetter(self):
        buttonRemove = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['button_remove'])))
        buttonRemove.click()

    def checkIfDeleteLetter(self):
        emptyLetter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['empty_letter'])))
        self.assertIn('', emptyLetter.get_attribute('innerText'))

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testDeleteLetterFromSpam(self):
        self.auth()
        self.toSpamSection()
        self.openLetter()
        self.checkIfNotRead()
        self.deleteLetter()
        self.checkIfDeleteLetter()

class SearchItemTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['enter'])))
        enter.click()

    def doSearch(self):
        search = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['search_input'])))
        search.send_keys('s')

    def checkResultOfSearch(self):
        result = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['search_list'])))
        self.assertIn('Отправители', result.get_attribute('innerText'))

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testSearchItem(self):
        self.auth()
        self.doSearch()
        self.checkResultOfSearch()

class SearchNotFoundTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['enter'])))
        enter.click()

    def doSearch(self):
        search = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['search_input'])))
        search.send_keys('4343')

    def checkNotFound(self):
        result = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['not_found'])))
        self.assertIn('Нет результатов', result.get_attribute('innerText'))

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testSearchNotFound(self):
        self.auth()
        self.doSearch()
        self.checkNotFound()

class OpenModalLabelTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['enter'])))
        enter.click()

    def createLabel(self):
        plus = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['plus'])))
        plus.click()
        _ = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['label_field'])))

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testOpenModalLabel(self):
        self.auth()
        self.createLabel()

class CloseModalLabelTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['enter'])))
        enter.click()

    def openModal(self):
        plus = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['plus'])))
        plus.click()
        _ = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['label_field'])))

    def closeModal(self):
        cross = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['cross_modal'])))
        cross.click()

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testCloseModalLabel(self):
        self.auth()
        self.openModal()
        self.closeModal()

class CreateLabelTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['enter'])))
        enter.click()

    def createLabel(self):
        plus = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['plus'])))
        plus.click()
        labelField = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['label_field'])))
        labelField.send_keys(self.nameOfLabel)
        labelButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['label_button'])))
        labelButton.click()

    def checkIfCreated(self):
        createdLabel = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input.folder-names' + '#' + self.nameOfLabel)))
        self.assertIn(self.nameOfLabel, createdLabel.get_attribute('value'))

    def setUp(self):
        self.nameOfLabel = 'щуопшукопщшуокшщпоущшкопщушпощуопшщукоп'
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testCreateLabel(self):
        self.auth()
        self.createLabel()
        self.checkIfCreated()

class LogoutTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['enter'])))
        enter.click()

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def logout(self):
        logout = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['logout'])))
        logout.click()

    def checkIfLogout(self):
        self.assertIn('Войти', self.browser.title)

    def testLogout(self):
        self.auth()
        self.logout()
        self.checkIfLogout()

class CheckProfileTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['enter'])))
        enter.click()

    def openProfile(self):
        profile = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['open_profile'])))
        profile.click()
        self.assertIn('Профиль', self.browser.title)

    def checkIfOpen(self):
        checkEmail = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['check_email'])))
        self.assertIn(config.login, checkEmail.get_attribute('innerText'))

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testCheckProfile(self):
        self.auth()
        self.openProfile()
        self.checkIfOpen()

class ChangeNameProfileTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['enter'])))
        enter.click()

    def openProfile(self):
        profile = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['open_profile'])))
        profile.click()
        self.assertIn('Профиль', self.browser.title)

    def checkIfOpen(self):
        checkEmail = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['check_email'])))
        self.assertIn(config.login, checkEmail.get_attribute('innerText'))

    def changeName(self):
        editButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['edit_button'])))
        editButton.click()
        name = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['name_input'])))
        name.send_keys(config.login + config.login)
        submit = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['submit_edit'])))
        submit.click()

    def checkIfChange(self):
        name = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['check_email'])))
        self.assertIn(config.login + config.login, name.get_attribute('innerText'))

    def cancelChanges(self):
        letter = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['header'])))
        letter.click()
        self.openProfile()
        editButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['edit_button'])))
        editButton.click()
        name = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['name_input'])))
        name.send_keys(config.login)
        submit = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['submit_edit'])))
        submit.click()

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testChangeNameProfile(self):
        self.auth()
        self.openProfile()
        self.checkIfOpen()
        self.changeName()
        self.checkIfChange()
        self.cancelChanges()

class ChangeSurnameProfileTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(config.login)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(config.password)
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['enter'])))
        enter.click()

    def openProfile(self):
        profile = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['open_profile'])))
        profile.click()
        self.assertIn('Профиль', self.browser.title)

    def checkIfOpen(self):
        checkEmail = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['check_email'])))
        self.assertIn(config.login, checkEmail.get_attribute('innerText'))

    def changeName(self):
        editButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['edit_button'])))
        editButton.click()
        name = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['surname_input'])))
        name.send_keys(config.login + config.login)
        submit = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['submit_edit'])))
        submit.click()

    def checkIfChange(self):
        name = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['surname_check'])))
        self.assertIn(config.login + config.login, name.get_attribute('innerText'))

    def cancelChanges(self):
        letter = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['header'])))
        letter.click()
        self.openProfile()
        editButton = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['edit_button'])))
        editButton.click()
        name = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['surname_input'])))
        name.send_keys(config.login)
        submit = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['submit_edit'])))
        submit.click()

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testChangeSurnameProfile(self):
        self.auth()
        self.openProfile()
        self.checkIfOpen()
        self.changeName()
        self.checkIfChange()
        self.cancelChanges()

class ErrorSignUpTestCase(unittest.TestCase):

    def openSignUp(self):
        signUpButton = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['signup'])))
        signUpButton.click()
        signUp = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['titlePage'])))
        self.assertIn('Регистрация', signUp.get_attribute('innerText'))

    def fillProfile(self):
        email = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['email'])))
        email.send_keys('33')
        password1 = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['password1'])))
        password1.send_keys('33')
        password2 = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['password2'])))
        password2.send_keys('33')
        name = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['name'])))
        name.send_keys('33')
        surname = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['surname'])))
        surname.send_keys('33')
        button = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['singup_button'])))
        button.click()

    def checkIfError(self):
        error = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, config.selectors['error_singup'])))
        self.assertIn('слишком короткий пароль', error.get_attribute('innerText'))

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testErrorSignUp(self):
        self.openSignUp()
        self.fillProfile()
        self.checkIfError()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str)
    parser.add_argument('--password', type=str)
    parser.add_argument('--browser', type=str)
    parser.add_argument('unittest_args', nargs='*')
    args = parser.parse_args()
    if len(args) != 3:
        print("Передайте первым аргументом email, вторым пароль, третьим браузер")
        sys.exit(1)

    sys.argv[1:] = args.unittest_args

    config = Config(args[0], args[1], args[2])
    unittest.main(verbosity=2)




