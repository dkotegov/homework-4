# -*- coding: utf-8 -*-
import urlparse

from selenium.webdriver import ActionChains


class Page(object):
    BASE_URL = 'http://msk.realty.mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class SalePage(Page):
    PATH = '/sale/living/'

    @property
    def offer(self):
        return PageOffer(self.driver)


# class NewBuildingsPage(Page):
#     PATH = '/sale/newbuilding/'
#
#     @property
#     def first_offer(self):
#         return PageOffer(self.driver)


class PageOffer(SalePage):
    CLASS_TITLE = 'p-instance__title'
    ADD_BTN = '//div[@data-module="Favorites"]'#//div[text()="В избранное"]'
    OFFER_ID = ''

    def open(self, offer_num=1):
        super(PageOffer, self).open()
        title_links = self.driver.find_elements_by_class_name(self.CLASS_TITLE)
        link = title_links[offer_num].get_attribute('href')
        self.driver.get(link)

    @property
    def slider(self):
        return Slider(self.driver)

    def add_to_favourites(self):
        button = self.driver.find_element_by_xpath(self.ADD_BTN)
        self.set_offer_id()
        button.click()

    def set_offer_id(self):
        button = self.driver.find_element_by_xpath(self.ADD_BTN)
        self.OFFER_ID = button.get_attribute('data-uid')

    def get_offer_id(self):
        return self.OFFER_ID


class FavouritesPage(Page):
    PATH = 'https://pro.realty.mail.ru/favorites/'
    LINK = '//span[@bem-id="234"]'
    DROPDOWN_CLASS = '//span[@bem-id="247"]/a/span'#/span[@class="pm-toolbar__dropdown__item__text"]'

    def open(self):
        self.driver.get(self.PATH)
        self.driver.maximize_window()

    @property
    def offer(self):
        return PageOffer(self.driver)

    def get_count(self):
        hover_link = self.driver.find_element_by_xpath(self.LINK)
        hover_link.click()
        text = self.driver.find_element_by_xpath(self.DROPDOWN_CLASS)

        s = text.text
        a = s.split('(')
        return a[1][:len(a[1])-1]


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)


class AuthForm(Component):
    LOGIN = '//input[@name="Login"]'
    PASSWORD = '//input[@name="Password"]'
    SUBMIT = '//input[@value="Войти"]'
    LOGIN_BUTTON = '//a[text()="Вход"]'

    def open_form(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class Slider(Component):
    OPEN_CLASS = 'photo__action'
    CLOSE_CLASS = 'viewbox__close'
    ICON_NEXT = 'icon_control_next'
    ICON_PREV = 'icon_control_previous'
    BOX_NEXT = 'viewbox__control_next'
    BOX_PREV = 'viewbox__control_previous'
    CURRENT_NUM = 'viewbox__current'
    TOTAL_NUM = 'viewbox__total'

    def __init__(self, driver):
        super(Slider, self).__init__(driver)
        self.page_num = 0

    def open_slider(self):
        slider = self.driver.find_element_by_class_name(self.OPEN_CLASS)
        slider.click()
        self.page_num = 1

    def close_slider(self):
        btn_close = self.driver.find_element_by_class_name(self.CLOSE_CLASS)
        btn_close.click()
        self.page_num = 0

    def click_next(self, method=0):
        btn_next = self.driver.find_element_by_class_name(self.ICON_NEXT)
        if method:
            btn_next = self.driver.find_element_by_class_name(self.BOX_NEXT)
        btn_next.click()
        self.page_num += 1

    def click_prev(self, method=0):
        btn_prev = self.driver.find_element_by_class_name(self.ICON_PREV)
        if method:
            btn_prev = self.driver.find_element_by_class_name(self.BOX_PREV)
        btn_prev.click()
        self.page_num -= 1

    def get_page_num(self):
        return self.page_num

    def get_page_num_from_browser(self):
        current_num = self.driver.find_element_by_class_name(self.CURRENT_NUM)
        return int(current_num.text)

    def get_max_page_num(self):
        max_num = self.driver.find_element_by_class_name(self.TOTAL_NUM)
        return int(max_num.text)

    @property
    def banner(self):
        return Banner(self.driver)

    @property
    def chare_block(self):
        return ChareBlock(self.driver)


class Banner(Component):
    CLASS = 'js-popup_banner'

    def find(self):
        self.driver.find_element_by_class_name(self.CLASS)


class ChareBlock(Component):
    BUTTONS_CLASSES = ['share_vk', 'share_fb', 'share_ok', 'share_my', 'share_tw']

    def click_btn(self, btn_class):
        btn = self.driver.find_element_by_class_name(btn_class)
        btn.click()

    def click_all_btn(self):
        for class_btn in self.BUTTONS_CLASSES:
            self.click_btn(class_btn)
