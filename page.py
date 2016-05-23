# -*- coding: utf-8 -*-

import urlparse

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


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


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title


class TopMenu(Component):
    LOGO = '//a[@class="pm-logo__link"]'
    FORUM = '//a[@title="Форум"][1]'
    NAMES = '//a[@title="Имена"]'
    RECEIPT = '//a[@title="Рецепты"]'
    CALENDAR = '//a[@title="Календарь развития"]'
    ROD_DOM = '//a[@title="Роддома"]'
    SEARCH_ICON = '//span[@class="js-link pm-toolbar__button__inner  pm-toolbar__button__inner_notext"]'
    SEARCH_INPUT = '//input[@name="q"]'
    SEARCH_SUBMIT = '//button[@class="class="js-submit-button pm-toolbar__' \
                    'search__button__input  pm-toolbar__search__button__' \
                    'input_expandable pm-toolbar__search__button__input_not-adaptive""]'

    SEARCH_URL = ''

    BASE_TITLE = u'Выбираем имя ребенку - Справочник имен - Дети Mail.Ru'
    LOGO_TITLE = u'Все о беременности, рождении ребенка, развитии и воспитании детей - детский портал - Дети Mail.Ru'
    FORUM_TITLE = u'Форум - Дети Mail.Ru'
    CONSULT_TITLE = u'Консультации врачей онлайн - консультации по интернет, горячая линия на Здоровье Mail.Ru'
    NAMES_TITLE = u'Выбираем имя ребенку - Справочник имен - Дети Mail.Ru'
    RECEIPT_TITLE = u'Рецепты для детей - Дети Mail.Ru'
    CALENDAR_TITLE = u'Развитие ребенка до 1 месяца, статьи на тему, этапы развития детей - Дети Mail.Ru'
    ROD_DOM_TITLE = u'Родильные дома - Учреждения - Дети Mail.Ru'
    ALL_ABOUT_TITLE = u'Анатомия грудного вскармливания: что, как и почему?'
    SEARCH_TITLE = u'Поиск - Дети Mail.Ru'

    def click_logo(self):
        self.driver.find_element_by_xpath(self.LOGO).click()

    def click_forum(self):
        self.driver.find_element_by_xpath(self.FORUM).click()

    def click_names(self):
        self.driver.find_element_by_xpath(self.NAMES).click()

    def click_receipt(self):
        self.driver.find_element_by_xpath(self.RECEIPT).click()

    def click_calendar(self):
        self.driver.find_element_by_xpath(self.CALENDAR).click()

    def click_rod_dom(self):
        self.driver.find_element_by_xpath(self.ROD_DOM).click()

    def search(self, query):
        self.driver.find_element_by_xpath(self.SEARCH_ICON).click()
        query_input = self.driver.find_element_by_xpath(self.SEARCH_INPUT)
        query_input.send_keys(query)
        query_input.send_keys(Keys.RETURN)
        self.SEARCH_URL = self.driver.current_url


class NavMenu(Component):
    FAMILY = '//a[@href="/family/" and @class="b-nav__item__title"]'
    PLANNING = '//a[@href="/planning/" and @class="b-nav__item__title"]'
    PLANNING_DAY_OVULATION = '//a[@href="/ovul/" and @class="b-nav__item__link "]'
    PREGNANCY = '//a[@href="/pregnancy/" and @class="b-nav__item__title"]'
    PREGNANCY_1 = '//a[@href="/pregnancy/week-1/" and @class="b-nav__weeks__link js-tooltip-pin "]'
    BIRTH = '//a[@href="/childbirth/" and @class="b-nav__item__title"]'
    KIDS = '//a[@href="/baby/newborn/" and @class="b-nav__item__title"]'

    FAMILY_TITLE = u'Статьи для всей семьи - Дети Mail.Ru'
    PLANNING_TITLE = u'Календарь планирования беременности - все о планировании беременности на Дети Mail.Ru'
    OVUL_TITLE = u'Календарь овуляции - бесплатный онлайн-калькулятор - женский календарь - Дети Mail.Ru'
    PREGNANCY_TITLE = u'Календарь беременности - все о беременности - Дети Mail.Ru'
    PREGNANCY_1_TITLE = u'1 неделя беременности - что происходит, симптомы, ощущения, признаки - Дети Mail.Ru'
    BIRTH_TITLE = u'Рассчитать дату родов по последней менструации - Дети Mail.Ru'
    KIDS_TITLE = u'Развитие ребенка до 1 месяца, статьи на тему, этапы развития детей - Дети Mail.Ru'

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

    def click_birth(self):
        self.driver.find_element_by_xpath(self.BIRTH).click()

    def click_kids(self):
        self.driver.find_element_by_xpath(self.KIDS).click()


