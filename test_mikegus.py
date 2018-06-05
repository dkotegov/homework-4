# -*- coding: utf-8 -*-

import unittest
import os
from pages.about_page import AboutPage
from pages.auth_page import AuthPage
from pages.community_page import CommunityPage
from pages.main_page import MainPage
from constants import profiles
from constants import army
from constants import career
from constants import comminity
from constants import study
from constants import main_page

from pages.base_settings_page import BaseSettingsPage

from selenium.webdriver import DesiredCapabilities, Remote


class TestsMikeGus(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', profiles.BROWSER)

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_change_sex_to_female_form(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        base_settings_page.make_male()

        base_settings_page.make_female()
        self.assertEqual(base_settings_page.female_on_form(), True)

    def test_change_sex_to_male_form(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        base_settings_page.make_female()

        base_settings_page.make_male()
        self.assertEqual(base_settings_page.male_on_form(), True)

    def test_change_sex_to_female_main(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        base_settings_page.make_female()

        m_page = MainPage(self.driver)
        m_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)
        self.assertEqual(m_page.my_birth_note(), main_page.FEMALE_BIRTH_NOTE)

    def test_change_sex_to_male_main(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        base_settings_page.make_male()

        m_page = MainPage(self.driver)
        m_page.open_page_by_url(profiles.PROFILE_TECHNOPARK11_SLUG)
        self.assertEqual(m_page.my_birth_note(), main_page.MALE_BIRTH_NOTE)

    def test_army_correct_city_unit(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver, profiles.PROFILE_TECHNOPARK11_SLUG)
        about_page.open()

        about_page.add_army_correct(army.CORRECT_CITY, army.CORRECT_UNIT)

        self.assertEqual(about_page.check_army_presence(), True)

        community_page = CommunityPage(self.driver, army.CORRECT_ARMY_REFERENCE)
        community_page.open()
        community_page.leave_community()

    def test_army_no_city_correct_unit(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver, profiles.PROFILE_TECHNOPARK11_SLUG)
        about_page.open()

        about_page.add_army_no_city_correct_unit(army.CORRECT_UNIT)

        self.assertEqual(about_page.check_army_presence(), True)

        community_page = CommunityPage(self.driver, army.CORRECT_ARMY_REFERENCE)
        community_page.open()
        community_page.leave_community()

    def test_army_incorrect_city_unit(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver, profiles.PROFILE_TECHNOPARK11_SLUG)
        about_page.open()

        error = about_page.add_army_correct_city_incorrect_unit(army.CORRECT_CITY,
                                                                army.INCORRECT_UNIT)
        self.assertEqual(error, army.ERROR_INVALID_UNIT)

    def test_army_incorrect_city_unit_presence(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver, profiles.PROFILE_TECHNOPARK11_SLUG)
        about_page.open()

        about_page.add_army_correct_city_incorrect_unit(army.CORRECT_CITY,
                                                        army.INCORRECT_UNIT)

        self.assertEqual(about_page.check_army_presence(), False)

    def test_army_duplicate(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver, profiles.PROFILE_TECHNOPARK11_SLUG)
        about_page.open()

        error = about_page.add_army_duplicate(army.CORRECT_CITY, army.CORRECT_UNIT)

        self.assertEqual(error, comminity.ERROR_DUPLICATE_COMMUNITY)

        community_page = CommunityPage(self.driver, army.CORRECT_ARMY_REFERENCE)
        community_page.open()
        community_page.leave_community()

    def test_career_correct_city_job(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver, profiles.PROFILE_TECHNOPARK11_SLUG)
        about_page.open()

        about_page.add_career_correct(career.CORRECT_CITY_COUNTRY, career.CORRECT_JOB)
        self.assertEqual(about_page.check_job_presence(), True)

        community_page = CommunityPage(self.driver, career.CORRECT_CAREER_REFERENCE)
        community_page.open()
        community_page.leave_community()

    def test_career_no_city_correct_job(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver, profiles.PROFILE_TECHNOPARK11_SLUG)
        about_page.open()

        about_page.add_career_no_city_correct_job(career.CORRECT_JOB)
        self.assertEqual(about_page.check_job_presence(), True)

        community_page = CommunityPage(self.driver, career.CORRECT_CAREER_REFERENCE)
        community_page.open()
        community_page.leave_community()

    def test_career_incorrect_city_correct_job(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver, profiles.PROFILE_TECHNOPARK11_SLUG)
        about_page.open()

        error = about_page.add_career_incorrect_city_correct_job(career.INCORRECT_CITY_COUNTRY)
        self.assertEqual(error, career.ERROR_INVALID_CITY)

    def test_career_correct_city_incorrect_job(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver, profiles.PROFILE_TECHNOPARK11_SLUG)
        about_page.open()

        error = about_page.add_career_correct_city_incorrect_job(career.CORRECT_CITY_COUNTRY,
                                                                 career.INCORRECT_JOB)
        self.assertEqual(error, career.ERROR_INVALID_JOB)

    def test_career_duplicate(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver, profiles.PROFILE_TECHNOPARK11_SLUG)
        about_page.open()

        error = about_page.add_career_duplicate(career.CORRECT_CITY_COUNTRY,
                                                career.CORRECT_JOB)
        self.assertEqual(error, comminity.ERROR_DUPLICATE_COMMUNITY)

        community_page = CommunityPage(self.driver, career.CORRECT_CAREER_REFERENCE)
        community_page.open()
        community_page.leave_community()

    def test_study_correct_city_school(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver, profiles.PROFILE_TECHNOPARK11_SLUG)
        about_page.open()

        about_page.add_school_correct(study.CORRECT_CITY_COUNTRY, study.CORRECT_SCHOOL)
        self.assertEqual(about_page.check_school_presence(), True)

        community_page = CommunityPage(self.driver, study.CORRECT_SCHOOL_REFERENCE)
        community_page.open()
        community_page.leave_community()

    def test_study_no_city_correct_school(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver, profiles.PROFILE_TECHNOPARK11_SLUG)
        about_page.open()

        about_page.add_school_no_city_correct_school(study.CORRECT_SCHOOL)
        self.assertEqual(about_page.check_school_presence(), True)

        community_page = CommunityPage(self.driver, study.CORRECT_SCHOOL_REFERENCE)
        community_page.open()
        community_page.leave_community()

    def test_study_incorrect_city_correct_school(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver, profiles.PROFILE_TECHNOPARK11_SLUG)
        about_page.open()

        error = about_page.add_school_incorrect_city_correct_school(study.INCORRECT_CITY_COUNTRY)
        self.assertEqual(error, study.ERROR_INVALID_CITY)

    def test_study_correct_city_incorrect_school(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver, profiles.PROFILE_TECHNOPARK11_SLUG)
        about_page.open()

        error = about_page.add_school_correct_city_incorrect_school(study.CORRECT_CITY_COUNTRY,
                                                                    study.INCORRECT_SCHOOL)
        self.assertEqual(error, study.ERROR_INVALID_SCHOOL)

    def test_school_duplicate(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver, profiles.PROFILE_TECHNOPARK11_SLUG)
        about_page.open()

        error = about_page.add_school_duplicate(study.CORRECT_CITY_COUNTRY,
                                                study.CORRECT_SCHOOL)
        self.assertEqual(error, comminity.ERROR_DUPLICATE_COMMUNITY)

        community_page = CommunityPage(self.driver, study.CORRECT_SCHOOL_REFERENCE)
        community_page.open()
        community_page.leave_community()
