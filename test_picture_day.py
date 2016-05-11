# coding=utf-8
import datetime
import unittest
from selenium.webdriver import Remote, DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page import CurrencyPage
import os
import time
from selenium.webdriver.support.ui import WebDriverWait

from picture_day import PictureDay, MainPage, OtvetPage

class DayTest(unittest.TestCase):

    OK = 200

    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()



    def test_main_news(self):
        
        pictureday = PictureDay(self.driver)
        pictureday.open()

        main_news = pictureday.main_news

        main_news.clickBigSquare()
        self.assertEqual(main_news.BIG_URL, main_news.get_url())
        self.assertEqual(main_news.get_status(main_news.BIG_URL), self.OK)        


    def test_moscow_news_header(self):

        pictureday = PictureDay(self.driver)
        pictureday.open()

        moscow_news = pictureday.moscow_news

        moscow_news.HEADER_URL = moscow_news.clickHeader(moscow_news.HEADER, moscow_news.HEADER_URL)
        self.assertEqual(moscow_news.HEADER_URL, moscow_news.get_url())        
        self.assertEqual(moscow_news.get_status(moscow_news.HEADER_URL), self.OK)


    def test_moscow_news_body(self):

        pictureday = PictureDay(self.driver)
        pictureday.open()

        moscow_news = pictureday.moscow_news

        moscow_news.BODY_URL = moscow_news.clickBody(moscow_news.BODY, moscow_news.BODY_URL)
        self.assertEqual(moscow_news.BODY_URL, moscow_news.get_url())        
        self.assertEqual(moscow_news.get_status(moscow_news.BODY_URL), self.OK)    

    def test_moscow_news_small_link(self):

        pictureday = PictureDay(self.driver)
        pictureday.open()

        moscow_news = pictureday.moscow_news

        moscow_news.SMALL_URL = moscow_news.clickSmall(moscow_news.SMALL, moscow_news.SMALL_URL)
        self.assertEqual(moscow_news.SMALL_URL, moscow_news.get_url())        
        self.assertEqual(moscow_news.get_status(moscow_news.SMALL_URL), self.OK)                


    def test_mail_login_OK(self):

        LOGIN = "seleniumov"
        PASSWORD = "123456qwerty"
        
        pictureday = MainPage(self.driver)
        pictureday.open()

        mail_login = pictureday.feed_back

        mail_login.set_login(LOGIN)
        mail_login.set_password(PASSWORD)
        mail_login.submit()
        self.assertEqual(mail_login.INBOX_URL, mail_login.get_url())


    def test_mail_logout_OK(self):
        LOGIN = "seleniumov"
        PASSWORD = "123456qwerty"

        URL = "https://mail.ru/?from=logout" 
        
        pictureday = MainPage(self.driver)
        pictureday.open()

        mail_login = pictureday.feed_back

        mail_login.set_login(LOGIN)
        mail_login.set_password(PASSWORD)
        mail_login.submit()

        mail_login.click_logout()
        self.assertEqual(URL, mail_login.get_url())

      

    def test_mail_login_empty_login(self):

        LOGIN = ""
        PASSWORD = "123456qwerty"

        pictureday = MainPage(self.driver)
        pictureday.open()

        mail_login = pictureday.feed_back

        mail_login.set_login(LOGIN)
        mail_login.set_password(PASSWORD)
        mail_login.submit() 

        self.assertEqual(mail_login.EMPTY_ALL_URL, mail_login.get_url())



    def test_ask_good_login(self):

        URL = "https://otvet.mail.ru/?login=1"
        
        pictureday = OtvetPage(self.driver)
        pictureday.open()

        mail_ask = pictureday.mail_ask

        mail_ask.clickAsk()

        mail_ask.iframe_select()
        mail_ask.set_login("seleniumov")
        mail_ask.set_password("123456qwerty")
        mail_ask.click_submit()

        self.assertEqual(mail_ask.GOOD_LOG_URL, mail_ask.get_url())        


    def test_empty_body(self):

        URL = "https://otvet.mail.ru/question/"
        ERROR = u'Невозможно опубликовать пустой текст'

        QUEST = u''

        
        pictureday = OtvetPage(self.driver)
        pictureday.open()

        mail_ask = pictureday.mail_ask

        mail_ask.clickAsk()

        mail_ask.iframe_select()
        mail_ask.set_login("seleniumov")
        mail_ask.set_password("123456qwerty")
        mail_ask.click_submit()

        mail_ask.clickAsk() 
        self.driver.switch_to_default_content()
        a = self.driver.find_elements_by_tag_name("button")

        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-orange ask-btn-submit']"))
        )
        
        mail_ask.click_public()
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "popup--content"))
        )
        self.assertEqual(ERROR, mail_ask.get_error_text())


    def test_ask_long_question(self):

        URL = "https://otvet.mail.ru/question/"
        ERROR = u'Невозможно опубликовать слишком длинный текст'

        QUEST = u'ФФФФФФФФФФФ ФФФФФФФФФФФ ФФФФФФФФФФФ ФФФФФФФФФФФ ФФФФФФФФФФФ ФФФФФФФФФФФ ФФФФФФФФФФФ ФФФФФФФФФФФ ФФФФФФФФФФФ ФФФФФФФФФФФ ФФФФФФФФФФФ'

        
        pictureday = OtvetPage(self.driver)
        pictureday.open()

        mail_ask = pictureday.mail_ask

        mail_ask.clickAsk()

        mail_ask.iframe_select()
        mail_ask.set_login("seleniumov")
        mail_ask.set_password("123456qwerty")
        mail_ask.click_submit()

        mail_ask.clickAsk() 
        self.driver.switch_to_default_content()
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//textarea[@id='ask-text']"))
        )
        mail_ask.set_question(QUEST)

        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-orange ask-btn-submit']"))
        )
        
        mail_ask.click_public()
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "popup--content"))
        )
        self.assertEqual(ERROR, mail_ask.get_error_text())


    def test_dublicat_(self):
        URL = "https://otvet.mail.ru/question/"

        ERROR = u'Невозможно опубликовать копию недавнего вопроса'

        QUEST = u'Почему так всё хорошо?'

        pictureday = OtvetPage(self.driver)
        pictureday.open()

        mail_ask = pictureday.mail_ask

        mail_ask.clickAsk()

        mail_ask.iframe_select()
        mail_ask.set_login("seleniumov")
        mail_ask.set_password("123456qwerty")
        mail_ask.click_submit()

        mail_ask.clickAsk() 

        self.driver.switch_to_default_content()
        mail_ask.set_question(QUEST)
        mail_ask.click_cid()
        mail_ask.click_subcid()
        mail_ask.click_public()

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "popup--content"))
        )
        self.assertEqual(ERROR, mail_ask.get_error_text())