import os
import unittest

from tests.pages.main_page import MainPage
from tests.pages.address_page import AddressPage
from tests.pages.add_rest_page import AddRestaurantPage
from tests.helpers.local_storage import LocalStorage
from tests.helpers.database import DatabaseFiller

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class AddRestaurantTest(unittest.TestCase):
    LOGIN = os.environ['ADMIN_LOGIN']
    PASSWORD = os.environ['ADMIN_PASSWORD']

    ADDRESS = 'Россия, Москва, 2-я Бауманская улица, 5с1'
    LONGITUDE = 55.765985
    LATITUDE = 37.68456

    REST_ADDRESS = 'Россия, Москва, Старокирочный переулок, 16/2с1'
    UNVALID_ADDRESS = 'Test address'

    TITLE = 'Test restaurant'
    TITLE_MAX_SIZE = 30
    TITLE_MIN_SIZE = 4
    UNVALID_SHORT_TITLE = ''.join(['a' for i in range(TITLE_MIN_SIZE-1)])
    UNVALID_LONG_TITLE = ''.join(['a' for i in range(TITLE_MAX_SIZE+1)])

    DESCRIPTION_MIN_SIZE = 10
    UNVALID_DESCRIPTION = ''.join(['a' for i in range(DESCRIPTION_MIN_SIZE-1)])

    NON_PHOTO = 'data/test_non_photo_file'
    PHOTO = 'data/test_rest_photo.jpg'
    BIG_PHOTO = 'data/test_big_photo.jpg'

    RADIUS = 10
    UNVALID_RADIUS_NEGATIVE = -10
    UNVALID_RADIUS_MAX = 100
    UNVALID_RADIUS_STRING = '{}string'.format(RADIUS)

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy() 
        )

        #Open site page before using local storage
        AddressPage(self.driver).open()
        storage = LocalStorage(self.driver)

        storage.set('deliveryGeo', self.ADDRESS)
        storage.set('longitude', self.LONGITUDE)
        storage.set('latitude', self.LATITUDE)

        self.driver.refresh()
        self.driver.maximize_window()

        main_page = MainPage(self.driver)
        main_page.wait_open()

        main_page.auth(self.LOGIN, self.PASSWORD)

        self.add_rest = AddRestaurantPage(self.driver)
        self.add_rest.open()

    def tearDown(self):
        self.driver.quit()

    def testUnvalidTitle(self):
        self.add_rest.add_restaurant('', self.REST_ADDRESS, self.RADIUS, self.PHOTO)
        form = self.add_rest.add_form

        self.assertEqual(self.driver.current_url, 'http://skydelivery.site/admin/restaurants/add')
        self.assertEqual(form.title_error(), 'Обязательное поле')

        form.set_title(self.UNVALID_SHORT_TITLE)
        form.submit()

        self.assertEqual(self.driver.current_url, 'http://skydelivery.site/admin/restaurants/add')
        self.assertEqual(form.title_error(), 'Минимальная длина: 4')

        form.clear_title()
        form.set_title(self.UNVALID_LONG_TITLE)

        self.assertEqual(self.driver.current_url, 'http://skydelivery.site/admin/restaurants/add')
        self.assertNotEqual(form.title_value(), self.UNVALID_LONG_TITLE)

    def testUnvalidDescription(self):
        self.add_rest.add_restaurant(self.TITLE, self.REST_ADDRESS, self.RADIUS, self.PHOTO, '')
        form = self.add_rest.add_form

        self.assertEqual(self.driver.current_url, 'http://skydelivery.site/admin/restaurants/add')
        self.assertEqual(form.description_error(), 'Обязательное поле')

        form.set_description(self.UNVALID_DESCRIPTION)
        form.submit()
        
        self.assertEqual(self.driver.current_url, 'http://skydelivery.site/admin/restaurants/add')
        self.assertEqual(form.description_error(), 'Минимальная длина: 10')

    def testUnvalidRadius(self):
        self.add_rest.add_restaurant(self.TITLE, self.REST_ADDRESS, '', self.PHOTO)
        form = self.add_rest.add_form

        self.assertEqual(self.driver.current_url, 'http://skydelivery.site/admin/restaurants/add')
        self.assertEqual(form.radius_error(), 'Обязательное поле')

        form.set_radius(self.UNVALID_RADIUS_NEGATIVE)
        form.submit()

        self.assertEqual(self.driver.current_url, 'http://skydelivery.site/admin/restaurants/add')
        self.assertEqual(form.radius_error(), 'Минимальное значение: 0.1')

        form.clear_radius()
        form.set_radius(self.UNVALID_RADIUS_MAX)
        form.submit()

        self.assertEqual(self.driver.current_url, 'http://skydelivery.site/admin/restaurants/add')
        self.assertEqual(form.radius_error(), 'Максимальное значение: 50')

        form.clear_radius()
        form.set_radius(self.UNVALID_RADIUS_STRING)

        self.assertEqual(self.driver.current_url, 'http://skydelivery.site/admin/restaurants/add')
        self.assertEqual(form.radius_value(), '')

    def testUnvalidAddress(self):
        self.add_rest.add_restaurant(self.TITLE, self.UNVALID_ADDRESS, self.RADIUS, self.PHOTO)
        form = self.add_rest.add_form

        WebDriverWait(self.driver, 5, 0.1).until_not(
            lambda d: form.address_error() == '...'
        )

        self.assertEqual(self.driver.current_url, 'http://skydelivery.site/admin/restaurants/add')
        self.assertEqual(form.address_error(), 'с точностью до дома')

    def testUnvalidBigPhoto(self):
        self.add_rest.add_restaurant(self.TITLE, self.REST_ADDRESS, self.RADIUS, self.BIG_PHOTO)
        form = self.add_rest.add_form

        self.assertEqual(self.driver.current_url, 'http://skydelivery.site/admin/restaurants/add')
        self.assertEqual(form.photo_error(), 'Максимальный размер файла - 1МБ')

    def testUnvalidPhotoFormat(self):
        self.add_rest.add_restaurant(self.TITLE, self.REST_ADDRESS, self.RADIUS, self.NON_PHOTO)
        form = self.add_rest.add_form

        self.assertEqual(self.driver.current_url, 'http://skydelivery.site/admin/restaurants/add')
        self.assertEqual(form.photo_error(), 'Выберите изображение (.png, .jpg)')

    def testAddRestaurant(self):
        self.add_rest.add_restaurant(self.TITLE, self.REST_ADDRESS, self.RADIUS, self.PHOTO)

        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.current_url == 'http://skydelivery.site/admin/restaurants'
        )

        db = DatabaseFiller()
        db.admin_auth()
        db.delete_restaurant_by_name(self.TITLE)
