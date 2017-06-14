# coding=utf-8
from selenium import webdriver
import unittest
import random
import string

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver

from page import MainPage, SettingsPage, MessagePage, CabinetPage
import os

#test_calendar_scroll
#test_subject_info_popup

# Создание заметки
# Изменение заметки
# Удаление заметки
# Изменение информации о себе
# Написание сообщения
# Добавление в друзья
# Удаление из друзей

class TestSchedule(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get("BROWSER")
        capability = {}
        if browser == "CHROME":
            capability = DesiredCapabilities.CHROME
        else:
            capability = DesiredCapabilities.FIREFOX
        self.browser = webdriver.Firefox(executable_path='./geckodriver')
        self.browser.implicitly_wait(3)
        main_page = MainPage(self.browser)
        main_page.auth()

    def test_change_about(self):
        settingsPage = SettingsPage(self.browser)
        text = "Some simle text about me"
        text = "".join( [random.choice(string.letters[:26]) for i in xrange(15)] )
        settingsPage.changeAbout(text)

        cabinetPage = CabinetPage(self.browser)
        self.assertTrue(cabinetPage.isNewAbout(text))

    """def test_add_notes(self):
        cabinetPage = CabinetPage(self.browser)
        text = "".join( [random.choice(string.letters[:26]) for i in xrange(15)] )
        cabinetPage.addNote(text)
        self.assertNotEqual(cabinetPage.getNote(), text)

    # Логаут
    def test_logout(self):
        cabinetPage = CabinetPage(self.browser)
        cabinetPage.logOut()
        self.assertTrue(cabinetPage.isExit())

    # Проверка открытия личного кабинета
    def test_open_cabinet(self):
        cabinetPage = CabinetPage(self.browser)
        self.assertTrue(cabinetPage.isOpened())

    # Проверка открытия экрана настроек
    def test_open_settings(self):
        settingsPage = SettingsPage(self.browser)
        self.assertTrue(settingsPage.isOpened())

    # Проверка открытия экрана сообщений
    def test_open_messages(self):
        messagePage = MessagePage(self.browser)
        self.assertTrue(messagePage.isOpened())"""

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
