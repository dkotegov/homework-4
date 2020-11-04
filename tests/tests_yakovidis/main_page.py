import os
import unittest

from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.registration_page import RegistrationPage
from tests.pages.main_page import MainPage
from tests.pages.address_page import AddressPage
from tests.pages.auth_page import AuthPage
from tests.pages.profile_page import ProfilePage
from tests.helpers.database import DatabaseFiller

from selenium.webdriver import DesiredCapabilities, Remote


class MainPageTest(unittest.TestCase):
    DEFAULT_PHOTO = 'data/test_prod_photo.jpg'
    PROFILE_PHOTO = 'data/test_rest_photo.jpg'
    BIG_PROFILE_PHOTO = 'data/test_big_photo.jpg'
    WRONG_PROFILE_PHOTO = 'data/test_non_photo_file'

    def setUp(self):
        self.login = os.environ.get('ADMIN_LOGIN')
        self.password = os.environ.get('ADMIN_PASSWORD')

        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        address_page = AddressPage(self.driver)
        address_page.open()
        address_page.start_address('Россия, Москва, Знаменская улица, 53')

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.wait_open()
        auth_page.auth(self.login, self.password)

        profile_page = ProfilePage(self.driver)
        profile_page.wait_open()

        self.main_page = MainPage(self.driver)
        self.main_page.open()

        self.main_form = self.main_page.main_form

    def test_recommendation_order(self):
        self.main_form.wait_open()
        recomendations = self.main_form.get_recommendations()
        curr_rec = recomendations[0].text

        filler = DatabaseFiller()
        filler.admin_auth()

        filler.clean_up_orders()

        products = filler.get_restaurant_products(curr_rec)
        user_id = filler.get_profile_id()

        filler.create_order(user_id, curr_rec, self.login, products[0])

        self.driver.refresh()
        self.main_page.wait_visible()

        upd_recommendations = self.main_form.get_recommendations()
        is_exists = False
        for rec in upd_recommendations:
            if rec.text == curr_rec:
                is_exists = True

        filler.clean_up_orders()

        self.assertEqual(is_exists, False)

    # TODO: доделать когда по тегам можно будет гулять
    def test_tag_search(self):
        self.main_form.wait_open()

        filler = DatabaseFiller()
        filler.admin_auth()
        filler.create_tag('testtag')
        filler.create_restaurant('testRest')
        filler.add_tag_to_restaurant('testtag', 'testRest')

        self.driver.refresh()
        self.main_form.wait_open()

        self.main_form.get_tag_button_by_name('testtag').click()

        self.driver.refresh()
        self.main_form.wait_open()

        is_exists = False
        restaurants = self.main_form.get_restaurants()
        for item in restaurants:
            if item.text == 'testRest':
                is_exists = True

        filler.delete_tag_from_restaurant('testtag', 'testRest')
        filler.delete_tag('testtag')
        filler.delete_restaurant_by_name('testRest')

        self.assertEqual(is_exists, True)

    def tearDown(self):
        self.driver.quit()
