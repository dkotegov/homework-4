# coding=utf-8
import datetime
import unittest
from selenium.webdriver import Remote, DesiredCapabilities
import os

from toolbar_page import Toolbar


class ToolbarTestCase(unittest.TestCase):
    OK = 200

    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.toolbar = Toolbar(self.driver)

    # def tearDown(self):
    #     self.driver.quit()

    # def testUSDLink(self):
    #     self.toolbar.open()
    #     left_toolbar = self.toolbar.leftToolbar

    #     left_toolbar.clickUSD()
    #     self.assertEqual(left_toolbar.USD_URL, left_toolbar.getURL())
    #     self.assertEqual(left_toolbar.getStatus(left_toolbar.USD_URL), self.OK)

    # def testLogoLink(self):
    #     self.toolbar.open()
    #     left_toolbar = self.toolbar.leftToolbar

    #     left_toolbar.clickLogo()
    #     self.assertEqual(self.toolbar.BASE_URL, left_toolbar.getURL())
    #     self.assertEqual(left_toolbar.getStatus(self.toolbar.BASE_URL), self.OK)

    # def testWeatherLink(self):
    #     self.toolbar.open()
    #     left_toolbar = self.toolbar.leftToolbar

    #     left_toolbar.clickWeather()
    #     self.assertEqual(left_toolbar.WEATHER_URL, left_toolbar.getURL())
    #     self.assertEqual(left_toolbar.getStatus(left_toolbar.WEATHER_URL), self.OK)

    # def testEURLink(self):
    #     self.toolbar.open()
    #     left_toolbar = self.toolbar.leftToolbar

    #     left_toolbar.clickEUR()
    #     self.assertEqual(left_toolbar.EUR_URL, left_toolbar.getURL())
    #     self.assertEqual(left_toolbar.getStatus(left_toolbar.EUR_URL), self.OK)

    # def testSearchByClick(self):
    #     self.toolbar.open()
    #     search = self.toolbar.searchNews

    #     search.setQuery()
    #     search.clickSearchIcon()
    #     self.assertEqual(search.QUERY_URL, search.getURL())
    #     self.assertEqual(search.getStatus(search.QUERY_URL), self.OK)

    # def testSearchByKeyPress(self):
    #     self.toolbar.open()
    #     search = self.toolbar.searchNews
    #     search.setQuery()
    #     search.pressEnterKey()
    #     self.assertEqual(search.QUERY_URL, search.getURL())
    #     self.assertEqual(search.getStatus(search.QUERY_URL), self.OK)
