# -*- coding: utf-8 -*-

import unittest
import os
import time
from pages.about_page import AboutPage
from pages.auth_page import AuthPage
from constants import profiles

from pages.base_settings_page import BaseSettingsPage

from selenium.webdriver import DesiredCapabilities, Remote


class Tests(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    # def test_home(self):
    #
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()
    #
    #     auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)
    #
    #     base_settings_page = BaseSettingsPage(self.driver)
    #     base_settings_page.open('/settings')
    #     personal_data = base_settings_page.personal_data()
    #
    #     city = u"Москва"
    #     country = u"Россия"
    #     personal_data.set_home_city_country(city, country)
    #     personal_data.save()
    #
    #     personal_data = base_settings_page.personal_data()
    #     new_city, new_country = personal_data.get_home_city_country()
    #
    #     self.assertEqual(city, new_city)
    #     self.assertEqual(country, new_country)
    #
    # def test_home_error(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()
    #
    #     auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)
    #
    #     base_settings_page = BaseSettingsPage(self.driver)
    #     base_settings_page.open('/settings')
    #     personal_data = base_settings_page.personal_data()
    #
    #     city = u"Масква"
    #     country = u"Россия"
    #     error = u"Пожалуйста, выберите место проживания из списка"
    #
    #     personal_data.set_home_city_country(city, country)
    #     personal_data.save()
    #
    #     e = personal_data.home_error()
    #     self.assertEqual(e, error)
    #
    #     city = u"Москва"
    #     country = u"Рассия"
    #     personal_data.set_home_city_country(city, country)
    #     personal_data.save()
    #
    #     e = personal_data.home_error()
    #     self.assertEqual(e, error)
    #
    # def test_change_sex(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()
    #
    #     auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)
    #
    #     base_settings_page = BaseSettingsPage(self.driver)
    #     base_settings_page.open('/settings')
    #     personal_data = base_settings_page.personal_data()
    #
    #     male = False
    #     personal_data.change_sex(male)
    #     personal_data.save()
    #
    #     personal_data = base_settings_page.personal_data()
    #     new_male = personal_data.get_sex()
    #
    #     self.assertEqual(male, new_male)

    def test_war_city(self):
        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open('/bochrvf260602.lp/about')

        about_form = about_page.about_form()
        war_form = about_form.war_data()
        war_form.city()
        war_form.unit()
        war_form.button_ok()

        time.sleep(1)

        # city = "Москва"
        # unit = "7456"
        #
        # war_data.set_city_unit(city, unit)
        # war_data = about_page.war_data()
        #
        # new_city, new_unit = war_data.get_city_unit()
        # self.assertEqual(city, new_city)
        # self.assertEqual(unit, new_unit)

    # def test_war_city_error(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()
    #
    #     auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)
    #
    #     about_page = AboutPage(self.driver)
    #     about_page.open('/bochrvf260602.lp/about')
    #
    #     war_data = about_page.war_data()
    #
    #     city = "Москва"
    #     unit = "91824018420214092109"
    #     error = "Мы не знаем о такой воинской части"
    #
    #     war_data.set_city_unit(city, unit)
    #
    #     e = war_data.get_error_unit()
    #     self.assertEqual(error, e)
    #
    # def test_war_city_dup(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()
    #
    #     auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)
    #
    #     about_page = AboutPage(self.driver)
    #     about_page.open('/bochrvf260602.lp/about')
    #
    #     war_data = about_page.war_data()
    #
    #     city = "Москва"
    #     unit = "7456"
    #     error = "Вы уже состоите в этом сообществе"
    #
    #     war_data.set_city_unit(city, unit)
    #     war_data.set_city_unit(city, unit)
    #
    #     e = war_data.get_error_unit()
    #     self.assertEqual(error, e)
    #
    # def test_study_city(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()
    #
    #     auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)
    #
    #     about_page = AboutPage(self.driver)
    #     about_page.open('/bochrvf260602.lp/about')
    #
    #     study_data = about_page.study_data()
    #
    #     city = "Москва"
    #     unit = "1 школа"
    #
    #     study_data.set_city_unit(city, unit)
    #     study_data = about_page.study_data()
    #
    #     new_city, new_unit = study_data.get_city_unit()
    #     self.assertEqual(city, new_city)
    #     self.assertEqual(unit, new_unit)
    #
    # def test_study_city_error(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()
    #
    #     auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)
    #
    #     about_page = AboutPage(self.driver)
    #     about_page.open('/bochrvf260602.lp/about')
    #
    #     study_data = about_page.study_data()
    #
    #     city = "Москва"
    #     unit = "1 школа"
    #     error = "Мы не знаем о такой школе"
    #
    #     study_data.set_city_unit(city, unit)
    #
    #     e = study_data.get_error_unit()
    #     self.assertEqual(error, e)
    #
    # def test_study_city_dup(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()
    #
    #     auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)
    #
    #     about_page = AboutPage(self.driver)
    #     about_page.open('/bochrvf260602.lp/about')
    #
    #     study_data = about_page.study_data()
    #
    #     city = "Москва"
    #     unit = "1 школа"
    #     error = "Вы уже состоите в этом сообществе"
    #
    #     study_data.set_city_unit(city, unit)
    #     study_data.set_city_unit(city, unit)
    #
    #     e = study_data.get_error_unit()
    #     self.assertEqual(error, e)
    #
    # def test_work_city(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()
    #
    #     auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)
    #
    #     about_page = AboutPage(self.driver)
    #     about_page.open('/bochrvf260602.lp/about')
    #
    #     work_data = about_page.work_data()
    #
    #     city = "Москва"
    #     unit = "11-й автобусный парк"
    #
    #     work_data.set_city_unit(city, unit)
    #     work_data = about_page.work_data()
    #
    #     new_city, new_unit = work_data.get_city_unit()
    #     self.assertEqual(city, new_city)
    #     self.assertEqual(unit, new_unit)
    #
    # def test_study_city_error(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()
    #
    #     auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)
    #
    #     about_page = AboutPage(self.driver)
    #     about_page.open('/bochrvf260602.lp/about')
    #
    #     work_data = about_page.work_data()
    #
    #     city = "Москва"
    #     unit = "11-й автобусный парк"
    #     error = "Мы не знаем о организации"
    #
    #     work_data.set_city_unit(city, unit)
    #
    #     e = work_data.get_error_unit()
    #     self.assertEqual(error, e)
    #
    # def test_study_city_dup(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.open()
    #
    #     auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)
    #
    #     about_page = AboutPage(self.driver)
    #     about_page.open('/bochrvf260602.lp/about')
    #
    #     work_data = about_page.work_data()
    #
    #     city = "Москва"
    #     unit = "11-й автобусный парк"
    #     error = "Вы уже состоите в этом сообществе"
    #
    #     work_data.set_city_unit(city, unit)
    #     work_data.set_city_unit(city, unit)
    #
    #     e = work_data.get_error_unit()
    #     self.assertEqual(error, e)