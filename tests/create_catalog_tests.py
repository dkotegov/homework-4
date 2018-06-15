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

        self.market_page = self.shop.market_page
        self.catalog_widget = self.market_page.catalog_widget

    def tearDown(self):
        self.shop.remove()
        self.driver.quit()

    def test_cancel_and_close_creating_catalog(self):
        catalog_stub = self.market_page.catalog_stub
        is_exist_catalog_stub = catalog_stub.is_exist()
        self.assertTrue(is_exist_catalog_stub)

        catalog_popup = self.market_page.catalog_popup
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
        catalog_popup = self.market_page.catalog_popup
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

    def test_create_empty_catalog_from_catalog_panel(self):
        Catalog(self.driver).create(self.CATALOG_NAME)

        is_exist_catalog_widget = self.catalog_widget.is_exist()
        self.assertTrue(is_exist_catalog_widget)

        widget_catalog_name = self.catalog_widget.get_name()
        self.assertEqual(self.CATALOG_NAME, widget_catalog_name)

        number_of_products = self.catalog_widget.get_number_of_products()
        self.assertEqual(0, number_of_products)

    def test_create_empty_catalog_from_product_stub(self):
        Catalog(self.driver).create_from_catalog_product_stub(self.CATALOG_NAME)

        is_exist_catalog_widget = self.catalog_widget.is_exist()
        self.assertTrue(is_exist_catalog_widget)

        widget_catalog_name = self.catalog_widget.get_name()
        self.assertEqual(self.CATALOG_NAME, widget_catalog_name)

        number_of_products = self.catalog_widget.get_number_of_products()
        self.assertEqual(0, number_of_products)

    def test_create_catalog_later_from_product_panel(self):
        catalog_stub = self.market_page.catalog_stub
        is_exist_catalog_stub = catalog_stub.is_exist()
        self.assertTrue(is_exist_catalog_stub)

        catalog_stub.create_catalog_later()
        is_exist_catalog_stub = catalog_stub.is_exist()
        self.assertFalse(is_exist_catalog_stub)
        is_exist_catalog_widget = self.catalog_widget.is_exist()
        self.assertFalse(is_exist_catalog_widget)

        Catalog(self.driver).create_from_catalog_product_panel(self.CATALOG_NAME)

        is_exist_catalog_widget = self.catalog_widget.is_exist()
        self.assertTrue(is_exist_catalog_widget)

        widget_catalog_name = self.catalog_widget.get_name()
        self.assertEqual(self.CATALOG_NAME, widget_catalog_name)

        number_of_products = self.catalog_widget.get_number_of_products()
        self.assertEqual(0, number_of_products)

    def test_remove_catalog_after_creating_later(self):
        catalog_stub = self.market_page.catalog_stub
        catalog_stub.create_catalog_later()

        catalog = Catalog(self.driver)
        catalog.create_from_catalog_product_panel()
        catalog.open()
        catalog.remove_saving_products()

        catalog_stub = self.market_page.catalog_stub
        is_exist_catalog_stub = catalog_stub.is_exist()
        self.assertFalse(is_exist_catalog_stub)

        is_exist_catalog_widget = self.catalog_widget.is_exist()
        self.assertFalse(is_exist_catalog_widget)

    def test_create_several_catalogs(self):
        NUMBER_OF_CATALOGS = 10
        for i in xrange(NUMBER_OF_CATALOGS):
            Catalog(self.driver).create()

        catalog_counter = self.market_page.catalog_counter
        actual_catalog_count = catalog_counter.get_number_of_catalogs()
        self.assertEquals(NUMBER_OF_CATALOGS, actual_catalog_count)

    def test_create_maximum_catalogs(self):
        NUMBER_OF_CATALOGS = 100
        for i in xrange(NUMBER_OF_CATALOGS):
            Catalog(self.driver).create()

        catalog_counter = self.market_page.catalog_counter
        actual_catalog_count = catalog_counter.get_number_of_catalogs()
        self.assertEquals(NUMBER_OF_CATALOGS, actual_catalog_count)

        catalog_popup = self.market_page.catalog_popup
        is_disabled_creation = catalog_popup.is_disabled_creation()
        self.assertTrue(is_disabled_creation)
