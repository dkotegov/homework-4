import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities, Remote

from tests.cases.base import TestAuthorized
from tests.pages.create_pin import CreatePinPage


class Test(TestAuthorized):
    def setUp(self):
        super().setUp()
        self.page = CreatePinPage(self.driver)

    def test_valid_data(self):
        pin_name = "this is valid test pin"
        pin_content = "this is normal pin description"
        file_name = "C:/312207-Lastochka.jpg"
        self.page.form_list.set_pin_name(pin_name)
        self.page.form_list.set_pin_content(pin_content)
        self.page.form_list.load_file(file_name)
        self.page.form_list.create_pin()
        if self.page.form_list.get_error() != '':
            assert "error"

