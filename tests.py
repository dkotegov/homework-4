# coding=utf-8
import unittest
import random
import string

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.remote.webdriver import WebDriver

from page import MainPage, SettingsPage, MessagePage, CabinetPage, AdditionalPage
import os

class Test(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get("BROWSER")
        capability = {}

        if browser == "CHROME":
            capability = "CHROME"
        else:
            capability = "FIREFOX"

        self.browser = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, capability).copy()
        )

        self.browser.implicitly_wait(3)
        mainPage = MainPage(self.browser)
        mainPage.auth()
        self.user = mainPage.getUserName()

    # Отправка сообщения
    def test_message(self):
        cabinetPage = CabinetPage(self.browser, "http://ftest.tech-mail.ru/profile/o.venger")
        text = "".join( [random.choice(string.letters[:26]) for i in xrange(20)] )
        cabinetPage.sendMessage(text)

        messagePage = MessagePage(self.browser)
        self.assertTrue(messagePage.checkMessage(text))

    # Изменение информации об аккаунте Одноклассники
    def test_change_additional_info(self):
        additionalPage = AdditionalPage(self.browser)
        account = "".join( [random.choice(string.letters[:26]) for i in xrange(15)] )
        additionalPage.changeOKAccount(account)

        cabinetPage = CabinetPage(self.browser, self.user)
        self.assertTrue(cabinetPage.isNewAccount(account))

    # Изменения номера телефона
    def test_change_phone(self):
        settingsPage = SettingsPage(self.browser)
        phoneNumber = "".join( [str(random.choice([1, 2, 3, 4, 5])) for i in xrange(11)] )
        phoneNumber = "+" + phoneNumber
        settingsPage.changePhoneNumber(phoneNumber)

        cabinetPage = CabinetPage(self.browser, self.user)
        self.assertTrue(cabinetPage.isNewNumber(phoneNumber))

    # Изменение информации о себе
    def test_change_about(self):
        settingsPage = SettingsPage(self.browser)
        text = "".join( [random.choice(string.letters[:26]) for i in xrange(15)] )
        settingsPage.changeAbout(text)

        cabinetPage = CabinetPage(self.browser, self.user)
        self.assertTrue(cabinetPage.isNewAbout(text))

    # Добавление заметки
    def test_add_notes(self):
        cabinetPage = CabinetPage(self.browser, "http://ftest.tech-mail.ru/profile/k.korolev")
        cabinetPage.deleteNote()
        text = "".join( [random.choice(string.letters[:26]) for i in xrange(15)] )
        cabinetPage.addNote(text)
        note = cabinetPage.getNote()

        self.assertNotEqual(note, text)

    # Проверка открытия личного кабинета
    def test_open_cabinet(self):
        cabinetPage = CabinetPage(self.browser, self.user)
        self.assertTrue(cabinetPage.isOpened())

    # Логаут
    def test_logout(self):
        cabinetPage = CabinetPage(self.browser, self.user)
        cabinetPage.logOut()
        self.assertTrue(cabinetPage.isExit())

    # Проверка открытия экрана настроек
    def test_open_settings(self):
        settingsPage = SettingsPage(self.browser)
        self.assertTrue(settingsPage.isOpened())

    # Проверка открытия экрана сообщений
    def test_open_messages(self):
        messagePage = MessagePage(self.browser)
        self.assertTrue(messagePage.isOpened())

    def tearDown(self):
        self.browser.quit()
