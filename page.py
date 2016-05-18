# -*- coding: utf-8 -*-

import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Page(object):
    BASE_URL = 'https://deti.mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class NamesPage(Page):
    PATH = 'names/'

    @property
    def menu(self):
        return TopMenu(self.driver)

    @property
    def nav(self):
        return NavMenu(self.driver)

    @property
    def baby_name(self):
        return BabyName(self.driver)

    @property
    def footer(self):
        return Footer(self.driver)

    @property
    def basement(self):
        return Basement(self.driver)

    @property
    def right_col(self):
        return RightColumn(self.driver)


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class TopMenu(Component):
    LOGO = '//div[@class="pm-logo pm-logo_press"]/a[@class="pm-logo__link"]'
    FORUM = '//a[@title="Форум"]'
    CONSULT = '//a[@title="Консультации"]'
    NAMES = '//a[@title="Имена"]'
    RECEIPT = '//a[@title="Рецепты"]'
    CALENDAR = '//a[@title="Календарь развития"]'
    ROD_DOM = '//a[@title="Роддома"]'
    ALL_ABOUT = '//a[@title="Все о вашей груди"]'  # (⁄ ⁄•⁄ω⁄•⁄ ⁄)
    MOM_AND_BABY = '//a[@title="Мама и малыш"]'
    SEARCH_ICON = '//span[@class="js-link pm-toolbar__button__inner  pm-toolbar__button__inner_notext"]'
    SEARCH_INPUT = '//input[@name="q"]'
    SEARCH_SUBMIT = '//button[@class="class="js-submit-button pm-toolbar__' \
                    'search__button__input  pm-toolbar__search__button__' \
                    'input_expandable pm-toolbar__search__button__input_not-adaptive""]'

    def click_logo(self):
        self.driver.find_element_by_xpath(self.LOGO).click()

    def click_forum(self):
        self.driver.find_element_by_xpath(self.FORUM).click()

    def click_consult(self):
        self.driver.find_element_by_xpath(self.CONSULT).click()

    def click_names(self):
        self.driver.find_element_by_xpath(self.NAMES).click()

    def click_receipt(self):
        self.driver.find_element_by_xpath(self.RECEIPT).click()

    def click_calendar(self):
        self.driver.find_element_by_xpath(self.CALENDAR).click()

    def click_rod_dom(self):
        self.driver.find_element_by_xpath(self.ROD_DOM).click()

    def click_all_about(self):
        self.driver.find_element_by_xpath(self.ALL_ABOUT).click()

    def click_mom_and_baby(self):
        self.driver.find_element_by_xpath(self.MOM_AND_BABY).click()

    def search(self, query):
        self.driver.find_element_by_xpath(self.SEARCH_ICON).click()
        query_input = self.driver.find_element_by_xpath(self.SEARCH_INPUT)
        query_input.send_keys(query)
        query_input.send_keys(Keys.RETURN)


