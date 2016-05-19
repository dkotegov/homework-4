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
    MODEL_DROPDOWN = '//div[contains(@class, "selt-firm_id")]/div/div/div[contains(@class, "js-select__selected__option")]'
    MODEL_DROPDOWN_ITEMS = '//div[@data-optidx and contains(@class, "js-select__options__item input__data__value_in-group")]'
    MODEL_DROPDOWN_ITEM_BY_NAME = '//div[@data-optidx and contains(@class, "js-select__options__item input__data__value_in-group") and text()="{}"]'
    STATION_DROPDOWN = '//div[contains(@class, "selt-subway_id")]/div/div/div[contains(@class, "js-select__selected__option")]'
    STATION_DROPDOWN_ITEMS = '//div[@data-optidx and contains(@class, "subway")]'
    STATION_DROPDOWN_ITEM_BY_NAME = u'//div[@data-optidx and contains(@class, "subway") and text()="{}"]'
    CHECKBOX_SHOWROOM_IS_OFFICIAL = '//span[@class="input-flag__text" and text()="Официальный дилер"]'
    SUBMIT = '//span[text()="Найти"]'

    @property
    def region_selection_form(self):
        return RegionSelectionForm(self.driver)

    def model_dropdown_drop(self):
        self.driver.find_element_by_xpath(self.MODEL_DROPDOWN).click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.MODEL_DROPDOWN_ITEMS))
        )

    def model_dropdown_items(self):
        models = []
        for model in self.driver.find_elements_by_xpath(self.MODEL_DROPDOWN_ITEMS):
            self.driver.execute_script("return arguments[0].scrollIntoView();", model)
            models.append(model.text)
        return list(models)

    def model_dropdown_item_select(self, model):
        item = self.driver.find_element_by_xpath(self.MODEL_DROPDOWN_ITEM_BY_NAME.format(model))
        self.driver.execute_script("return arguments[0].scrollIntoView();", item)
        item.click()

    def station_dropdown_drop(self):
        self.driver.find_element_by_xpath(self.STATION_DROPDOWN).click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.STATION_DROPDOWN_ITEMS))
        )

    def station_dropdown_items(self):
        stations = []
        for station in self.driver.find_elements_by_xpath(self.STATION_DROPDOWN_ITEMS):
            self.driver.execute_script("return arguments[0].scrollIntoView();", station)
            stations.append(station.text)
        return list(stations)

    def station_dropdown_item_select(self, station):
        item = self.driver.find_element_by_xpath(self.STATION_DROPDOWN_ITEM_BY_NAME.format(station))
        self.driver.execute_script("return arguments[0].scrollIntoView();", item)
        item.click()

    def is_official_checkbox_click(self):
        self.driver.find_element_by_xpath(self.CHECKBOX_SHOWROOM_IS_OFFICIAL).click()

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class RegionSelectionForm(Component):
    TITLE = '//div[text()="Выбор региона"]'
    COUNTRY = u'//span[@class="tab__pin__text" and text()="{}"]'
    REGION_INPUT = '//input[@placeholder="Введите название города или региона"]'
    SUBMIT_BUTTON = '//span[@class="button__text" and text()="Выбрать"]'
    OPEN_FORM_BUTTON = '//span[contains(@class, "js-geo_name")]'
    FOUNDED_REGIONS = '//div[@class="input__box input__box_dropdown"]/div/div[@data-val]'
    CANCEL_BUTTON = '//span[@class="button__text" and text()="Отменить"]'

    def open_form(self):
        self.driver.find_element_by_xpath(self.OPEN_FORM_BUTTON).click()
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.TITLE))
        )
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.REGION_INPUT))
        )

    def set_country(self, country):
        self.driver.find_element_by_xpath(self.COUNTRY.format(country)).click()
        WebDriverWait(self.driver, 30).until(
            lambda d: regions_search_done(d)
        )

    def set_region(self, region):
        self.driver.find_element_by_xpath(self.REGION_INPUT).send_keys(region)
        WebDriverWait(self.driver, 30).until(
            lambda d: regions_search_done(d)
        )

    def get_founded_regions(self):
        regions = []
        for region in self.driver.find_elements_by_xpath(self.FOUNDED_REGIONS):
            self.driver.execute_script("return arguments[0].scrollIntoView();", region)
            regions.append(region.text)
        return list(regions)

    def submit(self):
        self.select_first_region()
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.OPEN_FORM_BUTTON))
        )

    def select_first_region(self):
        self.driver.find_element_by_xpath(self.FOUNDED_REGIONS).click()

    def cancel(self):
        self.driver.find_element_by_xpath(self.CANCEL_BUTTON).click()

    def current_region(self):
        return self.driver.find_element_by_xpath(RegionSelectionForm.OPEN_FORM_BUTTON).text


def regions_search_done(driver):
    try:
        founded_elements = driver.find_elements_by_xpath(RegionSelectionForm.FOUNDED_REGIONS)
        var = list(e.text for e in founded_elements)
        return True
    except StaleElementReferenceException:
        return False


