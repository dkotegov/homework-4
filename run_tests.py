# -*- coding: utf-8 -*-

import unittest
import os

from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class EmailEmptyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/home/mark/.wdm/drivers/geckodriver/linux64/v0.29.1/geckodriver')
        self.addCleanup(self.browser.quit)
        self.browser.get('https://mailer.ru.com/signin')

    def testEmailEmpty(self):
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > section > div > div > section > div > form > fieldset > div.row > div.column.large-4 > button')))
        enter.click()
        self.assertIn('Войти', self.browser.title)

class PasswordEmptyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/home/mark/.wdm/drivers/geckodriver/linux64/v0.29.1/geckodriver')
        self.addCleanup(self.browser.quit)
        self.browser.get('https://mailer.ru.com/signin')

    def testPasswordEmpty(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > section > div > div > section > div > form > fieldset > div:nth-child(1) > input:nth-child(1)')))
        email.send_keys('name')
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div.row > div.column.large-4 > button')))
        enter.click()
        self.assertIn('Войти', self.browser.title)

class EmailMistakeTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(
            executable_path='/home/mark/.wdm/drivers/geckodriver/linux64/v0.29.1/geckodriver')
        self.addCleanup(self.browser.quit)
        self.browser.get('https://mailer.ru.com/signin')

    def testEmailMistake(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div:nth-child(1) > input:nth-child(1)')))
        email.send_keys('name')
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         'body > section > div > div > section > div > form > fieldset > div:nth-child(2) > input')))
        password.send_keys('pass')
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div.row > div.column.large-4 > button')))
        enter.click()

        error = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'p#emailError')))
        self.assertIn('Do not find this user in db', error.get_attribute('innerText'))


class SendLetterTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/home/mark/.wdm/drivers/geckodriver/linux64/v0.29.1/geckodriver')
        self.addCleanup(self.browser.quit)
        self.browser.get('https://mailer.ru.com/signin')
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div:nth-child(1) > input:nth-child(1)')))
        email.send_keys('mark')
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         'body > section > div > div > section > div > form > fieldset > div:nth-child(2) > input')))
        password.send_keys('mark')
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div.row > div.column.large-4 > button')))
        enter.click()

    def testSendLetter(self):
        sendPage = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > header > div > nav > ul > li:nth-child(2) > a')))
        sendPage.click()

        to = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > section > div > div > div > form > div:nth-child(1) > input')))
        to.send_keys('mark@mailer.ru.com')
        theme = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > section > div > div > div > form > div:nth-child(2) > input')))
        theme.send_keys('Тема')
        message = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > section > div > div > div > form > div.message.form-field > textarea')))
        message.send_keys('Сообщение')

        button = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > section > div > div > div > form > div.row > div:nth-child(1) > button')))
        button.click()
        self.assertIn('Письма', self.browser.title)


class SearchItemTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/home/mark/.wdm/drivers/geckodriver/linux64/v0.29.1/geckodriver')
        self.addCleanup(self.browser.quit)
        self.browser.get('https://mailer.ru.com/signin')
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div:nth-child(1) > input:nth-child(1)')))
        email.send_keys('mark')
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         'body > section > div > div > section > div > form > fieldset > div:nth-child(2) > input')))
        password.send_keys('mark')
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div.row > div.column.large-4 > button')))
        enter.click()

    def testSearchItem(self):
        search = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#search-input')))
        search.send_keys('s')

        result = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#search-result-list > span')))
        self.assertIn('Отправители', result.get_attribute('innerText'))


class CreateLabelTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/home/mark/.wdm/drivers/geckodriver/linux64/v0.29.1/geckodriver')
        self.addCleanup(self.browser.quit)
        self.browser.get('https://mailer.ru.com/signin')
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div:nth-child(1) > input:nth-child(1)')))
        email.send_keys('mark')
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         'body > section > div > div > section > div > form > fieldset > div:nth-child(2) > input')))
        password.send_keys('mark')
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div.row > div.column.large-4 > button')))
        enter.click()

    def testCreateLabel(self):
        nameOfLabel = 'папкапапкапапка'

        plus = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#add-folder-recived')))
        plus.click()

        labelField = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div:nth-child(3) > form > div > input')))
        labelField.send_keys(nameOfLabel)
        labelButton = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div:nth-child(3) > form > div > button')))
        labelButton.click()

        createdLabel = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.folder-names' + '#' + nameOfLabel)))
        self.assertIn(nameOfLabel, createdLabel.get_attribute('value'))


class OpenLetterTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/home/mark/.wdm/drivers/geckodriver/linux64/v0.29.1/geckodriver')
        self.addCleanup(self.browser.quit)
        self.browser.get('https://mailer.ru.com/signin')
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div:nth-child(1) > input:nth-child(1)')))
        email.send_keys('mark')
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         'body > section > div > div > section > div > form > fieldset > div:nth-child(2) > input')))
        password.send_keys('mark')
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div.row > div.column.large-4 > button')))
        enter.click()

    def testOpenLetter(self):
        letter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'article.brick.entry.format-standard')))
        letter.click()

        notReadButton = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.not-read-button')))
        self.assertIn('Не прочитать', notReadButton.get_attribute('innerText'))


class LetterToSpamTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/home/mark/.wdm/drivers/geckodriver/linux64/v0.29.1/geckodriver')
        self.addCleanup(self.browser.quit)
        self.browser.get('https://mailer.ru.com/signin')
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div:nth-child(1) > input:nth-child(1)')))
        email.send_keys('mark')
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         'body > section > div > div > section > div > form > fieldset > div:nth-child(2) > input')))
        password.send_keys('mark')
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div.row > div.column.large-4 > button')))
        enter.click()

    def testLetterToSpam(self):
        letter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'article.brick.entry.format-standard')))
        letter.click()

        notReadButton = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.not-read-button')))
        self.assertIn('Не прочитать', notReadButton.get_attribute('innerText'))

        addButton = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#button-form-add-letter-folder')))
        addButton.click()

        submitButton = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#choose-folder > div:nth-child(2) > button')))
        submitButton.click()

        emptyLetter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.main-columns.project_scroll')))
        self.assertIn('', emptyLetter.get_attribute('innerText'))


class LogoutTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/home/mark/.wdm/drivers/geckodriver/linux64/v0.29.1/geckodriver')
        self.addCleanup(self.browser.quit)
        self.browser.get('https://mailer.ru.com/signin')
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div:nth-child(1) > input:nth-child(1)')))
        email.send_keys('mark')
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         'body > section > div > div > section > div > form > fieldset > div:nth-child(2) > input')))
        password.send_keys('mark')
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div.row > div.column.large-4 > button')))
        enter.click()

    def testLogout(self):
        logout = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > header > div > nav > ul > li:nth-child(4) > a')))
        logout.click()

        self.assertIn('Войти', self.browser.title)


class CheckProfileTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/home/mark/.wdm/drivers/geckodriver/linux64/v0.29.1/geckodriver')
        self.addCleanup(self.browser.quit)
        self.browser.get('https://mailer.ru.com/signin')
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div:nth-child(1) > input:nth-child(1)')))
        email.send_keys('mark')
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         'body > section > div > div > section > div > form > fieldset > div:nth-child(2) > input')))
        password.send_keys('mark')
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                      'body > section > div > div > section > div > form > fieldset > div.row > div.column.large-4 > button')))
        enter.click()

    def testCheckProfile(self):
        profile = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > header > div > nav > ul > li:nth-child(3) > a')))
        profile.click()
        self.assertIn('Профиль', self.browser.title)

        checkEmail = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.form-field > p')))
        self.assertIn('mark', checkEmail.get_attribute('innerText'))

if __name__ == '__main__':
    unittest.main(verbosity=2)
