import unittest
from tests.default_setup import default_setup
from tests.pages.restaurant.profile import RestaurantProfilePage
from tests.steps.auth_restaurant import auth_setup


class ChangeRestaurantDataSuccessTests(unittest.TestCase):
    new_phone = "9197666701"
    new_email = "mail@mail.ru"
    new_cost = "1000"
    new_radius = "2000"
    new_title = "dsfeds"
    new_pass = "123456"

    def setUp(self):
        default_setup(self)
        auth_setup(self)
        self.profile_page = RestaurantProfilePage(self.driver)
        self.profile_page.open()

        self.old_title = self.profile_page.navbar.get_username()

    def tearDown(self):
        self.set_start_data()
        self.driver.quit()

    def set_start_data(self):
        self.profile_page.set_email(self.RESTAURANT_LOGIN)
        self.profile_page.set_current_password(self.old_title)
        self.profile_page.set_new_password(self.RESTAURANT_PASSWORD)
        self.profile_page.set_repeat_password(self.RESTAURANT_PASSWORD)
        self.profile_page.click_save()

    def test_change_all_data(self):
        self.profile_page.set_phone(self.new_phone)
        self.profile_page.set_email(self.new_email)
        self.profile_page.set_cost(self.new_cost)
        self.profile_page.set_radius(self.new_radius)
        self.profile_page.set_current_password(self.USER_PASSWORD)
        self.profile_page.set_new_password(self.new_pass)
        self.profile_page.set_repeat_password(self.new_pass)
        self.profile_page.click_save()
