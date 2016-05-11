# coding=utf-8
import datetime
import unittest
from selenium.webdriver import Remote, DesiredCapabilities
import os

from toolbar_page import Toolbar
from picture_day import PictureDay, MainPage, OtvetPage


class ToolbarTestCase(unittest.TestCase):
    OK = 200

    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.toolbar = Toolbar(self.driver)

    def tearDown(self):
        self.driver.quit()

    def testUSDLink(self):
        self.toolbar.open()
        left_toolbar = self.toolbar.leftToolbar

        left_toolbar.clickUSD()
        self.assertEqual(left_toolbar.USD_URL, left_toolbar.getURL())
        self.assertEqual(left_toolbar.getStatus(left_toolbar.USD_URL), self.OK)

    def testLogoLink(self):
        self.toolbar.open()
        left_toolbar = self.toolbar.leftToolbar

        left_toolbar.clickLogo()
        self.assertEqual(self.toolbar.BASE_URL, left_toolbar.getURL())
        self.assertEqual(left_toolbar.getStatus(self.toolbar.BASE_URL), self.OK)

    def testWeatherLink(self):
        self.toolbar.open()
        left_toolbar = self.toolbar.leftToolbar

        left_toolbar.clickWeather()
        self.assertEqual(left_toolbar.WEATHER_URL, left_toolbar.getURL())
        self.assertEqual(left_toolbar.getStatus(left_toolbar.WEATHER_URL), self.OK)

    def testEURLink(self):
        self.toolbar.open()
        left_toolbar = self.toolbar.leftToolbar

        left_toolbar.clickEUR()
        self.assertEqual(left_toolbar.EUR_URL, left_toolbar.getURL())
        self.assertEqual(left_toolbar.getStatus(left_toolbar.EUR_URL), self.OK)

    def testSearchByClick(self):
        self.toolbar.open()
        search = self.toolbar.searchNews

        search.setQuery()
        search.clickSearchIcon()
        self.assertEqual(search.QUERY_URL, search.getURL())
        self.assertEqual(search.getStatus(search.QUERY_URL), self.OK)

    def testSearchByKeyPress(self):
        self.toolbar.open()
        search = self.toolbar.searchNews
        search.setQuery()
        search.pressEnterKey()
        self.assertEqual(search.QUERY_URL, search.getURL())
        self.assertEqual(search.getStatus(search.QUERY_URL), self.OK)


    def test_mail_login_wrong_login(self):

        LOGIN = "seleniumofff_lol"
        PASSWORD = "123456qwerty"
        
        pictureday = MainPage(self.driver)
        pictureday.open()

        mail_login = pictureday.feed_back

        mail_login.set_login(LOGIN)
        mail_login.set_password(PASSWORD)
        mail_login.submit()
        self.assertEqual(mail_login.WRONG_LOGIN_URL, mail_login.get_url())

    def test_mail_login_wrong_password(self):

        LOGIN = "seleniumov"
        PASSWORD = "123456qwerty1234"
        
        pictureday = MainPage(self.driver)
        pictureday.open()

        mail_login = pictureday.feed_back

        mail_login.set_login(LOGIN)
        mail_login.set_password(PASSWORD)
        mail_login.submit()
        self.assertEqual(mail_login.WRONG_PSWD_URL, mail_login.get_url())     

   	def test_mail_login_empty_pswd(self):

        LOGIN = "seleniumov"
        PASSWORD = ""

        pictureday = MainPage(self.driver)
        pictureday.open()

        mail_login = pictureday.feed_back

        mail_login.set_login(LOGIN)        
        mail_login.set_password(PASSWORD)
        mail_login.submit()
        self.assertEqual(mail_login.EMPTY_PSWD_URL, mail_login.get_url())

    def test_ask_good_logout(self):

        URL = "https://otvet.mail.ru/"
        
        pictureday = OtvetPage(self.driver)
        pictureday.open()

        mail_ask = pictureday.mail_ask

        mail_ask.clickAsk()

        mail_ask.iframe_select()
        mail_ask.set_login("seleniumov")
        mail_ask.set_password("123456qwerty")
        mail_ask.click_submit()

        mail_ask.click_logout()
        self.assertEqual(URL, mail_ask.get_url())

    def test_wrong_body(self):

        URL = "https://otvet.mail.ru/question/"
        ERROR = u'Просьба более подробно и грамотно сформулировать тему вопроса.'

        QUEST = u'авыравыоалвыоалдвылащвыоавыра'

        
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

    def test_ask_correct(self):

        URL = "https://otvet.mail.ru/question/"

        QUEST = u'Почему в Норвегии хорошо живут?'

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
            EC.presence_of_element_located((By.CLASS_NAME, "actions"))
        )

        self.assertIn(URL, self.driver.current_url) 
