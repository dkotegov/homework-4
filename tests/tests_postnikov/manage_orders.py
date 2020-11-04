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

        self.driver.implicitly_wait(2)
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

        products = self.filler.get_restaurant_products(self.filler.TEST_REST_NAME.format(0))
        self.filler.create_order(self.user_id, self.filler.TEST_REST_NAME.format(0), self.LOGIN, products[0])

        self.rest_list_page.open()
        self.rest_list_page.wait_visible()

        self.rest_list_page.open_manage_orders(self.rest_id)
        self.form = self.rest_list_page.manage_orders_form
        self.form.wait_visible()

    def tearDown(self):
        self.filler.admin_auth()
        self.filler.delete_all_rests()
        self.driver.quit()

    def testChangeOrderStatus(self):
        self.assertEqual(self.form.status(0), 'Принят')
        self.form.change_status(0)

        WebDriverWait(self.driver, 5, 0.3).until(
            lambda d: self.form.message() != ''
        )

        self.driver.refresh()
        self.form.wait_visible()

        self.assertEqual(self.form.status(0), 'У курьера')
        self.form.change_status(0)

        WebDriverWait(self.driver, 5, 0.3).until(
            lambda d: self.form.message() != ''
        )

        self.driver.refresh()
        self.form.wait_visible()

        self.assertEqual(self.form.status(0), 'Доставлен')
