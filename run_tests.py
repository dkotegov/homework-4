# -*- coding: utf-8 -*-

import unittest
import os

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

class SendLetterTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      config.selectors['email'])))
        email.send_keys(LOGIN)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         config.selectors['password'])))
        password.send_keys(PASSWORD)
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
        self.assertIn('Письма', self.browser.title)

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testSendLetter(self):
        self.auth()
        self.openSendPage()
        self.fillAndSendMessage()
        self.checkIfSend()

class SearchItemTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(LOGIN)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(PASSWORD)
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

class CreateLabelTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(LOGIN)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(PASSWORD)
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

class OpenLetterTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(LOGIN)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(PASSWORD)
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

class LetterToSpamTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(LOGIN)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(PASSWORD)
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

class LogoutTestCase(unittest.TestCase):

    def auth(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          config.selectors['email'])))
        email.send_keys(LOGIN)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(PASSWORD)
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
        email.send_keys(LOGIN)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             config.selectors['password'])))
        password.send_keys(PASSWORD)
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
        self.assertIn(LOGIN, checkEmail.get_attribute('innerText'))

    def setUp(self):
        self.browser = config.useBrowser()
        self.addCleanup(self.browser.quit)
        self.browser.get(config.consts['loginPath'])

    def testCheckProfile(self):
        self.auth()
        self.openProfile()
        self.checkIfOpen()

if __name__ == '__main__':
    LOGIN = 'mark'
    PASSWORD = 'mark'
    BROWSER = 'Firefox'

    config = Config(BROWSER)

    unittest.main(verbosity=2)
