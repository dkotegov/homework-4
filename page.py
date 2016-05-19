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

    def click_family(self):
        self.driver.find_element_by_xpath(self.FAMILY).click()

    def click_planing(self):
        self.driver.find_element_by_xpath(self.PLANNING).click()

    def click_planing_day_ovulation(self):
        self.driver.find_element_by_xpath(self.PLANNING_DAY_OVULATION).click()

    def click_pregnancy(self):
        self.driver.find_element_by_xpath(self.PREGNANCY).click()

    def click_pregnancy_1(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_1).click()

    def click_pregnancy_2(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_2).click()

    def click_pregnancy_3(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_3).click()

    def click_pregnancy_4(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_4).click()

    def click_pregnancy_5(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_5).click()

    def click_pregnancy_6(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_6).click()

    def click_pregnancy_7(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_7).click()

    def click_pregnancy_8(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_8).click()

    def click_pregnancy_9(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_9).click()

    def click_pregnancy_10(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_10).click()

    def click_pregnancy_11(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_11).click()

    def click_pregnancy_12(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_12).click()

    def click_pregnancy_13(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_13).click()

    def click_pregnancy_14(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_14).click()

    def click_pregnancy_15(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_15).click()

    def click_pregnancy_16(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_16).click()

    def click_pregnancy_17(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_17).click()

    def click_pregnancy_18(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_18).click()

    def click_pregnancy_19(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_19).click()

    def click_pregnancy_20(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_20).click()

    def click_pregnancy_21(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_21).click()

    def click_pregnancy_22(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_22).click()

    def click_pregnancy_23(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_23).click()

    def click_pregnancy_24(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_24).click()

    def click_pregnancy_25(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_25).click()

    def click_pregnancy_26(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_26).click()

    def click_pregnancy_27(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_27).click()

    def click_pregnancy_28(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_28).click()

    def click_pregnancy_29(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_29).click()

    def click_pregnancy_30(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_30).click()

    def click_pregnancy_31(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_31).click()

    def click_pregnancy_32(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_32).click()

    def click_pregnancy_33(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_33).click()

    def click_pregnancy_34(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_34).click()

    def click_pregnancy_35(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_35).click()

    def click_pregnancy_36(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_36).click()

    def click_pregnancy_37(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_37).click()

    def click_pregnancy_38(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_38).click()

    def click_pregnancy_39(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_39).click()

    def click_pregnancy_40(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_40).click()

    def click_pregnancy_41(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_41).click()

    def click_pregnancy_42(self):
        self.driver.find_element_by_xpath(self.PREGNANCY_42).click()

    def click_birth(self):
        self.driver.find_element_by_xpath(self.BIRTH).click()

    def click_kids(self):
        self.driver.find_element_by_xpath(self.KIDS).click()

    def click_kids_0(self):
        self.driver.find_element_by_xpath(self.KIDS_0).click()

    def click_kids_1_6(self):
        self.driver.find_element_by_xpath(self.KIDS_1_6).click()

    def click_kids_7_12(self):
        self.driver.find_element_by_xpath(self.KIDS_7_12).click()

    def click_kids_1_3(self):
        self.driver.find_element_by_xpath(self.KIDS_1_3_YEARS).click()

    def click_kids_3_7(self):
        self.driver.find_element_by_xpath(self.KIDS_3_7_YEARS).click()

    def click_kids_7(self):
        self.driver.find_element_by_xpath(self.KIDS_7_YEARS).click()


