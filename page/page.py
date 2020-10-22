import os
from urllib.parse import urljoin
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class Page(object):
    BASE_URL = 'https://geomap.2035school.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    def waitRedirect(self, redirectUrl):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.current_url != redirectUrl
        )


class MainPage(Page):
    PATH = 'page/menu'
    HEADER = '//h2[contains(text(), "меню")]'

    def get_header(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.HEADER).text
        )

    @property
    def Menu(self):
        return MainMenu(self.driver)


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    KEY = '//input[@id="inpField"]'
    SUBMIT = '//div[@id="btnSend"]'

    def set_key(self, key):
        self.driver.find_element_by_xpath(self.KEY).send_keys(key)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class MainMenu(Component):
    LOGOUT = '//div[@id="exitLogOutBtn"]'

    def logout(self):
        self.driver.find_element_by_xpath(self.LOGOUT).click()


class ExampleTest(unittest.TestCase):
    KEY = os.environ['PASSWORD']
    AUTH_SUCCESS = 'Правильный ключ'
    MAIN_PAGE_HEADER = 'Главное меню'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='127.17.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
    ## Редирект при вводе верного ключа.
    # Вход
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_key(self.KEY)
        auth_form.submit()
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, self.AUTH_SUCCESS)
        alert.accept()

    # Главная страница
        main_page = MainPage(self.driver)
        self.assertEqual(self.driver.current_url, main_page.BASE_URL + main_page.PATH)
        main_page_header = main_page.get_header()
        self.assertEqual(self.MAIN_PAGE_HEADER, main_page_header)
        main_page.Menu.logout()

