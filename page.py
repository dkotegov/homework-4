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
        #self.driver.get('file:///home/metalray33/testing/homework-4/%D0%93%D0%BB%D0%B0%D0%B2%D0%BD%D0%BE%D0%B5%20-%20%D0%A2%D0%B5%D1%85%D0%BD%D0%BE%D0%BF%D0%B0%D1%80%D0%BA@Mail.ru.html')
    
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

    def isNewAbout(self, text):
        return self.checkPresence((By.XPATH, "//a[text()='%s']" % text))

    def logOut(self):
        dropdown = self.model.getUserDropdown()
        dropdown.click()
        self.waitUntilLoaded()

        self.driver.find_element(By.XPATH, "//li/a[text()='Выход']").click()
        self.waitUntilLoaded()

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
        aboutInput.send_keys(text)

        saveButton = self.model.getSaveButton()
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
