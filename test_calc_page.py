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
        delta_days = timedelta(days=139)
        last_day = now_date + delta_days
        self.first_date = now_date.strftime("%d.%m.%Y")
        self.last_date = last_day.strftime("%d.%m.%Y")
        self.salary = "100000"
        self.exp = 'менее 6 месяцев'
        self.rate = "2"
        self.stavka = "2"
        self.delta = "140 дней"

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_calc(self):
        calc_page = CalcPage(self.driver)
        calc_page.open()

        calc = calc_page.calc

        salary = self.salary
        exp = self.exp
        rate = self.rate
        stavka = self.stavka
        first_date = self.first_date
        last_date = self.last_date

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="form-0-first_year_salary"]'))
        )
        calc.set_first_salary(salary)
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="form-0-second_year_salary"]'))
        )
        calc.set_second_salary(salary)
        calc.set_area_rate(rate)
        calc.set_stavka(stavka)
        calc.set_first_day_holiday(first_date)
        calc.set_last_day_holiday(last_date)
        calc.set_experience(exp)

        calc.click_calculate()
        self.assertEquals(self.delta, calc.get_delta_days())
