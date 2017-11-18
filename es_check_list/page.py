# -*- coding: utf-8 -*-

import os
import time

import urlparse

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
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
    def photo_manager(self):
        return PhotoManager(self.driver)

    def get_name(self):
        return self.driver.find_element_by_xpath(self.NAME).text


class PhotoPage(Page):
    TEMPLATE = '/profile/{}/pphotos/{}'
    REMOVE = '//a[@class="ic-w lp"]'

    def __init__(self, driver, user, photo):
        Page.__init__(self, driver)
        self.PATH = self.TEMPLATE.format(user, photo)

    @property
    def mark(self):
        return Mark(self.driver)

    @property
    def marks(self):
        return MarksModal(self.driver)

    def remove(self):
        self.driver.find_element_by_xpath(self.REMOVE).click()


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class Mark(Component):
    MARK = '//a[contains(@class,"marks-new_ic")][text()="{}"]'
    RESULT = '//div[@class="marks marks-new __light jcol-r"]//span[contains(@class,"marks-new_ic")]'

    def set_mark(self, mark=5):
        try:
            self.driver.find_element_by_xpath(self.MARK.format(mark)).click()
        except TimeoutException:
            return 0

    def check_mark(self):
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
        self.driver.find_element_by_xpath(self.AVATAR).click()

    @property
    def marks(self):
        return MarksModal(self.driver)


class TopMenu(Component):
    DROPDOWN = '//div[@class="toolbar_dropdown_w h-mod"]'
    LOGOUT = '//a[@data-l="t,logoutCurrentUser"]'
    LOGOUT_CONFIRM = '//input[@data-l="t,confirm"]'

    def open(self):
        self.driver.find_element_by_xpath(self.DROPDOWN).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.LOGOUT).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.LOGOUT_CONFIRM).click()

    @property
    def events_modal(self):
        return EventsModal(self.driver)


class MarksModal(Component):
    COUNTER = '//a[@data-l="t,stats"]'
    EVENTS_COUNTER = '//span[@class="widget_ico ic12 ic12_i_marks-g"]'
    ALL_MARKS = '//a[@class="al"]'
    MARK_VALUE = '//a[contains(text(), "{}")]/../../span/span/span[@class="marks-new_ic __ac"]'
    REMOVE = '//a[@title="удалить"]'
    CANCEL = '//a[@class="il lp ml-x"]'
    TIME = '//a[contains(text(), "Евгеша")]/../../../../../div[@class="notif_footer"]/span'

    def open(self, events=False):
        if not events:
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.COUNTER)).perform()
            try:
                ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.ALL_MARKS)) \
                    .click().perform()
            except TimeoutException:
                return False
        else:
            self.driver.find_element_by_xpath(self.EVENTS_COUNTER).click()


        return True

    def check_mark(self, expected_value, name):
        try:
            value = int(self.driver.find_element_by_xpath(self.MARK_VALUE.format(name)).text)
        except:
            return False
        return value == expected_value

    def remove(self, name):
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.MARK_VALUE.format(name))).perform()

        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.REMOVE)).click().perform()

    def cancel_remove(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.CANCEL)).click().perform()


class PhotoManager(Component):
    UPLOAD_PHOTO = '//input[@type="file"][@name="photo"]'
    ALBUM = '//a[@hrefattrs="st.cmd=userPersonalPhotos"]'
    PHOTO = '//a[@class="photo-card_cnt"]'

    def upload_photo(self, url):
        self.driver.implicitly_wait(0)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.ID, 'pointerOverlay')))
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(
            self.UPLOAD_PHOTO).send_keys(os.path.join(os.getcwd(), 'es_check_list/uploads/', url))
        self.driver.find_element_by_xpath(self.ALBUM).click()
        url = self.driver.find_element_by_xpath(self.PHOTO).get_attribute('href').split('/')
        return url[len(url) - 1], url[len(url) - 3]


class EventsModal(Component):
    EVENTS = '//div[@class="toolbar_nav_i_tx-w usel-off"][contains(text(), "События")]'
    MARK = '//a[contains(text(), "{}")]/../../../../../../../div/div[@class="feedback_type"]/span'
    PHOTO = '//div[@data-l="t,previewCard"]/a'

    def open(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.ID, 'pointerOverlay')))
        self.driver.find_element_by_xpath(self.EVENTS).click()

    def check_mark(self, name, mark):
        return int(self.driver.find_element_by_xpath(self.MARK.format(name)).text) == mark

    @property
    def marks_modal(self):
        return MarksModal(self.driver)

    def get_photo(self):
        return self.driver.find_element_by_xpath(self.PHOTO).get_attribute('href')