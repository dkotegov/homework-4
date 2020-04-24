import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from steps.mainpage.main_page_steps import MainSteps
from tests.base_test import BaseTest


class RefAboutCompanyTest(BaseTest):

    def test(self):
        driver = self.driver

        mainsteps = MainSteps(driver)
        mainsteps.open()
        mainsteps.ref_about_company()

        assert "No results found." not in driver.page_source