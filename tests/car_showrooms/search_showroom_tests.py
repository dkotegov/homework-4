# coding=utf-8
import os
import unittest

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.car_showrooms.pages.pages import Component, ShowroomPage


class SearchForm(Component):
    @property
    def region_selection_form(self):
        return RegionSelectionForm(self.driver)


class RegionSelectionForm(Component):
    TITLE = '//div[text()="Выбор региона"]'
    COUNTRY = '//span[text()="{}"]'
    REGION_INPUT = '//input[@placeholder="Введите название города или региона"]'
    SUBMIT = '//span[text()="Выбрать"]'
    OPEN_FORM_BUTTON = '//span[contains(@class, "js-geo_name")]'
    FOUNDED_REGIONS = '//div[@class="input__box input__box_dropdown"]/div/div[@data-val]'

    def open_form(self):
        self.driver.find_element_by_xpath(self.OPEN_FORM_BUTTON).click()
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.TITLE))
        )

    def set_country(self, country):
        self.driver.find_element_by_xpath(self.COUNTRY.format(country)).click()

    def set_region(self, region):
        self.driver.find_element_by_xpath(self.REGION_INPUT).send_keys(region)
        WebDriverWait(self.driver, 30).until(
            lambda d: regions_search_done(d)
        )

    def get_founded_regions(self):
        founded_elements = self.driver.find_elements_by_xpath(self.FOUNDED_REGIONS)
        return [e.text for e in founded_elements]

    def submit(self):
        self.driver.find_element_by_xpath(self.FOUNDED_REGIONS).click()
        self.driver.find_element_by_xpath(self.SUBMIT).click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.OPEN_FORM_BUTTON))
        )


def regions_search_done(driver):
    try:
        founded_elements = driver.find_elements_by_xpath(RegionSelectionForm.FOUNDED_REGIONS)
        var = [e.text for e in founded_elements]
        return True
    except StaleElementReferenceException:
        return False


class SearchFormTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_search_region_by_name(self):
        page = ShowroomPage(self.driver)
        page.open()

        search_form = page.search_form
        region_selection_form = search_form.region_selection_form

        test_queries = (u"волго", u"люб", u"моск", u"санкт-петербург", u"свввв")
        for query in test_queries:
            region_selection_form.open_form()
            region_selection_form.set_region(query)
            regions_list = region_selection_form.get_founded_regions()
            for region in regions_list:
                self.assertTrue(query in region or query.title() in region,
                                u"Element {} not satisfies searching query".format(region))

            self.driver.refresh()

