# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support import expected_conditions as EC

import os
import unittest
import random

from tests.CustomWait import ElementEqualSubcategory

LOGIN_NEXT_BTN = "//button[@data-test-id='next-button']"
LOGIN_SUBMIT_BTN = "//button[@data-test-id='submit-button']"
LOGIN_FORM_LIST = "ag-popup__frame_show"
LOGIN_INPUT = 'Login'
LOGIN_BUTTON = 'PH_authLink'
LOGIN_FORM_FRAME = 'ag-popup__frame__layout__iframe'

UPLOAD_PHOTO_SPAN = '//span[text()="Фото"]'
UPLOAD_VIDEO_SPAN = '//span[text()="Видео"]'

SETTING_BUTTON = '//span[text()="Настройки"]'
SETTINGS_PAGE = 'page-settings'

# QUESTION_SUBMIT_BUTTON = "//a[@class='btn_3ykLdYEq']"
QUESTION_SUBMIT_BUTTON = "btn_3ykLdYEq"
QUESTION_UNDER_ALERT = "z1LfJpugzE39YVXERE-f__0"
QUESTION_SUBCOTEGORY = "select_1lZeUpFs_1"
QUESTION_EDIT_BTN = "q-edit-control-element"
QUESTION_TEXT = 'question_text'
QUESTION_ADDITIONAL = 'question_additional'

POLL_VARIANT_FIELD_3 = "//input[@placeholder='Вариант №3']"
POLL_VARIANT_FIELD_4 = "//input[@placeholder='Вариант №4']"
POLL_VARIANT_FIELD_5 = "//input[@placeholder='Вариант №5']"
POLL_FORM = 'menuItem__content_last_3LtjwRRK'

ALERT_ADDITIONAL = 'error_z1LfJpug'
POP_UP_ALERT = 'popup--content '
ALERT_WINDOW = 'window_3e48lyZw'

PROFILE_BUTTON = 'profile-menu-item_hoverable'
PROFILE_FORM = 'v--modal-overlay'

CATEGORY_DROP_DOWN_MENU = 'select_1lZeUpFs_1'
CATEGORY_ANOTHER = 'content__text_34Qv5DnE'
CATEGORY_MENU = 'default_1IJJ-JAn'

PASSWORD = 'Password'

IFRAME_LOGIN_DIV = 'ag-popup__frame_onoverlay'

PROFILE_MENU_SECTION = 'profileMenuColumn_1F5KVzKR'
PROFILE_EDIT_BUTTON = '//span[text()="Редактировать профиль"]'


class Page(object):
    BASE_URL = 'https://otvet.mail.ru/ask/'

    def __init__(self, driver):
        self.driver = driver
        # self.username = os.environ['USERNAME']
        # self.password = os.environ['PASSWORD']
        self.username = 'tp_qa_test5@mail.ru'
        self.password = 'SomePasswordHere'

    def open(self):
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()

    def can_press_esc(self):
        try:
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE) \
                .perform()
            return True
        except exceptions.ElementNotInteractableException:
            return False


