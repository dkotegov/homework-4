import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from tests.page import Page, ElementWaiter, SettingsPage, OpenFilterSettings

class CreateFilterPage(Page):

    CHANGE_RULE = '//a[@hhref="javascript:void(0)"]'

    def change_rule_open(self):
        elem = ElementWaiter.whait_by_xpath(driver = self.driver, locator = self.CHANGE_RULE)
        elem.click()
    
    def set_rule(self):
        elem = ElementWaiter.whait_by_xpath(driver = self.driver, locator = self.CHANGE_RULE)
        elem.click()

class CreateNewFilterTest(unittest.TestCase):
    def setUp(self):

        self.driver = Remote(
		    command_executor='http://127.0.0.1:4444/wd/hub',
	        desired_capabilities=DesiredCapabilities.CHROME )

    def tearDown(self):
        self.driver.quit()
    
    def test(self):
        open_filter_settings = OpenFilterSettings(self.driver)
        open_filter_settings.open();
        settings_page = SettingsPage(self.driver)
        settings_page.create_new_filter()
        self.assertEqual(True, True)