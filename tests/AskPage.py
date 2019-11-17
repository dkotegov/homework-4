# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support import expected_conditions as EC

import os
import unittest

from tests.CustomWait import ElementEqualSubcategory

class Page(object):
    BASE_URL = 'https://otvet.mail.ru/ask/'

    def __init__(self, driver):
        self.driver = driver
        self.username = 'test_qwerty1122@mail.ru'
        self.password = os.getenv('PASSWORD')

    def open(self):
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()

class AskPage(Page):
    def quitDriver(self):
        self.driver.quit()

    def setQuestionTheme(self, question):
        inputQuestionField = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.NAME, 'question_text')))
        inputQuestionField.click()
        inputQuestionField.send_keys(question)

    def autosettingSubcategory(self, Subcategory):
        WebDriverWait(self.driver, 10).until(ElementEqualSubcategory( \
            '_1lZeUpFslQAPq_G1uwjahr_1', u'Политика'))

    def clearQuestionThemeByKeys(self):
        inputQuestionField = self.driver.find_element_by_name('question_text')
        inputQuestionField.click()
        inputQuestionField.send_keys(Keys.CONTROL + "a")
        inputQuestionField.send_keys(Keys.DELETE)

    def getAlertUnderQuestion(self):
        alert = self.driver.find_element_by_class_name('z1LfJpugzE39YVXERE-f__0')
        return alert.get_attribute('innerHTML')
       
    def getSubcategory(self):
        subcategory = self.driver.find_elements_by_class_name('_1lZeUpFslQAPq_G1uwjahr_1')[1] \
            .find_elements_by_css_selector('*')
        return subcategory[-1].get_attribute('innerHTML')

    def clickLogin(self):
        clickBtn = self.driver.find_element_by_id('PH_authLink')
        clickBtn.click()

    def lofinFormIsVisible(self):
        loginFormList = self.driver.find_elements_by_class_name('ag-popup__frame_show')
        if len(loginFormList) <= 0:
            return False
        return True

    def login(self):
        self.driver.switch_to_default_content
        WebDriverWait(self.driver, 5).until( \
            EC.frame_to_be_available_and_switch_to_it( \
                (By.CLASS_NAME, 'ag-popup__frame__layout__iframe')))
        inputUsername = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.NAME, 'Login')))
        inputUsername.send_keys(self.username)

        self.driver.find_elements_by_class_name('login-row')[2].find_elements_by_css_selector('*')[5].click()

        inputPassword = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.NAME, 'Password')))
        inputPassword.send_keys(self.password)
        
        self.driver.find_elements_by_class_name('login-row')[2].find_elements_by_css_selector('*')[1].click()

    def checkUrl(self):
        if ("https://otvet.mail.ru" in self.driver.current_url):
            return True
        return False

    def clickAndWaitProfile(self):
        buttonEdit = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, \
                'profile-menu-item_hoverable')))[7]
        buttonEdit.click()

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, \
                'v--modal-overlay')))

    def clickSendQuestion(self):
        buttonSend = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, \
                '_3ykLdYEqVa47ACQrpqnZOj_0')))
        buttonSend.click()

    def clickChooseAutosport(self):
        buttonChoose = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, \
                '_3oJIbRjOJJ6UfBtvy3o6EW_1')))

        buttonChoose[0].click()

        buttonChooseAnother = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, \
                '_3BV4a0WZevpbLq-ArsDomg_0')))
        buttonChooseAnother[-1].click()

    def checkAlert(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, \
                '_3e48lyZw6JxqpxlQCH7ZrK_0')))