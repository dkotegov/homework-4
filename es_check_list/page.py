# -*- coding: utf-8 -*-

import os

import urlparse

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, MoveTargetOutOfBoundsException
from selenium.webdriver.common.action_chains import ActionChains


USERNAME_FIRST = 'technopark9'
USERNAME_SECOND = 'technopark36'
PASSWORD = os.environ['PASSWORD']


class Page(object):
    BASE_URL = 'https://ok.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self, first=False):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        if first:
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


class PersonPage(Page):
    PATH = '/profile'
    NAME = '//h1[@class="mctc_name_tx bl"]'

    def __init__(self, driver, login=''):
        Page.__init__(self, driver)
        self.PATH += '/' + login

    @property
    def photo_manager(self):
        return PhotoManager(self.driver)

    def get_name(self):
        return self.driver.find_element_by_xpath(self.NAME).text


class PhotoPage(Page):
    TEMPLATE = '/profile/{}/pphotos/{}'
    REMOVE = '//a[@class="ic-w lp"]'
    PHOTOS = '//a[@class="mctc_navMenuSec"][contains(text(), "Фото")]'
    PHOTO = '//a[@class="photo-card_cnt"][contains(@href, "{}")]'
    SIMPLE_PHOTO = '//a[@class="photo-card_cnt"]'

    def __init__(self, driver, user, photo):
        Page.__init__(self, driver)
        self.PATH = '/profile/{}'.format(user)
        self.PHOTO_ID = photo

    def open(self, first=False):
        Page.open(self)
        self.driver.find_element_by_xpath(self.PHOTOS).click()
        self.driver.find_element_by_xpath(self.PHOTO.format(self.PHOTO_ID)).click()

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
    UPDATE = '//a[@class="il marks-new_lk"]'
    FIVE_PLUS = '//span[@class="marks-new_ic-tx va_target"] ' \
                '| //div[@id="hook_Block_PopLayerViewFriendPhotoRating"]/a[@class="marks-new_ic __plus"]'
    LOADER = '//div[@class="photo-layer_process"]'

    def set_mark(self, mark=5):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(ec.invisibility_of_element_located((By.XPATH, self.LOADER)))
            element = self.driver.find_element_by_xpath(self.MARK.format(mark))
            self.driver.execute_script("arguments[0].click();", element)
            return True
        except NoSuchElementException:
            return False

    def check_mark(self):
        return self.driver.find_element_by_xpath(self.RESULT).text

    def update(self):
        try:
            element = self.driver.find_element_by_xpath(self.UPDATE)
            self.driver.execute_script("arguments[0].click();", element)
            return True
        except NoSuchElementException:
            return False


class AuthForm(Component):
    LOGIN = '//input[@name="st.email"]'
    PASSWORD = '//input[@name="st.password"]'
    SUBMIT = '//input[@data-l="t,loginButton"]'
    ADD = '//span[contains(text(), "Добавить профиль")]'

    def set_login(self, login):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(ec.element_to_be_clickable((By.XPATH, self.LOGIN)))
        except TimeoutException:
            self.driver.find_element_by_xpath(self.ADD).click()
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class TopMenu(Component):
    DROPDOWN = '//div[@class="toolbar_dropdown_w h-mod"]'
    LOGOUT = '//a[@data-l="t,logoff"]'
    LOGOUT_CONFIRM = '//input[@id="hook_FormButton_logoff.confirm_not_decorate"][contains(@value,"Выйти")]'
    ENTER = '//input[@class="button-pro __wide"]'
    PHOTO = '//div[@id="photoLayerWrapper"]'

    def open(self):
        self.driver.find_element_by_xpath(self.DROPDOWN).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.LOGOUT).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((By.XPATH, self.LOGOUT_CONFIRM)))
        self.driver.find_element_by_xpath(self.LOGOUT_CONFIRM).click()

    @property
    def events_modal(self):
        return EventsModal(self.driver)


