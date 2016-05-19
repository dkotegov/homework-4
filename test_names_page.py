# coding=utf-8

import os
import unittest

from selenium.webdriver import Remote, DesiredCapabilities

from page import NamesPage


class NamesTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        self.test_str = u'тест'

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_menu_logo(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        top_menu = names_page.menu

        top_menu.click_logo()

        self.assertEquals(top_menu.TITLE, top_menu.LOGO_TITLE)
        self.assertEquals(top_menu.TITLE, top_menu.get_title())

    def test_menu_forum(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        top_menu = names_page.menu

        top_menu.click_forum()
        self.assertEquals(top_menu.TITLE, top_menu.FORUM_TITLE)
        self.assertEquals(top_menu.TITLE, top_menu.get_title())

    def test_menu_receipt(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        top_menu = names_page.menu

        top_menu.click_receipt()
        self.assertEquals(top_menu.TITLE, top_menu.RECEIPT_TITLE)
        self.assertEquals(top_menu.TITLE, top_menu.get_title())

    def test_menu_calendar(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        top_menu = names_page.menu

        top_menu.click_calendar()
        self.assertEquals(top_menu.TITLE, top_menu.CALENDAR_TITLE)
        self.assertEquals(top_menu.TITLE, top_menu.get_title())

    def test_menu_rod_dom(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        top_menu = names_page.menu

        top_menu.click_rod_dom()
        self.assertEquals(top_menu.TITLE, top_menu.ROD_DOM_TITLE)
        self.assertEquals(top_menu.TITLE, top_menu.get_title())

    def test_search(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        top_menu = names_page.menu

        query = self.test_str
        top_menu.search(query)
        self.assertEquals(top_menu.TITLE, top_menu.SEARCH_TITLE)
        self.assertEquals(top_menu.TITLE, top_menu.get_title())

    def test_nav_family(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        nav = names_page.nav

        nav.click_family()
        self.assertEquals(nav.TITLE, nav.FAMILY_TITLE)
        self.assertEquals(nav.TITLE, nav.get_title())

    def test_nav_planning(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        nav = names_page.nav

        nav.click_planing()
        self.assertEquals(nav.TITLE, nav.PLANNING_TITLE)
        self.assertEquals(nav.TITLE, nav.get_title())

    def test_nav_planning_ovul(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        nav = names_page.nav

        nav.click_planing_day_ovulation()
        self.assertEquals(nav.TITLE, nav.OVUL_TITLE)
        self.assertEquals(nav.TITLE, nav.get_title())

    def test_nav_pregnancy(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        nav = names_page.nav

        nav.click_pregnancy()
        self.assertEquals(nav.TITLE, nav.PREGNANCY_TITLE)
        self.assertEquals(nav.TITLE, nav.get_title())

    def test_nav_pregnancy_1(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        nav = names_page.nav

        nav.click_pregnancy_1()
        self.assertEquals(nav.TITLE, nav.PREGNANCY_1_TITLE)
        self.assertEquals(nav.TITLE, nav.get_title())

    def test_nav_pregnancy_2(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        nav = names_page.nav

        nav.click_pregnancy_2()
        self.assertEquals(nav.TITLE, nav.PREGNANCY_2_TITLE)
        self.assertEquals(nav.TITLE, nav.get_title())

    def test_nav_pregnancy_3(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        nav = names_page.nav

        nav.click_pregnancy_3()
        self.assertEquals(nav.TITLE, nav.PREGNANCY_3_TITLE)
        self.assertEquals(nav.TITLE, nav.get_title())

    def test_nav_birth(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        nav = names_page.nav

        nav.click_birth()
        self.assertEquals(nav.TITLE, nav.BIRTH_TITLE)
        self.assertEquals(nav.TITLE, nav.get_title())

    def test_nav_kids(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        nav = names_page.nav

        nav.click_kids()
        self.assertEquals(nav.TITLE, nav.KIDS_TITLE)
        self.assertEquals(nav.TITLE, nav.get_title())

    def test_nav_kids_0(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        nav = names_page.nav

        nav.click_kids_0()
        self.assertEquals(nav.TITLE, nav.KIDS_TITLE_0)
        self.assertEquals(nav.TITLE, nav.get_title())

    def test_baby_name_search_with_empty_query(self):
        url = 'https://deti.mail.ru/names/male/'

        names_page = NamesPage(self.driver)
        names_page.open()

        baby_name = names_page.baby_name

        query = ""
        baby_name.search_name(query)
        self.assertEquals(baby_name.NAMES_FOR_KUN_URL, url)
        self.assertEquals(baby_name.TITLE, baby_name.NAMES_FOR_KUN_TITLE)
        self.assertEquals(baby_name.TITLE, baby_name.get_title())

    def test_baby_name_search(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        baby_name = names_page.baby_name

        query = self.test_str
        baby_name.search_name(query)
        self.assertEquals(baby_name.TITLE, baby_name.NAMES_FOR_KUN_TITLE)
        self.assertEquals(baby_name.TITLE, baby_name.get_title())

    def test_baby_name_search_with_gender_female(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        baby_name = names_page.baby_name

        query = self.test_str
        gender = 'F'
        baby_name.search_name(query, gender=gender)
        self.assertEquals(baby_name.TITLE, baby_name.NAMES_FOR_CHAN_TITLE)
        self.assertEquals(baby_name.TITLE, baby_name.get_title())

    def test_baby_name_search_with_gender_male(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        baby_name = names_page.baby_name

        query = self.test_str
        gender = 'M'
        baby_name.search_name(query, gender=gender)
        self.assertEquals(baby_name.TITLE, baby_name.NAMES_FOR_KUN_TITLE)
        self.assertEquals(baby_name.TITLE, baby_name.get_title())

    def test_baby_name_search_with_option(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        baby_name = names_page.baby_name

        query = self.test_str
        option = 'арабское'
        baby_name.search_name(query, option)
        self.assertEquals(baby_name.TITLE, baby_name.ARABIAN_NAME_FOR_KUN_TITLE)
        self.assertEquals(baby_name.TITLE, baby_name.get_title())

    def test_baby_calendar_name(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        baby_name = names_page.baby_name

        baby_name.click_calendar_names()
        self.assertEquals(baby_name.TITLE, baby_name.CALENDAR_NAMES_TITLE)
        self.assertEquals(baby_name.TITLE, baby_name.get_title())

    def test_baby_calendar_name_jan(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        baby_name = names_page.baby_name

        baby_name.click_calendar_names_jan()
        self.assertEquals(baby_name.TITLE, baby_name.CALENDAR_NAMES_JAN_TITLE)
        self.assertEquals(baby_name.TITLE, baby_name.get_title())

    def test_baby_calendar_name_feb(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        baby_name = names_page.baby_name

        baby_name.click_calendar_names_feb()
        self.assertEquals(baby_name.TITLE, baby_name.CALENDAR_NAMES_FEB_TITLE)
        self.assertEquals(baby_name.TITLE, baby_name.get_title())

    def test_baby_calendar_name_mar(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        baby_name = names_page.baby_name

        baby_name.click_calendar_names_mar()
        self.assertEquals(baby_name.TITLE, baby_name.CALENDAR_NAMES_MAR_TITLE)
        self.assertEquals(baby_name.TITLE, baby_name.get_title())

    def test_baby_name_for_boy(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        baby_name = names_page.baby_name

        baby_name.click_names_for_kun()
        self.assertEquals(baby_name.TITLE, baby_name.NAMES_FOR_KUN_TITLE)
        self.assertEquals(baby_name.TITLE, baby_name.get_title())

    def test_baby_name_for_boy_maksim(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        baby_name = names_page.baby_name

        baby_name.click_name_for_kun_maxim()
        self.assertEquals(baby_name.TITLE, baby_name.MAXIM_TITLE)
        self.assertEquals(baby_name.TITLE, baby_name.get_title())

    def test_baby_name_for_boy_artyom(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        baby_name = names_page.baby_name

        baby_name.click_name_for_kun_artyom()
        self.assertEquals(baby_name.TITLE, baby_name.ARTYOM_TITLE)
        self.assertEquals(baby_name.TITLE, baby_name.get_title())

    def test_baby_name_for_girl(self):
        names_page = NamesPage(self.driver)
        names_page.open()

        baby_name = names_page.baby_name

        baby_name.click_names_for_chan()
        self.assertEquals(baby_name.TITLE, baby_name.NAMES_FOR_CHAN_TITLE)
        self.assertEquals(baby_name.TITLE, baby_name.get_title())


