import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.series import SeriesPage
from pages.details import DetailsPage


class ClickOnSeriesTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        series_page = SeriesPage(self.driver)
        details_page = DetailsPage(self.driver)

        series_page.open()
        title = series_page.get_title_of_first_movie()
        series_page.click_on_first_movie()

        self.assertEqual(
            title,
            details_page.get_title()
        )