class MarksModal(Component):
    COUNTER = '//a[@data-l="t,stats"]'
    EVENTS_COUNTER = '//span[@class="widget_ico ic12 ic12_i_marks-g"]'
    ALL_MARKS = '//a[@class="al"]'
    MARK_VALUE = '//a[contains(text(), "{}")]/../../span/span/span[contains(@class, "marks-new_ic __ac")]'
    REMOVE = '//a[@title="удалить"]'
    CANCEL = '//a[@class="il lp ml-x"]'
    LOADER = '//div[@class="photo-layer_process"]'

    def open(self, events=False):
        try:
            if not events:
                wait = WebDriverWait(self.driver, 10)
                wait.until(ec.invisibility_of_element_located((By.XPATH, self.LOADER)))
                ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.COUNTER)).perform()
                ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.ALL_MARKS))\
                    .click().perform()
            else:
                self.driver.find_element_by_xpath(self.EVENTS_COUNTER).click()
            return True
        except NoSuchElementException:
            return False

    def check_mark(self, expected_value, name):
        try:
            value = int(self.driver.find_element_by_xpath(self.MARK_VALUE.format(name)).text)
        except NoSuchElementException, TimeoutException:
            return False
        return value == expected_value

    def remove(self, name):
        try:
            ActionChains(self.driver).move_to_element(
                self.driver.find_element_by_xpath(self.MARK_VALUE.format(name))).perform()
        except NoSuchElementException:
            return False

        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.REMOVE)).click().perform()
        return True

    def cancel_remove(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.CANCEL)).click().perform()


class PhotoManager(Component):
    UPLOAD_PHOTO = '//input[@type="file"][@name="photo"][not(@value)]'
    UPLOAD_LABEL = '//span[@class="html5-link_w js-fileapi-wrapper photo_upload_btn"]'
    PHOTO = '//a[@class="photo-card_cnt"]'
    PHOTOS = '//a[@class="mctc_navMenuSec"][@hrefattrs="st.cmd=userPhotos&st._aid=NavMenu_User_Photos"]'
    BACK = '//span[@class="tico tico__12"][contains(text(), "Вернуться")]'
    SUCCESS = '//div[@class="js-show-controls"]'
    EDIT = '//span[@class="tico tico__12"][contains(text(), "Редактировать")]'
    ALBUM = '//span[@class="portlet_h_name_t"]/a[@class="o"]'

    last_href = None

    def open(self):
        self.driver.find_element_by_xpath(self.PHOTOS).click()

    def upload_photo(self, url):
        self.driver.find_element_by_xpath(self.UPLOAD_LABEL)
        self.driver.find_element_by_xpath(
            self.UPLOAD_PHOTO).send_keys(os.path.join(os.getcwd(), 'es_check_list/uploads/', url))

        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((By.XPATH, self.SUCCESS)))
        self.driver.find_element_by_xpath(self.BACK).click()

        self.last_href = self.driver.find_element_by_xpath(self.PHOTO).get_attribute('href').split('/')
        return self.last_href[len(self.last_href) - 1], self.last_href[len(self.last_href) - 3]


class EventsModal(Component):
    EVENTS = '//span[@id="HeaderTopNewFeedbackInToolbar"][not(@onclick)]'
    MARK = '//a[contains(text(), "{}")]/../../../../../../../div/div[@class="feedback_type"]/span'
    PHOTO = '//div[@data-l="t,previewCard"]/a'

    def open(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.EVENTS)).click().perform()

    def check_mark(self, name, mark):
        try:
            result = int(self.driver.find_element_by_xpath(self.MARK.format(name)).text)
        except NoSuchElementException:
            result = None

        return result == mark

    @property
    def marks_modal(self):
        return MarksModal(self.driver)

    def get_photo(self):
        try:
            photo = self.driver.find_element_by_xpath(self.PHOTO).get_attribute('href')
        except NoSuchElementException:
            photo = None
        return photo
