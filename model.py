# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Model(object):
    def __init__(self, driver):
        self.driver = driver

    def getElementByPath(self, path):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(path)
        )

    def getDropdownByPath(self, path):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(path)
        )
        return element.find_element_by_class_name('nav-pills_dropdown__active__title')

    def getAreaByPath(self, path):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(path)
        )
        return element.find_element_by_class_name('input-text')

    def getPeriodSwitcher(self):
        return self.getElementByPath((By.XPATH, "//li/a[text()='Весь семестр']"))

    def getSheduleTable(self):
        return self.getElementByPath((By.XPATH, "//table[@class='schedule-timetable']"))

    def getSettings(self):
        return self.getElementByPath((By.XPATH, "//div[@class='settings']"))

    def getMessages(self):
        return self.getElementByPath((By.XPATH, "//table[@class='table table-talk']"))

    def getAddButton(self):
        return self.getElementByPath((By.XPATH, "//a[text()='Написать заметку']"))

    def getSaveButton(self):
        return self.getElementByPath((By.XPATH, "//button[text()='Сохранить']"))

    def getNoteInput(self):
        return self.getAreaByPath((By.XPATH, "//div[@id='usernote-form']"))

    def getAboutInput(self):
        return self.getAreaByPath((By.XPATH, "//div[@id='profile_about']"))

    def getCabinet(self):
        return self.getElementByPath((By.XPATH, "//div[@class='profile']"))

    def getUserDropdown(self):
        return self.getElementByPath((By.XPATH, "//div[@class='dropdown-user-trigger']"))

    def getScheduleElement(self):
        return self.getElementByPath((By.XPATH, "//tr[@class='schedule-timetable__item']"))

    def getDisciplineDropdown(self):
        return self.getDropdownByPath((By.XPATH, "//div[@class='schedule-filters__item schedule-filters__item_discipline']"))

    def getGroupDropdown(self):
        return self.getDropdownByPath((By.XPATH, "//div[@class='schedule-filters__item schedule-filters__item_group']"))

class AjaxLoader(object):
    def waitToDisappear(self, driver):
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[@class='icon-ajax-loader']"))
        )
