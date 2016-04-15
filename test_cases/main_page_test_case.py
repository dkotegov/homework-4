# -*- coding: utf-8 -*-

import unittest

from selenium import webdriver
from pages.headpage import HeadPage

#тесты иногда падают когда что то на странице не догрузилось(чертов ajax)
#бывает падают тесты из за защиты мэйла на подбор пароля

class MainPageTestCase(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Chrome('./chromedriver')
        self.driver = webdriver.Firefox()
        self.driver.get("https://horo.mail.ru/")
        self.driver.implicitly_wait(10)
        self.head_page = HeadPage(self.driver)

    def test_links_head(self):
        urls = ["https://mail.ru","https://e.mail.ru","https://my.mail.ru",
                "http://ok.ru","https://games.mail.ru","http://love.mail.ru",
                "https://news.mail.ru","http://go.mail.ru"]

        for i in range(len(urls)):
            self.head_page.clik_link(i)
            self.assertIn(urls[i], self.driver.current_url)
            self.driver.back()

    def _test_link_registration(self):
        self.head_page.click_link_registraition();
        self.assertIn("https://e.mail.ru", self.driver.current_url)

    def _test_login_incorrect(self):
        self.head_page.login(login="ErrorError", password="ErrorError")

        text_login_incorrect = u"Неверное имя пользователя или пароль. Проверьте правильность введенных данных."
        text_color_login_incorrect = "rgba(234, 0, 0, 1)"

        if "https://e.mail.ru" not in self.driver.current_url:#при частом вводе некоректных данных кидает на другую страницу
            self.assertEquals(self.head_page.get_text_login_incorrect(),text_login_incorrect)
            self.assertEquals(self.head_page.get_color_text_login_incorrect(),text_color_login_incorrect)

    def _test_login_correct(self):
        login = "myLogin@list.ru"
        password = "myPassword"
        self.head_page.login(login, password)

        self.assertEquals(self.head_page.get_email_user_login_correct(), login.lower())

        self.head_page.logout()

    def tearDown(self):
        pass
        self.driver.quit()


