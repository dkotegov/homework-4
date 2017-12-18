# -*- coding: utf-8 -*-

import re
import unittest
from random import randint
from urllib2 import unquote

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_test import BaseTest
from pages import SearchFilterPage


class BaseSearchPageTest(BaseTest):
    BASE_URL = 'https://ok.ru/search'

    def setUp(self):
        super(BaseSearchPageTest, self).setUp()

        self.driver.get(self.BASE_URL)


class SearchPageMusicTest(BaseSearchPageTest):
    TEST_GROUP = u'Ария'
    GROUP_SELECTOR = u'Категория'
    REQUEST_PARAMETER = 'st.query='

    def test(self):
        search_page = SearchFilterPage(self.driver)
        search_page.click_music_search()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR,
                search_page.GROUP_SEARCH_TYPE_CSS),
                self.GROUP_SELECTOR
            )
        )

        search_page.send_search_query(self.TEST_GROUP)
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.current_url.find(self.REQUEST_PARAMETER) != -1
        )
        encoded = self.driver.current_url.encode('ASCII')
        self.assertTrue(self.TEST_GROUP in unquote(encoded).decode('utf-8'))


class SearchPageMusicAlbumTest(BaseSearchPageTest):
    TEST_ALBUM = u'Химера'
    GROUP_SELECTOR = u'Категория'

    def test(self):
        search_page = SearchFilterPage(self.driver)
        search_page.click_music_search()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR,
                search_page.GROUP_SEARCH_TYPE_CSS),
                self.GROUP_SELECTOR
            )
        )

        search_page.click_album_search()
        search_page.send_search_query(self.TEST_ALBUM)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                search_page.SEARCH_RESULTS_HEADER
            ))
        )
        result = search_page.get_search_result_header().text
        number_from_result_header = None

        for item in result.split(' '):
            if item.isdigit():
                number_from_result_header = int(item)
                break
        self.assertTrue(number_from_result_header is not None and number_from_result_header != 0)


class SearchPageUniversityTest(BaseSearchPageTest):
    TEST_UNIVERSITY = u'МГТУ им. Баумана'
    GROUP_SELECTOR = u'Тип'
    FOUND_TEXT = u'Найдено'

    def test(self):
        search_page = SearchFilterPage(self.driver)
        search_page.click_group_search()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR,
                search_page.GROUP_SEARCH_TYPE_CSS),
                self.GROUP_SELECTOR
            )
        )

        search_page.click_university_search()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR,
                search_page.SEARCH_RESULTS_HEADER),
                self.FOUND_TEXT
            )
        )

        search_page.send_search_query(self.TEST_UNIVERSITY)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                search_page.SEARCH_RESULTS_HEADER
            ))
        )

        result = search_page.get_search_result_header().text
        number_from_result_header = None

        for item in result.split(' '):
            if item.isdigit():
                number_from_result_header = int(item)
                break
        self.assertTrue(number_from_result_header is not None and number_from_result_header != 0)


class SearchPageSetCountryTest(BaseSearchPageTest):
    TEST_COUNTRY = u'Россия'

    def test(self):
        search_page = SearchFilterPage(self.driver)
        search_page.set_country(self.TEST_COUNTRY)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                search_page.SEARCH_TAGS
            ))
        )
        result = search_page.get_search_results()
        self.assertEqual(len(result), len([s for s in result if self.TEST_COUNTRY in s.text]))


class SearchPageSetFullLocationTest(BaseSearchPageTest):
    TEST_TOWN = u'Балашиха'
    TEST_COUNTRY = u'Россия'

    def test(self):
        search_page = SearchFilterPage(self.driver)
        search_page.set_country(self.TEST_COUNTRY)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                search_page.SEARCH_TAGS
            ))
        )

        search_page.set_town(self.TEST_TOWN)
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((
                By.XPATH,
                search_page.SEARCH_TAGS),
                self.TEST_TOWN
            )
        )
        result = search_page.get_search_results()
        self.assertEqual(len(result), len([s for s in result if self.TEST_TOWN in s.text]))
        # For unknown reason, OK.RU returns incorrect value of user's location on search page
        # On search page it returns, for example, Moscow, but in profile location set to Balashikha
        # Propably, I simply don't understand the way it should work


class SearchPageAgeLimitTest(BaseSearchPageTest):
    from_age = randint(14, 50)
    till_age = randint(from_age, 50)

    def test(self):
        search_page = SearchFilterPage(self.driver)

        search_page.set_from_age(self.from_age)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                search_page.SEARCH_TAGS
            ))
        )

        search_page.set_till_age(self.till_age)
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((
                By.XPATH,
                search_page.SEARCH_TAGS),
                str(self.till_age)
            )
        )

        result = search_page.get_search_results()
        for i in result:
            if re.search(u'[0-9][0-9]\sлет', i.text) is not None:
                self.assertTrue(self.from_age <= int(re.search(u'[0-9][0-9]\sлет', i.text).group(0)[:2]) <= self.till_age)
                continue
            if re.search(u'[0-9][0-9]\sгод', i.text) is not None:
                self.assertTrue(self.from_age <= int(re.search(u'[0-9][0-9]\sгод', i.text).group(0)[:2]) <= self.till_age)
                continue
        # For unknown reason, OK.RU returns list of users, which includes users without year of birth
        # Maybe, list of users contains users with hidden date of birth?


class SearchPageGroupSearchTest(BaseSearchPageTest):
    SEARCH_QUERY = u'Программирование'
    GROUP_SELECTOR = u'Тип'
    REQUEST_PARAMETER = 'st.query'

    def test(self):
        search_page = SearchFilterPage(self.driver)
        search_page.click_group_search()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR,
                search_page.GROUP_SEARCH_TYPE_CSS),
                self.GROUP_SELECTOR
            )
        )
        search_page.send_search_query(self.SEARCH_QUERY)
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.current_url.find(self.REQUEST_PARAMETER) != -1
        )


class SearchPageGenderTest(BaseSearchPageTest):
    FEMALE_QUERY = 'st.gender=f'
    NOT_FOUND = -1

    def test(self):
        search_filter_page = SearchFilterPage(self.driver)
        search_filter_page.set_female()

        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.current_url.find(self.FEMALE_QUERY) != self.NOT_FOUND
        )


search_page_tests = [
    unittest.TestSuite((
        unittest.makeSuite(SearchPageSetCountryTest)
    )),
    unittest.TestSuite((
        unittest.makeSuite(SearchPageSetFullLocationTest)
    )),
    unittest.TestSuite((
        unittest.makeSuite(SearchPageAgeLimitTest)
    )),
    unittest.TestSuite((
        unittest.makeSuite(SearchPageGroupSearchTest)
    )),
    unittest.TestSuite((
        unittest.makeSuite(SearchPageMusicTest)
    )),
    unittest.TestSuite((
        unittest.makeSuite(SearchPageMusicAlbumTest)
    )),
    unittest.TestSuite((
        unittest.makeSuite(SearchPageUniversityTest)
    )),
    unittest.TestSuite((
        unittest.makeSuite(SearchPageGenderTest),
    )),
]
