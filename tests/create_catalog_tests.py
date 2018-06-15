# -*- coding: utf-8 -*-
import unittest

from tests.common import get_driver, Auth, Main, Shop, Catalog


class CreateCatalogTests(unittest.TestCase):
    CATALOG_NAME = u'Каталог'
    EMPTY_CATALOG_NAME_WARNING = u'Введите название каталога'
    VERY_LONG_CATALOG_NAME_WARNING = u'Название каталога не должно превышать 50 знаков'

    def setUp(self):
        self.driver = get_driver()
        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()
        self.shop = Shop(self.driver)
        self.shop.create()
        self.catalog_widget = self.shop.market_page.catalog_widget

    def tearDown(self):
        self.shop.remove()
        self.driver.quit()

    def test_cancel_and_close_creating_catalog(self):
        market_page = self.shop.market_page

        catalog_stub = market_page.catalog_stub
        is_exist_catalog_stub = catalog_stub.is_exist()
        self.assertTrue(is_exist_catalog_stub)

        catalog_popup = market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()
        catalog_popup.cancel_saving()
        catalog_popup.waiting_closing()

        catalog_popup.open_from_catalog_panel()
        catalog_popup.close()
        catalog_popup.waiting_closing()

        is_exist_catalog_stub = catalog_stub.is_exist()
        self.assertTrue(is_exist_catalog_stub)

    def test_create_catalog_with_wrong_names(self):
        # empty name
        catalog_popup = self.shop.market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()
        catalog_popup.save()

        error_message = catalog_popup.get_error_message()
        self.assertEqual(self.EMPTY_CATALOG_NAME_WARNING, error_message)

        catalog_popup.cancel_saving()
        catalog_popup.waiting_closing()

        # name consist o spaces
        NUMBER_OF_SPACES = 10
        SPACES_NAME = ' ' * NUMBER_OF_SPACES
        catalog_popup.open_from_catalog_panel()
        catalog_popup.set_name(SPACES_NAME)
        catalog_popup.save()

        error_message = catalog_popup.get_error_message()
        self.assertEqual(self.EMPTY_CATALOG_NAME_WARNING, error_message)

        catalog_popup.cancel_saving()
        catalog_popup.waiting_closing()

        # very long name
        NAME_LENGTH = 51
        VERY_LONG_NAME = 'x' * NAME_LENGTH
        catalog_popup.open_from_catalog_panel()
        catalog_popup.set_name(VERY_LONG_NAME)
        catalog_popup.save()

        error_message = catalog_popup.get_error_message()
        self.assertEqual(self.VERY_LONG_CATALOG_NAME_WARNING, error_message)

        catalog_popup.cancel_saving()
        catalog_popup.waiting_closing()

    def test_create_catalog_with_long_name(self):
        NAME_LENGTH = 50
        LONG_NAME = 'x' * NAME_LENGTH

        Catalog(self.driver).create(LONG_NAME)

        widget_catalog_name = self.catalog_widget.get_name()
        self.assertEqual(LONG_NAME, widget_catalog_name)

    def test_create_catalog_with_name_consist_of_spec_chars(self):
        SPEC_NAME = u'~`!@#№$;%:^?&*()-_+=/.,|\"\'\\<>[]{}1234567890'

        Catalog(self.driver).create(SPEC_NAME)

        widget_catalog_name = self.catalog_widget.get_name()
        self.assertEqual(SPEC_NAME, widget_catalog_name)

    def test_create_catalog_with_name_include_space_chars(self):
        ORIGINAL_CATALOG_NAME = u'   А Б  В     Г Д  Е Ж   З И К    '
        EXPECTED_CATALOG_NAME = u'А Б В Г Д Е Ж З И К'

        Catalog(self.driver).create(ORIGINAL_CATALOG_NAME)

        widget_catalog_name = self.catalog_widget.get_name()
        self.assertEqual(EXPECTED_CATALOG_NAME, widget_catalog_name)

    def test_create_empty_catalog_from_catalog_panel(self, name=CATALOG_NAME):
        catalog_popup = self.shop.market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()

        self.create_and_check_empty_catalog(catalog_popup, name)

    def test_create_empty_catalog_from_product_stub(self, name=CATALOG_NAME):
        catalog_popup = self.shop.market_page.catalog_popup
        catalog_popup.open_from_catalog_stub()

        self.create_and_check_empty_catalog(catalog_popup, name)

    def test_create_catalog_later_from_product_panel(self, name=CATALOG_NAME):
        market_page = self.shop.market_page
        catalog_stub = market_page.catalog_stub
        is_exist_catalog_stub = catalog_stub.is_exist()
        self.assertTrue(is_exist_catalog_stub)

        catalog_stub.create_catalog_later()
        is_not_exist_catalog_stub = catalog_stub.is_not_exist()
        self.assertTrue(is_not_exist_catalog_stub)

        is_not_exist_catalog_widget = self.catalog_widget.is_not_exist()
        self.assertTrue(is_not_exist_catalog_widget)

        catalog_popup = market_page.catalog_popup
        catalog_popup.open_from_product_panel()

        self.create_and_check_empty_catalog(catalog_popup, name)

    def create_and_check_empty_catalog(self, popup, name):
        # creating catalog
        popup.set_name(name)
        popup.save()
        popup.waiting_closing()

        # checks
        is_exist_catalog_widget = self.catalog_widget.is_exist()
        self.assertTrue(is_exist_catalog_widget)

        widget_catalog_name = self.catalog_widget.get_name()
        self.assertEqual(name, widget_catalog_name)

        number_of_products = self.catalog_widget.get_number_of_products()
        self.assertEqual(0, number_of_products)

    def test_remove_catalog_after_creating_later(self):
        self.test_create_catalog_later_from_product_panel()

        catalog = Catalog(self.driver)
        catalog.open()
        catalog.remove_saving_products()

        market_page = self.shop.market_page

        catalog_stub = market_page.catalog_stub
        is_not_exist_catalog_stub = catalog_stub.is_not_exist()
        self.assertTrue(is_not_exist_catalog_stub)

        is_not_exist_catalog_widget = self.catalog_widget.is_not_exist()
        self.assertTrue(is_not_exist_catalog_widget)

    def test_create_several_catalogs(self, number_of_catalogs=10):
        for i in xrange(number_of_catalogs):
            self.test_create_empty_catalog_from_catalog_panel(str(i))

        catalog_counter = self.shop.market_page.catalog_counter
        actual_catalog_count = catalog_counter.get_number_of_catalogs()
        self.assertEquals(number_of_catalogs, actual_catalog_count)

    def test_create_maximum_catalogs(self):
        self.test_create_several_catalogs(100)

        catalog_popup = self.shop.market_page.catalog_popup
        is_disabled_creation = catalog_popup.is_disabled_creation()
        self.assertTrue(is_disabled_creation)
