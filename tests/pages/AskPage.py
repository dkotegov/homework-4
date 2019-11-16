from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import os

class AskPage(object):
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://otvet.mail.ru/ask')
        self.username = 'test_qwerty1122@mail.ru'
        self.password = os.getenv('PASSWORD')

    def quitDriver(self):
        self.driver.quit()

    def setQuestionTheme(self, question):
        inputQuestionField = self.driver.find_elements_by_name('question_text')[0]
        inputQuestionField.click()
        inputQuestionField.send_keys(question)

    def clearQuestionThemeByKeys(self):
        inputQuestionField = self.driver.find_elements_by_name('question_text')[0]
        inputQuestionField.click()
        inputQuestionField.send_keys(Keys.CONTROL + "a")
        inputQuestionField.send_keys(Keys.DELETE)

    def getAlertUnderQuestion(self):
        alert = self.driver.find_elements_by_class_name('z1LfJpugzE39YVXERE-f__0')[0]
        return alert.get_attribute('innerHTML')


