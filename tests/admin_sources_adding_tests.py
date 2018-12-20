# -*- coding: utf-8 -*-

import os
import random
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.pages.admin_page import AdminPage


class AdminSourcesAddingTests(unittest.TestCase):
    SRC_NAME = "Laptop"
    SRC_DESCRIPTION = "ThinkPad T430p"

    get_ok_msg = "Источник успешно добавлен."
    get_already_exists_msg = "Источник уже существует в базе данных."
    get_empty_id_msg = "Id is empty."
    get_empty_name_msg = "Name is empty."
    get_empty_description_msg = "Description is empty."
    get_empty_number_msg = "Number is empty."
    get_id_not_int_msg = "Id is not integer."
    get_number_not_int_msg = "Number is not integer."

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
        alert_text = self.admin_page.add_source(name="", description="", number="", src_id="")

        self.assertEqual(alert_text, self.get_empty_id_msg)

    def test_form_empty_id(self):
        src_id = 1000 + int(random.random() * 1000)
        alert_text = self.admin_page.add_source(
            name=self.SRC_NAME + str(src_id),
            description=self.SRC_DESCRIPTION,
            number=5,
            src_id="")

        self.assertEqual(alert_text, self.get_empty_id_msg)

    def test_form_empty_name(self):
        src_id = 1000 + int(random.random() * 1000)
        alert_text = self.admin_page.add_source(
            name="",
            description=self.SRC_DESCRIPTION,
            number=5,
            src_id=src_id)

        self.assertEqual(alert_text, self.get_empty_name_msg)

    def test_form_empty_description(self):
        src_id = 1000 + int(random.random() * 1000)
        alert_text = self.admin_page.add_source(
            name=self.SRC_NAME + str(src_id),
            description="",
            number=5,
            src_id=src_id)

        self.assertEqual(alert_text, self.get_empty_description_msg)

    def test_form_empty_number(self):
        src_id = 1000 + int(random.random() * 1000)
        alert_text = self.admin_page.add_source(
            name=self.SRC_NAME + str(src_id),
            description=self.SRC_DESCRIPTION,
            number="",
            src_id=src_id)

        self.assertEqual(alert_text, self.get_empty_number_msg)

    def test_form_invalid_id(self):
        src_id = "string" + str(int(random.random() * 1000))
        alert_text = self.admin_page.add_source(
            name=self.SRC_NAME + str(src_id),
            description=self.SRC_DESCRIPTION,
            number=5,
            src_id=src_id)

        self.assertEqual(alert_text, self.get_id_not_int_msg)

    def test_form_invalid_number(self):
        src_id = 1000 + int(random.random() * 1000)
        alert_text = self.admin_page.add_source(
            name=self.SRC_NAME + str(src_id),
            description=self.SRC_DESCRIPTION,
            number="string",
            src_id=src_id)

        self.assertEqual(alert_text, self.get_number_not_int_msg)

    def test_form_valid_all(self):
        src_id = 1000 + int(random.random() * 1000)
        alert_text = self.admin_page.add_source(
            name=self.SRC_NAME + str(src_id),
            description=self.SRC_DESCRIPTION,
            number=5,
            src_id=src_id)

        self.assertEqual(alert_text, self.get_ok_msg)

    def test_form_already_exists(self):
        src_id = 1000 + int(random.random() * 1000)

        self.admin_page.add_source(
            name=self.SRC_NAME + str(src_id),
            description=self.SRC_DESCRIPTION,
            number=5,
            src_id=src_id)

        self.src_form.clear_form()

        alert_text = self.admin_page.add_source(
            name=self.SRC_NAME + str(src_id),
            description=self.SRC_DESCRIPTION,
            number=5,
            src_id=src_id)

        self.assertEqual(alert_text, self.get_already_exists_msg)

    def test_add_source_to_base(self):
        self.admin_page.goto_source_list()
        start_count = self.src_list.count_records()

        self.admin_page.goto_source_form()
        src_id = 1000 + int(random.random() * 1000)
        self.admin_page.add_source(
            name=self.SRC_NAME + str(src_id),
            description=self.SRC_DESCRIPTION,
            number=5,
            src_id=src_id)

        self.admin_page.goto_source_list()
        current_count = self.src_list.count_records()

        self.assertEqual(current_count, start_count + 1)
