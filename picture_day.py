# -*- coding: utf-8 -*-

import os

import unittest
import urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

import requests

class Page(object):
    BASE_URL = 'https://news.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

class Component(object):

    def __init__(self, driver):
        self.driver = driver

    def get_status(self, url):
        r = requests.get(url)
        return (int(r.status_code))

    def get_url(self):
        return self.driver.current_url

    def time_out(self, driver):
        self.driver.set_page_load_timeout(20)

    def click_header(self, header):
        self.driver.find_element_by_xpath(header).click()

    def get_href(self, path):
        href = self.driver.find_element_by_xpath(path).get_attribute('href') 
        return href

    def clickHeader(self, header, header_url):
        header_url = self.driver.find_element_by_xpath(header).get_attribute('href')       
        self.driver.find_element_by_xpath(header).click()       
        return header_url

    def clickBody(self, body, body_url):
        body_url = self.driver.find_element_by_xpath(body).get_attribute('href')        
        self.driver.find_element_by_xpath(body).click() 
        return body_url

    def clickSmall(self, small, small_url):
        small_url = self.driver.find_element_by_xpath(small).get_attribute('href')              
        self.driver.find_element_by_xpath(small).click()    
        return small_url

    def clickCard(self, card, card_url):
        card_url = self.driver.find_element_by_xpath(card).get_attribute('href')
        self.driver.find_element_by_xpath(card).click()
        return card_url

    def clickPhoto(self, photo, photo_url):
        photo_url = self.driver.find_element_by_xpath(photo).get_attribute('href')
        self.driver.find_element_by_xpath(photo).click()
        return photo_url

class PictureDay(Page):

    PATH = ''
    BASE_URL = 'http://news.mail.ru/'

    @property
    def main_news(self):
        return MainNews(self.driver)

    @property
    def moscow_news(self):
        return MoscowNews(self.driver)
    
    @property
    def politics(self):
        return Politics(self.driver)

    @property
    def economics(self):
        return Economics(self.driver)

    @property
    def society(self):
        return Society(self.driver)

    @property
    def events(self):
        return Events(self.driver)

    @property
    def helps(self):
        return Helps(self.driver)

    @property
    def photo(self):
        return Photo(self.driver)
    
    @property
    def health(self):
        return Health(self.driver)
    
    @property
    def auto(self):
        return Auto(self.driver)
    
    @property
    def lady(self):
        return Lady(self.driver)

    @property
    def cinema(self):
        return Cinema(self.driver)

    @property
    def children(self):
        return Children(self.driver)

    @property
    def hitech(self):
        return HiTech(self.driver)
    
    @property
    def blockleft(self):
        return BlockLeft(self.driver)

    @property
    def blockright(self):
        return BlockRight(self.driver)
    
    
    
    
class MainNews(Component):
    BIG = '//div[@data-new-item-clb="clb14642789"]//td[@class="daynews__main"]//a'
    BIG_URL = ''
    SECOND = '//div[@data-new-item-clb="clb14642789"]//td[@class="daynews__items"]/div[1]//a'
    SECOND_URL = ''
    SMALL = "//div[@name='clb20268353']//a"
    SMALL_URL = ''
    
    def clickBigSquare(self):
        self.BIG_URL = self.driver.find_element_by_xpath(self.BIG).get_attribute('href')
        self.driver.find_element_by_xpath(self.BIG).click()

    def clickSecondSquare(self):
        self.SECOND_URL = self.driver.find_element_by_xpath(self.SECOND).get_attribute('href')
        self.driver.find_element_by_xpath(self.SECOND).click()

    def clickSmallLinks(self):
        self.SMALL_URL = self.driver.find_element_by_xpath(self.SMALL).get_attribute('href')
        self.driver.find_element_by_xpath(self.SMALL).click()

class MoscowNews(Component):
    HEADER = "//div[@name='clb20268373']//div[@class='hdr__wrapper']//a"
    HEADER_URL = ''
    BODY = '//div[@name="clb20268373"]//span[@class="cell"]/a'
    BODY_URL = ''
    SMALL = '//div[@name="clb20268373"]/div[2]//li/a'
    SMALL_URL = ''
    


class Politics(Component):
    HEADER = '//div[@name="clb20268392"]/div/div[1]//a[@class="hdr__text"]'
    HEADER_URL = ''
    BODY = '//div[@name="clb20268392"]/div/div[1]//a[@class="hdr__text"]'
    BODY_URL = ''
    SMALL = '//div[@name="clb20268392"]/div/div[1]//ul/li[1]/a'
    SMALL_URL = ''



