# coding=utf-8
import os

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

    def waitAjax(self):
        AjaxLoader().waitToDisappear(self.driver)

    def checkExist(self, path):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(path)
            )
            return True
        except TimeoutException:
            return False

class MainPage(Page):
    login = os.environ.get("TP_LOGIN")
    password = os.environ.get("TP_PASSWORD")

    def __init__(self, driver):
        self.driver = driver
        self.model = Model(self.driver)
        self.driver.get('http://ftest.tech-mail.ru/')

    def auth(self):
        self.driver.find_element(By.XPATH, "//a[text()='Вход для участников']").click()
        self.driver.find_element(By.XPATH, "//input[@name='login']").send_keys(self.login)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(self.password)
        self.driver.find_element(By.XPATH, "//span[text()='Войти']").click()
        self.checkExist((By.XPATH, "//div[@class='dropdown-user']"))

    def getUserName(self):
        user = self.model.getUser()
        return user.get_attribute('href')

class CabinetPage(Page):
    def __init__(self, driver, name):
        self.driver = driver
        self.model = Model(self.driver)
        self.driver.get(name)

    def deleteNote(self):
        note = self.model.getNote()
        print note
        if note.text != "":
            delete = self.model.getDelete()
            if (delete != None):
                delete.click()
        self.waitAjax()
      
    def addNote(self, text):
        addButton = self.model.getAddButton()
        addButton.click()
        self.waitAjax()

        noteInput = self.model.getNoteInput()
        noteInput.send_keys(text)

        saveButton = self.model.getSaveButton()
        saveButton.click()
        self.waitAjax()

    def getNote(self):
        note = self.model.getNoteInput()
        # При self.model.getNote() отдает AssertionError хотя строки одинаковые 
        return note.text

    def logOut(self):
        dropdown = self.model.getUserDropdown()
        dropdown.click()
        self.waitAjax()

        self.driver.find_element(By.XPATH, "//li/a[text()='Выход']").click()
        self.waitAjax()

    def sendMessage(self, text):
        messageButton = self.model.getMessageButton()
        messageButton.click()
        self.waitAjax()

        messageInput = self.model.getMessageInput()
        messageInput.send_keys(text)

        sendButton = self.model.getSendButton()
        sendButton.click()
        self.waitAjax()

    def isNewAbout(self, text):
        return self.checkExist((By.XPATH, "//p[text()='%s']" % text))

    def isNewNumber(self, text):
        return self.checkExist((By.XPATH, "//a[@href='tel:%s']" % text))

    def isNewAccount(self, text):
        return self.checkExist((By.XPATH, "//a[@href='http://ok.ru/profile/%s']" % text))

    def isExit(self):
        return self.checkExist((By.XPATH, "//a[text()='Вход для участников']"))

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
        self.waitAjax()

    def changePhoneNumber(self, phoneNumber):
        phoneNumberInput = self.model.getPhoneNumberInput()
        phoneNumberInput.clear()
        phoneNumberInput.send_keys(phoneNumber)

        saveButton = self.model.getSaveSettingsButton()
        saveButton.click()
        self.waitAjax()

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

    def checkMessage(self, text):
        return self.checkExist((By.XPATH, "//*[contains(text(), '%s')]" % text))

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
        self.waitAjax()