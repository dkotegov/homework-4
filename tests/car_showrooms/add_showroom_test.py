# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.car_showrooms.pages import ShowroomPage, Component


class AddShowroomForm(Component):
    TITLE = u'ДОБАВИТЬ АВТОСАЛОН'

    __OPEN_BUTTON = 'button.button.button_wide.button_type-1.js-show_form'
    __FORM_TITLE = 'div.box__title'

    def open_form(self):
        self.driver.find_element_by_css_selector(self.__OPEN_BUTTON).click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.__FORM_TITLE))
        )

    def get_title(self):
        return self.driver.find_element_by_css_selector(self.__FORM_TITLE).text


class AddShowroomFormTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_open(self):
        page = ShowroomPage(self.driver)
        page.open()

        add_showroom_form = page.add_showroom_form
        add_showroom_form.open_form()

        self.assertEqual(add_showroom_form.get_title(), add_showroom_form.TITLE)
