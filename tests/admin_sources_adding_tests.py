# -*- coding: utf-8 -*-

import os
import random
import unittest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.pages.admin_page import AdminPage


class AdminSourcesAddingTests(unittest.TestCase):
    SRC_NAME = "Laptop"
    SRC_DESCRIPTION = "ThinkPad T430p"

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.admin_page = AdminPage(self.driver)
        self.admin_page.open()
        self.admin_page.goto_source_form()
        self.src_form = self.admin_page.source_form
        self.src_list = self.admin_page.source_list

    def tearDown(self):
        self.admin_page.reset()
        self.driver.quit()

    def test_form_empty_all(self):
        self.src_form.set_id("")
        self.src_form.set_name("")
        self.src_form.set_description("")
        self.src_form.set_number("")
        self.src_form.submit()
        alert_text = self.admin_page.alert_accept()

        self.assertEqual(alert_text.encode('utf-8'), self.src_form.get_empty_id_msg())

    def test_form_empty_id(self):
        src_id = 1000 + int(random.random() * 1000)
        self.src_form.set_id("")
        self.src_form.set_name(self.SRC_NAME + str(src_id))
        self.src_form.set_description(self.SRC_DESCRIPTION)
        self.src_form.set_number(5)
        self.src_form.attach_image()
        self.src_form.submit()
        alert_text = self.admin_page.alert_accept()

        self.assertEqual(alert_text.encode('utf-8'), self.src_form.get_empty_id_msg())

    def test_form_empty_name(self):
        src_id = 1000 + int(random.random() * 1000)
        self.src_form.set_id(src_id)
        self.src_form.set_name("")
        self.src_form.set_description(self.SRC_DESCRIPTION)
        self.src_form.set_number(5)
        self.src_form.attach_image()
        self.src_form.submit()
        alert_text = self.admin_page.alert_accept()

        self.assertEqual(alert_text.encode('utf-8'), self.src_form.get_empty_name_msg())

    def test_form_empty_description(self):
        src_id = 1000 + int(random.random() * 1000)
        self.src_form.set_id(src_id)
        self.src_form.set_name(self.SRC_NAME + str(src_id))
        self.src_form.set_description("")
        self.src_form.set_number(5)
        self.src_form.attach_image()
        self.src_form.submit()
        alert_text = self.admin_page.alert_accept()

        self.assertEqual(alert_text.encode('utf-8'), self.src_form.get_empty_description_msg())

    def test_form_empty_number(self):
        src_id = 1000 + int(random.random() * 1000)
        self.src_form.set_id(src_id)
        self.src_form.set_name(self.SRC_NAME + str(src_id))
        self.src_form.set_description(self.SRC_DESCRIPTION)
        self.src_form.set_number("")
        self.src_form.attach_image()
        self.src_form.submit()
        alert_text = self.admin_page.alert_accept()

        self.assertEqual(alert_text.encode('utf-8'), self.src_form.get_empty_number_msg())

    def test_form_invalid_id(self):
        src_id = "string" + str(int(random.random() * 1000))
        self.src_form.set_id(src_id)
        self.src_form.set_name(self.SRC_NAME + str(src_id))
        self.src_form.set_description(self.SRC_DESCRIPTION)
        self.src_form.set_number(5)
        self.src_form.attach_image()
        self.src_form.submit()
        alert_text = self.admin_page.alert_accept()

        self.assertEqual(alert_text.encode('utf-8'), self.src_form.get_id_not_int_msg())

    def test_form_invalid_number(self):
        src_id = 1000 + int(random.random() * 1000)
        self.src_form.set_id(src_id)
        self.src_form.set_name(self.SRC_NAME + str(src_id))
        self.src_form.set_description(self.SRC_DESCRIPTION)
        self.src_form.set_number("string")
        self.src_form.attach_image()
        self.src_form.submit()
        alert_text = self.admin_page.alert_accept()

        self.assertEqual(alert_text.encode('utf-8'), self.src_form.get_number_not_int_msg())

    def test_form_valid_all(self):
        src_id = 1000 + int(random.random() * 1000)
        self.src_form.set_id(src_id)
        self.src_form.set_name(self.SRC_NAME + str(src_id))
        self.src_form.set_description(self.SRC_DESCRIPTION)
        self.src_form.set_number(5)
        self.src_form.attach_image()
        self.src_form.submit()
        alert_text = self.admin_page.alert_accept()

        self.assertEqual(alert_text.encode('utf-8'), self.src_form.get_ok_msg())

    def test_form_already_exists(self):
        src_id = 1000 + int(random.random() * 1000)

        self.src_form.set_id(src_id)
        self.src_form.set_name(self.SRC_NAME + str(src_id))
        self.src_form.set_description(self.SRC_DESCRIPTION)
        self.src_form.set_number(5)
        self.src_form.attach_image()
        self.src_form.submit()
        self.admin_page.alert_accept()

        self.src_form.clear_form()

        self.src_form.set_id(src_id)
        self.src_form.set_name(self.SRC_NAME + str(src_id))
        self.src_form.set_description(self.SRC_DESCRIPTION)
        self.src_form.set_number(5)
        self.src_form.attach_image()
        self.src_form.submit()
        alert_text = self.admin_page.alert_accept()

        self.assertEqual(alert_text.encode('utf-8'), self.src_form.get_already_exists_msg())

    def test_add_source_to_base(self):
        self.admin_page.goto_source_list()
        start_count = self.src_list.count_records()

        self.admin_page.goto_source_form()
        src_id = 1000 + int(random.random() * 1000)
        self.src_form.set_id(src_id)
        self.src_form.set_name(self.SRC_NAME + str(src_id))
        self.src_form.set_description(self.SRC_DESCRIPTION)
        self.src_form.set_number(5)
        self.src_form.attach_image()
        self.src_form.submit()
        self.admin_page.alert_accept()

        self.admin_page.goto_source_list()
        current_count = self.src_list.count_records()

        self.assertEqual(current_count, start_count + 1)
