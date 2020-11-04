import os
import unittest

from tests.pages.address_page import AddressPage
from tests.pages.main_page import MainPage
from tests.pages.admin_rest_page import AdminRestaurantsPage
from tests.helpers.database import DatabaseFiller
from tests.helpers.local_storage import LocalStorage

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.wait import WebDriverWait

class ManageOrdersTest(unittest.TestCase):
    LOGIN = os.environ['ADMIN_LOGIN']
    PASSWORD = os.environ['ADMIN_PASSWORD']

    USER_LOGIN = os.environ['LOGIN']

    ADDRESS = 'Россия, Москва, 2-я Бауманская улица, 5с1'
    LONGITUDE = 55.765985
    LATITUDE = 37.68456

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy() 
        )

        AddressPage(self.driver).open()
        storage = LocalStorage(self.driver)

        storage.set('deliveryGeo', self.ADDRESS)
        storage.set('longitude', self.LONGITUDE)
        storage.set('latitude', self.LATITUDE)

        self.driver.refresh()
        self.driver.maximize_window()

        main_page = MainPage(self.driver)
        main_page.wait_visible()

        main_page.auth(self.LOGIN, self.PASSWORD)

        self.filler = DatabaseFiller()

        self.filler.user_auth()
        self.user_id = self.filler.get_profile_id()

        self.filler.admin_auth()
        self.filler.create_test_restaurants(1)
        self.filler.create_products_for_rests(1, 100)

        self.rest_id = self.filler.get_restaurant_id_by_name(self.filler.TEST_REST_NAME.format(0))
        self.rest_list_page = AdminRestaurantsPage(self.driver)

        products = self.filler.get_restaurant_products(self.rest_id)
        self.filler.create_order(self.user_id, self.rest_id, self.LOGIN, products[0])

        self.rest_list_page.open()
        self.rest_list_page.wait_visible()

    def tearDown(self):
        self.filler.user_auth()
        self.filler.clean_up_orders()
        self.filler.admin_auth()
        self.filler.delete_all_rests()
        self.driver.quit()

    def testChangeOrderStatus(self):
        pass

