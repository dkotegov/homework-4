# -*- coding: utf-8 -*-
__author__ = 'alla'
import os
import unittest
from drugs.pages.one_drug_page import DrugPage

from selenium.webdriver import DesiredCapabilities, Remote


class LinksTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = DrugPage(self.driver, 'vizarsin')
        self.page.open()
        self.contraindication = self.page.contraindication
        self.social_networks = self.page.social_networks
        self.instructions = self.page.instructions

    def test_contraindications(self):
        for link in self.contraindication.links():
            self.assertTrue(self.contraindication.check_link(link))

    def test_instructions(self):
        for link in self.page.instructions.links():
            self.assertTrue(self.page.instructions.check_link(link))

    def test_social_networks(self):
        for link in self.page.social_networks.links():
            self.assertTrue(self.page.social_networks.check_link(link))

    def tearDown(self):
        #self.page.close()
        self.driver.quit()
