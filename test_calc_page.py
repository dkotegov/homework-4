# coding=utf-8

import os
import unittest

from selenium.webdriver import Remote, DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date, timedelta

from selenium.webdriver.support.wait import WebDriverWait

from page import CalcPage


class CalcTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        now_date = date.today()
        delta_days_140 = timedelta(days=139)
        delta_days_599421 = timedelta(days=599421)
        last_day_140 = now_date + delta_days_140
        last_day_599421 = now_date + delta_days_599421
        self.first_date = now_date.strftime("%d.%m.%Y")
        self.last_date = last_day_140.strftime("%d.%m.%Y")
        self.last_day_599421 = last_day_599421.strftime("%d.%m.%Y")
        self.salary = u'100000'
        self.exp = u'менее 6 месяцев'
        self.rate = u'2'
        self.stavka = u'2'
        self.delta = u'140 дней'
        self.delta_599421 = u'599422 дня'

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_calc_with_140_days(self):
        calc_page = CalcPage(self.driver)
        calc_page.open()

        calc = calc_page.calc

        salary = self.salary
        exp = self.exp
        rate = self.rate
        stavka = self.stavka
        first_date = self.first_date
        last_date = self.last_date

        calc.set_first_salary(salary)
        calc.set_second_salary(salary)
        calc.set_area_rate(rate)
        calc.set_stavka(stavka)
        calc.set_first_day_holiday(first_date)
        calc.set_last_day_holiday(last_date)
        calc.set_experience(exp)

        calc.click_calculate()
        self.assertEquals(self.delta, calc.get_delta_days())

    def test_calc_with_599421_days(self):
        calc_page = CalcPage(self.driver)
        calc_page.open()

        calc = calc_page.calc

        salary = self.salary
        exp = self.exp
        rate = self.rate
        stavka = self.stavka
        first_date = self.first_date
        last_date = self.last_day_599421

        calc.set_first_salary(salary)
        calc.set_second_salary(salary)
        calc.set_area_rate(rate)
        calc.set_stavka(stavka)
        calc.set_first_day_holiday(first_date)
        calc.set_last_day_holiday(last_date)
        calc.set_experience(exp)

        calc.click_calculate()
        self.assertEquals(self.delta_599421, calc.get_delta_days())
