import os
import unittest
import requests
import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.wait import WebDriverWait


class Page(object):
    BASE_URL = 'https://news.mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class Toolbar(Page):
    PATH = ''
    BASE_URL = 'https://news.mail.ru/'

    @property
    def leftToolbar(self):
        return LeftToolbar(self.driver)

    @property
    def searchNews(self):
        return SearchNews(self.driver)


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def getStatus(self, url):
        r = requests.get(url)
        return (int(r.status_code))

    def getURL(self):
        return self.driver.current_url


class LeftToolbar(Component):
    LOGO = 'pm-logo__link__pic'
    WEATHER = "clb17284889"
    USD = "clb17284908"
    EUR = "clb17284917"
    WEATHER_URL = "https://pogoda.mail.ru/prognoz/moskva/"
    USD_URL = "https://news.mail.ru/currency.html?charcode=USD"
    EUR_URL = "https://news.mail.ru/currency.html?charcode=EUR"

    def clickLogo(self):
        self.driver.find_element_by_class_name(self.LOGO).click()

    def clickWeather(self):
        self.driver.find_element_by_name(self.WEATHER).click()

    def clickUSD(self):
        self.driver.find_element_by_name(self.USD).click()

    def clickEUR(self):
        self.driver.find_element_by_name(self.EUR).click()


class SearchNews(Component):
    QUERY_URL = "https://news.mail.ru/search/?usid=90&q=null"
    SEARCH_ICON = '//span[@bem-id="95"]'

    def setQuery(self):
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("null")

    def clickSearchIcon(self):
        self.driver.find_element_by_xpath(self.SEARCH_ICON).click()

    def pressEnterKey(self):
        elem = self.driver.find_element_by_name("q")
        elem.send_keys(Keys.RETURN)

