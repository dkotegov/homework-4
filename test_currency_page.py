# coding=utf-8
import datetime
import unittest
from selenium.webdriver import Remote, DesiredCapabilities
from page import CurrencyPage
import os


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()


class TestCurrencyPage(BaseTestCase):
    MIN_VALUE = 1
    MAX_VALUE = 200

    def setUp(self):
        super(TestCurrencyPage, self).setUp()
        self.page = CurrencyPage(self.driver)

    def test_cb_rates(self):
        self.page.open()
        usd = self.page.cb.get_usd()
        self.assertTrue(self.MIN_VALUE < usd < self.MAX_VALUE)
        eur = self.page.cb.get_eur()
        self.assertTrue(self.MIN_VALUE < eur < self.MAX_VALUE)
        gbp = self.page.cb.get_gbp()
        self.assertTrue(self.MIN_VALUE < gbp < self.MAX_VALUE)
        chf = self.page.cb.get_chf()
        self.assertTrue(self.MIN_VALUE < chf < self.MAX_VALUE)

    def test_mmvb_rates(self):
        self.page.open()
        usd = self.page.mmvb.get_usd()
        self.assertTrue(self.MIN_VALUE < usd < self.MAX_VALUE)
        eur = self.page.mmvb.get_eur()
        self.assertTrue(self.MIN_VALUE < eur < self.MAX_VALUE)

    def test_cb_other_rates(self):
        self.page.open()
        for rate in self.page.cb.get_other_rates():
            self.assertTrue(self.MIN_VALUE < rate < self.MAX_VALUE)

    def test_cb_date(self):
        self.page.open()
        date = self.page.cb.get_date()
        today = datetime.datetime.today()
        today_str = today.strftime("%d.%m.%Y")
        tomorrow_str = (today + datetime.timedelta(days=1)).strftime("%d.%m.%Y")
        dates = [today_str, tomorrow_str]
        self.assertIn(date, dates)

    def test_cb_shares(self):
        window_name = 'share'
        old_window_name = self.driver.current_window_handle

        self.page.open()
        button = self.page.cb.get_button_share_my()
        button.click()
        self.driver.switch_to_window(window_name) #Если не происходит exception, значит открылось новое окно с предложением поделиться
        self.driver.close()

        self.driver.switch_to_window(old_window_name)

        button = self.page.cb.get_button_share_ok()
        button.click()
        self.driver.switch_to_window(window_name)
        self.driver.close()

        self.driver.switch_to_window(old_window_name)

        button = self.page.cb.get_button_share_vk()
        button.click()
        self.driver.switch_to_window(window_name)
        self.driver.close()

        self.driver.switch_to_window(old_window_name)

        button = self.page.cb.get_button_share_tw()
        button.click()
        self.driver.switch_to_window(window_name)
        self.driver.close()

        self.driver.switch_to_window(old_window_name)

    def test_currency_pairs(self):
        self.page.open()
        for rate in self.page.middle_block.get_currency_pairs():
            self.assertTrue(0 < rate < 10000)

    def test_oil_and_precious_metals(self):
        self.page.open()
        for rate in self.page.middle_block.get_oil_open_pairs():
            self.assertTrue(0 < rate < 10000)

    def test_blue(self):
        self.page.open()
        for rate in self.page.middle_block.get_blue():
            self.assertTrue(0 < rate < 10000)

    def test_converter(self):
        self.page.open()
        # self.page.currency_converter.set_first_input()