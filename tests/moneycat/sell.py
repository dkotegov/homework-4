from .utils import TestCase
from .pages.main import MainPage


class MoneyCatSellTest(TestCase):
    def setUp(self):
        super().setUp()
        self.main = MainPage(self.driver)
        self.sell_form = self.main.sell_form

    def tearDown(self) -> None:
        self.driver.quit()

    def test_sell_ok(self):
        self.main.currency_list.open_first_currency()
        before = self.sell_form.wallet_status()

        amount = 1
        self.sell_form.fill_input(amount)
        self.sell_form.sell()
        self.sell_form.wait_for_message()

        after = self.sell_form.wallet_status()

        self.assertEqual(before - after, amount)

    def test_sell_zero(self):
        self.main.currency_list.open_first_currency()
        before = self.sell_form.wallet_status()

        amount = 0
        self.sell_form.fill_input(amount)
        self.sell_form.sell()
        self.sell_form.wait_for_message()

        after = self.sell_form.wallet_status()

        self.assertEqual(before - after, amount)
        self.assertNotEqual(self.sell_form.get_error_message(), "")

    def test_sell_no_exist_currency(self):
        # try to buy euro by japan currency
        self.main.currency_list.open_last_currency()
        before = self.sell_form.wallet_status()

        amount = 1
        self.sell_form.fill_input(amount)
        self.sell_form.sell()
        self.sell_form.wait_for_message()

        after = self.sell_form.wallet_status()

        self.assertEqual(before - after, 0)
        self.assertNotEqual(self.sell_form.get_error_message(), "")

    def test_sell_too_much(self):
        self.main.currency_list.open_last_currency()
        before = self.sell_form.wallet_status()

        amount = before.__mul__(2.0)
        self.sell_form.fill_input(str(amount))
        self.sell_form.sell()
        self.sell_form.wait_for_message()

        after = self.sell_form.wallet_status()

        self.assertEqual(before - after, 0)
        self.assertNotEqual(self.sell_form.get_error_message(), "")
