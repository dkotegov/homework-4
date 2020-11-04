import os
import unittest

from tests.pages.main_page import MainPage
from tests.pages.address_page import AddressPage
from tests.pages.admin_rest_page import AdminRestaurantsPage
from tests.helpers.local_storage import LocalStorage
from tests.helpers.database import DatabaseFiller

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class AddProductTest(unittest.TestCase):
    LOGIN = os.environ['ADMIN_LOGIN']
    PASSWORD = os.environ['ADMIN_PASSWORD']

    ADDRESS = 'Россия, Москва, 2-я Бауманская улица, 5с1'
    LONGITUDE = 55.765985
    LATITUDE = 37.68456

    TITLE = "Test product"
    TITLE_MAX_SIZE = 80
    TITLE_MIN_SIZE = 4
    UNVALID_SHORT_TITLE = ''.join(['a' for i in range(TITLE_MIN_SIZE-1)])
    UNVALID_LONG_TITLE = ''.join(['a' for i in range(TITLE_MAX_SIZE+1)])

    PRICE = 100
    UNVALID_PRICE_NEGATIVE = -10
    UNVALID_PRICE_MAX = 10001
    UNVALID_PRICE_STRING = '{}string'.format(PRICE)

    PHOTO = 'data/test_rest_photo.jpg'
    NON_PHOTO = 'data/test_non_photo_file'
    BIG_PHOTO = 'data/test_big_photo.jpg'

    URL_FORM = 'http://skydelivery.site/admin/restaurants/{}/add/product'
    URL_RESTAURANT = 'http://skydelivery.site/restaurants/{}'

    PRODUCT_LIST = '//div[@class="restaurant-view__product-list"]'
    PRODUCT_CARD = '//div[@class="product-card__container"]'
    PRODUCT_CARD_TITLE = '//span[@class="product-card__name"]'
    PRODUCT_CARD_PRICE = '//span[@class="product-card__description"]'

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

    def testUnvlaidTitle(self):
        url_form = self.URL_FORM.format(self.rest_id)
        self.rest_list_page.add_product(self.rest_id, '', self.PRICE, self.PHOTO)
        form = self.rest_list_page.add_product_form

        self.assertEqual(self.driver.current_url, url_form)
        self.assertEqual(form.title_error(), 'Обязательное поле')

        form.set_title(self.UNVALID_SHORT_TITLE)
        form.submit()

        self.assertEqual(self.driver.current_url, url_form)
        self.assertEqual(form.title_error(), 'Минимальная длина: 4')

        form.clear_title()
        form.set_title(self.UNVALID_LONG_TITLE)

        self.assertNotEqual(form.title_value(), self.UNVALID_LONG_TITLE)

    def testUnvalidPrice(self):
        url_form = self.URL_FORM.format(self.rest_id)
        self.rest_list_page.add_product(self.rest_id, self.TITLE, '', self.PHOTO)
        form = self.rest_list_page.add_product_form

        self.assertEqual(self.driver.current_url, url_form)
        self.assertEqual(form.price_error(), 'Обязательное поле')

        form.set_price(self.UNVALID_PRICE_NEGATIVE)
        form.submit()

        self.assertEqual(self.driver.current_url, url_form)
        self.assertEqual(form.price_error(), 'Минимальное значение: 0.1')

        form.clear_price()
        form.set_price(self.UNVALID_PRICE_MAX)
        form.submit()

        self.assertEqual(self.driver.current_url, url_form)
        self.assertEqual(form.price_error(), 'Максимальное значение: 10000')

        form.clear_price()
        form.set_price(self.UNVALID_PRICE_STRING)

        self.assertEqual(form.price_value(), '')

    def testUnvalidBigPhoto(self):
        url_form = self.URL_FORM.format(self.rest_id)
        self.rest_list_page.add_product(self.rest_id, self.TITLE, self.PRICE, self.BIG_PHOTO)
        form = self.rest_list_page.add_product_form

        self.assertEqual(self.driver.current_url, url_form)
        self.assertEqual(form.photo_error(), 'Максимальный размер файла - 1МБ')

    def testUnvalidPhotoFormat(self):
        url_form = self.URL_FORM.format(self.rest_id)
        self.rest_list_page.add_product(self.rest_id, self.TITLE, self.PRICE, self.NON_PHOTO)
        form = self.rest_list_page.add_product_form

        self.assertEqual(self.driver.current_url, url_form)
        self.assertEqual(form.photo_error(), 'Выберите изображение (.png, .jpg)')

    def testAddProduct(self):
        self.rest_list_page.add_product(self.rest_id, self.TITLE, self.PRICE, self.PHOTO)
        
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.current_url == self.URL_RESTAURANT.format(self.rest_id) and
            d.find_element_by_xpath(self.PRODUCT_LIST).is_displayed() and
            d.find_element_by_xpath(self.PRODUCT_CARD).is_displayed()
        )

        card = self.driver.find_element_by_xpath(self.PRODUCT_CARD)

        self.assertEqual(card.find_element_by_xpath(self.PRODUCT_CARD_TITLE).text, self.TITLE)
        self.assertEqual(card.find_element_by_xpath(self.PRODUCT_CARD_PRICE).text, '{}₽'.format(self.PRICE))