class RegionSelectFormTest(unittest.TestCase):
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
            page.open()

    def test_region_selection(self):
        page = ShowroomPage(self.driver)
        page.open()

        search_form = page.search_form
        region_selection_form = search_form.region_selection_form

        new_region = u"Вязники"

        region_selection_form.open_form()
        region_selection_form.set_region(new_region)
        region_selection_form.submit()

        self.assertEqual(new_region, region_selection_form.current_region())

    def test_cancel_region_selection(self):
        page = ShowroomPage(self.driver)
        page.open()

        search_form = page.search_form
        region_selection_form = search_form.region_selection_form

        current_region = region_selection_form.current_region()

        region_selection_form.open_form()
        region_selection_form.set_region(u"Санкт-Петербург")
        region_selection_form.select_first_region()
        region_selection_form.cancel()

        self.assertEqual(current_region, region_selection_form.current_region())

    def test_search_cities_by_country(self):
        page = ShowroomPage(self.driver)
        page.open()

        search_form = page.search_form
        region_selection_form = search_form.region_selection_form
        region_selection_form.open_form()

        test_data_set = {
            # u'Россия': (u'Москва', u'Санкт-Петербург', u'Волгоград', u'Андреевка', u'Ярославль'), VERY SLOW BECAUSE VERY BIG
            u'Беларусь': (u'Минск', u'Береза', u'Белоозерск', u'Шклов'),
            u'Казахстан': (u'Алга', u'Иргиз', u'Сарань', u'Шаян'),
            u'Украина': (u'Киев', u'Богуслав', u'Мариуполь', u'Хотин'),
            u'Молдова': (u'Атаки', u'Кагул', u'Бричаны', u'Яловены')
        }

        for country in test_data_set.keys():
            region_selection_form.set_country(country)
            founded_regions = region_selection_form.get_founded_regions()
            for city in test_data_set[country]:
                self.assertIn(city, founded_regions)


class SelectCarModelTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_dropdown_showing(self):
        page = ShowroomPage(self.driver)
        page.open()

        search_form = page.search_form
        search_form.model_dropdown_drop()

        test_data_set = (u"Audi", u"Tesla", u"Opel", u"УАЗ")

        dropdown_items = search_form.model_dropdown_items()

        for data in test_data_set:
            self.assertIn(data, dropdown_items, u"{} model is not in dropdown list".format(data))

    def test_filter(self):
        page = ShowroomPage(self.driver)
        page.open()

        test_models = ("Audi", "BMW", "Toyota")

        for test_model in test_models:
            search_form = page.search_form
            search_form.model_dropdown_drop()
            search_form.model_dropdown_item_select(test_model)
            search_form.submit()

            list_special_offers = page.special_offers_list
            offers_models = list_special_offers.get_item_titles()

            for model in offers_models:
                self.assertTrue(test_model in model, "Model filter not working...")

            page.open()


class SelectStationTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_dropdown_showing(self):
        page = ShowroomPage(self.driver)
        page.open()

        search_form = page.search_form
        region_selection_form = search_form.region_selection_form

        region_selection_form.open_form()
        region_selection_form.set_region(u"Москва")
        region_selection_form.submit()

        search_form.station_dropdown_drop()

        test_data_set = (u"Выхино", u"Тропарёво", u"Братиславская", u"Авиамоторная")

        dropdown_items = search_form.station_dropdown_items()

        for data in test_data_set:
            self.assertIn(data, dropdown_items, u"{} station is not in dropdown list".format(data))

    def test_filter(self):
        page = ShowroomPage(self.driver)
        page.open()

        test_stations = (u"Аннино", u"Отрадное", u"Чертановская")

        search_form = page.search_form
        region_selection_form = search_form.region_selection_form
        region_selection_form.open_form()
        region_selection_form.set_region(u"Москва")
        region_selection_form.submit()

        for test_station in test_stations:
            search_form.station_dropdown_drop()
            search_form.station_dropdown_item_select(test_station)
            search_form.submit()

            showroom_list = page.showroom_list
            dealers_stations = showroom_list.get_items_metro_stations()

            for station in dealers_stations:
                self.assertEqual(test_station, station, "Station filter not working...")

            page.open()


class IsOfficialCheckboxTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_filter(self):
        page = ShowroomPage(self.driver)
        page.open()

        test_models = ("Audi", "BMW", "Toyota")

        search_form = page.search_form

        for test_model in test_models:
            search_form.model_dropdown_drop()
            search_form.model_dropdown_item_select(test_model)
            search_form.is_official_checkbox_click()
            search_form.submit()

            showroom_list = page.showroom_list
            items_count = showroom_list.get_items_count()
            official_dealers_count = showroom_list.get_items_official_dealers_by_model(test_model)
            self.assertEqual(official_dealers_count, items_count, "These dealers are not all official")

            page.open()
