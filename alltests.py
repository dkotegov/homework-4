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

    def test_change_sex(self):
        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()

        personal_data.check_female()
        personal_data.save()
        personal_data.close_save()

        personal_data = base_settings_page.personal_data()
        self.assertEqual(personal_data.is_female(), True)
        self.assertEqual(personal_data.is_male(), False)

        m_page = MainPage(self.driver)
        m_page.open(main_page.PROFILE_TECHNOPARK11_REFERENCE)
        self.assertEqual(m_page.my_birth_note(), main_page.FEMALE_BIRTH_NOTE)

        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()
        personal_data.check_male()
        personal_data.save()
        personal_data.close_save()

        personal_data = base_settings_page.personal_data()
        self.assertEqual(personal_data.is_female(), False)
        self.assertEqual(personal_data.is_male(), True)

        m_page.open(main_page.PROFILE_TECHNOPARK11_REFERENCE)
        self.assertEqual(m_page.my_birth_note(), main_page.MALE_BIRTH_NOTE)

    def test_army_correct_city_unit(self):
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

    def test_army_no_city_correct_unit(self):

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open(profiles.PROFILE_TECHNOPARK11_ABOUT_PAGE)

        about_form = about_page.about_form()
        army_form = about_form.army_form()
        army_form.add_city_unit('', army.CORRECT_UNIT)
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

        army_form.add_city_unit(army.INCORRECT_CITY, army.CORRECT_UNIT)
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

    def test_army_duplicate(self):
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

    def test_career_no_city_correct_job(self):
        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open(profiles.PROFILE_TECHNOPARK11_ABOUT_PAGE)

        about_form = about_page.about_form()
        career_form = about_form.career_form()
        career_form.put_city('')
        career_form.add_job(career.CORRECT_JOB)
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

        career_form.put_job('')
        career_form.put_city(career.INCORRECT_CITY_COUNTRY)
        error = career_form.city_error()
        self.assertEqual(error, career.ERROR_INVALID_CITY)

    def test_career_duplicate(self):
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

    def test_study_correct_city_school(self):
        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open(profiles.PROFILE_TECHNOPARK11_ABOUT_PAGE)

        about_form = about_page.about_form()
        study_form = about_form.study_form()
        study_form.add_city_school(study.CORRECT_CITY_COUNTRY, study.CORRECT_SCHOOL)
        study_form.button_ok()
        about_form.close_popup()

        try:
            about_form.get_top_school()
        except NoSuchElementException:
            self.fail('место учебы не добавлено')

        community_page = CommunityPage(self.driver)
        community_page.open(study.CORRECT_SCHOOL_REFERENCE)
        community_form = community_page.community_form()
        community_form.leave()

    def test_study_no_city_correct_school(self):
        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open(profiles.PROFILE_TECHNOPARK11_ABOUT_PAGE)

        about_form = about_page.about_form()
        study_form = about_form.study_form()
        study_form.put_city('')
        study_form.add_school(study.CORRECT_SCHOOL)
        study_form.button_ok()
        about_form.close_popup()

        try:
            about_form.get_top_school()
        except NoSuchElementException:
            self.fail('место учебы не добавлено')

        community_page = CommunityPage(self.driver)
        community_page.open(study.CORRECT_SCHOOL_REFERENCE)
        community_form = community_page.community_form()
        community_form.leave()

    def test_study_incorrect_city_school(self):
        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open(profiles.PROFILE_TECHNOPARK11_ABOUT_PAGE)

        about_form = about_page.about_form()
        study_form = about_form.study_form()
        study_form.put_city(study.INCORRECT_CITY_COUNTRY)
        error = study_form.city_error()
        self.assertEqual(error, study.ERROR_INVALID_CITY)

        about_page.open(profiles.PROFILE_TECHNOPARK11_ABOUT_PAGE)
        about_form = about_page.about_form()
        study_form = about_form.study_form()

        study_form.add_city(study.CORRECT_CITY_COUNTRY)
        study_form.put_school(study.INCORRECT_SCHOOL)
        error = study_form.school_error()
        self.assertEqual(error, study.ERROR_INVALID_SCHOOL)

        study_form.put_school('')
        study_form.put_city(study.INCORRECT_CITY_COUNTRY)
        error = study_form.city_error()
        self.assertEqual(error, study.ERROR_INVALID_CITY)

    def test_school_duplicate(self):
        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        about_page = AboutPage(self.driver)
        about_page.open(profiles.PROFILE_TECHNOPARK11_ABOUT_PAGE)

        about_form = about_page.about_form()
        study_form = about_form.study_form()
        study_form.add_city_school(study.CORRECT_CITY_COUNTRY, study.CORRECT_SCHOOL)
        study_form.button_ok()
        about_form.close_popup()

        study_form = about_form.study_form()
        study_form.add_city_school(study.CORRECT_CITY_COUNTRY, study.CORRECT_SCHOOL)
        error = study_form.school_error()
        self.assertEqual(error, comminity.ERROR_DUPLICATE_COMMUNITY)

        community_page = CommunityPage(self.driver)
        community_page.open(study.CORRECT_SCHOOL_REFERENCE)
        community_form = community_page.community_form()
        community_form.leave()

    def test_name_surname_letters(self):
        name = "Name"
        surname = "Surname"

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()
        personal_data.name_surname(name, surname)
        personal_data.save()
        personal_data.close_save()

        name_surname = base_settings_page.profile_get()
        self.assertEqual(name + " " + surname, name_surname)
        base_settings_page.profile()

        main_page = MainPage(self.driver)
        name_surname = main_page.my_name_surname()
        self.assertEqual(name + " " + surname, name_surname)

    def test_name_surname_letters_small(self):
        name = "name"
        surname = "surname"

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()
        personal_data.name_surname(name, surname)
        personal_data.save()
        personal_data.close_save()

        name_surname = base_settings_page.profile_get()
        self.assertEqual(name + " " + surname, name_surname)
        base_settings_page.profile()

        main_page = MainPage(self.driver)
        name_surname = main_page.my_name_surname()
        self.assertEqual(name + " " + surname, name_surname)

    def test_name_surname_letters_capital(self):
        name = "NAME"
        surname = "SURNAME"

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()
        personal_data.name_surname(name, surname)
        personal_data.save()
        personal_data.close_save()

        name_surname = base_settings_page.profile_get()
        self.assertEqual(name + " " + surname, name_surname)
        base_settings_page.profile()

        main_page = MainPage(self.driver)
        name_surname = main_page.my_name_surname()
        self.assertEqual(name + " " + surname, name_surname)

    def test_name_surname_digits(self):
        name = "123"
        surname = "456"

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()
        personal_data.name_surname(name, surname)
        personal_data.save()
        personal_data.close_save()

        name_surname = base_settings_page.profile_get()
        self.assertEqual(name + " " + surname, name_surname)
        base_settings_page.profile()

        main_page = MainPage(self.driver)
        name_surname = main_page.my_name_surname()
        self.assertEqual(name + " " + surname, name_surname)

    def test_name_surname_letters_digits(self):
        name = "Name123"
        surname = "Surname456"

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK12, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()
        personal_data.name_surname(name, surname)
        personal_data.save()
        personal_data.close_save()

        name_surname = base_settings_page.profile_get()
        self.assertEqual(name + " " + surname, name_surname)
        base_settings_page.profile()

        main_page = MainPage(self.driver)
        name_surname = main_page.my_name_surname()
        self.assertEqual(name + " " + surname, name_surname)

    def test_name_surname_error_symbols(self):
        name = "Name_1"
        surname = "Surname_1"
        error = u"Пожалуйста, используйте только буквы."

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()
        personal_data.name_surname(name, surname)
        personal_data.save()

        e1, e2 = personal_data.name_surname_error()

        self.assertEqual(error, e1)
        self.assertEqual(error, e2)

    def test_name_surname_long_ok(self):
        name = "Name" * 100
        surname = "Surname" * 100

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK13, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()
        personal_data.name_surname_send_keys(name, surname)
        personal_data.save()
        personal_data.close_save()

        base_settings_page.profile()

        main_page = MainPage(self.driver)
        name_surname = main_page.my_name_surname()
        self.assertEqual(41, len(name_surname))

    def test_name_surname_long_error(self):
        name = "Name1" * 100
        surname = "Surname1" * 100
        error = u"Текст слишком длинный"

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()
        personal_data.name_surname(name, surname)
        personal_data.save()

        e1, e2 = personal_data.name_surname_error()

        self.assertEqual(error, e1)
        self.assertEqual(error, e2)

    def test_name_surname_error_void(self):
        name = ""
        surname = ""
        error_name = u"Пожалуйста, укажите ваше имя."
        error_surname = u"Пожалуйста, укажите вашу фамилию."

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()
        personal_data.name_surname(name, surname)
        personal_data.save()

        e1, e2 = personal_data.name_surname_error()

        self.assertEqual(error_name, e1)
        self.assertEqual(error_surname, e2)

    def test_name_surname_error_space(self):
        name = " " * 10
        surname = " " * 10
        error_name = u"Пожалуйста, укажите ваше имя."
        error_surname = u"Пожалуйста, укажите вашу фамилию."

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()
        personal_data.name_surname(name, surname)
        personal_data.save()

        e1, e2 = personal_data.name_surname_error()

        self.assertEqual(error_name, e1)
        self.assertEqual(error_surname, e2)

    def test_name_surname_long_space(self):
        name = " " * 10 + "Name1" + " " * 10
        surname = " " * 10 + "Surname1" + " " * 10

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK19, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()
        personal_data.name_surname(name, surname)
        personal_data.save()
        personal_data.close_save()

        name_surname = base_settings_page.profile_get()
        self.assertEqual("Name1" + " " + "Surname1", name_surname)
        base_settings_page.profile()

        main_page = MainPage(self.driver)
        name_surname = main_page.my_name_surname()
        self.assertEqual("Name1" + " " + "Surname1", name_surname)

    def test_name_surname_space(self):
        name = "Name" + " " * 5 + "1"
        surname = "Surname" + " " * 5 + "1"

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK14, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()
        personal_data.name_surname(name, surname)
        personal_data.save()
        personal_data.close_save()

        name_surname = base_settings_page.profile_get()
        self.assertEqual("Name 1" + " " + "Surname 1", name_surname)
        base_settings_page.profile()

        main_page = MainPage(self.driver)
        name_surname = main_page.my_name_surname()
        self.assertEqual("Name 1" + " " + "Surname 1", name_surname)

        # Birthday

    def test_birthday(self):
        birthday = u"5 февраля 2001 (17 лет)"

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()

        personal_data.birthday()
        personal_data.save()
        personal_data.close_save()

        base_settings_page.profile()
        main_page = MainPage(self.driver)
        my_birthday = main_page.my_birthday()

        self.assertEqual(birthday, my_birthday)

    def test_birthday_error_29(self):
        error = u"День вашего рождения указан некорректно."

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()

        personal_data.birthday_error_29()
        personal_data.save()

        e = personal_data.get_birthday_error()
        self.assertEqual(e, error)

    def test_birthday_error_void(self):
        error = u"День вашего рождения указан некорректно."

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()

        personal_data.birthday_error_void_day()
        personal_data.save()

        e = personal_data.get_birthday_error()
        self.assertEqual(e, error)

        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()
        personal_data.birthday_error_void_month()
        personal_data.save()

        e = personal_data.get_birthday_error()
        self.assertEqual(e, error)

        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()
        personal_data.birthday_error_void_year()
        personal_data.save()

        e = personal_data.get_birthday_error()
        self.assertEqual(e, error)

        # Phone number

    def test_phone_number_error_symbol(self):
        number = "999a997777"
        error = u"Ошибки:\n" + u"В номере неверное количество цифр"

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        phone_number = base_settings_page.phone_number()
        phone_number.set_number(number)
        phone_number.ok_button_click()
        e = phone_number.number_error()
        self.assertEqual(e, error)

    def test_phone_number_error_small(self):
        number = "9997777"
        error = u"Ошибки:\n" + u"В номере неверное количество цифр"

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        phone_number = base_settings_page.phone_number()
        phone_number.set_number(number)
        phone_number.ok_button_click()
        e = phone_number.number_error()
        self.assertEqual(e, error)

    def test_phone_number_error_long(self):
        number = "99977771231231123"
        error = u"Ошибки:\n" + u"В номере неверное количество цифр"

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        phone_number = base_settings_page.phone_number()
        phone_number.set_number(number)
        phone_number.ok_button_click()
        e = phone_number.number_error()
        self.assertEqual(e, error)

    def test_phone_number_error_void(self):
        number = ""
        error = u"Ошибки:\n" + u"Введите номер телефона"

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        phone_number = base_settings_page.phone_number()
        phone_number.set_number(number)
        phone_number.ok_button_click()
        e = phone_number.number_error()
        self.assertEqual(e, error)

    def test_phone_number_error_space(self):
        number = " " * 10
        error = u"Ошибки:\n" + u"Введите номер телефона"

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        phone_number = base_settings_page.phone_number()
        phone_number.set_number(number)
        phone_number.ok_button_click()
        e = phone_number.number_error()
        self.assertEqual(e, error)

    def test_phone_number(self):
        number = "9999977771"

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        phone_number = base_settings_page.phone_number()
        phone_number.set_number(number)
        phone_number.ok_button_click()
        phone_number.ok_button2()  # если появилась кнопка подтвержить код, то номер телефона принят
