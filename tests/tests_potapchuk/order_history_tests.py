from tests.pages.order_history_page import OrderHistoryPage
from tests.tests_potapchuk.base_test import BaseTest


class OrderHistoryTest(BaseTest):
    def setUp(self):
        super().setUp(auth='user', with_address=True)
        super().create_restaurant_with_products(1)
        super().checkout_order(self.rest_id)

        self.historyPage = OrderHistoryPage(self.driver)
        # self.historyPage.open()
        self.historyPage.wait_visible()

    def tearDown(self):
        super().tearDown()
        super().clear_restaurant()

    def test_last_order_info(self):
        self.assertEqual(
            self.DEFAULT_REST_NAME,
            self.historyPage.last_restaurant_name(),
        )
        self.assertEqual(
            self.DEFAULT_PROD_PRICE,
            parse_int(self.historyPage.last_product_price()),
        )
        self.assertEqual(
            self.DEFAULT_PROD_NAME % 0,
            self.historyPage.last_product_name(),
        )

    def test_last_order_decline(self):
        last_num = self.historyPage.order_num()
        self.historyPage.decline_last_order()
        cur_num = self.historyPage.order_num()
        self.assertEqual(last_num - 1, cur_num)


def parse_int(string):
    try:
        return int(''.join([x for x in string if x.isdigit()]))
    except:
        return None