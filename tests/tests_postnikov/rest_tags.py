import os
import unittest

from tests.pages.address_page import AddressPage
from tests.pages.main_page import MainPage
from tests.pages.admin_rest_page import AdminRestaurantsPage
from tests.helpers.database import DatabaseFiller
from tests.helpers.local_storage import LocalStorage

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.wait import WebDriverWait

class ManageRestaurantTagsTest(unittest.TestCase):
    LOGIN = os.environ['ADMIN_LOGIN']
    PASSWORD = os.environ['ADMIN_PASSWORD']

    ADDRESS = 'Россия, Москва, 2-я Бауманская улица, 5с1'
    LONGITUDE = 55.765985
    LATITUDE = 37.68456

    TAG_NAME = 'Test Tag'

    MAIN_URL = 'http://skydelivery.site/restaurant_list/1'
    REST_ELEMENT = '//div[contains(@class, "restaurant-list__restaurant-{}")]'
    REST_LIST = '//div[@id="restaurant-list"]'
    REST_NAME = './/span[@class="restaurant__name"]'

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

        self.filler.create_tag(self.TAG_NAME)
        self.tag_id = self.filler.get_tag_by_name(self.TAG_NAME)

        self.rest_id = self.filler.get_restaurant_id_by_name(self.filler.TEST_REST_NAME.format(0))
        self.rest_list_page = AdminRestaurantsPage(self.driver)

        self.rest_list_page.open()
        self.rest_list_page.wait_visible()

        self.rest_list_page.open_manage_tags(self.rest_id)
        self.form = self.rest_list_page.manage_tags_form
        self.form.wait_visible()

    def tearDown(self):
        self.filler.delete_all_rests()
        self.filler.delete_tag(self.TAG_NAME)
        self.driver.quit()

    def testAddTagToRestaurant(self):
        self.form.set_tag(self.tag_id)
        self.form.submit()
    
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: self.form.message() != '' 
        )

        self.assertEqual(self.form.message(), 'Теги успешно изменены')

        main_page = MainPage(self.driver)
        main_page.open()

        main_form = main_page.main_form
        main_form.wait_open()
        main_form.set_tag(self.tag_id)

        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.current_url == self.MAIN_URL 
        )

        main_page.wait_visible()
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.REST_LIST).find_element_by_xpath(self.REST_ELEMENT.format(self.rest_id)).is_displayed()
        )
        rest_el = self.driver.find_element_by_xpath(self.REST_LIST).find_element_by_xpath(self.REST_ELEMENT.format(self.rest_id))
        self.assertEqual(rest_el.find_element_by_xpath(self.REST_NAME).text, self.filler.TEST_REST_NAME.format(0))

    def testDeleteTagFromRestaurant(self):
        self.filler.add_tag_to_restaurant(self.TAG_NAME, self.filler.TEST_REST_NAME.format(0))

        self.driver.refresh()

        self.form.wait_visible()
        self.form.unset_tag(self.tag_id)
        self.form.submit()
    
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: self.form.message() != '' 
        )

        self.assertEqual(self.form.message(), 'Теги успешно изменены')

        main_page = MainPage(self.driver)
        main_page.open()

        main_form = main_page.main_form
        main_form.wait_open()
        main_form.set_tag(self.tag_id)

        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.current_url == self.MAIN_URL 
        )

        self.driver.refresh()

        main_page.wait_visible()
        self.assertEqual(self.driver.find_element_by_xpath(self.REST_LIST).text, 'К сожалению, мы пока не доставляем в ваш район 🙁')
