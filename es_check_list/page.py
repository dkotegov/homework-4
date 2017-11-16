# -*- coding: utf-8 -*-

import os
import time

import urlparse

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


USERNAME_FIRST = 'technopark36'
USERNAME_SECOND = 'technopark9'
PASSWORD = os.environ['PASSWORD']


class Page(object):
    BASE_URL = 'https://ok.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        print(url)
        self.driver.maximize_window()
        self.driver.get(url)

    @property
    def top_menu(self):
        return TopMenu(self.driver)


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)


class OnlinePage(Page):
    PATH = '/online'
    AVATAR = '//a[@class="photoWrapper"]'
    OVERLAY = '//div[@class=__auto]'

    @property
    def first_person(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.ID, 'pointerOverlay')))

        self.driver.find_element_by_xpath(self.AVATAR).click()

        url = self.driver.find_element_by_xpath(self.AVATAR).get_attribute('href').split('/')

        return PersonPage(self.driver, url[len(url) - 1])


class PersonPage(Page):
    PATH = '/profile'
    NAME = '//h1[@class="mctc_name_tx bl"]'

    def __init__(self, driver, login):
        Page.__init__(self, driver)
        self.PATH += '/' + login

    @property
    def avatar(self):
        return Avatar(self.driver)

    @property
    def marks_modal(self):
        return MarksModal(self.driver)

    @property
    def photo_manager(self):
        return PhotoManager(self.driver)

    def get_name(self):
        return self.driver.find_element_by_xpath(self.NAME).text


class PhotoPage(Page):
    TEMPLATE = '/profile/{}/pphotos/{}'

    def __init__(self, driver, user, photo):
        Page.__init__(self, driver)
        self.PATH = self.TEMPLATE.format(user, photo)

    @property
    def mark(self):
        return Mark(self.driver)

    @property
    def marks(self):
        return MarksModal(self.driver)


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class Mark(Component):
    MARK = '//a[contains(@class,"marks-new_ic")][text()="{}"]'
    RESULT = '//div[@class="marks marks-new __light jcol-r"]//span[contains(@class,"marks-new_ic")]'

    def set_mark(self, mark=5):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.marks-new_ic')))
        except TimeoutException:
            return 0
        self.driver.find_element_by_xpath(self.MARK.format(mark)).click()

    def check_mark(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.RESULT)))
        return self.driver.find_element_by_xpath(self.RESULT).text


class AuthForm(Component):
    LOGIN = '//input[@name="st.email"]'
    PASSWORD = '//input[@name="st.password"]'
    SUBMIT = '//input[@data-l="t,loginButton"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class Avatar(Component):
    AVATAR = '//a[@class="card_wrp"]'

    def open(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.ID, 'pointerOverlay')))

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.card_wrp')))

        self.driver.find_element_by_xpath(self.AVATAR).click()

    @property
    def marks(self):
        return MarksModal(self.driver)


class TopMenu(Component):
    DROPDOWN = '//div[@class="toolbar_dropdown_w h-mod"]'
    LOGOUT = '//a[@data-l="t,logoutCurrentUser"]'
    LOGOUT_CONFIRM = '//input[@data-l="t,confirm"]'

    def open(self):
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(EC.invisibility_of_element_located((By.ID, 'popLayer_mo')))
        self.driver.find_element_by_xpath(self.DROPDOWN).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.LOGOUT).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-l="t,confirm"]')))
        self.driver.find_element_by_xpath(self.LOGOUT_CONFIRM).click()


class MarksModal(Component):
    COUNTER = '//a[@data-l="t,stats"]'
    ALL_MARKS = '//a[@class="al"]'
    MARK_VALUE = '//a[contains(text(), "{}")]/../../span/span/span[@class="marks-new_ic __ac"]'
    REMOVE = '//a[@title="удалить"]'
    CANCEL = '//a[@class="il lp ml-x"]'

    def open(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.COUNTER)))

        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.COUNTER)).perform()

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, self.ALL_MARKS)))
        except TimeoutException:
            return False
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.ALL_MARKS))\
                .click().perform()

        return True

    def check_mark(self, expected_value, name):

        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, self.MARK_VALUE.format(name))))
        except TimeoutException:
            return False

        value = int(self.driver.find_element_by_xpath(self.MARK_VALUE.format(name)).text)

        return value == expected_value

    def remove(self, name):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.MARK_VALUE.format(name))))
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.MARK_VALUE.format(name))).perform()

        wait.until(EC.element_to_be_clickable((By.XPATH, self.REMOVE)))
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.REMOVE)).click().perform()

    def cancel_remove(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.CANCEL)))

        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.CANCEL)).click().perform()


class PhotoManager(Component):
    UPLOAD_PHOTO = '//input[@type="file"][@name="photo"]'
    ALBUM = '//a[@hrefattrs="st.cmd=userPersonalPhotos"]'
    PHOTO = '//a[@class="photo-card_cnt"]'

    def upload_photo(self, url):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.ID, 'pointerOverlay')))
        self.driver.find_element_by_xpath(
            self.UPLOAD_PHOTO).send_keys(os.path.join(os.getcwd(), 'es_check_list/uploads/', url))
        wait.until(EC.element_to_be_clickable((By.XPATH, self.ALBUM)))
        self.driver.find_element_by_xpath(self.ALBUM).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.PHOTO)))
        url = self.driver.find_element_by_xpath(self.PHOTO).get_attribute('href').split('/')
        return url[len(url) - 1], url[len(url) - 3]