import os
import unittest

from components.login_and_write import login_and_write
from selenium.webdriver import DesiredCapabilities, Remote

from tests.base_test import BaseTest


class AttachTests(BaseTest):

    def test(self):
        login_and_write(self.driver, self.USEREMAIL, self.PASSWORD)