# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_test import BaseTest
from pages import SearchPage, SearchFilterPage


class BaseSearchPageTest(BaseTest):
    BASE_URL = 'https://ok.ru/search'

    def setUp(self):
        super(BaseSearchPageTest, self).setUp()

        self.driver.get(self.BASE_URL)



class SearchPageDefaultSearchTest(BaseSearchPageTest):
    MENU_ACTIVE = u'Люди'

    def test(self):
        search_page = SearchPage(self.driver)
        self.assertEqual(self.MENU_ACTIVE, search_page.get_menu_active())


class SearchPageGenderTest(BaseSearchPageTest):
    FEMALE_QUERY = 'st.gender=f'
    NOT_FOUND = -1

    def test(self):
        search_filter_page = SearchFilterPage(self.driver)
        search_filter_page.set_female()

        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.current_url.find(self.FEMALE_QUERY) != self.NOT_FOUND
        )


class SearchPageAgeTest(BaseSearchPageTest):
    FROM_AGE = 20
    FROM_AGE_QUERY = 'st.fromAge=20'
    TILL_AGE = 25
    TILL_AGE_QUERY = 'st.tillAge=25'
    NOT_FOUND = -1

    def test(self):
        search_filter_page = SearchFilterPage(self.driver)

        search_filter_page.click_from_age()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                search_filter_page._from_age_selector(self.FROM_AGE)
            ))
        )
        search_filter_page.click_from_age_select(self.FROM_AGE)
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.current_url.find(self.FROM_AGE_QUERY) != self.NOT_FOUND
        )

        search_filter_page.click_till_age()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                search_filter_page._till_age_selector(self.FROM_AGE)
            ))
        )
        search_filter_page.click_till_age_select(self.TILL_AGE)
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.current_url.find(self.TILL_AGE_QUERY) != self.NOT_FOUND
        )


class SearchPageHideFilterTest(BaseSearchPageTest):
    OPEN_CLASS = '__open'

    def test(self):
        search_filter_page = SearchFilterPage(self.driver)
        gender_block = search_filter_page.get_gender_block()

        gender_title = search_filter_page.get_gender_title()
        self.assertIn(self.OPEN_CLASS, gender_block.get_attribute('class'))

        gender_title.click()

        WebDriverWait(self.driver, 10).until(
            lambda driver: self.OPEN_CLASS not in gender_block.get_attribute('class')
        )


class SearchPageClearTest(BaseSearchPageTest):
    SEARCH_STRING = 'kek'

    def test(self):
        search_page = SearchPage(self.driver)

        search_input = search_page.get_search_input()
        search_input.send_keys(self.SEARCH_STRING)

        search_cancel = search_page.get_search_cancel()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, search_page.SEARCH_CANCEL))
        )
        search_cancel.click()

        WebDriverWait(self.driver, 10).until(
            lambda driver: search_input.text == ''
        )


class SearchPageFilterTagsTest(SearchPageGenderTest):
    FEMALE_TAG = u'Женщины'

    def test(self):
        super(SearchPageFilterTagsTest, self).test()

        search_page = SearchPage(self.driver)
        filter_tags = search_page.get_filter_tags()

        self.assertEqual(self.FEMALE_TAG, filter_tags[0].text)


class SearchPageClearFilterTest(SearchPageGenderTest):
    FEMALE_TAG = u'Женщины'

    def test(self):
        super(SearchPageClearFilterTest, self).test()

        search_page = SearchPage(self.driver)
        search_page.clear_filter_result()

        WebDriverWait(self.driver, 10).until(
            lambda driver: len(search_page.get_filter_tags()) == 0
        )
