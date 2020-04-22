import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities, Remote

from tests.cases.base import TestAuthorized
from tests.pages.auth import AuthPage
from tests.pages.user_details import UserDetailsPage


class Test(TestAuthorized):
    def setUp(self):
        super().setUp()
        self.page = UserDetailsPage(self.driver,  'testTest')

    def test_subscribe(self):
        self.page.form.subscribe()

    def test_unsubscribe(self):
        self.page.form.unsubscribe()

