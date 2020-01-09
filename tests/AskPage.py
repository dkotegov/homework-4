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

UPLOAD_PHOTO_BTN = '//span[text()="Фото"]'
UPLOAD_PHOTO_SECION = 'window_3e48lyZw'
UPLOAD_VIDEO_BTN = '//span[text()="Видео"]'
UPLOAD_VIDEO_SECTION_ON_NEW_WINDOW = 'popup-show'

SETTING_BUTTON = '//span[text()="Настройки"]'
SETTINGS_PAGE = 'page-settings'

QUESTION_SUBMIT_BUTTON = "btn_3ykLdYEq"
QUESTION_UNDER_ALERT = "z1LfJpugzE39YVXERE-f__0"
QUESTION_CATEGORY_BTN = 'select_1lZeUpFs_1'
QUESTION_CATEGORY_DROP_DOWN_MENU = 'default_1IJJ-JAn'
QUESTION_CURRENT_CATEGORY = "//div[@class='" + QUESTION_CATEGORY_BTN + "']/span"
QUESTION_CATEGORY = "//span[@class='content__text_34Qv5DnE' and text()='"
QUESTION_EDIT_BTN = "q-edit-control-element"
QUESTION_TEXT = 'question_text'
QUESTION_ADDITIONAL = 'question_additional'
QUESTION_SECTION = 'q--head hentry'
QUESTION_EDIT_SECTION = 'window_3e48lyZw'
QUESTION_WRAPPER = 'layout__contentCol2_2sC-W1d6'
QUESTION_TITLE = 'q--qtext'
QUESTION_EDIT_TITLE = 'question_text'
QUESTION_SAVE_EDITED_BTN = 'btn_3ykLdYEq'
QUESTION_PAGE_BTN = 'profile-menu-item__content'

POLL_VARIANT_FIELD = "//input[@placeholder='Вариант №"
POLL_VARIANT_FIELD_3 = "//input[@placeholder='Вариант №3']"
POLL_VARIANT_FIELD_4 = "//input[@placeholder='Вариант №4']"
POLL_VARIANT_FIELD_5 = "//input[@placeholder='Вариант №5']"
POLL_FORM = 'menuItem__content_last_3LtjwRRK'
POLL_OPTIONS_SECTION = 'poll_options'

ALERT_ADDITIONAL = 'error_z1LfJpug'
POP_UP_ALERT = 'popup--content '
ALERT_WINDOW = 'window_3e48lyZw'
ALERT_WINDOWS_TEXT = 'msg_FrSe12sF'

PROFILE_BUTTON = 'profile-menu-item_hoverable'
PROFILE_FORM = 'v--modal-overlay'

PROFILE_MENU_SECTION = 'profileMenuColumn_1F5KVzKR'
PROFILE_EDIT_BUTTON = '//span[text()="Редактировать профиль"]'
PROFILE_EDIT_SECTION = 'v--modal-box'
PROFILE_DESCRIPTION_INPUT = 'desc'
PROFILE_SAVE_DESCRIPTION = "//*[contains(text(), 'Сохранить профиль')]"

LOGIN_NEXT_BTN = "//button[@data-test-id='next-button']"
LOGIN_SUBMIT_BTN = "//button[@data-test-id='submit-button']"
LOGIN_FORM_LIST = "ag-popup__frame_show"
LOGIN_BUTTON = 'PH_authLink'
LOGIN_FORM_FRAME = 'ag-popup__frame__layout__iframe'
LOGIN_IFRAME_LOGIN_DIV = 'ag-popup__frame_onoverlay'
LOGIN_INPUT_LABEL = 'Login'
LOGIN_PASSWORD_LABEL = 'Password'


class Page(object):
    BASE_URL = 'https://otvet.mail.ru/ask/'
    UPLOAD_VIDEO_WINDOW_URL = 'https://my.mail.ru/cgi-bin/video/external_upload?cb=actionUploadVideo&album=_vanswers'

    def __init__(self, driver):
        self.driver = driver
        self.username = os.environ['USERNAME']
        self.password = os.environ['PASSWORD']

    def open(self):
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()

    def press_esc(self):
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE) \
            .perform()


