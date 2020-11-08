from tests.pages.manage_orders_page import ManageOrderPage
from tests.tests_potapchuk.base_test import BaseTest


class NotificationTest(BaseTest):
    def setUp(self):
        super().setUp(auth='admin', with_address=True)
        super().create_restaurant_with_products(1)
        super().checkout_order(self.rest_id)

        self.manageOrderPage = ManageOrderPage(self.driver, self.rest_id)
        self.manageOrderPage.open()
        self.manageOrderPage.wait_visible()

    def tearDown(self):
        super().tearDown()
        super().clear_restaurant()

    def test_receive_notifications(self):
        self.manageOrderPage.last_order_set_next_status()
        self.assert_notif_message('У курьера')

        self.manageOrderPage.last_order_set_next_status()
        self.assert_notif_message('Доставлен')

        for i in range(2):
            self.delete_last_notif()

    def assert_notif_message(self, message):
        self.assertEqual(
            message,
            self.manageOrderPage.last_notif_message(),
        )

    def assert_notif_quantity(self, quant):
        self.assertEqual(
            quant,
            self.manageOrderPage.status_cards_num()
        )

    def delete_last_notif(self):
        self.manageOrderPage.delete_last_notif()

