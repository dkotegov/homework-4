from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time
import unittest

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

    def wait(self, wait_until=None, timeout=5):
        if wait_until == None:
            WebDriverWait(self.driver, timeout)
        WebDriverWait(self.driver, timeout).until(wait_until).click()
       
    def getSubcategory(self):
        subcategory = self.driver.find_elements_by_class_name('_1lZeUpFslQAPq_G1uwjahr_1')[1] \
            .find_elements_by_css_selector('*')
        return subcategory[-1].get_attribute('innerHTML')

    def clickLogin(self):
        clickBtn = self.driver.find_elements_by_id('PH_authLink')[0]
        clickBtn.click()
        time.sleep(4)

    def lofinFormIsVisible(self):
        lofinFormList = self.driver.find_elements_by_class_name('ag-popup__frame_show')
        if len(lofinFormList) <= 0:
            return False
        return True


