# coding=utf-8
import os
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.remote.webdriver import WebDriver

from model import Model, AjaxLoader

class Page(object):
    def __init__(self, driver):
        self.driver = driver
        self.model = Model(self.driver)

    def waitUntilLoaded(self):
        AjaxLoader().waitToDisappear(self.driver)

    def checkPresence(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def checkContainerPresence(self, element, text):
        try:
            element.find_element(By.XPATH, "//span[text()='%s']" % text)
            return True
        except TimeoutException:
            return False


class MainPage(Page):
    login = os.environ.get("TP_LOGIN")
    password = os.environ.get("PASSWORD")

    def __init__(self, driver):
        self.driver = driver
        self.model = Model(self.driver)
        self.driver.get('http://ftest.tech-mail.ru/')

    def auth(self):
        self.driver.find_element(By.XPATH, "//a[text()='Вход для участников']").click()
        self.driver.find_element(By.XPATH, "//input[@name='login']").send_keys(self.login)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(self.password)
        self.driver.find_element(By.XPATH, "//span[text()='Войти']").click()
        self.checkPresence((By.XPATH, "//div[@class='dropdown-user']"))

class CabinetPage(Page):
    def __init__(self, driver):
        self.driver = driver
        self.model = Model(self.driver)
        self.driver.get('http://ftest.tech-mail.ru/profile/k.korolev')
      
    def addNote(self, text):
        addButton = self.model.getAddButton()
        addButton.click()
        self.waitUntilLoaded()

        noteInput = self.model.getNoteInput()
        noteInput.send_keys(text)

        saveButton = self.model.getSaveButton()
        saveButton.click()
        self.waitUntilLoaded()

    def getNote(self):
        noteInput = self.model.getNoteInput()
        return noteInput.text

    def logOut(self):
        dropdown = self.model.getUserDropdown()
        dropdown.click()
        self.waitUntilLoaded()

        self.driver.find_element(By.XPATH, "//li/a[text()='Выход']").click()
        self.waitUntilLoaded()

    def isNewAbout(self, text):
        return self.checkPresence((By.XPATH, "//p[text()='%s']" % text))

    def isNewNumber(self, text):
        return self.checkPresence((By.XPATH, "//a[@href='tel:%s']" % text))

    def isNewAccount(self, text):
        return self.checkPresence((By.XPATH, "//a[@href='http://ok.ru/profile/%s']" % text))

    def isExit(self):
        return self.checkPresence((By.XPATH, "//a[text()='Вход для участников']"))

    def isOpened(self):
        try:
            self.model.getCabinet()
        except TimeoutException:
            return False
        return True

class SettingsPage(Page):
    def __init__(self, driver):
        self.driver = driver
        self.model = Model(self.driver)
        self.driver.get('http://ftest.tech-mail.ru/settings/')

    def changeAbout(self, text):
        aboutInput = self.model.getAboutInput()
        aboutInput.clear()
        aboutInput.send_keys(text)

        saveButton = self.model.getSaveSettingsButton()
        saveButton.click()
        self.waitUntilLoaded()

    def changePhoneNumber(self, phoneNumber):
        phoneNumberInput = self.model.getPhoneNumberInput()
        phoneNumberInput.clear()
        phoneNumberInput.send_keys(phoneNumber)

        saveButton = self.model.getSaveSettingsButton()
        saveButton.click()
        self.waitUntilLoaded()

    def isOpened(self):
        try:
            self.model.getSettings()
        except TimeoutException:
            return False
        return True

class MessagePage(Page):
    def __init__(self, driver):
        self.driver = driver
        self.model = Model(self.driver)
        self.driver.get('http://ftest.tech-mail.ru/talk/')

    def isOpened(self):
        try:
            self.model.getMessages()
        except TimeoutException:
            return False
        return True

class AdditionalPage(Page):
    def __init__(self, driver):
        self.driver = driver
        self.model = Model(self.driver)
        self.driver.get('http://ftest.tech-mail.ru/settings/additional_info')

    def changeOKAccount(self, account):
        OKInput = self.model.getOKInput()
        OKInput.clear()
        OKInput.send_keys(account)

        saveButton = self.model.getSaveAdditionalButton()
        saveButton.click()
        self.waitUntilLoaded()