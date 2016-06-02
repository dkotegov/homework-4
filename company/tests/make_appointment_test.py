# -*- coding: utf-8 -*-
__author__ = 'niggor'
import os
import unittest
from company.pages.companies_page import CompaniesPage
from selenium.webdriver import DesiredCapabilities, Remote


class MakeAppointmentTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = CompaniesPage(self.driver)
        self.page.open()
        self.appointment = self.page.make_an_appointment

    def test_make_an_appointment(self):
        self.page.make_an_appointment.submit()
        #self.page.wait_for_another_page()
        self.assertEquals(u'Запись к врачу', self.page.make_an_appointment.get_title())

    def tearDown(self):
       # self.page.close()
        self.driver.quit()
