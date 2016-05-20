# -*- coding: utf-8 -*-
import os

from selenium.webdriver import Remote, DesiredCapabilities

from pages.pages import AwardsPage
import unittest

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.page = AwardsPage(self.driver)
        self.page.open()

    def tearDown(self):
        self.driver.quit()


class AwardsPageTestCase(BaseTestCase):

    def test_click_oscar_btn(self):
        self.page.awards_block.click_oscar_btn()
        self.assertEqual(self.driver.current_url, self.page.awards_block.OSCAR_BTN_URL)

    def test_click_globus_btn(self):
        self.page.awards_block.click_globus_btn()
        self.assertEqual(self.driver.current_url, self.page.awards_block.GLOBUS_BTN_URL)

    def test_click_emmy_btn(self):
        self.page.awards_block.click_emmy_btn()
        self.assertEqual(self.driver.current_url, self.page.awards_block.EMMY_BTN_URL)

    def test_click_cannes_btn(self):
        self.page.awards_block.click_cannes_btn()
        self.assertEqual(self.driver.current_url, self.page.awards_block.CANNES_BTN_URL)

    def test_click_oscar_btn(self):
        self.page.awards_block.click_oscar_btn()
        self.assertEqual(self.driver.current_url, self.page.awards_block.OSCAR_BTN_URL)

    def test_click_msk_kf_btn(self):
        self.page.awards_block.click_msk_kf_btn()
        self.assertEqual(self.driver.current_url, self.page.awards_block.MSK_KF_BTN_URL)

    def test_click_odes_kf_btn(self):
        self.page.awards_block.click_odes_kf_btn()
        self.assertEqual(self.driver.current_url, self.page.awards_block.ODES_KF_BTN_URL)

    def test_click_ven_kf_btn(self):
        self.page.awards_block.click_ven_kf_btn()
        self.assertEqual(self.driver.current_url, self.page.awards_block.VEN_KF_BTN_URL)

    def test_click_oscar_link(self):
        self.page.awards_block.click_oscar_link()
        self.assertEqual(self.driver.current_url, self.page.awards_block.OSCAR_BTN_URL)

    def test_click_globus_link(self):
        self.page.awards_block.click_globus_link()
        self.assertEqual(self.driver.current_url, self.page.awards_block.GLOBUS_BTN_URL)

    def test_click_emmy_link(self):
        self.page.awards_block.click_emmy_link()
        self.assertEqual(self.driver.current_url, self.page.awards_block.EMMY_BTN_URL)

    def test_click_cannes_link(self):
        self.page.awards_block.click_cannes_link()
        self.assertEqual(self.driver.current_url, self.page.awards_block.CANNES_BTN_URL)

    def test_click_oscar_link(self):
        self.page.awards_block.click_oscar_link()
        self.assertEqual(self.driver.current_url, self.page.awards_block.OSCAR_BTN_URL)

    def test_click_msk_kf_link(self):
        self.page.awards_block.click_msk_kf_link()
        self.assertEqual(self.driver.current_url, self.page.awards_block.MSK_KF_BTN_URL)

    def test_click_odes_kf_link(self):
        self.page.awards_block.click_odes_kf_link()
        self.assertEqual(self.driver.current_url, self.page.awards_block.ODES_KF_BTN_URL)

    def test_click_ven_kf_link(self):
        self.page.awards_block.click_ven_kf_link()
        self.assertEqual(self.driver.current_url, self.page.awards_block.VEN_KF_BTN_URL)
