# coding=utf-8
import datetime
import unittest
from selenium.webdriver import Remote, DesiredCapabilities
from page import CurrencyPage
import os

from picture_day import PictureDay


class DayTest(unittest.TestCase):


    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()


    def test_main_news_1(self):
        
        OK = 200
        pictureday = PictureDay(self.driver)
        pictureday.open()

        main_news = pictureday.main_news

        main_news.clickBigSquare()
        self.assertEqual(main_news.BIG_URL, main_news.get_url())
        self.assertEqual(main_news.get_status(main_news.BIG_URL), OK)        

    def test_main_news_2(self):

        OK = 200
        pictureday = PictureDay(self.driver) 
        pictureday.open()

        main_news = pictureday.main_news

        main_news.clickSecondSquare()
        self.assertEqual(main_news.SECOND_URL, main_news.get_url())
        self.assertEqual(main_news.get_status(main_news.SECOND_URL), OK)

    def test_main_news_3(self):
        OK = 200
        pictureday = PictureDay(self.driver) 
        pictureday.open()

        main_news = pictureday.main_news

        main_news.clickSmallLinks()
        self.assertEqual(main_news.SMALL_URL, main_news.get_url())
        self.assertEqual(main_news.get_status(main_news.SMALL_URL), OK)

    def test_moscow_news_1(self):
        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        moscow_news = pictureday.moscow_news

        moscow_news.HEADER_URL = moscow_news.clickHeader(moscow_news.HEADER, moscow_news.HEADER_URL)
        self.assertEqual(moscow_news.HEADER_URL, moscow_news.get_url())        
        self.assertEqual(moscow_news.get_status(moscow_news.HEADER_URL), OK)


    def test_moscow_news_2(self):
        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        moscow_news = pictureday.moscow_news

        moscow_news.BODY_URL = moscow_news.clickBody(moscow_news.BODY, moscow_news.BODY_URL)
        self.assertEqual(moscow_news.BODY_URL, moscow_news.get_url())        
        self.assertEqual(moscow_news.get_status(moscow_news.BODY_URL), OK)    

    def test_moscow_news_3(self):

        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        moscow_news = pictureday.moscow_news

        moscow_news.SMALL_URL = moscow_news.clickSmall(moscow_news.SMALL, moscow_news.SMALL_URL)
        self.assertEqual(moscow_news.SMALL_URL, moscow_news.get_url())        
        self.assertEqual(moscow_news.get_status(moscow_news.SMALL_URL), OK)                

    def test_politics_1(self):
        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        politics = pictureday.politics

        politics.HEADER_URL = politics.clickHeader(politics.HEADER, politics.HEADER_URL)
        self.assertEqual(politics.HEADER_URL, politics.get_url())        
        self.assertEqual(politics.get_status(politics.HEADER_URL), OK)


    def test_politics_2(self):
        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        politics = pictureday.politics

        politics.BODY_URL = politics.clickBody(politics.BODY, politics.BODY_URL)
        self.assertEqual(politics.BODY_URL, politics.get_url())        
        self.assertEqual(politics.get_status(politics.BODY_URL), OK)    

    def test_politics_3(self):

        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        politics = pictureday.politics

        politics.SMALL_URL = politics.clickSmall(politics.SMALL, politics.SMALL_URL)
        self.assertEqual(politics.SMALL_URL, politics.get_url())        
        self.assertEqual(politics.get_status(politics.SMALL_URL), OK)    

    def test_economics_1(self):
        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        economics = pictureday.economics

        economics.HEADER_URL = economics.clickHeader(economics.HEADER, economics.HEADER_URL)
        self.assertEqual(economics.HEADER_URL, economics.get_url())        
        self.assertEqual(economics.get_status(economics.HEADER_URL), OK)


    def test_economics_2(self):
        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        economics = pictureday.economics

        economics.BODY_URL = economics.clickBody(economics.BODY, economics.BODY_URL)
        self.assertEqual(economics.BODY_URL, economics.get_url())        
        self.assertEqual(economics.get_status(economics.BODY_URL), OK)    

    def test_economics_3(self):

        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        economics = pictureday.economics

        economics.SMALL_URL = economics.clickSmall(economics.SMALL, economics.SMALL_URL)
        self.assertEqual(economics.SMALL_URL, economics.get_url())        
        self.assertEqual(economics.get_status(economics.SMALL_URL), OK)   

    def test_society_1(self):
        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        society = pictureday.society

        society.HEADER_URL = society.clickHeader(society.HEADER, society.HEADER_URL)
        self.assertEqual(society.HEADER_URL, society.get_url())        
        self.assertEqual(society.get_status(society.HEADER_URL), OK)


    def test_society_2(self):
        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        society = pictureday.society

        society.BODY_URL = society.clickBody(society.BODY, society.BODY_URL)
        self.assertEqual(society.BODY_URL, society.get_url())        
        self.assertEqual(society.get_status(society.BODY_URL), OK)    

    def test_society_3(self):

        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        society = pictureday.society

        society.SMALL_URL = society.clickSmall(society.SMALL, society.SMALL_URL)
        self.assertEqual(society.SMALL_URL, society.get_url())        
        self.assertEqual(society.get_status(society.SMALL_URL), OK)   

    def test_events_1(self):
        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        events = pictureday.events

        events.HEADER_URL = events.clickHeader(events.HEADER, events.HEADER_URL)
        self.assertEqual(events.HEADER_URL, events.get_url())        
        self.assertEqual(events.get_status(events.HEADER_URL), OK)


    def test_events_2(self):
        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        events = pictureday.events

        events.BODY_URL = events.clickBody(events.BODY, events.BODY_URL)
        self.assertEqual(events.BODY_URL, events.get_url())        
        self.assertEqual(events.get_status(events.BODY_URL), OK)    

    def test_events_3(self):

        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        events = pictureday.events

        events.SMALL_URL = events.clickSmall(events.SMALL, events.SMALL_URL)
        self.assertEqual(events.SMALL_URL, events.get_url())        
        self.assertEqual(events.get_status(events.SMALL_URL), OK)   


    def test_helps_1(self):
        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        helps = pictureday.helps

        helps.CARD_ONE_URL = helps.clickCard(helps.CARD_ONE, helps.CARD_ONE_URL)
        self.assertEqual(helps.CARD_ONE_URL, helps.get_url())      
        self.assertEqual(helps.get_status(helps.CARD_ONE_URL), OK)

    def test_helps_2(self):
        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        helps = pictureday.helps        
        helps.CARD_TWO_URL = helps.clickCard(helps.CARD_TWO, helps.CARD_TWO_URL)
        self.assertEqual(helps.CARD_TWO_URL, helps.get_url())      
        self.assertEqual(helps.get_status(helps.CARD_TWO_URL), OK)

    def test_helps_3(self):
        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        helps = pictureday.helps
        helps.CARD_THREE_URL = helps.clickCard(helps.CARD_THREE, helps.CARD_THREE_URL)
        self.assertEqual(helps.CARD_THREE_URL, helps.get_url())      
        self.assertEqual(helps.get_status(helps.CARD_THREE_URL), OK)

    def test_helps_4(self):
        OK = 200

        pictureday = PictureDay(self.driver)
        pictureday.open()

        helps = pictureday.helps
        helps.CARD_FOUR_URL = helps.clickCard(helps.CARD_FOUR, helps.CARD_FOUR_URL)
        self.assertEqual(helps.CARD_FOUR_URL, helps.get_url())      
        self.assertEqual(helps.get_status(helps.CARD_FOUR_URL), OK)
