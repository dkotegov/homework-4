# coding=utf-8
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.car_showrooms.pages.pages import ShowroomPage


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

            list_showroom = page.showroom_list
            page_title = list_showroom.get_page_title()

            self.assertIn(test_model, page_title, "Model filter not working...")
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

        search_form = page.search_form
        search_form.is_official_checkbox_click()
        search_form.submit()

        showroom_list = page.showroom_list
        items_count = showroom_list.get_items_count()
        official_dealers_count = len(showroom_list.get_items_official_dealers())
        self.assertEqual(official_dealers_count, items_count, "These dealers are not all official")

        page.open()


class SearchFormTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_filter_station_and_is_official_dealer(self):
        page = ShowroomPage(self.driver)
        page.open()

        test_data_set = (u"Отрадное", u"Беговая", u"Рижская", u"Кантемировская")

        search_form = page.search_form

        for station in test_data_set:
            search_form.station_dropdown_drop()
            search_form.station_dropdown_item_select(station)
            search_form.is_official_checkbox_click()
            search_form.submit()

            showroom_list = page.showroom_list
            dealers_metro_stations = showroom_list.get_items_metro_stations()

            for dealer_station in dealers_metro_stations:
                if not showroom_list.is_list_empty():
                    self.assertEqual(station, dealer_station, "Filter combination: station and is official not works")

            page.open()

    def test_filter_model_and_is_official_dealer(self):
        page = ShowroomPage(self.driver)
        page.open()

        test_models = ("Audi", "Kia", "Infiniti")

        search_form = page.search_form

        for test_model in test_models:
            search_form.model_dropdown_drop()
            search_form.model_dropdown_item_select(test_model)
            search_form.is_official_checkbox_click()
            search_form.submit()

            showroom_list = page.showroom_list
            items_count = showroom_list.get_items_count()
            official_dealers_count = len(showroom_list.get_items_official_dealers_by_model(test_model))
            self.assertEqual(official_dealers_count, items_count, "These dealers are not all official for model {}. "
                                                                  "Filter combination: model and is official not works".format(test_model))

            page.open()

    def test_filter_model_and_station_and_is_official_dealer(self):
        page = ShowroomPage(self.driver)
        page.open()

        test_models = ("Audi", "Toyota", "Volvo")
        test_stations = (u"Молодежная", u"Строгино", u"Рижская")

        search_form = page.search_form

        for station in test_stations:
            for model in test_models:
                search_form.model_dropdown_drop()
                search_form.model_dropdown_item_select(model)
                search_form.station_dropdown_drop()
                search_form.station_dropdown_item_select(station)
                search_form.is_official_checkbox_click()
                search_form.submit()

                showroom_list = page.showroom_list
                if not showroom_list.is_list_empty():
                    items_count = showroom_list.get_items_count()
                    official_model_dealers_count = len(showroom_list.get_items_official_dealers_by_model(model))
                    self.assertEqual(official_model_dealers_count, items_count, "These dealers are not all official for model {}. "
                                                                  "Filter combination: model and station and is official not works".format(model))

                    dealers_metro_stations = showroom_list.get_items_metro_stations()
                    for dealer_station in dealers_metro_stations:
                        if not showroom_list.is_list_empty():
                            self.assertEqual(station, dealer_station, "These dealers are not all at station {}. "
                                                                      "Filter combination: model and station and is official not works".format(station))

                    items_count = showroom_list.get_items_count()
                    official_dealers_count = len(showroom_list.get_items_official_dealers())
                    self.assertEqual(official_dealers_count, items_count, "These dealers are not all official"
                                                                          "Filter combination: model and station and is official not works")

                page.open()

