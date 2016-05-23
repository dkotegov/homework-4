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

    @property
    def basement(self):
        return Basement(self.driver)

    @property
    def right_col(self):
        return RightColumn(self.driver)


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
    CONSULT = '//a[@title="Консультации"][1]'
    CONSULT_URL = 'https://health.mail.ru/consultation/'
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

    TITLE = ''
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
        self.SEARCH_URL = self.driver.current_url


class NavMenu(Component):
    FAMILY = '//li[@class="b-nav__item b-nav__item_red b-nav__item_family"]/a[@class="b-nav__item__title"]'
    PLANNING = '//li[@class="b-nav__item b-nav__item_blue b-nav__item_plan"]/a[@class="b-nav__item__title"]'
    PLANNING_DAY_OVULATION = '//li[@class="b-nav__item b-nav__item_blue b-nav__item_plan"]' \
                             '/div[@class="b-nav__item__links"]/a'
    PREGNANCY = '//li[@class="b-nav__item b-nav__item_green b-nav__item_preg"]/a[@class="b-nav__item__title"]'
    PREGNANCY_1 = '//a[@title="1 неделя беременности"]'
    BIRTH = '//li[@class="b-nav__item b-nav__item_yellow b-nav__item_birth"]/a[@class="b-nav__item__title"]'
    KIDS = '//li[@class="b-nav__item b-nav__item_orange b-nav__item_kids "]/a[@class="b-nav__item__title"]'

    TITLE = ''

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

    TITLE = ''

    NAMES_FOR_KUN_TITLE = u'Имена для мальчика - Выбираем имя ребенку - Дети Mail.Ru'
    NAMES_FOR_CHAN_TITLE = u'Имена для девочки - Выбираем имя ребенку - Дети Mail.Ru'
    ARABIAN_NAME_FOR_KUN_TITLE = u'Арабское имя для мальчика - Выбираем имя ребенку - Дети Mail.Ru'
    CALENDAR_NAMES_TITLE = u'Имена по святцам для мальчиков и девочек - по месяцам - Дети Mail.Ru'
    CALENDAR_NAMES_JAN_TITLE = u'Имена по святцам - Январь - для мальчиков и девочек - Дети Mail.Ru'
    MAXIM_TITLE = u'Значение и происхождение имени Максим - отзывы об именах для мальчика - Дети Mail.Ru'
    ARTYOM_TITLE = u'Значение и происхождение имени Артём - отзывы об именах для мальчика - Дети Mail.Ru'

    NAMES_FOR_KUN_URL = 'https://deti.mail.ru/names/male/'
    NAMES_FOR_CHAN_URL = 'https://deti.mail.ru/names/female/'

    def search_name(self, name, origin='---------', gender='M'):
        elem = self.driver.find_element_by_xpath(self.SEARCH_INPUT)
        elem.send_keys(name)
        if origin != '---------':
            select = Select(self.driver.find_element_by_xpath(self.SEARCH_SELECT))
            select.select_by_visible_text(origin)
        if gender != 'M':
            gen = self.driver.find_element_by_xpath(self.SEARCH_INPUT_GENDER_F)
            gen.click()
        self.driver.find_element_by_xpath(self.SEARCH_BUTTON).click()

    def click_calendar_names(self):
        self.driver.find_element_by_xpath(self.CALENDAR_NAMES).click()

    def click_calendar_names_jan(self):
        self.driver.find_element_by_xpath(self.CALENDAR_NAMES_JAN).click()

    def click_names_for_kun(self):
        self.driver.find_element_by_xpath(self.NAMES_FOR_KUN).click()
        self.TITLE = self.driver.title

    def click_name_for_kun_maxim(self):
        self.driver.find_element_by_xpath(self.NAMES_FOR_KUN_MAXIM).click()
        self.TITLE = self.driver.title

    def click_names_for_chan(self):
        self.driver.find_element_by_xpath(self.NAMES_FOR_CHAN).click()
        self.TITLE = self.driver.title

    def click_names_for_chan_anastasia(self):
        self.driver.find_element_by_xpath(self.NAMES_FOR_CHAN_NASTYA).click()
        self.TITLE = self.driver.title


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
