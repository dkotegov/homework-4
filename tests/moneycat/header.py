from .utils import TestCase
from .pages.main import MainPage


class MoneyCatHeaderTest(TestCase):
    def setUp(self):
        super().setUp()
        self.main = MainPage(self.driver)
        self.header_form = self.main.header

    def tearDown(self) -> None:
        self.driver.quit()

    def test_header_open_by_click_logo(self):
        self.header_form.click_logo()
        visible = self.main.currency_list.is_currency_card_visible()
        self.assertEqual(visible, True)

    def test_header_open_by_click_catalog(self):
        self.header_form.click_catalog()
        visible = self.main.currency_list.is_currency_card_visible()
        self.assertEqual(visible, True)

    def test_header_open_by_click_settings(self):
        is_settings_page = self.header_form.click_account()
        self.assertEqual(is_settings_page, True)

    def test_header_open_drop_down_menu(self):
        drop_down_menu_visible = self.header_form.click_avatar()
        self.assertEqual(drop_down_menu_visible, True)

    def test_header_settings_drop_down_menu(self):
        self.header_form.click_avatar()
        is_settings_page = self.header_form.click_settings_in_drop_down_menu()
        self.assertEqual(is_settings_page, True)

    def test_header_exit_from_drop_down_menu(self):
        self.header_form.click_avatar()
        is_auth_page = self.header_form.click_exit_in_drop_down_menu()
        self.assertEqual(is_auth_page, True)

    def test_header_bag(self):
        is_bag_page = self.header_form.click_bag()
        self.assertEqual(is_bag_page, True)

    def test_header_history(self):
        is_history_page = self.header_form.click_history()
        self.assertEqual(is_history_page, True)