class BabyName(Component):
    SEARCH_INPUT = '//input[@id="id_title"]'
    SEARCH_SELECT = '//select[@id="id_origin"]'
    SEARCH_SELECT_OPTION = '//select[@id="id_origin"]/option'
    SEARCH_INPUT_GENDER_M = '//input[@id="id_gender_0"]'
    SEARCH_INPUT_GENDER_F = '//input[@id="id_gender_1"]'
    SEARCH_BUTTON = '//a[@class="pin-button pin-button_orange js-names-search-btn"]'
    CALENDAR_NAMES = '//a[@href="/names/namedays/"]'
    CALENDAR_NAMES_JAN = '//a[@href="/names/all/nameday/january/"]'
    CALENDAR_NAMES_FEB = '//a[@href="/names/all/nameday/february/"]'
    CALENDAR_NAMES_MAR = '//a[@href="/names/all/nameday/march/"]'
    CALENDAR_NAMES_APR = '//a[@href="/names/all/nameday/april/"]'
    CALENDAR_NAMES_MAY = '//a[@href="/names/all/nameday/may/"]'
    CALENDAR_NAMES_JUN = '//a[@href="/names/all/nameday/june/"]'
    CALENDAR_NAMES_JUL = '//a[@href="/names/all/nameday/july/"]'
    CALENDAR_NAMES_AUG = '//a[@href="/names/all/nameday/august/"]'
    CALENDAR_NAMES_SEP = '//a[@href="/names/all/nameday/september/"]'
    CALENDAR_NAMES_OCT = '//a[@href="/names/all/nameday/october/"]'
    CALENDAR_NAMES_NOV = '//a[@href="/names/all/nameday/november/"]'
    CALENDAR_NAMES_DEC = '//a[@href="/names/all/nameday/december/"]'
    NAMES_FOR_KUN = '//a[@href="/names/male/"]'
    NAMES_FOR_KUN_MAXIM = '//a[@href="/names/maksim/"]'
    NAMES_FOR_KUN_ARTYOM = '//a[@href="/names/artyom/"]'
    NAMES_FOR_KUN_ALEKSANDR = '//a[@href="/names/aleksandr/"]'
    NAMES_FOR_CHAN = '//a[@href="/names/female/"]'
    NAMES_FOR_CHAN_NASTYA = '//a[@href="/names/anastasiya/"]'
    NAMES_FOR_CHAN_DARYA = '//a[@href="/names/darya/"]'
    NAMES_FOR_CHAN_VIKTORIYA = '//a[@href="/names/viktoriya/"]'

    def search_name(self, name, origin='---------', gender='M'):
        elem = self.driver.find_element_by_xpath(self.SEARCH_INPUT)
        elem.send_keys(name)
        if origin != '---------':
            option = self.driver.find_element_by_xpath(self.SEARCH_SELECT_OPTION)
            for opt in option:
                if opt.text == origin:
                    opt.click()
        if gender != 'M':
            gen = self.driver.find_element_by_xpath(self.SEARCH_INPUT_GENDER_F)
            gen.click()
        self.driver.find_element_by_xpath(self.SEARCH_BUTTON).click()

    def click_calendar_names(self):
        self.driver.find_element_by_xpath(self.CALENDAR_NAMES).click()

    def click_calendar_names_jan(self):
        self.driver.find_element_by_xpath(self.CALENDAR_NAMES_JAN).click()

    def click_calendar_names_feb(self):
        self.driver.find_element_by_xpath(self.CALENDAR_NAMES_FEB).click()

    def click_calendar_names_mar(self):
        self.driver.find_element_by_xpath(self.CALENDAR_NAMES_MAR).click()

    def click_calendar_names_apr(self):
        self.driver.find_element_by_xpath(self.CALENDAR_NAMES_APR).click()

    def click_calendar_names_may(self):
        self.driver.find_element_by_xpath(self.CALENDAR_NAMES_MAY).click()

    def click_calendar_names_jun(self):
        self.driver.find_element_by_xpath(self.CALENDAR_NAMES_JUN).click()

    def click_calendar_names_jul(self):
        self.driver.find_element_by_xpath(self.CALENDAR_NAMES_JUL).click()

    def click_calendar_names_aug(self):
        self.driver.find_element_by_xpath(self.CALENDAR_NAMES_AUG).click()

    def click_calendar_names_sep(self):
        self.driver.find_element_by_xpath(self.CALENDAR_NAMES_SEP).click()

    def click_calendar_names_oct(self):
        self.driver.find_element_by_xpath(self.CALENDAR_NAMES_OCT).click()

    def click_calendar_names_nov(self):
        self.driver.find_element_by_xpath(self.CALENDAR_NAMES_NOV).click()

    def click_calendar_names_dec(self):
        self.driver.find_element_by_xpath(self.CALENDAR_NAMES_DEC).click()

    def click_names_for_kun(self):
        self.driver.find_element_by_xpath(self.NAMES_FOR_KUN).click()

    def click_name_for_kun_maxim(self):
        self.driver.find_element_by_xpath(self.NAMES_FOR_KUN_MAXIM).click()

    def click_name_for_kun_artyom(self):
        self.driver.find_element_by_xpath(self.NAMES_FOR_KUN_ARTYOM).click()

    def click_name_for_kun_aleksandr(self):
        self.driver.find_element_by_xpath(self.NAMES_FOR_KUN_ALEKSANDR).click()

    def click_names_for_chan(self):
        self.driver.find_element_by_xpath(self.NAMES_FOR_CHAN).click()

    def click_names_for_chan_anastasia(self):
        self.driver.find_element_by_xpath(self.NAMES_FOR_CHAN_NASTYA).click()

    def click_names_for_chan_darya(self):
        self.driver.find_element_by_xpath(self.NAMES_FOR_CHAN_DARYA).click()

    def click_names_for_chan_viktoria(self):
        self.driver.find_element_by_xpath(self.NAMES_FOR_CHAN_VIKTORIYA).click()


