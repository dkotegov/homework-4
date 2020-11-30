import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from pages.AuthPage import AuthPage
from pages.SecurityPage import SecurityPage


class SecurityTest(unittest.TestCase):
    def setUp(self) -> None:
        browser = os.environ.get("BROWSER", "CHROME")
        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
        )

        LOGIN = os.environ["LOGIN"]
        PASSWORD = os.environ["PASSWORD"]
        self.password = PASSWORD
        self.login = LOGIN

        auth_page = AuthPage(self.driver)
        auth_page.auth(LOGIN, PASSWORD)
        security_page = SecurityPage(self.driver)
        security_page.open()
        self.page = SecurityPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_click_devices_link(self):
        self.page.click_devices_link()
        self.assertTrue(self.page.is_device_page_open())

    def test_click_services_link(self):
        self.page.click_services_link()
        self.assertTrue(self.page.is_service_page_open())

    def test_click_setPassword_link(self):
        self.page.click_set_password_link()
        self.assertTrue(self.page.is_set_password_popup_open())

    def test_click_history_link(self):
        self.page.click_history_link()
        self.assertTrue(self.page.is_history_page_open())

    def test_click_2fact_link(self):
        self.page.click_2fact_link()
        self.assertTrue(self.page.is_2fact_page_load())

    def test_click_keys_link(self):
        self.page.click_keys_link()
        self.assertTrue(self.page.is_keys_page_load())

    def test_click_2fact_more_link(self):
        self.page.click_2fact_more_link()
        self.assertTrue(self.page.is_2fact_more_page_load())

    def test_click_keys_more_link(self):
        self.page.click_keys_more_link()
        self.assertTrue(self.page.is_keys_more_page_load())
