# coding=utf-8
import datetime
import unittest
from selenium.webdriver import Remote, DesiredCapabilities
from page import CurrencyPage
import os
import time
from selenium.webdriver.support.ui import WebDriverWait

from picture_day import PictureDay, MainPage, OtvetPage

class DayTest(unittest.TestCase):


    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    # def tearDown(self):
    #     self.driver.quit()



    # def test_main_news_1(self):
        
    #     OK = 200
    #     pictureday = PictureDay(self.driver)
    #     pictureday.open()

    #     main_news = pictureday.main_news

    #     main_news.clickBigSquare()
    #     self.assertEqual(main_news.BIG_URL, main_news.get_url())
    #     self.assertEqual(main_news.get_status(main_news.BIG_URL), OK)        

    # def test_main_news_2(self):

    #     OK = 200
    #     pictureday = PictureDay(self.driver) 
    #     pictureday.open()

    #     main_news = pictureday.main_news

    #     main_news.clickSecondSquare()
    #     self.assertEqual(main_news.SECOND_URL, main_news.get_url())
    #     self.assertEqual(main_news.get_status(main_news.SECOND_URL), OK)

    # def test_main_news_3(self):
    #     OK = 200
    #     pictureday = PictureDay(self.driver) 
    #     pictureday.open()

    #     main_news = pictureday.main_news

    #     main_news.clickSmallLinks()
    #     self.assertEqual(main_news.SMALL_URL, main_news.get_url())
    #     self.assertEqual(main_news.get_status(main_news.SMALL_URL), OK)

    # def test_moscow_news_1(self):
    #     OK = 200

    #     pictureday = PictureDay(self.driver)
    #     pictureday.open()

    #     moscow_news = pictureday.moscow_news

    #     moscow_news.HEADER_URL = moscow_news.clickHeader(moscow_news.HEADER, moscow_news.HEADER_URL)
    #     self.assertEqual(moscow_news.HEADER_URL, moscow_news.get_url())        
    #     self.assertEqual(moscow_news.get_status(moscow_news.HEADER_URL), OK)


    # def test_moscow_news_2(self):
    #     OK = 200

    #     pictureday = PictureDay(self.driver)
    #     pictureday.open()

    #     moscow_news = pictureday.moscow_news

    #     moscow_news.BODY_URL = moscow_news.clickBody(moscow_news.BODY, moscow_news.BODY_URL)
    #     self.assertEqual(moscow_news.BODY_URL, moscow_news.get_url())        
    #     self.assertEqual(moscow_news.get_status(moscow_news.BODY_URL), OK)    

    # def test_moscow_news_3(self):

    #     OK = 200

    #     pictureday = PictureDay(self.driver)
    #     pictureday.open()

    #     moscow_news = pictureday.moscow_news

    #     moscow_news.SMALL_URL = moscow_news.clickSmall(moscow_news.SMALL, moscow_news.SMALL_URL)
    #     self.assertEqual(moscow_news.SMALL_URL, moscow_news.get_url())        
    #     self.assertEqual(moscow_news.get_status(moscow_news.SMALL_URL), OK)                


    # def test_mail_login(self):
        
    #     pictureday = MainPage(self.driver)
    #     pictureday.open()

    #     mail_login = pictureday.feed_back

    #     mail_login.set_login("seleniumov")
    #     mail_login.set_password("123456qwerty")
    #     mail_login.submit()
    #     self.assertEqual(mail_login.INBOX_URL, mail_login.get_url())

    # def test_ask_login(self):

    #     URL = "https://otvet.mail.ru/?login=1"
        
    #     pictureday = OtvetPage(self.driver)
    #     pictureday.open()

    #     mail_ask = pictureday.mail_ask

    #     mail_ask.clickAsk()

    #     mail_ask.iframe_select()
    #     mail_ask.set_login("seleniumov")
    #     mail_ask.set_password("123456qwerty")
    #     mail_ask.click_submit()


    #     self.assertEqual(URL, self.driver.current_url)     

    def test_ask_(self):

        URL = "https://otvet.mail.ru/question/"

        QUEST = u'Почему я влюбился в одногруппницу?'

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

        # element = WebDriverWait(driver, 10).until(
        self.assertIn(URL, self.driver.current_url) 
        # )


        # self.assertIn(URL, self.driver.current_url) 
