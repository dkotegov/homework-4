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

    def can_press_esc(self):
        try:
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            return True
        except:
            return False

class AskPage(Page):
    QUESTION_TEXT = 'question_text'
    QUESTION_ADDITIONAL = 'question_additional'
    ALERT_ADDITIONAL = 'z1LfJpugzE39YVXERE-f__0'

    LOGIN_INPUT = 'Login'
    LOGIN_BUTTON = 'PH_authLink'
    LOGIN_FORM_FRAME = 'ag-popup__frame__layout__iframe'
    PROFILE_BUTTON = 'profile-menu-item_hoverable'
    PROFILE_FORM = 'v--modal-overlay'

    POP_UP_ALERT = '_3e48lyZw6JxqpxlQCH7ZrK_0'

    CATEGORY = '_3oJIbRjOJJ6UfBtvy3o6EW_1'
    CATEGORY_ANOTHER = '_3BV4a0WZevpbLq-ArsDomg_0'

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
    
    def clickLogin(self):
        clickBtn = self.driver.find_element_by_id(self.LOGIN_BUTTON)
        clickBtn.click()

    def sameUrl(self, url):
        if (url in self.driver.current_url):
            return True
        return False

    def login(self):
        self.driver.switch_to_default_content
        WebDriverWait(self.driver, 5).until( \
            EC.frame_to_be_available_and_switch_to_it( \
                (By.CLASS_NAME, self.LOGIN_FORM_FRAME)))
        self.driver.find_elements_by_css_selector('*')[0].get_attribute('innerHTML')

        inputUsername = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.NAME, self.LOGIN_INPUT)))
        inputUsername.send_keys(self.username)

        self.driver.find_element_by_xpath("//button[@data-test-id='next-button']").click()

        inputPassword = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.NAME, 'Password')))
        inputPassword.send_keys(self.password)
        
        self.driver.find_element_by_xpath("//button[@data-test-id='submit-button']").click()

    def clickAndWaitProfile(self):
        buttonEdit = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, \
                self.PROFILE_BUTTON)))[7]
        buttonEdit.click()

        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, \
                    self.PROFILE_FORM)))
            return True
        except:
            return False

    def isAlert(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, \
                    self.POP_UP_ALERT)))
            return False
        except:
            return True

    def clickChooseAnother(self):
        buttonChoose = self.waitForElementVisible((By.CLASS_NAME, self.CATEGORY))
        buttonChoose.click()

        buttonChooseAnother = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, \
                self.CATEGORY_ANOTHER)))
        buttonChooseAnother[-1].click()

    def clickSendQuestion(self):
        buttonSend = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, \
                '_3ykLdYEqVa47ACQrpqnZOj_0')))
        buttonSend.click()

    def autosettingSubcategory(self, Subcategory):
        WebDriverWait(self.driver, 10).until(ElementEqualSubcategory( \
            '_1lZeUpFslQAPq_G1uwjahr_1', u'Политика'))

    def clearQuestionThemeByKeys(self):
        inputQuestionField = self.driver.find_element_by_name(self.QUESTION_TEXT)
        inputQuestionField.click()
        inputQuestionField.send_keys(Keys.CONTROL + "a")
        inputQuestionField.send_keys(Keys.DELETE)

    def getSubcategory(self):
        subcategory = self.driver.find_elements_by_class_name('_1lZeUpFslQAPq_G1uwjahr_1')[1] \
            .find_elements_by_css_selector('*')
        return subcategory[-1].get_attribute('innerHTML')

    def lofinFormIsVisible(self):
        loginFormList = self.driver.find_elements_by_class_name('ag-popup__frame_show')
        if len(loginFormList) <= 0:
            return False
        return True

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

        try:
            WebDriverWait(self.driver, 10, 0.1).until(
                lambda d: d.find_element_by_class_name('page-settings')
            )
            return True
        except:
            return False

    def make_default_question(self):
        ask_button = WebDriverWait(self.driver, 10, 0.1).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "_3ykLdYEqVa47ACQrpqnZOj_0"))
        )
        ask_button.click()

    def can_edit_time(self):
        try:
            WebDriverWait(self.driver, 10, 0.1).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "q-edit-control"))
            )
            return True
        except:
            return False

    def check_poll_option_correct_add(self):

        variant_3 = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath('//div[@name="poll_options"]/div[4]/label/div[2]/div/div/div/input')
        )
        variant_3.click()
        variant_3.send_keys("getting 4 option")
        
        variant_4 = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath('//div[@name="poll_options"]/div[5]/label/div[2]/div/div/div/input')
        )

        variant_4.click()
        variant_4.send_keys("getting 5 option")

        try:
            self.driver.find_element_by_xpath('//div[@name="poll_options"]/div[6]/label/div[2]/div/div/div/input')
            return True
        except:
            return False

    def open_poll_form(self):
        poll_form = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_class_name('_3LtjwRRK3wqD0IfUUl1sxB_0')
        )
        poll_form.click()
