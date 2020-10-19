import unittest
from selenium.webdriver import DesiredCapabilities, Remote


class GetTest(unittest.TestCase):
    def setUp(self) -> None:
        browser = 'CHROME'
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self) -> None:
        self.driver.quit()

    def runTest(self):
        self.driver.get("http://park.mail.ru/")
