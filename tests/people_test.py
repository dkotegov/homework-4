# -*- coding: utf-8 -*-

import os
import re
import itertools
from time import sleep

import unittest
import urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Page(object):
    BASE_URL = 'http://ftest.tech-mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

class PeoplePage(Page):
    PATH = '/people/'
    NAVIGATION_MENU = '//select[contains(@class,"people-navigator-groups")]'
    NAVIGATION_ENTRY = '//select[contains(@class,"people-navigator-groups")]' \
        '/option[text()="TEXT"]'
    SEARCH_FIELD = '//input[@id="search-user-login"]'
    ERROR_BLOCK = '//div[@class="content-error"]'

    def __init__(self, driver,
                 page=1, order_by='user_rating', order_way='desc'):
        Page.__init__(self, driver)
        self.PATH = '/people/%d/?order=%s&order_way=%s' % \
                    (page, order_by, order_way)

    @property
    def people_list(self):
        count = len(self.driver.find_elements_by_xpath(Man.LOGIN))
        return [Man(self.driver, i) for i in range(1, count+1)]

    @property
    def paginator(self):
        return Paginator(self.driver)

    @property
    def statistic(self):
        return Statistic(self.driver)

    @property
    def navigation_group(self):
        return Select(self.driver.find_element_by_xpath(
            self.NAVIGATION_MENU))

    @navigation_group.setter
    def navigation_group(self, group):
        self.driver.find_element_by_xpath(
            self.NAVIGATION_ENTRY.replace('TEXT', group)).click()
        sleep(1)

    @property
    def error(self):
        try:
            self.driver.find_element_by_xpath(self.ERROR_BLOCK)
        except NoSuchElementException:
            return False
        return True


    def search(self, text):
        search_field = self.driver.find_element_by_xpath(self.SEARCH_FIELD)
        search_field.send_keys(text)
        sleep(1)
        search_field.send_keys(Keys.RETURN)
        sleep(1)


class Man(Component):
    NAME = '//p[@class="realname"]/a'
    LOGIN = '//p[@class="realname"]/a'
    ROLE = '//span[@class="user-group"]'
    SKILL = '//td[@class="cell-skill"]'
    RAITING = '//td[contains(@class, "cell-rating")]/strong'

    def __init__(self, driver, index):
        Component.__init__(self, driver)
        self.index = index

    def __add_index(self, path):
        return '(%s)[%d]' % (path, self.index)

    @property
    def login(self):
        href = urlparse.unquote(self.driver.find_element_by_xpath(
            self.__add_index(self.LOGIN)).get_attribute('href'))
        return re.findall(r'/([^/]+)/$', href)[0]

    @property
    def name(self):
        return self.driver.find_element_by_xpath(
            self.__add_index(self.NAME)).text

    @property
    def skill(self):
        return float(self.driver.find_element_by_xpath(
            self.__add_index(self.SKILL)).text.replace(',', '.'))

    @property
    def raiting(self):
        return float(self.driver.find_element_by_xpath(
            self.__add_index(self.RAITING)).text)

    @property
    def role(self):
        return self.driver.find_element_by_xpath(
            self.__add_index(self.ROLE)).text


class Paginator(Component):
    PAGINATOR = '//div[@class="pagination"]'
    FIRST = '//div[@class="pagination"]/ul/li/a[text()="первая"]'
    LAST = '//div[@class="pagination"]/ul/li/a[text()="последняя"]'
    PAGES = '//div[@class="pagination"]/ul/li'

    @property
    def exists(self):
        try:
            self.driver.find_element_by_xpath(self.PAGINATOR)
        except NoSuchElementException:
            return False
        return True

    def to_first(self):
        try:
            self.driver.find_element_by_xpath(self.FIRST).click()
            sleep(1)
        except NoSuchElementException:
            pass

    def to_last(self):
        self.driver.find_element_by_xpath(self.LAST).click()
        try:
            self.driver.find_element_by_xpath(self.LAST).click()
            sleep(1)
        except NoSuchElementException:
            pass

    @property
    def visible_pages(self):
        try:
            els = self.driver.find_elements_by_xpath(self.PAGES)
        except NoSuchElementException:
            els = []
        return [int(i.text) for i in els if re.findall('^[0-9]+$', i.text)]


class Statistic(Component):
    STATISTIC = '//div[@class="block-content"]/ul/li[text()="TEXT: "]/strong'
    def __getitem__(self, key):
        return int(self.driver.find_element_by_xpath(
            self.STATISTIC.replace('TEXT', key)).text)


