
# -*- coding: utf-8 -*-

import os

import unittest
import urlparse
from selenium.webdriver.support.ui import Select

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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


class PictureDay(Page):

    PATH = ''
    BASE_URL = 'https://news.mail.ru/'

    @property
    def main_news(self):
        return MainNews(self.driver)

    @property
    def moscow_news(self):
        return MoscowNews(self.driver)

    @property
    def helps(self):
        return Helps(self.driver)
    
    
class MainPage(Page):

    PATH = ''
    BASE_URL = 'https://mail.ru/'  

    @property
    def feed_back(self):
        return LoginMail(self.driver)   

class OtvetPage(Page):

    PATH = ''
    BASE_URL = 'https://otvet.mail.ru'

    @property
    def mail_ask(self):
        return Ask(self.driver)  
   
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


class Helps(Component):

    CARD_ONE = '//div[@name="clb20268418"]//tbody/tr/td[1]//a'
    CARD_ONE_URL = ''
    CARD_TWO = '//div[@name="clb20268418"]//tbody/tr/td[2]//a'
    CARD_TWO_URL = ''
    CARD_THREE = '//div[@name="clb20268418"]//tbody/tr/td[3]//a'
    CARD_THREE_URL = ''
    CARD_FOUR = '//div[@name="clb20268418"]//tbody/tr/td[4]//a'
    CARD_FOUR_URL = ''


class LoginMail(Component):
    LOGIN = '//input[@name="Login"]'
    PASSWORD = '//input[@name="Password"]'
    SUBMIT = "//div[@class='mailbox__auth']//input[@id='mailbox__auth__button']"
    LOGIN_S = "seleniumov"
    LOGIN_WRONG = "seleniumofff_lol"

    INBOX_URL = "https://e.mail.ru/messages/inbox/?back=1"
    EMPTY_PSWD_URL = "https://e.mail.ru/login?email=" + LOGIN_S + "@mail.ru&fail=1"
    WRONG_LOGIN_URL = "https://e.mail.ru/login?email=" + LOGIN_WRONG + "@mail.ru&fail=1"
    WRONG_PSWD_URL = "https://e.mail.ru/login?email=" + LOGIN_S + "@mail.ru&fail=1"
    EMPTY_ALL_URL = "https://e.mail.ru/login?fail=1"


    def open_form(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()


    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
        
    def click_logout(self):
        self.driver.find_element_by_id("PH_logoutLink").click()

class Ask(Component):
    FRAME = "//body[1]/div[4]/div[1]//iframe"
    ASK = "clb3917180"
    LOGIN = '//input[@name="Username"]'
    PASSWORD = '//input[@name="Password"]'
    SUBMIT = '//button[@data-name="submit"]'
    QUESTION_AREA = "//textarea[@id='ask-text']"
    PUBLIC = "button"
    THEME = "cid"
    SUBTHEME = "subcid"
    ERROR = "popup--content"
    GOOD_LOG_URL = "https://otvet.mail.ru/?login=1"



    def clickAsk(self):
        self.driver.find_element_by_name(self.ASK).click()

    def iframe_select(self):
        f = self.driver.find_elements_by_tag_name("iframe")
        self.driver.switch_to.frame(f[0])

    def iframe_unselect(self):
        self.driver.switch_to_default_content()

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def click_submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def set_question(self, text):
        self.driver.find_element_by_xpath(self.QUESTION_AREA).send_keys(text)

    def click_public(self):
        self.driver.find_elements_by_tag_name(self.PUBLIC)[1].click()  

    def click_cid(self):
         select = Select(self.driver.find_element_by_name(self.THEME))
         select.select_by_value("3")              
        
    def click_subcid(self):
         select = Select(self.driver.find_element_by_name(self.SUBTHEME))
         select.select_by_value("1335")

    def get_error_text(self):
        return self.driver.find_element_by_class_name(self.ERROR).text
 
    def click_logout(self):
        self.driver.find_element_by_id("PH_logoutLink").click()