class AskPage(Page):
    # Tools
    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    def sendText(self, webElement, text):
        self.driver.execute_script("arguments[0].value = arguments[1]",
                                   webElement, text[:len(text)-1])
        webElement.send_keys(text[len(text)-1])

    def sameUrl(self, url):
        if (url in self.driver.current_url):
            return True
        return False

    def getGetRandomTitle(self):
        firstWordDict = [
            u'Как',
            u'Где',
            u'Когда'
        ]
        secondWordDict = [
            u'Собрать',
            u'Починить',
            u'Построить',
            u'Приготовить',
            u'Испечь',
            u'Сделать',
            u'Смастерить',
            u'Запустить',
            u'Установить'
        ]
        thirdWordDict = [
            u'Дом',
            u'Пирог',
            u'Кухню',
            u'Лего',
            u'Салат',
            u'Пасту',
            u'Программу',
            u'Систему',
            u'Винду',
            u'Комнату',
            u'Будку',
            u'Конструктор',
            u'Полку'
        ]

        return firstWordDict[0] + ' ' +\
            secondWordDict[random.randint(0, len(secondWordDict)) - 1] + ' ' +\
            thirdWordDict[random.randint(0, len(thirdWordDict)) - 1] + '?'

    # Login

    def clickLogin(self):
        clickBtn = self.driver.find_element_by_id(LOGIN_BUTTON)
        clickBtn.click()

    def lofinFormIsVisible(self):
        loginFormList = self.driver\
            .find_elements_by_class_name(LOGIN_FORM_LIST)
        if len(loginFormList) <= 0:
            return False
        return True

    def login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, IFRAME_LOGIN_DIV)))

        WebDriverWait(self.driver, 20)\
            .until(EC.frame_to_be_available_and_switch_to_it(
                (By.CLASS_NAME, LOGIN_FORM_FRAME)))

        inputUsername = WebDriverWait(self.driver, 20)\
            .until(EC.visibility_of_element_located((By.NAME, LOGIN_INPUT)))
        inputUsername.send_keys(self.username)

        self.driver.\
            find_element_by_xpath(LOGIN_NEXT_BTN).\
            click()

        inputPassword = WebDriverWait(self.driver, 5)\
            .until(EC.visibility_of_element_located((By.NAME, PASSWORD)))
        inputPassword.send_keys(self.password)

        self.driver.\
            find_element_by_xpath(LOGIN_SUBMIT_BTN).\
            click()

    # Profile
    def clickAndWaitProfile(self):
        try:
            self.driver.switch_to.default_content()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, PROFILE_MENU_SECTION))
            )

            profileEditButton = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, PROFILE_EDIT_BUTTON))
            )

            profileEditButton.click()

            return True
        except (exceptions.ElementNotVisibleException,
                exceptions.NoSuchElementException,
                exceptions.TimeoutException) as error:
            print('ERROR: ', error)
            return False

    # Questions
    def getAlertUnderAdditional(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, ALERT_ADDITIONAL))
        )
        return self.waitForElementVisible((By.CLASS_NAME,
                                          ALERT_ADDITIONAL)) \
            .get_attribute('innerText')

    def setQuestionAdditional(self, additional):
        inputQuestionField = self.waitForElementVisible(
            (By.NAME, QUESTION_ADDITIONAL))
        self.sendText(inputQuestionField, additional)

        WebDriverWait(self.driver, 10).until(
            lambda browser:
                inputQuestionField.get_attribute('value') == additional
        )

    def setQuestionTitle(self, question):
        self.driver.switch_to.default_content()
        inputQuestionField = self.waitForElementVisible(
            (By.NAME, QUESTION_TEXT))
        self.sendText(inputQuestionField, question)

        WebDriverWait(self.driver, 10).until(
            lambda browser:
                inputQuestionField.get_attribute('value') == question
        )

    def isAlert(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, ALERT_WINDOW)))

            return True
        except exceptions.TimeoutException:
            return False

    def switchCategoryToAnother(self):
        categoryDropDownMenu = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_any_elements_located(
                (By.CLASS_NAME, CATEGORY_DROP_DOWN_MENU)))
        categoryDropDownMenu[0].click()

        buttonChooseAnother = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_any_elements_located(
                (By.CLASS_NAME, CATEGORY_ANOTHER)))
        for i in range(2):
            try:
                buttonChooseAnother[-1].click()
            except:
                pass

    def clickSendQuestion(self):
        ask_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, QUESTION_SUBMIT_BUTTON))
        )
        ask_button.click()

    def autosettingSubcategory(self, Subcategory):
        WebDriverWait(self.driver, 10).until(
            ElementEqualSubcategory(QUESTION_SUBCOTEGORY,
                                    u'Политика'))

    def clearQuestionThemeByKeys(self):
        inputQuestionField = self.driver\
            .find_element_by_name(QUESTION_TEXT)
        inputQuestionField.click()
        inputQuestionField.send_keys(Keys.CONTROL + "a")
        inputQuestionField.send_keys(Keys.DELETE)

    def getAlertUnderQuestion(self):
        alert = self.driver\
            .find_element_by_class_name(
                QUESTION_UNDER_ALERT)
        return alert.get_attribute('innerHTML')

    def getSubcategory(self):
        subcategory = self.driver \
            .find_elements_by_class_name(QUESTION_SUBCOTEGORY)[1] \
            .find_elements_by_css_selector('*')
        return subcategory[-1].get_attribute('innerHTML')

    # Upload
    def open_photo_upload_form(self):
        photo_span = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(UPLOAD_PHOTO_SPAN)
        )
        photo_span.find_element_by_xpath('./..').click()

    def open_video_upload_form(self):
        video_span = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(UPLOAD_VIDEO_SPAN)
        )
        video_span.find_element_by_xpath('./..').click()

    def check_settings_page(self):
        self.driver.switch_to.default_content()
        settings_button = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(SETTING_BUTTON)
        )
        settings_button.click()

        settings = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_elements_by_class_name(SETTINGS_PAGE)
        )

        if len(settings) == 1:
            return True
        else:
            return False

    def can_edit_time(self):
        self.driver.switch_to.default_content()
        button = WebDriverWait(self.driver, 10, 0.1).until(
            EC.visibility_of_any_elements_located(
                (By.ID, QUESTION_EDIT_BTN))
        )

        if (len(button) == 1):
            return True
        else:
            return False

    # Poll
    def check_poll_option_correct_add(self):
        variant_3 = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(POLL_VARIANT_FIELD_3)
        )
        variant_3.click()
        variant_3.send_keys("getting 4 option")

        variant_4 = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(POLL_VARIANT_FIELD_4)
        )

        variant_4.click()
        variant_4.send_keys("getting 5 option")

        polls = self.driver\
            .find_elements_by_xpath(POLL_VARIANT_FIELD_5)

        if len(polls) == 1:
            return True
        else:
            return False

    def open_poll_form(self):
        poll_form = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_class_name(POLL_FORM)
        )
        poll_form.click()
