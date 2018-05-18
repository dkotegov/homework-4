# -*- coding: utf-8 -*-
import unittest

from Components.market_page_components import RemoveCatalogPopup
from PageObjects.page_objects import ShopMarketPage, CatalogPage
from tests.common import getDriver, Auth, Main, Shop


class CatalogTests(unittest.TestCase):
    CATALOG_NAME = u'Каталог'
    CATALOG_IMAGE = 'catalog-icon.png'
    CHARS_IN_SUBSTRING = 83

    def setUp(self):
        self.driver = getDriver()
        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()
        Shop(self.driver).create()

    def tearDown(self):
        Shop(self.driver).remove()
        self.driver.quit()

    def test_cancel_creating_catalog(self):
        shop_market_page = ShopMarketPage(self.driver)

        catalog_stub = shop_market_page.catalog_stub
        self.check_catalog_stub(catalog_stub)

        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup()
        catalog_popup.cancel_saving()
        catalog_popup.waiting_until_close()

        self.check_catalog_stub(catalog_stub)

    def test_close_creating_catalog(self):
        shop_market_page = ShopMarketPage(self.driver)

        catalog_stub = shop_market_page.catalog_stub
        self.check_catalog_stub(catalog_stub)

        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup()
        catalog_popup.close_popup()
        catalog_popup.waiting_until_close()

        self.check_catalog_stub(catalog_stub)

    def test_create_catalog_without_name(self):
        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup()
        catalog_popup.save()

        error_message = catalog_popup.get_error_message()
        self.assertEqual(u'Введите название каталога', error_message)

        catalog_popup.cancel_saving()
        catalog_popup.waiting_until_close()

    def test_create_catalog_with_name_consist_of_spaces(self):
        name_length = 10
        spaces_name = ' ' * name_length

        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.set_catalog_name(spaces_name)
        catalog_popup.open_popup()
        catalog_popup.save()

        error_message = catalog_popup.get_error_message()
        self.assertEqual(u'Введите название каталога', error_message)

        catalog_popup.cancel_saving()
        catalog_popup.waiting_until_close()

    def test_create_catalog_with_very_long_name(self):
        name_length = 51
        very_long_catalog_name = 'x' * name_length

        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup()
        catalog_popup.set_catalog_name(very_long_catalog_name)
        catalog_popup.save()

        error_message = catalog_popup.get_error_message()
        self.assertEqual(u'Название каталога не должно превышать 50 знаков', error_message)

        catalog_popup.cancel_saving()
        catalog_popup.waiting_until_close()

    def test_create_catalog_with_long_name(self):
        name_length = 50
        long_catalog_name = 'x' * name_length

        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup()
        catalog_popup.set_catalog_name(long_catalog_name)
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        catalog_widget = shop_market_page.catalog_widget
        widget_catalog_name = catalog_widget.get_catalog_name()
        self.assertEqual(long_catalog_name, widget_catalog_name)

    def test_create_catalog_with_name_consist_of_spec_chars(self):
        spec_name = u'~`!@#№$;%:^?&*()-_+=/.,|\"\'\\<>[]{}'

        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup()
        catalog_popup.set_catalog_name(spec_name)
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        catalog_widget = shop_market_page.catalog_widget
        widget_catalog_name = catalog_widget.get_catalog_name()
        self.assertEqual(spec_name, widget_catalog_name)

    def test_create_catalog_with_name_include_space_chars(self):
        original_catalog_name = u'   А Б  В     Г Д  Е Ж   З И К    '
        expected_catalog_name = u'А Б В Г Д Е Ж З И К'

        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup()
        catalog_popup.set_catalog_name(original_catalog_name)
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        catalog_widget = shop_market_page.catalog_widget
        widget_catalog_name = catalog_widget.get_catalog_name()
        self.assertEqual(expected_catalog_name, widget_catalog_name)

    def test_create_empty_catalog(self):
        # creating catalog
        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup()
        catalog_popup.set_catalog_name(self.CATALOG_NAME)
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        # checks
        catalog_widget = shop_market_page.catalog_widget
        self.check_catalog_widget(catalog_widget)

        widget_catalog_name = catalog_widget.get_catalog_name()
        self.assertEqual(self.CATALOG_NAME, widget_catalog_name)

        number_of_products = catalog_widget.get_number_of_products()
        self.assertEqual(u'0', number_of_products)

    def test_create_catalog_with_image(self):
        # creating catalog
        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup()
        catalog_popup.set_catalog_name()
        catalog_popup.upload_catalog_image(self.CATALOG_IMAGE)
        catalog_popup.waiting_until_image_upload()

        upload_image_src = catalog_popup.get_image_src()

        catalog_popup.save()
        catalog_popup.waiting_until_close()

        # check
        catalog_widget = shop_market_page.catalog_widget
        widget_image_src = catalog_widget.get_image_src()
        self.assertEqual(upload_image_src[:self.CHARS_IN_SUBSTRING], widget_image_src[:self.CHARS_IN_SUBSTRING])

    def test_edit_catalog_name(self):
        # creating catalog
        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup()
        catalog_popup.set_catalog_name(self.CATALOG_NAME)
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        # check name before
        catalog_widget = shop_market_page.catalog_widget
        catalog_widget.open_catalog()
        catalog_page = CatalogPage(self.driver)
        catalog_panel = catalog_page.catalog_panel

        catalog_name_before_edit = catalog_panel.get_catalog_name()
        self.assertEquals(self.CATALOG_NAME, catalog_name_before_edit)

        # editing catalog name
        other_catalog_name = u'Другой каталог'

        catalog_panel.edit_catalog()
        catalog_popup.set_catalog_name(other_catalog_name)
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        # check name after
        catalog_name_after_edit = catalog_panel.get_catalog_name()
        self.assertEquals(other_catalog_name, catalog_name_after_edit)

    def test_edit_catalog_upload_image_after_creating_catalog(self):
        # creating catalog
        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup()
        catalog_popup.set_catalog_name()
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        # check image stub
        catalog_widget = shop_market_page.catalog_widget
        is_exist_image_stub = catalog_widget.is_exist_image_stub()
        self.assertTrue(is_exist_image_stub)

        catalog_widget.open_catalog()
        catalog_page = CatalogPage(self.driver)
        catalog_panel = catalog_page.catalog_panel

        is_exist_image_stub = catalog_panel.is_exist_image_stub()
        self.assertTrue(is_exist_image_stub)

        # editing catalog
        catalog_panel.edit_catalog()
        catalog_popup.upload_catalog_image(self.CATALOG_IMAGE)
        catalog_popup.waiting_until_image_upload()
        upload_image_src = catalog_popup.get_image_src()
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        current_image_src = catalog_panel.get_image_src()
        self.assertEqual(upload_image_src[:self.CHARS_IN_SUBSTRING], current_image_src[:self.CHARS_IN_SUBSTRING])

    def test_delete_empty_catalog(self):
        # check stub
        shop_market_page = ShopMarketPage(self.driver)
        catalog_stub = shop_market_page.catalog_stub
        self.check_catalog_stub(catalog_stub)

        # creating catalog
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup()
        catalog_popup.set_catalog_name()
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        # check widget
        catalog_widget = shop_market_page.catalog_widget
        self.check_catalog_widget(catalog_widget)

        # removing catalog
        catalog_widget.open_catalog()
        catalog_page = CatalogPage(self.driver)
        catalog_panel = catalog_page.catalog_panel

        catalog_panel.remove_catalog()
        remove_catalog_popup = RemoveCatalogPopup(self.driver)
        remove_catalog_popup.submit_remove()
        remove_catalog_popup.waiting_until_close()

        # check stub
        self.check_catalog_stub(catalog_stub)

    def check_catalog_stub(self, catalog_stub):
        is_exist_catalog_stub = catalog_stub.is_exist_catalog_stub()
        self.assertTrue(is_exist_catalog_stub)

    def check_catalog_widget(self, catalog_widget):
        is_exist_catalog_widget = catalog_widget.is_exist_catalog_widget()
        self.assertTrue(is_exist_catalog_widget)