class Footer(Component):
    PLANING = '//table[@class="b-foot-nav__list"]/tbody/tr/td[1]/ul/li[@href="/planning/"]'
    PREGNANCY = '//table[@class="b-foot-nav__list"]/tbody/tr/td[1]/ul/li[@href="/pregnancy/"]'
    BIRTH = '//table[@class="b-foot-nav__list"]/tbody/tr/td[1]/ul/li[@href="/childbirth/"]'
    OVUL = '//table[@class="b-foot-nav__list"]/tbody/tr/td[1]/ul/li[@href="/ovul/"]'
    CONSULT = '//table[@class="b-foot-nav__list"]/tbody/tr/td[1]/ul/li[@href="https://health.mail.ru/consultation/"]'

    NEWBORN = '//table[@class="b-foot-nav__list"]/tbody/tr/td[2]/ul/li[@href="/baby/newborn/"]'
    MONTHS_1_6 = '//table[@class="b-foot-nav__list"]/tbody/tr/td[2]/ul/li[@href="/baby/1-6/"]'
    MONTHS_7_12 = '//table[@class="b-foot-nav__list"]/tbody/tr/td[2]/ul/li[@href="/baby/7-12/"]'
    YEARS_1_3 = '//table[@class="b-foot-nav__list"]/tbody/tr/td[2]/ul/li[@href="/baby/1-3/"]'
    YEARS_3_7 = '//table[@class="b-foot-nav__list"]/tbody/tr/td[2]/ul/li[@href="/child/"]'
    DETI_OLDER = '//table[@class="b-foot-nav__list"]/tbody/tr/td[2]/ul/li[@href="/teenager/"]'
    FAMILY = '//table[@class="b-foot-nav__list"]/tbody/tr/td[2]/ul/li[@href="/family/"]'
    CONSULT_2 = '//table[@class="b-foot-nav__list"]/tbody/tr/td[2]/ul/li[@href="https://health.mail.ru/consultation/"]'
    RECEIPT = '//table[@class="b-foot-nav__list"]/tbody/tr/td[2]/ul/li[@href="/recipes/"]'

    NEWS = '//table[@class="b-foot-nav__list"]/tbody/tr/td[3]/ul/li[@href="/news/"]'
    ARTICLES = '//table[@class="b-foot-nav__list"]/tbody/tr/td[3]/ul/li[@href="/articles/"]'
    TALES = '//table[@class="b-foot-nav__list"]/tbody/tr/td[3]/ul/li[@href="/birthstories/"]'

    FORUM = '//table[@class="b-foot-nav__list"]/tbody/tr/td[4]/ul/li[@href="/forum/"]'
    COMMUNITY = '//table[@class="b-foot-nav__list"]/tbody/tr/td[4]/ul/li[@href="/community/"]'
    KIDS_COMMUNITY = '//table[@class="b-foot-nav__list"]/tbody/tr/td[4]/ul/li[@href="/community/"]'
    LINES = '//table[@class="b-foot-nav__list"]/tbody/tr/td[4]/ul/li[@href="/lines/"]'
    RULES = '//table[@class="b-foot-nav__list"]/tbody/tr/td[4]/ul/li[@href="/forum/rules/"]'

    BIRTHING_CENTER = '//table[@class="b-foot-nav__list"]/tbody/tr/td[5]/ul/li[@href="/birthing_center/"]'
    CHOSING_NAMES = '//table[@class="b-foot-nav__list"]/tbody/tr/td[5]/ul/li[@href="/names/"]'


class Basement(Component):
    pass


class RightColumn(Component):
    pass
