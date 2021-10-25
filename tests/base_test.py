import unittest

import settings as s
from selenium.webdriver import DesiredCapabilities, Remote


class BaseTest(unittest.TestCase):
    driver = None
    page = None

    @classmethod
    def setUpClass(cls):
        cls.driver = Remote(
            command_executor=s.HUB_URL,
            desired_capabilities=getattr(DesiredCapabilities, 'CHROME').copy()
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
