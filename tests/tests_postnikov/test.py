import os
import unittest

from tests.pages.main_page import MainPage
from tests.pages.address_page import AddressPage
from tests.pages.add_rest_page import AddRestaurantPage
from tests.helpers.local_storage import LocalStorage
from tests.helpers.database import DatabaseFiller

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class FirstTest(unittest.TestCase):
    ADDRESS = 'Россия, Москва, 2-я Бауманская улица, 5с1'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy() 
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        addr_page = AddressPage(self.driver)
        addr_page.open()

        addr_page.start_address(self.ADDRESS)

class AddRestaurantTest(unittest.TestCase):
    LOGIN = os.environ['ADMIN_LOGIN']
    PASSWORD = os.environ['ADMIN_PASSWORD']

    ADDRESS = 'Россия, Москва, 2-я Бауманская улица, 5с1'
    LONGITUDE = 55.765985
    LATITUDE = 37.68456

    REST_ADDRESS = 'Россия, Москва, Старокирочный переулок, 16/2с1'
    TITLE = 'Test restaurant'
    NON_PHOTO = 'data/test_non_photo_file'
    PHOTO = 'data/test_rest_photo.jpg'
    BIG_PHOTO = 'data/test_big_photo.jpg'
    RADIUS = 10

    ERROR_CLASS = 'checked-input__error'
    TITLE_ERROR = '//div[@id="add-restaurant__name-input-wrapper_err"]'
    DESCRIPTION_ERROR = '//div[@id="add-restaurant__desc-textarea-wrapper_err"]'
    ADDRESS_ERROR = '//div[@id="alone_geo-input__add-rest-point-wrapper_err"]'
    PHOTO_ERROR = '//div[@id="img-input__error"]'

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

        main_page = MainPage(self.driver)
        main_page.wait_open()

        main_page.auth(self.LOGIN, self.PASSWORD)

        self.add_rest = AddRestaurantPage(self.driver)
        self.add_rest.open()

    def tearDown(self):
        self.driver.quit()

    def testUnvalidTitle(self):
        self.add_rest.add_restaurant('l', self.REST_ADDRESS, self.RADIUS, self.PHOTO)

        self.assertEqual(self.driver.current_url, 'http://skydelivery.site/admin/restaurants/add')
        self.assertEqual(self.driver.find_element_by_xpath(self.TITLE_ERROR).text, 'Минимальная длина: 4')

        # self.add_rest.add_restaurant('There is a text of a title is more than 30 characters long', self.REST_ADDRESS, self.RADIUS, self.PHOTO)
        # self.assertEqual(self.driver.current_url, 'http://skydelivery.site/admin/restaurants/add')
        # self.assertEqual(self.driver.find_element_by_xpath(self.TITLE_ERROR).text, 'Максимальная длина: 30')

    def testUnvalidDescription(self):
        self.add_rest.add_restaurant(self.TITLE, self.REST_ADDRESS, self.RADIUS, self.PHOTO, 'l')

        self.assertEqual(self.driver.current_url, 'http://skydelivery.site/admin/restaurants/add')
        self.assertEqual(self.driver.find_element_by_xpath(self.DESCRIPTION_ERROR).text, 'Минимальная длина: 10')

    # def testUnvalidAddress(self):
    # TODO block button
        # self.add_rest.add_restaurant(self.TITLE, "Unvalid address", self.RADIUS, self.PHOTO)

        # self.assertEqual(self.driver.current_url, 'http://skydelivery.site/admin/restaurants/add')
        # self.assertEqual(self.driver.find_element_by_xpath(self.ADDRESS_ERROR).text, 'с точностью до дома')

# TODO block button submit on errors

    # def testUnvalidRadius(self):
    #     TODO error on front

    # def testUnvalidBigPhoto(self):
    #     TODO error on front

    def testUnvalidPhotoFormat(self):
        self.add_rest.add_restaurant(self.TITLE, self.REST_ADDRESS, self.RADIUS, self.NON_PHOTO)

        self.assertEqual(self.driver.current_url, 'http://skydelivery.site/admin/restaurants/add')
        self.assertEqual(self.driver.find_element_by_xpath(self.PHOTO_ERROR).text, 'Выберите изображение (.png, .jpg)')

    def testAddRestaurant(self):
        self.add_rest.add_restaurant(self.TITLE, self.REST_ADDRESS, self.RADIUS, self.PHOTO)

        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.current_url != 'http://skydelivery.site/admin/restaurants'
        )

        db = DatabaseFiller()
        db.admin_auth()
        db.delete_restaurant_by_name(self.TITLE)