class Economics(Component):
    HEADER = '//div[@name="clb20268392"]/div/div[2]//a[@class="hdr__text"]'
    HEADER_URL = ''
    BODY = '//div[@name="clb20268392"]/div/div[2]//a[@class="hdr__text"]'
    BODY_URL = ''
    SMALL = '//div[@name="clb20268392"]/div/div[2]//ul/li[1]/a'
    SMALL_URL = ''


class Society(Component):
    HEADER = '//div[@name="clb20268392"]/div/div[3]//a[@class="hdr__text"]'
    HEADER_URL = ''
    BODY = '//div[@name="clb20268392"]/div/div[3]//a[@class="hdr__text"]'
    BODY_URL = ''
    SMALL = '//div[@name="clb20268392"]/div/div[4]//ul/li[1]/a'
    SMALL_URL = ''

class Events(Component):
    HEADER = '//div[@name="clb20268392"]/div/div[4]//a[@class="hdr__text"]'
    HEADER_URL = ''
    BODY = '//div[@name="clb20268392"]/div/div[4]//a[@class="hdr__text"]'
    BODY_URL = ''
    SMALL = '//div[@name="clb20268392"]/div/div[4]//ul/li[1]/a'
    SMALL_URL = ''


class Helps(Component):

    CARD_ONE = '//div[@name="clb20268418"]//tbody/tr/td[1]//a'
    CARD_ONE_URL = ''
    CARD_TWO = '//div[@name="clb20268418"]//tbody/tr/td[2]//a'
    CARD_TWO_URL = ''
    CARD_THREE = '//div[@name="clb20268418"]//tbody/tr/td[3]//a'
    CARD_THREE_URL = ''
    CARD_FOUR = '//div[@name="clb20268418"]//tbody/tr/td[4]//a'
    CARD_FOUR_URL = ''

class Photo(Component):

    PHOTO_ONE = '//div[@name="clb20268379"]/div[2]/div/div[1]//a'
    PHOTO_ONE_URL = ''
    PHOTO_TWO = '//div[@name="clb20268379"]/div[2]/div/div[2]//a'
    PHOTO_TWO_URL = ''
    PHOTO_THREE = '//div[@name="clb20268379"]/div[2]/div/div[3]//a'
    PHOTO_THREE_URL = ''

class Health(Component):

    HEADER = '//a[@name="clb16368045"]'
    HEADER_URL = ''
    BODY = '//div[@class="layout"]/div[@data-counter-id="20268428"]/div[1]/div[1]/div[1]//span[2]/a'
    BODY_URL = ''
    SMALL = ''
    SMALL_URL = ''



class Auto(Component):

    HEADER = '//a[@name="clb8034587"]'
    HEADER_URL = ''
    BODY = '//div[@class="layout"]/div[@data-counter-id="20268428"]/div[1]/div[1]/div[2]//span[2]/a'
    BODY_URL = ''
    SMALL = ''
    SMALL_URL = ''



class Lady(Component):

    HEADER = '//a[@name="clb12824613"]'
    HEADER_URL = ''
    BODY = '//div[@class="layout"]/div[@data-counter-id="20268428"]/div[1]/div[1]/div[3]//span[2]/a'
    BODY_URL = ''
    SMALL = ''
    SMALL_URL = ''



class Cinema(Component):

    HEADER = '//a[@name="clb6284802"]'
    HEADER_URL = ''
    BODY = '//div[@class="layout"]/div[@data-counter-id="20268428"]/div[1]/div[1]/div[4]//span[2]/a'
    BODY_URL = ''
    SMALL = ''
    SMALL_URL = ''



class Children(Component):
    HEADER = '//a[@name="n180877646"]'
    HEADER_URL = ''
    BODY = '//div[@class="layout"]/div[@data-counter-id="20268428"]/div[1]/div[1]/div[6]//span[2]/a'
    BODY_URL = ''
    SMALL = ''
    SMALL_URL = ''


class HiTech(Component):

    HEADER = '//a[@name="clb13570528"]'
    HEADER_URL = ''
    BODY = '//div[@class="layout"]/div[@data-counter-id="20268428"]/div[1]/div[1]/div[7]//span[2]/a'
    BODY_URL = ''
    SMALL = ''
    SMALL_URL = ''



class BlockLeft(Component):

    HEADER = '//a[@name="clb19839801"]'
    HEADER_URL = ''
    BODY = '//div[@class="layout"]/div[@data-counter-id="20268428"]/div[1]/div[1]/div[5]//span[2]/a'
    BODY_URL = ''



class BlockRight(Component):

    HEADER = '//div[@class="layout"]/div[@name="clb20268429"]/div[1]/div[2]/div[4]//a[@class="hdr__text"]'
    HEADER_URL = ''
    BODY = '//div[@class="layout"]/div[@data-counter-id="20268428"]/div[1]/div[1]/div[8]//span[2]/a'
    BODY_URL = ''