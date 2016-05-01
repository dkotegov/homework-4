# -*- coding: utf-8 -*-

import unittest
import datetime
import os

from helpers import tune_driver

from pages.main_page_pages import HeadMailPage
from pages.main_page_pages import PortalMenuToolbarPage
from pages.main_page_pages import PortalMenuSubmenuPage
from pages.main_page_pages import AdvertisingUnitPage
from pages.main_page_pages import BlockHoroPage
from pages.main_page_pages import ZodiacSignPage
from pages.main_page_pages import SearchDreamPage
from pages.main_page_pages import LunisolarForecastPage
from pages.main_page_pages import SubscriptionUnitPage
from pages.main_page_pages import LadyUnitPage

LOGIN = os.environ['HW4LOGIN']
PASSWORD = os.environ['HW4PASSWORD']

page = "https://horo.mail.ru/"


def _get_zodiac_sign_by_date(month, day):
    if (month == 3 and 21 <= day <= 31) or (month == 4 and 1 <= day <= 20):
        return u"Овен"
    if (month == 4 and 21 <= day <= 30) or (month == 5 and 1 <= day <= 20):
        return u"Телец"
    if (month == 5 and 21 <= day <= 31) or (month == 6 and 1 <= day <= 20):
        return u"Близнецы"
    if (month == 6 and 21 <= day <= 30) or (month == 7 and 1 <= day <= 22):
        return u"Рак"
    if (month == 7 and 23 <= day <= 31) or (month == 8 and  1 <= day <= 22):
        return u"Лев"
    if (month == 8  and 23 <= day <= 31) or (month == 9 and  1 <= day <= 23):
        return u"Дева"
    if (month == 9 and 24 <= day <= 30) or (month == 10 and  1 <= day <= 23):
        return u"Весы"
    if (month == 10 and 24 <= day <= 31) or (month == 11 and  1 <= day <= 21):
        return u"Скорпион"
    if (month == 11 and 22 <= day <= 30) or (month == 12 and 1 <= day <= 21):
        return u"Стрелец"
    if (month == 12 and 22 <= day <= 31) or (month == 1 and  1 <= day <= 19):
        return u"Козерог"
    if (month == 1 and 22 <= day <= 30) or (month == 2 and 1 <= day <= 18):
        return u"Водолей"
    if (month == 2 and 19 <= day <= 29) or (month == 3 and 1 <= day <= 20):
        return u"Рыбы"

_months = (
    u"января",
    u"февраля",
    u"марта",
    u"апреля",
    u"мая",
    u"июня",
    u"июля",
    u"августа",
    u"сентября",
    u"октября",
    u"ноября",
    u"декабря",
)

_alphabet = (
    "a",
    "b",
    "v",
    "g",
    "d",
    "e",
    "zh",
    "z",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "f",
    "h",
    "ts",
    "ch",
    "sh",
    "shh",
    "je",
    "ju",
    "ja",
)

class HeadMailPageTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver(page)
        self.page = HeadMailPage(self.driver)

    def test_links_head(self):
        for url in self.page.urls:
            self.page.click_link(url)
            self.assertIn(url, self.driver.current_url)
            self.driver.back()

    def test_link_registration(self):
        self.page.click_link_registration()
        self.assertIn("https://e.mail.ru", self.driver.current_url)

    def test_login_incorrect(self):
        self.page.login(login="ERROR", password="ERROR")
        self.assertIn("https://account.mail.ru/user/login", self.driver.current_url)
        text_error = u"Неверное имя пользователя или пароль. Проверьте правильность введенных данных."
        self.assertEquals(self.page.get_text_error_login(), text_error)

    def test_login_correct(self):
        self.page.login(LOGIN, PASSWORD)
        self.assertEquals(self.page.get_email_user_login_correct(), LOGIN.lower())

    def tearDown(self):
        self.driver.quit()


class PortalMenuToolbarPageTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver(page)
        self.page = PortalMenuToolbarPage(self.driver)

    def test_click_logo(self):
        self.page.click_logo()
        self.assertIn("https://lady.mail.ru/", self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

class PortalMenuSubmenuPageTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver(page)
        self.page = PortalMenuSubmenuPage(self.driver)

    def test_dropdown_move_to_show(self):
        self.assertFalse(self.page.dropdown_is_open())
        self.page.move_to_link()
        self.page.wait_show_dropdown()
        self.assertTrue(self.page.dropdown_is_open())

    def tearDown(self):
        self.driver.quit()


class AdvertisingUnitPageTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver(page)
        self.page = AdvertisingUnitPage(self.driver)

    def test_click_all_links(self):
        last_url = self.driver.current_url
        for selector in self.page.links:
            self.page.open_advertising(selector)
            self.assertNotEquals(last_url, self.driver.current_url)
            self.page.close_advertising()

    def test_hide_advertising(self):
        self.page.move_to_advertising()
        self.page.hide_advertising()

        text = u"Спасибо. Объявление скрыто."
        self.assertEquals(self.page.get_baner_text(), text)


    def tearDown(self):
       self.driver.quit()


class BlockHoroTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver(page)
        self.page = BlockHoroPage(self.driver)

    def test_today_date(self):
        date = datetime.date.today()
        date_site = self.page.get_date().split("\n")
        day_site = int(date_site[0])
        month_site = date_site[1].upper()

        month_current = _months[date.month - 1].upper()

        self.assertEquals(date.day, day_site)
        self.assertEquals(month_current, month_site)

    def test_horo_for_all(self):
        title = u"Гороскоп для всех знаков на сегодня"
        self.assertEquals(title, self.page.get_horo_title())

    def test_choice_date(self):
        title = u"Гороскоп для всех знаков на "
        date = [u"вчера", u"сегодня", u"завтра", u"неделю", u"месяц", u"2016 год"]
        for i in range(6):
            self.page.click_button_choice_date(i)
            full_title = title + date[i]
            self.assertEquals(full_title, self.page.get_horo_title())

    def test_zodiac_sign(self):
        head_mail_page = HeadMailPage(self.driver)
        head_mail_page.login(LOGIN, PASSWORD)

        date_birth = self.page.get_date_birth().split(" ")
        day = int(date_birth[0])
        month = _months.index(date_birth[1]) + 1

        zodiac_sing = self.page.get_zodiac_sign()
        self.assertEquals(zodiac_sing, _get_zodiac_sign_by_date(month,day))

    def tearDown(self):
        self.driver.quit()

class ZodiacSignTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver(page)
        self.page = ZodiacSignPage(self.driver)

    def test_select_date(self):
        day = 2
        month = 4
        year = 1999
        self.page.select_date(day,month,year)
        self.page.click_all_horo()

        block_horo_page = BlockHoroPage(self.driver)
        zodiac_sing = block_horo_page.get_zodiac_sign()

        self.assertEquals(zodiac_sing, _get_zodiac_sign_by_date(month,day))

    def tearDown(self):
        self.driver.quit()

class SearchDreamTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver(page)
        self.page = SearchDreamPage(self.driver)

    def test_search_dream(self):
        dream = "testDream"
        self.page.search_by_text(dream)

        self.assertIn(dream, self.driver.current_url)

    def test_search_alphabet(self):
        for character_index in range(29):
            character = _alphabet[character_index]
            self.page.search_by_alphabet(character_index)
            self.assertIn("https://horo.mail.ru/sonnik/" + character + "/", self.driver.current_url)
            self.driver.back()

    def tearDown(self):
        self.driver.quit()


class LunisolarForecastTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver(page)
        self.page = LunisolarForecastPage(self.driver)

    def test_check_date(self):
        date = datetime.date.today()
        date_site = self.page.get_date().split("\n")
        day_site = int(date_site[0])
        month_site = date_site[1].upper()

        month_current = _months[date.month - 1].upper()

        self.assertEquals(date.day, day_site)
        self.assertEquals(month_current, month_site)

    def tearDown(self):
        self.driver.quit()

class SubscriptionUnitTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver(page)
        self.page = SubscriptionUnitPage(self.driver)
        self.url_vk = "https://vk.com/ladymailru"
        self.url_facebook = "https://www.facebook.com/lady.mail.ru?ref=bookmarks"
        self.url_ok = "http://ok.ru/ladymailru"

    def test_go_group_vk(self):
        self.page.go_group_vk()
        self.assertEqual(self.driver.current_url, self.url_vk)

    def test_go_group_facebook(self):
        self.page.go_group_facebook()
        self.assertEqual(self.driver.current_url, self.url_facebook)

    def test_go_group_ok(self):
        self.page.go_group_ok()
        self.assertEqual(self.driver.current_url, self.url_ok)

    def test_subscription_horo(self):
        head_mail_page = HeadMailPage(self.driver)
        head_mail_page.login(LOGIN, PASSWORD)

        if self.page.is_subscription_horo():
            self.page.unsubscribe_horo()

        self.page.subscribe_horo()
        self.assertTrue(self.page.is_subscription_horo())

    def tearDown(self):
        self.driver.quit()


class LadyUnitTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver(page)
        self.page = LadyUnitPage(self.driver)

    def test_scale_image(self):
        for index in range(4):
            self.assertEquals(self.page.get_scale_image(index), u'none')
            self.page.move_to_image(index)
            self.assertEquals(self.page.get_scale_image(index), u'matrix(1.02, 0, 0, 1.02, 0, 0)')

    def test_slider(self):
        left = self.page.get_transform(0)
        center = self.page.get_transform(1)
        right = self.page.get_transform(2)
        self.page.click_slider_left()

        self.assertEquals(self.page.get_transform(0), right)
        self.assertEquals(self.page.get_transform(2), center)
        self.assertEquals(self.page.get_transform(1), left)

        self.page.click_slider_right()

        self.assertEquals(self.page.get_transform(0), left)
        self.assertEquals(self.page.get_transform(2), right)
        self.assertEquals(self.page.get_transform(1), center)

    def tearDown(self):
        self.driver.quit()