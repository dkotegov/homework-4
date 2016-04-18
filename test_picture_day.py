# coding=utf-8
import datetime
import unittest
from selenium.webdriver import Remote, DesiredCapabilities
from page import CurrencyPage
import os

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

    # def test_photo_1(self):
    #     OK = 200

    #     pictureday = PictureDay(self.driver)
    #     pictureday.open()

    #     photo = pictureday.photo

    #     photo.PHOTO_ONE_URL = photo.clickPhoto(photo.PHOTO_ONE, photo.PHOTO_ONE_URL)
    #     self.assertIn(photo.PHOTO_ONE_URL, photo.get_url())      
    #     self.assertEqual(photo.get_status(photo.PHOTO_ONE_URL), OK)

    # def test_photo_2(self):
    #     OK = 200

    #     pictureday = PictureDay(self.driver)
    #     pictureday.open()

    #     photo = pictureday.photo        
    #     photo.PHOTO_TWO_URL = photo.clickPhoto(photo.PHOTO_TWO, photo.PHOTO_TWO_URL)
    #     self.assertIn(photo.PHOTO_TWO_URL, photo.get_url())      
    #     self.assertEqual(photo.get_status(photo.PHOTO_TWO_URL), OK)

    # def test_photo_3(self):
    #     OK = 200

    #     pictureday = PictureDay(self.driver)
    #     pictureday.open()

    #     photo = pictureday.photo
    #     photo.PHOTO_THREE_URL = photo.clickPhoto(photo.PHOTO_THREE, photo.PHOTO_THREE_URL)
    #     self.assertIn(photo.PHOTO_THREE_URL, photo.get_url())      
    #     self.assertEqual(photo.get_status(photo.PHOTO_THREE_URL), OK)


    # def test_health_1(self):
    #     OK = 200

    #     pictureday = PictureDay(self.driver)
    #     pictureday.open()

    #     health = pictureday.health

    #     health.HEADER_URL = health.clickHeader(health.HEADER, health.HEADER_URL)
    #     self.assertEqual(health.HEADER_URL, health.get_url())        
    #     self.assertEqual(health.get_status(health.HEADER_URL), OK)


    # def test_health_2(self):
    #     OK = 200

    #     pictureday = PictureDay(self.driver)
    #     pictureday.open()

    #     health = pictureday.health

    #     health.BODY_URL = health.clickBody(health.BODY, health.BODY_URL)
    #     self.assertEqual(health.BODY_URL, health.get_url())        
    #     self.assertEqual(health.get_status(health.BODY_URL), OK)    

   #  def test_health_3(self):

   #      OK = 200

   #      pictureday = PictureDay(self.driver)
   #      pictureday.open()

   #      health = pictureday.health

   #      health.SMALL_URL = health.clickSmall(health.SMALL, health.SMALL_URL)
   #      self.assertEqual(health.SMALL_URL, health.get_url())        
   #      self.assertEqual(health.get_status(health.SMALL_URL), OK)   



    # def test_auto_1(self):
    #     OK = 200

    #     pictureday = PictureDay(self.driver)
    #     pictureday.open()

    #     auto = pictureday.auto

    #     auto.HEADER_URL = auto.clickHeader(auto.HEADER, auto.HEADER_URL)
    #     self.assertEqual(auto.HEADER_URL, auto.get_url())        
    #     self.assertEqual(auto.get_status(auto.HEADER_URL), OK)


   #  def test_auto_2(self):
   #      OK = 200

   #      pictureday = PictureDay(self.driver)
   #      pictureday.open()

   #      auto = pictureday.auto

   #      auto.BODY_URL = auto.clickBody(auto.BODY, auto.BODY_URL)
   #      self.assertEqual(auto.BODY_URL, auto.get_url())        
   #      self.assertEqual(auto.get_status(auto.BODY_URL), OK)    

   #  def test_auto_3(self):

   #      OK = 200

   #      pictureday = PictureDay(self.driver)
   #      pictureday.open()

   #      auto = pictureday.auto

   #      auto.SMALL_URL = auto.clickSmall(auto.SMALL, auto.SMALL_URL)
   #      self.assertEqual(auto.SMALL_URL, auto.get_url())        
   #      self.assertEqual(auto.get_status(auto.SMALL_URL), OK) 


    # def test_lady_1(self):
    #     OK = 200

    #     pictureday = PictureDay(self.driver)
    #     pictureday.open()

    #     lady = pictureday.lady

    #     lady.HEADER_URL = lady.clickHeader(lady.HEADER, lady.HEADER_URL)
    #     self.assertEqual(lady.HEADER_URL, lady.get_url())        
    #     self.assertEqual(lady.get_status(lady.HEADER_URL), OK)


   #  def test_lady_2(self):
   #      OK = 200

   #      pictureday = PictureDay(self.driver)
   #      pictureday.open()

   #      lady = pictureday.lady

   #      lady.BODY_URL = lady.clickBody(lady.BODY, lady.BODY_URL)
   #      self.assertEqual(lady.BODY_URL, lady.get_url())        
   #      self.assertEqual(lady.get_status(lady.BODY_URL), OK)    

   #  def test_lady_3(self):

   #      OK = 200

   #      pictureday = PictureDay(self.driver)
   #      pictureday.open()

   #      lady = pictureday.lady

   #      lady.SMALL_URL = lady.clickSmall(lady.SMALL, lady.SMALL_URL)
   #      self.assertEqual(lady.SMALL_URL, lady.get_url())        
   #      self.assertEqual(lady.get_status(lady.SMALL_URL), OK) 


    # def test_cinema_1(self):
    #     OK = 200

    #     pictureday = PictureDay(self.driver)
    #     pictureday.open()

    #     cinema = pictureday.cinema

    #     cinema.HEADER_URL = cinema.clickHeader(cinema.HEADER, cinema.HEADER_URL)
    #     self.assertEqual(cinema.HEADER_URL, cinema.get_url())        
    #     self.assertEqual(cinema.get_status(cinema.HEADER_URL), OK)


   #  def test_cinema_2(self):
   #      OK = 200

   #      pictureday = PictureDay(self.driver)
   #      pictureday.open()

   #      cinema = pictureday.cinema

   #      cinema.BODY_URL = cinema.clickBody(cinema.BODY, cinema.BODY_URL)
   #      self.assertEqual(cinema.BODY_URL, cinema.get_url())        
   #      self.assertEqual(cinema.get_status(cinema.BODY_URL), OK)    

   #  def test_cinema_3(self):

   #      OK = 200

   #      pictureday = PictureDay(self.driver)
   #      pictureday.open()

   #      cinema = pictureday.cinema

   #      cinema.SMALL_URL = cinema.clickSmall(cinema.SMALL, cinema.SMALL_URL)
   #      self.assertEqual(cinema.SMALL_URL, cinema.get_url())        
   #      self.assertEqual(cinema.get_status(cinema.SMALL_URL), OK) 


    # def test_children_1(self):
    #     OK = 200

    #     pictureday = PictureDay(self.driver)
    #     pictureday.open()

    #     children = pictureday.children

    #     children.HEADER_URL = children.clickHeader(children.HEADER, children.HEADER_URL)
    #     self.assertEqual(children.HEADER_URL, children.get_url())        
    #     self.assertEqual(children.get_status(children.HEADER_URL), OK)


   #  def test_children_2(self):
   #      OK = 200

   #      pictureday = PictureDay(self.driver)
   #      pictureday.open()

   #      children = pictureday.children

   #      children.BODY_URL = children.clickBody(children.BODY, children.BODY_URL)
   #      self.assertEqual(children.BODY_URL, children.get_url())        
   #      self.assertEqual(children.get_status(children.BODY_URL), OK)    

   #  def test_children_3(self):

   #      OK = 200

   #      pictureday = PictureDay(self.driver)
   #      pictureday.open()

   #      children = pictureday.children

   #      children.SMALL_URL = children.clickSmall(children.SMALL, children.SMALL_URL)
   #      self.assertEqual(children.SMALL_URL, children.get_url())        
   #      self.assertEqual(children.get_status(children.SMALL_URL), OK)

    # def test_hightech_1(self):
    #     OK = 200

    #     pictureday = PictureDay(self.driver)
    #     pictureday.open()

    #     hightech = pictureday.hightech

    #     hightech.HEADER_URL = hightech.clickHeader(hightech.HEADER, hightech.HEADER_URL)
    #     self.assertEqual(hightech.HEADER_URL, hightech.get_url())        
    #     self.assertEqual(hightech.get_status(hightech.HEADER_URL), OK)


   #  def test_hightech_2(self):
   #      OK = 200

   #      pictureday = PictureDay(self.driver)
   #      pictureday.open()

   #      hightech = pictureday.hightech

   #      hightech.BODY_URL = hightech.clickBody(hightech.BODY, hightech.BODY_URL)
   #      self.assertEqual(hightech.BODY_URL, hightech.get_url())        
   #      self.assertEqual(hightech.get_status(hightech.BODY_URL), OK)    

   #  def test_hightech_3(self):

   #      OK = 200

   #      pictureday = PictureDay(self.driver)
   #      pictureday.open()

   #      hightech = pictureday.hightech

   #      hightech.SMALL_URL = hightech.clickSmall(hightech.SMALL, hightech.SMALL_URL)
   #      self.assertEqual(hightech.SMALL_URL, hightech.get_url())        
   #      self.assertEqual(hightech.get_status(hightech.SMALL_URL), OK)   

    # def test_blockleft_1(self):
    #     OK = 200

    #     pictureday = PictureDay(self.driver)
    #     pictureday.open()

    #     blockleft = pictureday.blockleft

    #     blockleft.HEADER_URL = blockleft.clickHeader(blockleft.HEADER, blockleft.HEADER_URL)
    #     self.assertEqual(blockleft.HEADER_URL, blockleft.get_url())        
    #     self.assertEqual(blockleft.get_status(blockleft.HEADER_URL), OK)


   #  def test_blockleft_2(self):
   #      OK = 200

   #      pictureday = PictureDay(self.driver)
   #      pictureday.open()

   #      blockleft = pictureday.blockleft

   #      blockleft.BODY_URL = blockleft.clickBody(blockleft.BODY, blockleft.BODY_URL)
   #      self.assertEqual(blockleft.BODY_URL, blockleft.get_url())        
   #      self.assertEqual(blockleft.get_status(blockleft.BODY_URL), OK)     

    # def test_blockright_1(self):
    #     OK = 200

    #     pictureday = PictureDay(self.driver)
    #     pictureday.open()

    #     blockright = pictureday.blockright

    #     blockright.HEADER_URL = blockright.clickHeader(blockright.HEADER, blockright.HEADER_URL)
    #     self.assertEqual(blockright.HEADER_URL, blockright.get_url())        
    #     self.assertEqual(blockright.get_status(blockright.HEADER_URL), OK)


   #  def test_blockright_2(self):
   #      OK = 200

   #      pictureday = PictureDay(self.driver)
   #      pictureday.open()

   #      blockright = pictureday.blockright

   #      blockright.BODY_URL = blockright.clickBody(blockright.BODY, blockright.BODY_URL)
   #      self.assertEqual(blockright.BODY_URL, blockright.get_url())        
   #      self.assertEqual(blockright.get_status(blockright.BODY_URL), OK)     
