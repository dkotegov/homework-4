# -*- coding: utf-8 -*-

import unittest
import time
import datetime

from selenium import webdriver

from pages.main_page_pages import HeadMailPage
from pages.main_page_pages import PortalMenuToolbarPage
from pages.main_page_pages import PortalMenuSubmenuPage
from pages.main_page_pages import AdvertisingUnitPage
from pages.main_page_pages import BlockHoroPage

#тесты иногда падают когда что то на странице не догрузилось(чертов ajax)
#бывает падают тесты из за защиты мэйла на подбор пароля

def tune_driver():
    # self.driver = webdriver.Chrome('./chromedriver')
    driver = webdriver.Firefox()
    driver.get("https://horo.mail.ru/")
    driver.implicitly_wait(10)
    return driver

class HeadMailPageTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver()
        self.page = HeadMailPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def _test_links_head(self):
        urls = ["https://mail.ru","https://e.mail.ru","https://my.mail.ru",
                "http://ok.ru","https://games.mail.ru","http://love.mail.ru",
                "https://news.mail.ru","http://go.mail.ru"]

        for i in range(len(urls)):
            self.page.click_link(i)
            self.assertIn(urls[i], self.driver.current_url)
            self.driver.back()

    def _test_link_registration(self):
        self.page.click_link_registration()
        self.assertIn("https://e.mail.ru", self.driver.current_url)

    def _test_login_incorrect(self):
        self.page.login(login="ErrorError", password="ErrorError")

        text_login_incorrect = u"Неверное имя пользователя или пароль. Проверьте правильность введенных данных."
        text_color_login_incorrect = "rgba(234, 0, 0, 1)"

        if "https://e.mail.ru" not in self.driver.current_url:#при частом вводе некоректных данных кидает на другую страницу
            self.assertEquals(self.page.get_text_login_incorrect(),text_login_incorrect)
            self.assertEquals(self.page.get_color_text_login_incorrect(),text_color_login_incorrect)

    def _test_login_correct(self):
        login = "myLogin@list.ru"
        password = "myPassword"
        self.page.login(login, password)

        self.assertEquals(self.page.get_email_user_login_correct(), login.lower())

        self.page.logout()



class PortalMenuToolbarPageTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver()
        self.page = PortalMenuToolbarPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def _test_click_logo(self):
        self.page.click_logo()
        self.assertIn("https://lady.mail.ru/", self.driver.current_url)

    def _test_move_to_link(self):
        self.assertEquals(self.page.get_background_color_link(), u'transparent')
        self.page.move_to_link()
        time.sleep(10)
        self.assertEquals(self.page.get_background_color_link(), u'rgba(20, 127, 203, 1)')

#дальше работу ссылок не проверяю

class PortalMenuSubmenuPageTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver()
        self.page = PortalMenuSubmenuPage(self.driver)

    def _test_dropdown_move_to_show(self):
        self.assertFalse(self.page.dropdown_is_open())
        self.page.move_to_link()
        time.sleep(10)
        self.assertTrue(self.page.dropdown_is_open())

    def tearDown(self):
        self.driver.quit()


class AdvertisingUnitPageTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver()
        self.page = AdvertisingUnitPage(self.driver)

    def _test_click_all_links(self): #незнаю как получить url новой вкладки
        last_url = self.driver.current_url
        for selector in self.page.links:
            self.page.click_link(selector)
            time.sleep(10)
            self.assertNotEquals(last_url, self.driver.current_url)
            self.driver.back()

    def tearDown(self):
        self.driver.quit()


class BlockHoroTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = tune_driver()
        self.page = BlockHoroPage(self.driver)

    def _test_today_date(self):
        date = datetime.date.today()
        months = [
            u"Января",
            u"Февраля",
            u"Марта",
            u"Апреля",
            u"Мая",
            u"Июня",
            u"Июля",
            u"Августа",
            u"Сентября",
            u"Октября",
            u"Ноября",
            u"Декабря",
        ]
        date_site = self.page.get_date().split("\n")
        self.assertEquals(date.day, int(date_site[0]))
        self.assertEquals(months[date.month - 1].upper(), date_site[1].upper())

    def _test_horo_for_all(self):
        title = u"Гороскоп для всех знаков на сегодня"
        self.assertEquals(title, self.page.get_horo_title())

    def test_choice_date(self):
        title = u"Гороскоп для всех знаков на "
        date = [u"вчера", u"сегодня", u"завтра", u"неделю", u"месяц", u"2016 год"]
        for i in range(1, 6, 1):
            self.page.click_button_choice_date(i)
            full_title = title + date[i - 1]
            self.assertEquals(full_title, self.page.get_horo_title())

    def tearDown(self):
        self.driver.quit()




