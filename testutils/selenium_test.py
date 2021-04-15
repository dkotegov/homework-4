import unittest

from selenium.webdriver import Remote, DesiredCapabilities
from .utils import CurrentBrowser


def get_driver(browser):
    return Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=getattr(DesiredCapabilities, browser).copy()
    )


GlobalCurrentBrowser = CurrentBrowser()


class SeleniumTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver(GlobalCurrentBrowser.get())

    def tearDown(self) -> None:
        self.driver.quit()
