# -*- coding: utf-8 -*-

import unittest
import os
import time
from pages.about_page import AboutPage
from pages.auth_page import AuthPage
from pages.community_page import CommunityPage
from constants import profiles
from constants import army
from constants import career
from constants import comminity
from selenium.common.exceptions import NoSuchElementException

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

    def test_army_correct_city_unit(self):
        return
        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open(profiles.PROFILE_TECHNOPARK11_ABOUT_PAGE)

        about_form = about_page.about_form()
        army_form = about_form.army_form()
        army_form.add_city_unit(army.CORRECT_CITY, army.CORRECT_UNIT)
        army_form.button_ok()
        about_form.close_popup()

        try:
            about_form.get_top_unit()
        except NoSuchElementException:
            self.fail('в/ч не добавлена')

        community_page = CommunityPage(self.driver)
        community_page.open(army.CORRECT_ARMY_REFERENCE)
        community_form = community_page.community_form()
        community_form.leave()

    def test_army_incorrect_city_unit(self):
        return
        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open(profiles.PROFILE_TECHNOPARK11_ABOUT_PAGE)

        about_form = about_page.about_form()
        army_form = about_form.army_form()
        army_form.put_city(army.CORRECT_CITY)
        army_form.put_unit(army.INCORRECT_UNIT)

        error = army_form.army_error()
        self.assertEqual(error, army.ERROR_INVALID_UNIT)

    def test_army_duplicate(self):
        return
        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open(profiles.PROFILE_TECHNOPARK11_ABOUT_PAGE)

        about_form = about_page.about_form()
        army_form = about_form.army_form()
        army_form.add_city_unit(army.CORRECT_CITY, army.CORRECT_UNIT)
        army_form.button_ok()
        about_form.close_popup()

        army_form = about_form.army_form()
        army_form.add_city_unit(army.CORRECT_CITY, army.CORRECT_UNIT)
        error = army_form.army_error()
        self.assertEqual(error, comminity.ERROR_DUPLICATE_COMMUNITY)

        community_page = CommunityPage(self.driver)
        community_page.open(army.CORRECT_ARMY_REFERENCE)
        community_form = community_page.community_form()
        community_form.leave()

    def test_career_correct_city_job(self):
        return
        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open(profiles.PROFILE_TECHNOPARK11_ABOUT_PAGE)

        about_form = about_page.about_form()
        career_form = about_form.career_form()
        career_form.add_city_job(career.CORRECT_CITY_COUNTRY, career.CORRECT_JOB)
        career_form.button_ok()
        about_form.close_popup()

        try:
            about_form.get_top_job()
        except NoSuchElementException:
            self.fail('место работы не добавлено')

        community_page = CommunityPage(self.driver)
        community_page.open(career.CORRECT_CAREER_REFERENCE)
        community_form = community_page.community_form()
        community_form.leave()

    def test_career_incorrect_city_job(self):
        return
        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open(profiles.PROFILE_TECHNOPARK11_ABOUT_PAGE)

        about_form = about_page.about_form()
        career_form = about_form.career_form()
        career_form.put_city(career.INCORRECT_CITY_COUNTRY)
        error = career_form.city_error()
        self.assertEqual(error, career.ERROR_INVALID_CITY)

        about_page.open(profiles.PROFILE_TECHNOPARK11_ABOUT_PAGE)
        about_form = about_page.about_form()
        career_form = about_form.career_form()

        career_form.add_city(career.CORRECT_CITY_COUNTRY)
        career_form.put_job(career.INCORRECT_JOB)
        error = career_form.job_error()
        self.assertEqual(error, career.ERROR_INVALID_JOB)

    def test_career_duplicate(self):
        return
        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open(profiles.PROFILE_TECHNOPARK11_ABOUT_PAGE)

        about_form = about_page.about_form()
        career_form = about_form.career_form()
        career_form.add_city_job(career.CORRECT_CITY_COUNTRY, career.CORRECT_JOB)
        career_form.button_ok()
        about_form.close_popup()

        career_form = about_form.career_form()
        career_form.add_city_job(career.CORRECT_CITY_COUNTRY, career.CORRECT_JOB)
        error = career_form.job_error()
        self.assertEqual(error, comminity.ERROR_DUPLICATE_COMMUNITY)

        community_page = CommunityPage(self.driver)
        community_page.open(career.CORRECT_CAREER_REFERENCE)
        community_form = community_page.community_form()
        community_form.leave()

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
