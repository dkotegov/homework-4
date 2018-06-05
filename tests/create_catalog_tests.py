# -*- coding: utf-8 -*-
import unittest

from Components.market_page_components import CatalogStub, CatalogCounter, RemoveCatalogPopup
from PageObjects.page_objects import ShopMarketPage, CatalogPage
from tests.common import get_driver, Auth, Main, Shop


class CreateCatalogTests(unittest.TestCase):
    CATALOG_NAME = u'Каталог'

    def setUp(self):
        self.driver = get_driver()
        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()
        Shop(self.driver).create()

    def tearDown(self):
        Shop(self.driver).remove()
        self.driver.quit()

    def test_cancel_creating_catalog(self):
        shop_market_page = ShopMarketPage(self.driver)

        catalog_stub = shop_market_page.catalog_stub
        self.check_catalog_stub_is_exist(catalog_stub)

        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()
        catalog_popup.cancel_saving()
        catalog_popup.waiting_closing()

        self.check_catalog_stub_is_exist(catalog_stub)

    def test_close_creating_catalog(self):
        shop_market_page = ShopMarketPage(self.driver)

        catalog_stub = shop_market_page.catalog_stub
        self.check_catalog_stub_is_exist(catalog_stub)

        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()
        catalog_popup.close()
        catalog_popup.waiting_closing()

        self.check_catalog_stub_is_exist(catalog_stub)

    def test_create_catalog_without_name(self):
        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()
        catalog_popup.save()

        error_message = catalog_popup.get_error_message()
        self.assertEqual(u'Введите название каталога', error_message)

        catalog_popup.cancel_saving()
        catalog_popup.waiting_closing()

    def test_create_catalog_with_name_consist_of_spaces(self):
        name_length = 10
        spaces_name = ' ' * name_length

        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
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

        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
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

        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()
        catalog_popup.set_name(long_catalog_name)
        catalog_popup.save()
        catalog_popup.waiting_closing()

        catalog_widget = shop_market_page.catalog_widget
        widget_catalog_name = catalog_widget.get_name()
        self.assertEqual(long_catalog_name, widget_catalog_name)

    def test_create_catalog_with_name_consist_of_spec_chars(self):
        spec_name = u'~`!@#№$;%:^?&*()-_+=/.,|\"\'\\<>[]{}1234567890'

        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()
        catalog_popup.set_name(spec_name)
        catalog_popup.save()
        catalog_popup.waiting_closing()

        catalog_widget = shop_market_page.catalog_widget
        widget_catalog_name = catalog_widget.get_name()
        self.assertEqual(spec_name, widget_catalog_name)

    def test_create_catalog_with_name_include_space_chars(self):
        original_catalog_name = u'   А Б  В     Г Д  Е Ж   З И К    '
        expected_catalog_name = u'А Б В Г Д Е Ж З И К'

        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()
        catalog_popup.set_name(original_catalog_name)
        catalog_popup.save()
        catalog_popup.waiting_closing()

        catalog_widget = shop_market_page.catalog_widget
        widget_catalog_name = catalog_widget.get_name()
        self.assertEqual(expected_catalog_name, widget_catalog_name)

    def create_and_check_empty_catalog(self, popup, name):
        # creating catalog
        popup.set_name(name)
        popup.save()
        popup.waiting_closing()

        # checks
        shop_market_page = ShopMarketPage(self.driver)
        catalog_widget = shop_market_page.catalog_widget
        self.check_catalog_widget_is_exist(catalog_widget)

        widget_catalog_name = catalog_widget.get_name()
        self.assertEqual(name, widget_catalog_name)

        number_of_products = catalog_widget.get_number_of_products()
        self.assertEqual(u'0', number_of_products)

    def test_create_empty_catalog_from_catalog_panel(self, name=CATALOG_NAME):
        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()

        self.create_and_check_empty_catalog(catalog_popup, name)

    def test_create_empty_catalog_from_product_stub(self, name=CATALOG_NAME):
        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_from_catalog_stub()

        self.create_and_check_empty_catalog(catalog_popup, name)

    def test_create_catalog_later_from_product_panel(self, name=CATALOG_NAME):
        catalog_stub = CatalogStub(self.driver)
        self.check_catalog_stub_is_exist(catalog_stub)

        catalog_stub.create_catalog_later()
        self.check_catalog_stub_is_not_exist(catalog_stub)

        shop_market_page = ShopMarketPage(self.driver)
        catalog_widget = shop_market_page.catalog_widget
        self.check_catalog_widget_is_not_exist(catalog_widget)

        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_from_product_panel()

        self.create_and_check_empty_catalog(catalog_popup, name)

    def test_delete_catalog_after_creating_later(self):
        self.test_create_catalog_later_from_product_panel()

        shop_market_page = ShopMarketPage(self.driver)
        catalog_widget = shop_market_page.catalog_widget
        catalog_widget.open_catalog()
        catalog_page = CatalogPage(self.driver)
        catalog_panel = catalog_page.catalog_panel

        catalog_panel.remove()
        remove_catalog_popup = RemoveCatalogPopup(self.driver)
        remove_catalog_popup.submit_removing()
        remove_catalog_popup.waiting_closing()

        catalog_stub = CatalogStub(self.driver)
        self.check_catalog_stub_is_not_exist(catalog_stub)
        self.check_catalog_widget_is_not_exist(catalog_widget)

    def test_create_several_catalogs(self, number_of_catalogs=10):
        for i in xrange(number_of_catalogs):
            self.test_create_empty_catalog_from_catalog_panel(str(i))

        catalog_counter = CatalogCounter(self.driver)
        actual_catalog_count = catalog_counter.get_number_of_catalogs()
        self.assertEquals(number_of_catalogs, actual_catalog_count)

    def test_create_maximum_catalogs(self):
        self.test_create_several_catalogs(100)

        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        is_disabled_creation = catalog_popup.is_disabled_creation()
        self.assertTrue(is_disabled_creation)

    def create_and_check_catalog_with_image(self, image_name):
        # creating catalog
        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()
        catalog_popup.set_name()
        catalog_popup.upload_catalog_image(image_name)
        catalog_popup.waiting_image_upload()

        upload_image_src = catalog_popup.get_image_src()

        catalog_popup.save()
        catalog_popup.waiting_closing()

        # check
        catalog_widget = shop_market_page.catalog_widget
        widget_image_src = catalog_widget.get_image_src()
        self.assertEqual(upload_image_src, widget_image_src)

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

    def check_catalog_stub_is_exist(self, catalog_stub):
        is_exist_catalog_stub = catalog_stub.is_exist()
        self.assertTrue(is_exist_catalog_stub)

    def check_catalog_stub_is_not_exist(self, catalog_stub):
        is_not_exist_catalog_stub = catalog_stub.is_not_exist()
        self.assertTrue(is_not_exist_catalog_stub)

    def check_catalog_widget_is_exist(self, catalog_widget):
        is_exist_catalog_widget = catalog_widget.is_exist()
        self.assertTrue(is_exist_catalog_widget)

    def check_catalog_widget_is_not_exist(self, catalog_widget):
        is_not_exist_catalog_widget = catalog_widget.is_not_exist()
        self.assertTrue(is_not_exist_catalog_widget)
