import os
from dotenv import load_dotenv
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium import webdriver


class Test(unittest.TestCase):
    def setUp(self):
        load_dotenv(".env")

        browser = os.environ.get("BROWSER", "CHROME")

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        # self.driver = webdriver.Firefox(executable_path="../geckodriver")
        # self.driver = webdriver.Chrome(executable_path="../chromedriver")

    def tearDown(self):
        self.driver.quit()
