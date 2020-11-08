from tests.pages.order_history_page import OrderHistoryPage
from tests.pages.order_page import OrderPage
from tests.tests_potapchuk.base_test import BaseTest


class OrderApproveTest(BaseTest):
    def setUp(self):
        super().create_restaurant_with_products(2)
        super().setUp(auth='user')
        super().order_product(self.rest_id)

        self.orderPage = OrderPage(self.driver)
        self.orderPage.open()
        self.orderPage.wait_visible()

    def tearDown(self):
        super().tearDown()
        super().clear_restaurant()

    def test_incorrect_phone(self):
        self.orderPage.set_phone('qwer')
        self.assertEqual('', self.orderPage.phone())

        self.orderPage.set_phone('123')
        self.orderPage.wait_phone_error()
        self.assertNotEqual(0, len(self.orderPage.phone_error()))

    def test_incorrect_email(self):
        self.orderPage.set_email('qwer')
        self.orderPage.wait_email_error()
        self.assertNotEqual(0, len(self.orderPage.email_error()))

    def test_confirm_order(self):
        self.orderPage.click_checkout_button()
        history = OrderHistoryPage(self.driver)
        history.wait_visible()
