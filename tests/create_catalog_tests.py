# -*- coding: utf-8 -*-
import unittest

from tests.common import get_driver, Auth, Main, Shop, Catalog


class CreateCatalogTests(unittest.TestCase):
    CATALOG_NAME = u'Каталог'

    def setUp(self):
        self.driver = get_driver()
        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()
        self.shop = Shop(self.driver)
        self.shop.create()

    def tearDown(self):
        self.shop.remove()
        self.driver.quit()

    def test_cancel_creating_catalog(self):
        market_page = self.shop.market_page

        catalog_stub = market_page.catalog_stub
        is_exist_catalog_stub = catalog_stub.is_exist()
        self.assertTrue(is_exist_catalog_stub)

        catalog_popup = market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()
        catalog_popup.cancel_saving()
        catalog_popup.waiting_closing()

        is_exist_catalog_stub = catalog_stub.is_exist()
        self.assertTrue(is_exist_catalog_stub)

    def test_close_creating_catalog(self):
        market_page = self.shop.market_page

        catalog_stub = market_page.catalog_stub
        is_exist_catalog_stub = catalog_stub.is_exist()
        self.assertTrue(is_exist_catalog_stub)

        catalog_popup = market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()
        catalog_popup.close()
        catalog_popup.waiting_closing()

        is_exist_catalog_stub = catalog_stub.is_exist()
        self.assertTrue(is_exist_catalog_stub)

    def test_create_catalog_without_name(self):
        catalog_popup = self.shop.market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()
        catalog_popup.save()

        error_message = catalog_popup.get_error_message()
        self.assertEqual(u'Введите название каталога', error_message)

        catalog_popup.cancel_saving()
        catalog_popup.waiting_closing()

    def test_create_catalog_with_name_consist_of_spaces(self):
        name_length = 10
        spaces_name = ' ' * name_length

        catalog_popup = self.shop.market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()
        catalog_popup.set_name(spaces_name)
        catalog_popup.save()

        error_message = catalog_popup.get_error_message()
        self.assertEqual(u'Введите название каталога', error_message)

        catalog_popup.cancel_saving()
        catalog_popup.waiting_closing()

    def test_create_catalog_with_very_long_name(self):
        name_length = 51
        very_long_catalog_name = 'x' * name_length

        catalog_popup = self.shop.market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()
        catalog_popup.set_name(very_long_catalog_name)
        catalog_popup.save()

        error_message = catalog_popup.get_error_message()
        self.assertEqual(u'Название каталога не должно превышать 50 знаков', error_message)

        catalog_popup.cancel_saving()
        catalog_popup.waiting_closing()

    def test_create_catalog_with_long_name(self):
        name_length = 50
        long_catalog_name = 'x' * name_length

        Catalog(self.driver).create(long_catalog_name)

        catalog_widget = self.shop.market_page.catalog_widget
        widget_catalog_name = catalog_widget.get_name()
        self.assertEqual(long_catalog_name, widget_catalog_name)

    def test_create_catalog_with_name_consist_of_spec_chars(self):
        spec_name = u'~`!@#№$;%:^?&*()-_+=/.,|\"\'\\<>[]{}1234567890'

        Catalog(self.driver).create(spec_name)

        catalog_widget = self.shop.market_page.catalog_widget
        widget_catalog_name = catalog_widget.get_name()
        self.assertEqual(spec_name, widget_catalog_name)

    def test_create_catalog_with_name_include_space_chars(self):
        original_catalog_name = u'   А Б  В     Г Д  Е Ж   З И К    '
        expected_catalog_name = u'А Б В Г Д Е Ж З И К'

        Catalog(self.driver).create(original_catalog_name)

        catalog_widget = self.shop.market_page.catalog_widget
        widget_catalog_name = catalog_widget.get_name()
        self.assertEqual(expected_catalog_name, widget_catalog_name)

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

        catalog_widget = market_page.catalog_widget
        is_not_exist_catalog_widget = catalog_widget.is_not_exist()
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
        catalog_widget = self.shop.market_page.catalog_widget
        is_exist_catalog_widget = catalog_widget.is_exist()
        self.assertTrue(is_exist_catalog_widget)

        widget_catalog_name = catalog_widget.get_name()
        self.assertEqual(name, widget_catalog_name)

        number_of_products = catalog_widget.get_number_of_products()
        self.assertEqual(0, number_of_products)

    def test_delete_catalog_after_creating_later(self):
        self.test_create_catalog_later_from_product_panel()

        catalog = Catalog(self.driver)
        catalog.open()
        catalog.remove_saving_products()

        market_page = self.shop.market_page

        catalog_stub = market_page.catalog_stub
        is_not_exist_catalog_stub = catalog_stub.is_not_exist()
        self.assertTrue(is_not_exist_catalog_stub)

        catalog_widget = market_page.catalog_widget
        is_not_exist_catalog_widget = catalog_widget.is_not_exist()
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

    def test_create_catalog_with_small_jpg_image(self):
        self.create_and_check_catalog_with_image('image_64x64.jpg')

    def test_create_catalog_with_small_png_image(self):
        self.create_and_check_catalog_with_image('image_64x64.png')

    def test_create_catalog_with_small_gif_image(self):
        self.create_and_check_catalog_with_image('image_64x64.gif')

    def test_create_catalog_with_medium_jpg_image(self):
        self.create_and_check_catalog_with_image('image_512x512.jpg')

    def test_create_catalog_with_medium_png_image(self):
        self.create_and_check_catalog_with_image('image_512x512.png')

    def test_create_catalog_with_medium_gif_image(self):
        self.create_and_check_catalog_with_image('image_512x512.gif')

    def test_create_catalog_with_large_jpg_image(self):
        self.create_and_check_catalog_with_image('image_4K.jpg')

    def test_create_catalog_with_large_png_image(self):
        self.create_and_check_catalog_with_image('image_4K.png')

    def test_create_catalog_with_large_gif_image(self):
        self.create_and_check_catalog_with_image('image_4K.gif')

    def create_and_check_catalog_with_image(self, image_name):
        market_page = self.shop.market_page
        # creating catalog
        catalog_popup = market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()
        catalog_popup.set_name()
        catalog_popup.upload_catalog_image(image_name)
        catalog_popup.waiting_image_upload()

        upload_image_src = catalog_popup.get_image_src()

        catalog_popup.save()
        catalog_popup.waiting_closing()

        # check
        catalog_widget = market_page.catalog_widget
        widget_image_src = catalog_widget.get_image_src()
        self.assertEqual(upload_image_src, widget_image_src)