class AskPage(Page):
    # Tools
    def _wait_visibility(self, locator, timeout=10, step=0.1):
        return WebDriverWait(self.driver, timeout, step) \
            .until(EC.visibility_of_element_located(locator))

    def _wait_clickability(self, locator, timeout=10, step=0.1):
        return WebDriverWait(self.driver, timeout, step) \
            .until(EC.element_to_be_clickable(locator))

    def _wait_to_switch(self, locator, timeout=10, step=0.1):
        return WebDriverWait(self.driver, timeout, step) \
            .until(EC.frame_to_be_available_and_switch_to_it(locator))

    def _find_element(self, locator, timeout=10, step=0.1):
        return WebDriverWait(self.driver, timeout, step) \
            .until(self.driver.find_element(locator))

    def _find_elements(self, locator, timeout=10, step=0.1):
        return WebDriverWait(self.driver, timeout, step) \
            .until(self.driver.find_elements(locator))

    def _send_large_text(self, webElement, text):
        self.driver.execute_script("arguments[0].value = arguments[1]",
                                   webElement, text[:len(text)-1])
        webElement.send_keys(text[len(text)-1])

    def _click_to_close_drop_down_category_menu(self):
        wrapper = self._wait_visibility((By.CLASS_NAME, QUESTION_WRAPPER))
        wrapper.click()
    
    # Profile
    def _click_edit_profile(self):
        self._wait_visibility((By.CLASS_NAME, PROFILE_MENU_SECTION))
        profileEditButton = self._wait_clickability((By.XPATH, PROFILE_EDIT_BUTTON))
        profileEditButton.click()

    def get_random_title(self):
        firstWordDict = [
            u'Как',
            u'Где',
            u'Когда'
            u'Каким образом'
            u'Каким способом'
            u'Каким методом'
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
            u'Написать'
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
            u'Тесты'
        ]

        return firstWordDict[0] + ' ' +\
            secondWordDict[random.randint(0, len(secondWordDict)) - 1] + ' ' +\
            thirdWordDict[random.randint(0, len(thirdWordDict)) - 1] + '?'

    def get_url(self):
        return self.driver.current_url
    
    def refresh_page(self):
        self.driver.refresh()

    # Login
    def click_login_button(self):
        button = self._wait_clickability((By.ID, LOGIN_BUTTON))
        button.click()

    def login(self):
        # Свитч на iframe логина
        self._wait_visibility((By.CLASS_NAME, LOGIN_IFRAME_LOGIN_DIV))
        self._wait_to_switch((By.CLASS_NAME, LOGIN_FORM_FRAME))

        # Логин
        inputUsername = self._wait_clickability((By.NAME, LOGIN_INPUT_LABEL))
        inputUsername.click()
        inputUsername.send_keys(self.username)

        # Next
        nextButton = self.driver.find_element_by_xpath(LOGIN_NEXT_BTN)
        nextButton.click()

        # Пароль
        inputPassword = self._wait_clickability((By.NAME, LOGIN_PASSWORD_LABEL))
        inputPassword.click()
        inputPassword.send_keys(self.password)

        # Submit
        submitButton = self.driver.find_element_by_xpath(LOGIN_SUBMIT_BTN)
        submitButton.click()

        self.driver.switch_to.default_content()

    def get_edit_profile_section(self):
        return self._wait_visibility((By.CLASS_NAME, PROFILE_EDIT_SECTION))

    def edit_profile_description(self, desc):
        self._click_edit_profile()
        self._wait_visibility((By.CLASS_NAME, PROFILE_EDIT_SECTION))
        descriptionInput = self._wait_visibility((By.NAME, PROFILE_DESCRIPTION_INPUT))
        descriptionInput.clear()
        descriptionInput.send_keys(desc)

        descriptionSaveBtn = self._wait_visibility((By.XPATH, PROFILE_SAVE_DESCRIPTION))
        descriptionSaveBtn.click()        

    def get_profile_description(self):
        self._click_edit_profile()
        self._wait_visibility((By.CLASS_NAME, PROFILE_EDIT_SECTION))
        descriptionInput = self._wait_visibility((By.NAME, PROFILE_DESCRIPTION_INPUT))
        return descriptionInput.get_attribute('value')

    # Questions
    def get_alert_under_additional(self):
        alert = self._wait_visibility((By.CLASS_NAME, ALERT_ADDITIONAL))
        return alert.get_attribute('innerText')

    def set_question_category(self, category):
        categoryDropDownMenu = self._wait_visibility((By.CLASS_NAME, QUESTION_CATEGORY_BTN))
        categoryDropDownMenu.click()

        self._wait_visibility((By.CLASS_NAME, QUESTION_CATEGORY_DROP_DOWN_MENU))

        anotherCategoryButton = self._wait_visibility((By.XPATH, QUESTION_CATEGORY + category + "']"))
        anotherCategoryButton.click()

        self._click_to_close_drop_down_category_menu()

    def get_question_category(self):
        self._wait_visibility((By.CLASS_NAME, QUESTION_CATEGORY_BTN))
        currentCategory = self._wait_visibility((By.XPATH, QUESTION_CURRENT_CATEGORY))
        return currentCategory.get_attribute('innerText')

    def get_question_title(self):
        title = self._wait_visibility((By.TAG_NAME, 'index'), 20)
        return title.get_attribute('innerText')

    def edit_question_title(self, title):
        input = self._wait_visibility((By.NAME, QUESTION_EDIT_TITLE))
        input.click()

        while len(input.get_attribute('value')) != 0:
            input.send_keys(Keys.BACKSPACE)

        input.send_keys(title)

    def save_edited_question(self):
        btn = self._wait_clickability((By.CLASS_NAME, QUESTION_SAVE_EDITED_BTN))
        btn.click()

    def set_question_additional(self, additional):
        inputQuestionField = self._wait_visibility((By.NAME, QUESTION_ADDITIONAL))
        self._send_large_text(inputQuestionField, additional)

    def set_question_title(self, question):
        inputQuestionField = self._wait_visibility((By.NAME, QUESTION_TEXT))
        inputQuestionField.send_keys(question)

    def click_send_question(self):
        ask_button = self._wait_clickability((By.CLASS_NAME, QUESTION_SUBMIT_BUTTON))
        ask_button.click()

    def get_alert_message(self):
        alert_text = self._wait_visibility((By.CLASS_NAME, ALERT_WINDOWS_TEXT))
        return alert_text.text

    def clear_question_theme_by_keys(self):
        inputQuestionField = self._wait_clickability((By.NAME, QUESTION_TEXT))
        inputQuestionField.click()

        while len(inputQuestionField.get_attribute('value')) != 0:
            inputQuestionField.send_keys(Keys.BACKSPACE)

    # Upload
    def open_photo_upload_form(self):
        uploadPhotoButton = self._wait_clickability((By.XPATH, UPLOAD_PHOTO_BTN))
        uploadPhotoButton.click()

    def open_video_upload_form(self):
        uploadVideoButton = self._wait_clickability((By.XPATH, UPLOAD_VIDEO_BTN))
        uploadVideoButton.click()

    def get_photo_upload_section(self):
        return self._wait_visibility((By.CLASS_NAME, UPLOAD_PHOTO_SECION))

    def get_video_upload_section(self):
        uploadWindow = self.driver.window_handles[1]
        self.driver.switch_to_window(uploadWindow)
        self._wait_visibility((By.CLASS_NAME, UPLOAD_VIDEO_SECTION_ON_NEW_WINDOW))
        return self.driver.current_url

    def click_edit_question(self):
        editQuestionButton = self._wait_clickability((By.ID, QUESTION_EDIT_BTN))
        editQuestionButton.click()

    def get_edit_question_section(self):
        return self._wait_visibility((By.CLASS_NAME, QUESTION_EDIT_SECTION))

    # Poll
    def set_text_to_poll_option(self, poolOptionNumber, text):
        optionSelector = POLL_VARIANT_FIELD + str(poolOptionNumber) + "']"
        option = self.driver.find_element_by_xpath(optionSelector)
        option.click()
        option.send_keys(text)

    def get_text_of_poll_option(self, poolOptionNumber):
        optionSelector = POLL_VARIANT_FIELD + str(poolOptionNumber) + "']"
        option = self.driver.find_element_by_xpath(optionSelector)
        return option.get_attribute('value')

    def get_poll_section(self):
        return self._wait_visibility((By.NAME, POLL_OPTIONS_SECTION))

    def open_poll_form(self):
        pollForm = self._wait_clickability((By.CLASS_NAME, POLL_FORM))
        pollForm.click()
