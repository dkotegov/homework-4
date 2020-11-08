from tests.pages.map_page import MapPage
from tests.pages.restaurant_page import RestaurantPage
from tests.tests_potapchuk.base_test import BaseTest


class MapTest(BaseTest):
    def setUp(self):
        super().setUp(auth='user', with_address=True)

        self.mapPage = MapPage(self.driver)
        self.mapPage.open()
        self.mapPage.wait_visible()

    def test_href_to_restaurant(self):
        self.mapPage.click_to_center_pointer()
        self.mapPage.wait_rest_button_visible()
        self.mapPage.click_rest_button()
        RestaurantPage(self.driver).wait_visible()

        self.assertNotEqual(
            -1,
            self.driver.current_url.index('/restaurants/'),
        )