class NavMenu(Component):
    FAMILY = '//li[@class="b-nav__item b-nav__item_red b-nav__item_family"]/a[@class="b-nav__item__title"]'
    PLANNING = '//li[@class="b-nav__item b-nav__item_blue b-nav__item_plan"]/a[@class="b-nav__item__title"]'
    PLANNING_DAY_OVULATION = '//li[@class="b-nav__item b-nav__item_blue b-nav__item_plan"]' \
                             '/div[@class="b-nav__item__links"]/a'
    PREGNANCY = '//li[@class="b-nav__item b-nav__item_green b-nav__item_preg"]/a[@class="b-nav__item__title"]'
    PREGNANCY_1 = '//a[@title="1 неделя беременности"]'
    PREGNANCY_2 = '//a[@title="2 неделя беременности"]'
    PREGNANCY_3 = '//a[@title="3 неделя беременности"]'
    PREGNANCY_4 = '//a[@title="4 неделя беременности"]'
    PREGNANCY_5 = '//a[@title="5 неделя беременности"]'
    PREGNANCY_6 = '//a[@title="6 неделя беременности"]'
    PREGNANCY_7 = '//a[@title="7 неделя беременности"]'
    PREGNANCY_8 = '//a[@title="8 неделя беременности"]'
    PREGNANCY_9 = '//a[@title="9 неделя беременности"]'
    PREGNANCY_10 = '//a[@title="10 неделя беременности"]'
    PREGNANCY_11 = '//a[@title="11 неделя беременности"]'
    PREGNANCY_12 = '//a[@title="12 неделя беременности"]'
    PREGNANCY_13 = '//a[@title="13 неделя беременности"]'
    PREGNANCY_14 = '//a[@title="14 неделя беременности"]'
    PREGNANCY_15 = '//a[@title="15 неделя беременности"]'
    PREGNANCY_16 = '//a[@title="16 неделя беременности"]'
    PREGNANCY_17 = '//a[@title="17 неделя беременности"]'
    PREGNANCY_18 = '//a[@title="18 неделя беременности"]'
    PREGNANCY_19 = '//a[@title="19 неделя беременности"]'
    PREGNANCY_20 = '//a[@title="20 неделя беременности"]'
    PREGNANCY_21 = '//a[@title="21 неделя беременности"]'
    PREGNANCY_22 = '//a[@title="22 неделя беременности"]'
    PREGNANCY_23 = '//a[@title="23 неделя беременности"]'
    PREGNANCY_24 = '//a[@title="24 неделя беременности"]'
    PREGNANCY_25 = '//a[@title="25 неделя беременности"]'
    PREGNANCY_26 = '//a[@title="26 неделя беременности"]'
    PREGNANCY_27 = '//a[@title="27 неделя беременности"]'
    PREGNANCY_28 = '//a[@title="28 неделя беременности"]'
    PREGNANCY_29 = '//a[@title="29 неделя беременности"]'
    PREGNANCY_30 = '//a[@title="30 неделя беременности"]'
    PREGNANCY_31 = '//a[@title="31 неделя беременности"]'
    PREGNANCY_32 = '//a[@title="32 неделя беременности"]'
    PREGNANCY_33 = '//a[@title="33 неделя беременности"]'
    PREGNANCY_34 = '//a[@title="34 неделя беременности"]'
    PREGNANCY_35 = '//a[@title="35 неделя беременности"]'
    PREGNANCY_36 = '//a[@title="36 неделя беременности"]'
    PREGNANCY_37 = '//a[@title="37 неделя беременности"]'
    PREGNANCY_38 = '//a[@title="38 неделя беременности"]'
    PREGNANCY_39 = '//a[@title="39 неделя беременности"]'
    PREGNANCY_40 = '//a[@title="40 неделя беременности"]'
    PREGNANCY_41 = '//a[@title="41 неделя беременности"]'
    PREGNANCY_42 = '//a[@title="42 неделя беременности"]'
    BIRTH = '//li[@class="b-nav__item b-nav__item_yellow b-nav__item_birth"]/a[@class="b-nav__item__title"]'
    KIDS = '//li[@class="b-nav__item b-nav__item_orange b-nav__item_kids "]/a[@class="b-nav__item__title"]'
    KIDS_0 = '//li[@class="b-nav__weeks__item b-nav__weeks__item_round b-nav__weeks__item_round-l ' \
             'b-nav__weeks__item_cap"]/a[@href="/baby/newborn/"]'
    KIDS_1_6 = '//li[@class="b-nav__weeks__item"]/a[@href="/baby/1-6/"]'
    KIDS_7_12 = '//li[@class="b-nav__weeks__item b-nav__weeks__item_round b-nav__weeks__item_round-r"]' \
                '/a[@href="/baby/7-12/"]'
    KIDS_1_3_YEARS = '//li[@class="b-nav__weeks__item b-nav__weeks__item_round b-nav__weeks__item_round-l"]' \
                     '/a[@href="/baby/1-3/"]'
    KIDS_3_7_YEARS = '//li[@class="b-nav__weeks__item"]/a[@href="/child/"]'
    KIDS_7_YEARS = '//li[@class="b-nav__weeks__item b-nav__weeks__item_round b-nav__weeks' \
                   '__item_round-r b-nav__weeks__item_cap"]' \
                   '/a[@href="/teenager/"]'

    pass


class BabyName(Component):
    pass


class Footer(Component):
    pass


class Basement(Component):
    pass


class RightColumn(Component):
    pass