class AuthForm(Component):
    LOGIN = '//input[@name="login"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//span[text()="Войти"]'
    LOGIN_BUTTON = '//a[text()="Вход для участников"]'
    USER_DROPDOWN = '//div[@class="dropdown-user"]'

    def open_form(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.USER_DROPDOWN).text)


def apply_pairs(lst, func):
    a, b = itertools.tee(lst)
    next(b, None)
    for a, b in itertools.izip(a, b):
        func(a, b)


class PeopleTest(unittest.TestCase):
    USEREMAIL = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    @classmethod
    def setUpClass(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')
        caps = getattr(DesiredCapabilities, browser).copy()
        caps['chromeOptions'] = {
            'prefs': {
                'credentials_enable_service': False,
                'profile': {
                    'password_manager_enabled': False
                }
            }
        }
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=caps
        )

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.open_form()
        sleep(3)
        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_sort_by_raiting_asc(self):
        page = PeoplePage(self.driver,
                          order_by='user_raiting', order_way='asc')
        page.open()
        apply_pairs(page.people_list,
                    lambda x, y: self.assertLessEqual(x.raiting, y.raiting))

    def test_sort_by_raiting_desc(self):
        page = PeoplePage(self.driver,
                          order_by='user_raiting', order_way='desc')
        page.open()
        apply_pairs(page.people_list,
                    lambda x, y: self.assertGreaterEqual(x.raiting, y.raiting))

    def test_sort_by_login_asc(self):
        page = PeoplePage(self.driver, order_by='user_login', order_way='asc')
        page.open()
        apply_pairs(page.people_list,
                    lambda x, y: self.assertLessEqual(x.login.lower(),
                                                      y.login.lower()))

    def test_sort_by_login_desc(self):
        page = PeoplePage(self.driver, order_by='user_login', order_way='desc')
        page.open()
        apply_pairs(page.people_list,
                    lambda x, y: self.assertGreaterEqual(x.login.lower(),
                                                         y.login.lower()))

    @unittest.expectedFailure
    def test_sort_by_skill_asc(self):
        page = PeoplePage(self.driver, order_by='user_skill', order_way='asc')
        page.open()
        apply_pairs(page.people_list,
                    lambda x, y: self.assertLessEqual(x.skill,
                                                      y.skill))

    @unittest.expectedFailure
    def test_sort_by_skill_desc(self):
        page = PeoplePage(self.driver, order_by='user_skill', order_way='desc')
        page.open()
        apply_pairs(page.people_list,
                    lambda x, y: self.assertGreaterEqual(x.skill,
                                                         y.skill))

    def test_search_by_name(self):
        name = u'Леся'
        full_name = u'Леся Жеребкина'
        page = PeoplePage(self.driver)
        page.open()
        page.search(name)
        self.assertIn(full_name, [i.name for i in page.people_list])

    def test_search_by_surname(self):
        surname = u'Чернега'
        full_name = u'Елена Чернега'
        page = PeoplePage(self.driver)
        page.open()
        page.search(surname)
        self.assertIn(full_name, [i.name for i in page.people_list])

    def test_search_by_login(self):
        login = 'Voloshin'
        full_name = u'Дмитрий Волошин'
        page = PeoplePage(self.driver)
        page.open()
        page.search(login)
        self.assertIn(full_name, [i.name for i in page.people_list])

    def test_search_in_group(self):
        surname = u'Чернега'
        full_name = u'Елена Чернега'
        page = PeoplePage(self.driver)
        page.open()
        page.navigation_group = 'Студент'
        page.search(surname)
        self.assertNotIn(full_name, [i.name for i in page.people_list])

    def test_sort_in_group(self):
        page = PeoplePage(self.driver, order_by='user_login', order_way='desc')
        page.open()
        page.navigation_group = 'Студент'
        apply_pairs(page.people_list,
                    lambda x, y: self.assertGreaterEqual(x.login.lower(),
                                                         y.login.lower()))

    def test_count_in_group(self):
        page = PeoplePage(self.driver)
        page.open()
        page.navigation_group = 'Студент'
        count_per_page = len(page.people_list)
        paginator = page.paginator
        paginator.to_last()
        total = paginator.visible_pages[-2] * count_per_page + \
                len(page.people_list)
        self.assertEqual(total, page.statistic['Студент'])

    def test_not_exists(self):
        page = PeoplePage(self.driver, page=9999)
        page.open()
        self.assertTrue(page.error)
