import unittest
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote
from Auth import AuthPage
from Home import HomePage


class SortAndFilterTest(unittest.TestCase):
    USEREMAIL = 'adolgavintest@mail.ru'
    PASSWORD = 'homework1234'

    def setUp(self):
        browser = 'CHROME'

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth_page = AuthPage(self.driver)
        auth_page.auth(self.USEREMAIL, self.PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def test_buttons(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.banners.close_banner_if_exists()
        home_page.buttons.change_view()

        home_page.buttons.sort_by_alphabet()
        home_page.buttons.sort_by_size()
        home_page.buttons.sort_by_date()

        home_page.buttons.filter_by_image()
        home_page.buttons.filter_by_all()