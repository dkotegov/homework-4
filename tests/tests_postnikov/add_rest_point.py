import os
import unittest

from tests.pages.main_page import MainPage
from tests.pages.address_page import AddressPage
from tests.pages.admin_rest_page import AdminRestaurantsPage
from tests.helpers.local_storage import LocalStorage
from tests.helpers.database import DatabaseFiller

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class AddPointTest(unittest.TestCase):
    LOGIN = os.environ['ADMIN_LOGIN']
    PASSWORD = os.environ['ADMIN_PASSWORD']

    ADDRESS = 'Россия, Москва, 2-я Бауманская улица, 5с1'
    LONGITUDE = 55.765985
    LATITUDE = 37.68456

    POINT_ADDRESS = 'Россия, Москва, Старокирочный переулок, 16/2с1'
    UNVALID_ADDRESS = 'Test address'
    RADIUS = 5
    UNVALID_RADIUS_NEGATIVE = -10
    UNVALID_RADIUS_MAX = 100
    UNVALID_RADIUS_STRING = '{}string'.format(RADIUS)

    URL_FORM = 'http://skydelivery.site/admin/restaurants/{}/add/point'

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
        self.filler.admin_auth()
        self.filler.create_test_restaurants(1)

        self.rest_id = self.filler.get_restaurant_id_by_name(self.filler.TEST_REST_NAME.format(0))
        self.rest_list_page = AdminRestaurantsPage(self.driver)

        self.rest_list_page.open()
        self.rest_list_page.wait_visible()

    def tearDown(self):
        self.filler.delete_all_rests()
        self.driver.quit()

    def testUnvalidRadius(self):
        url_add = self.URL_FORM.format(self.rest_id)

        form = self.rest_list_page.add_point_form
        self.rest_list_page.add_point(self.rest_id, self.POINT_ADDRESS, self.UNVALID_RADIUS_NEGATIVE)

        self.assertEqual(self.driver.current_url, url_add)
        self.assertEqual(form.radius_error(), 'Минимальное значение: 0.1')

        form.clear_radius()
        form.set_radius(self.UNVALID_RADIUS_MAX)
        form.submit()

        self.assertEqual(self.driver.current_url, url_add)
        self.assertEqual(form.radius_error(), 'Максимальное значение: 50')

        form.clear_radius()
        form.set_radius(self.UNVALID_RADIUS_STRING)
        
        self.assertEqual(form.radius_text(), '')

    def testUnvalidAddress(self):
        url_add = self.URL_FORM.format(self.rest_id)
        self.rest_list_page.add_point(self.rest_id, self.UNVALID_ADDRESS, self.RADIUS)

        form = self.rest_list_page.add_point_form

        WebDriverWait(self.driver, 5, 0.1).until_not(
            lambda d: form.address_error() == '...'
        )

        self.assertEqual(self.driver.current_url, url_add)
        self.assertEqual(form.address_error(), 'с точностью до дома')

    def testAddPoint(self):
        self.rest_list_page.add_point(self.rest_id, self.POINT_ADDRESS, self.RADIUS)

        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.current_url == 'http://skydelivery.site/admin/restaurants'
        )

        self.rest_list_page.wait_visible()
        self.assertEqual(self.rest_list_page.message(), 'Точка успешно добавлена')