class BabyName(Component):
    SEARCH_INPUT = '//input[@id="id_title"]'
    SEARCH_SELECT = '//select[@id="id_origin"]'
    SEARCH_SELECT_OPTION = '//select[@id="id_origin"]/option'
    SEARCH_INPUT_GENDER_M = '//input[@id="id_gender_0"]'
    SEARCH_INPUT_GENDER_F = '//input[@id="id_gender_1"]'
    SEARCH_BUTTON = '//a[@class="pin-button pin-button_orange js-names-search-btn"]'
    CALENDAR_NAMES = '//a[@href="/names/namedays/"]'
    CALENDAR_NAMES_JAN = '//a[@href="/names/all/nameday/january/"]'
    NAMES_FOR_KUN = '//a[@href="/names/male/"]'
    NAMES_FOR_KUN_MAXIM = '//a[@href="/names/maksim/"]'
    NAMES_FOR_CHAN = '//a[@href="/names/female/"]'
    NAMES_FOR_CHAN_NASTYA = '//a[@href="/names/anastasiya/"]'

    NAMES_FOR_KUN_TITLE = u'Имена для мальчика - Выбираем имя ребенку - Дети Mail.Ru'
    NAMES_FOR_CHAN_TITLE = u'Имена для девочки - Выбираем имя ребенку - Дети Mail.Ru'
    ARABIAN_NAME_FOR_KUN_TITLE = u'Арабское имя для мальчика - Выбираем имя ребенку - Дети Mail.Ru'
    CALENDAR_NAMES_TITLE = u'Имена по святцам для мальчиков и девочек - по месяцам - Дети Mail.Ru'
    CALENDAR_NAMES_JAN_TITLE = u'Имена по святцам - Январь - для мальчиков и девочек - Дети Mail.Ru'
    MAXIM_TITLE = u'Значение и происхождение имени Максим - отзывы об именах для мальчика - Дети Mail.Ru'

    NAMES_FOR_KUN_URL = 'https://deti.mail.ru/names/male/'
    NAMES_FOR_CHAN_URL = 'https://deti.mail.ru/names/female/'

    def search_name(self, name, origin=None, gender=None):
        elem = self.driver.find_element_by_xpath(self.SEARCH_INPUT)
        elem.send_keys(name)
        if origin:
            select = Select(self.driver.find_element_by_xpath(self.SEARCH_SELECT))
            select.select_by_visible_text(origin)
        if gender:
            gen = self.driver.find_element_by_xpath(self.SEARCH_INPUT_GENDER_F)
            gen.click()
        self.driver.find_element_by_xpath(self.SEARCH_BUTTON).click()

    def click_calendar_names(self):
        self.driver.find_element_by_xpath(self.CALENDAR_NAMES).click()

    def click_calendar_names_jan(self):
        self.driver.find_element_by_xpath(self.CALENDAR_NAMES_JAN).click()

    def click_names_for_kun(self):
        self.driver.find_element_by_xpath(self.NAMES_FOR_KUN).click()

    def click_name_for_kun_maxim(self):
        self.driver.find_element_by_xpath(self.NAMES_FOR_KUN_MAXIM).click()

    def click_names_for_chan(self):
        self.driver.find_element_by_xpath(self.NAMES_FOR_CHAN).click()

    def click_names_for_chan_anastasia(self):
        self.driver.find_element_by_xpath(self.NAMES_FOR_CHAN_NASTYA).click()


class Footer(Component):
    PLANNING = '//a[@href="/planning/" and @name="clb1682426"]'
    PREGNANCY = '//a[@href="/pregnancy/" and @name="clb1682426"]'

    NEWBORN = '//a[@href="/baby/newborn/" and @name="clb1682426"]'
    FAMILY = '//a[@href="/family/" and @name="clb1682426"]'

    FORUM = '//a[@href="/forum/" and @name="clb1682426"]'
    COMMUNITY = '//a[@href="/community/" and @name="clb1682426"]'

    BIRTHING_CENTER = '//a[@href="/birthing_center/" and @name="clb1682426"]'
    CHOSING_NAMES = '//a[@href="/names/" and @name="clb1682426"]'

    FAMILY_TITLE = u'Статьи для всей семьи - Дети Mail.Ru'
    PLANNING_TITLE = u'Календарь планирования беременности - все о планировании беременности на Дети Mail.Ru'
    PREGNANCY_TITLE = u'Календарь беременности - все о беременности - Дети Mail.Ru'
    FORUM_TITLE = u'Форум - Дети Mail.Ru'
    COMMUNITY_TITLE = u'Наше сообщество - Дети Mail.Ru'
    BIRTHING_CENTER_TITLE = u'Родильные дома - Учреждения - Дети Mail.Ru'
    CHOSING_NAMES_TITLE = u'Выбираем имя ребенку - Справочник имен - Дети Mail.Ru'

    def click_planing(self):
        self.driver.find_element_by_xpath(self.PLANNING).click()

    def click_pregnancy(self):
        self.driver.find_element_by_xpath(self.PREGNANCY).click()

    def click_family(self):
        self.driver.find_element_by_xpath(self.FAMILY).click()

    def click_forum(self):
        self.driver.find_element_by_xpath(self.FORUM).click()

    def click_community(self):
        self.driver.find_element_by_xpath(self.COMMUNITY).click()

    def click_birthing_center(self):
        self.driver.find_element_by_xpath(self.BIRTHING_CENTER).click()

    def click_choosing_names(self):
        self.driver.find_element_by_xpath(self.CHOSING_NAMES).click()
