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

    def press_esc(self):
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

class AskPage(Page):
    QUESTION_TEXT = 'question_text'
    QUESTION_ADDITIONAL = 'question_additional'
    LOGIN = 'login'
    ALERT_ADDITIONAL = 'z1LfJpugzE39YVXERE-f__0'

    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    def sendText(self, webElement, text):
        self.driver.execute_script("arguments[0].value = arguments[1]",
            webElement, text[:len(text)-1])
        webElement.send_keys(text[len(text)-1])

    def getAlertUnderAdditional(self):
        return self.waitForElementVisible((By.CLASS_NAME, self.ALERT_ADDITIONAL)) \
            .get_attribute('innerHTML')

    def setQuestionAdditional(self, additional):
        inputQuestionField = self.waitForElementVisible((By.NAME, self.QUESTION_ADDITIONAL))
        self.sendText(inputQuestionField, additional)

    def setQuestionTheme(self, question):
        inputQuestionField = self.waitForElementVisible((By.NAME, self.QUESTION_TEXT))
        self.sendText(inputQuestionField, question)





    def autosettingSubcategory(self, Subcategory):
        WebDriverWait(self.driver, 10).until(ElementEqualSubcategory( \
            '_1lZeUpFslQAPq_G1uwjahr_1', u'Политика'))

    def clearQuestionThemeByKeys(self):
        inputQuestionField = self.driver.find_element_by_name(self.QUESTION_TEXT)
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
        inputUsername = self.waitForElementVisible((By.NAME, self.LOGIN))
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

    def clickChooseAnother(self):
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

    def open_photo_upload_form(self):
        photo_span = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath('//span[text()="Фото"]')
        )
        photo_span.find_element_by_xpath('./..').click()

    def open_video_upload_form(self):
        video_span = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath('//span[text()="Видео"]')
        )
        video_span.find_element_by_xpath('./..').click()

    def check_settings_page(self):
        settings_button = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath('//span[text()="Настройки"]')
        )
        settings_button.click()
        WebDriverWait(self.driver, 10, 0.1).until(
            # lambda d: d.find_element_by_xpath('//button[@name="submit_btn"]').click()
            lambda d: d.find_element_by_class_name('page-settings')
        )

    def make_default_question(self):
        self.setQuestionTheme(u"Вопрос про салаты")
        self.setQuestionAdditional(u"Собственно говоря, если греческий салат испортился, то можно ли его называть древнегреческим?")

        ask_button = WebDriverWait(self.driver, 10, 0.1).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "_3ykLdYEqVa47ACQrpqnZOj_0"))
        )
        ask_button.click()

    def check_edit_time(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_class_name('q-edit-control')
        )

    def check_poll_option_correct_add(self):

        variant_3 = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath('//div[@name="poll_options"]/div[4]/label/div[2]/div/div/div/input')
        )
        variant_3.click()
        variant_3.send_keys("getting 4 option")
        
        variant_4 = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath('//div[@name="poll_options"]/div[5]/label/div[2]/div/div/div/input')
        )

        variant_4.click()
        variant_4.send_keys("getting 5 option")

        self.driver.find_element_by_xpath('//div[@name="poll_options"]/div[6]/label/div[2]/div/div/div/input')

    def open_poll_form(self):
        poll_form = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_class_name('_3LtjwRRK3wqD0IfUUl1sxB_0')
        )
        poll_form.click()
