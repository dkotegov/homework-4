from selenium import webdriver

import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import unittest
from urllib.parse import urljoin

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class Page(object):
    BASE_URL = 'https://zinterest.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


    @property
    def top(self):
        return Top(self.driver)

class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)


class PinPage(Page):
    PATH = '/pin/339'

    def open_pin(self):
        url = urljoin(super().BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    @property
    def pin(self):
        return Pin(self.driver)

class Component(object):
    def __init__(self, driver):
        self.driver = driver

class AuthForm(Component):
    LOGIN = 'loginUser'
    PASSWORD = 'passUser'
    SUBMIT = "//input[@value='Войти']"
    LOGIN_BUTTON = 'loginModal'
    INFO = 'closeInfo'

    def open_form(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id(self.LOGIN_BUTTON)
        ).click()
        #self.driver.find_elment_by_id()
        #//self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def set_login(self, login):
        self.driver.find_element_by_id(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_id(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
        confirm_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id(self.INFO)
        )
        confirm_button.click()

class Top(Component):
    SMARTFEED = 'smartLink'
    CHAT = 'chatsLink'
    NOTIFICATIONS = 'notifLink'
    PROFILE = 'profileLink'

    def switch_to_smart_feed(self):
        self.driver.find_element_by_id(self.SMARTFEED).click()

    def switch_to_chat(self):
        self.driver.find_element_by_id(self.CHAT).click()

    def switch_to_notifications(self):
        self.driver.find_element_by_id(self.NOTIFICATIONS).click()

    def switch_to_profile(self):
        self.driver.find_element_by_id(self.PROFILE).click()

    def get_title(self):
        WebDriverWait(self.driver, 15, 0.1).until(
            lambda d: d.find_element_by_tag_name('title')
        )
        return self.driver.title

class Feed(Page):
    SMARTFEED = 'smartLink'

    def move_to_pin_page(self):
        WebDriverWait(self.driver, 20, 0.1).until(lambda d: d.find_element_by_xpath("//div[@id='columns']/div[@class='card'][1]/div/img")).click()

    def switch_to_smart(self):
        WebDriverWait(self.driver, 20, 0.1).until(lambda d: d.find_element_by_id(self.SMARTFEED)).click()


class Search_Page(Page):
    PATH = ''

    @property
    def line(self):
        return Search_Line(self.driver)

    #@property

class Search_Line(Component):

    SMARTFEED = 'smartLink'
    SEARCH_LINE = 'search_main_input'
    SEARCH_BUTTON = 'search_main_img'
    PIN_FILTER = "search_select_pin_vars"
    USER_FILTER = "search_select_user_vars"
    INFO = "main_page_info"

    @property
    def pin(self):
        return Pin(self.driver)

    def set_pin_filter(self):
        #sel = Select(self.driver.find_element_by_xpath("//ul[@class='search_submenu']"))
        frame = self.driver.find_element_by_xpath("//ul[@class='search_menu search_select']").click()
        self.driver.find_element_by_id('search_select_pin_vars').click()
        #frame.find_element_by_id(self.PIN_FILTER).click()
        #self.driver.find_element_by_id(self.PIN_FILTER)
        #sel.select_by_visible_text('Пины')

    def set_user_filter(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script('return window.SELENIUM_TEST_PASSES;')
        )
        WebDriverWait(self.driver, 15, 0.1).until(
            lambda d: d.find_element_by_xpath("//ul[@class='search_menu search_select']")).click()
        WebDriverWait(self.driver, 15, 0.1).until(
            lambda d: d.find_element_by_id(self.USER_FILTER)).click()

    def set_text(self, text):
        WebDriverWait(self.driver, 15, 0.1).until(
            lambda d: d.find_element_by_id(self.SEARCH_LINE)
        ).send_keys(text)

    def get_text(self):
        return WebDriverWait(self.driver, 15, 0.1).until(
            lambda d: d.find_element_by_id(self.SEARCH_LINE)
        ).get_attribute('value')

    def search(self):
        WebDriverWait(self.driver, 15, 0.1).until(
            lambda d: d.find_element_by_id(self.SEARCH_BUTTON)
        ).click()

    def get_info(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id(self.INFO).text
        )

    def switch_menu(self):
        self.driver.find_element_by_id(self.SMARTFEED).click()

class Pin(Component):

    def get_name_pin(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//div[@class='header']/h1").text
        )

    def get_author_pin(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//div[@class='author']/div").text
        )

    def click_on_author_name(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//div[@class='author']/div")
        ).click()

    def click_on_author_avatar(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//div[@class='author']/img")
        ).click()

    def click_on_save_pin(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//div[@class='up']/div/input")
        ).click()

    def save_pin(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//*[@id='saveChoosePin']")
        ).click()

    @property
    def comment(self):
        return Comment(self.driver)

    @property
    def share(self):
        return Share(self.driver)

class Comment(Component):

    def set_comment_text(self, text):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id("commentUser")
        ).send_keys(text)

    def send_comment(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id('sendComment')
        ).click()

    def get_amount_of_comments(self):
        parent =  WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id("commentBlock")
        )

        return len(parent.find_elements_by_xpath("//div[@class='comment_item']"))

class Share(Component):

    def open_form(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id('sharePinModal')
        ).click()

    def share_in_whatsapp(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//*[@id='modal']/div/div[2]/div[2]/a[1]/div")
        ).click()

    def share_in_twitter(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//*[@id='modal']/div/div[2]/div[2]/a[2]/div")
        ).click()

    def share_in_facebook(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//*[@id='modal']/div/div[2]/div[2]/a[3]/div")
        ).click()

    def get_share_url(self):
        self.driver.switch_to_window(self.driver.window_handles[-1])
        return self.driver.current_url


class PinAndCommentTest(unittest.TestCase):
    USERNAME = 'testuser'
    PASSWORD = 'testuser'
    PINNAME = 'Testpin'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        #browser = os.environ.get('BROWSER', 'CHROME')
        #self.driver = webdriver.Chrome('./chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test_move_to_pin_page(self):
        pp = PinPage(self.driver)
        pp.open_pin()

        self.assertEqual(pp.pin.get_name_pin(), self.PINNAME)

    def test_reload_pin_page(self):
        pp = PinPage(self.driver)
        pp.open_pin()
        pp.driver.refresh()

        self.assertEqual(pp.pin.get_name_pin(), self.PINNAME)

    def test_click_on_author_name(self):
        pp = PinPage(self.driver)
        pp.open_pin()

        pin = pp.pin
        name = pin.get_author_pin()
        pin.click_on_author_name()
        self.assertEqual(name, WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//*[@id='content']/div/div/div[3]/div[2]").text)
                         )

    def test_click_on_author_avatar(self):
        pp = PinPage(self.driver)
        pp.open_pin()

        pin = pp.pin
        name = pin.get_author_pin()
        pin.click_on_author_avatar()
        self.assertEqual(name, WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//*[@id='content']/div/div/div[3]/div[2]").text)
                         )

    def test_share_in_whatsapp(self):
        pp = PinPage(self.driver)
        pp.open_pin()

        share = pp.pin.share
        share.open_form()
        share.share_in_whatsapp()

        self.assertIn('whatsapp', share.get_share_url())

    def test_share_in_twitter(self):
        pp = PinPage(self.driver)
        pp.open_pin()

        share = pp.pin.share
        share.open_form()
        share.share_in_twitter()

        self.assertIn('twitter', share.get_share_url())

    def test_share_in_facebook(self):
        pp = PinPage(self.driver)
        pp.open_pin()

        share = pp.pin.share
        share.open_form()
        share.share_in_facebook()

        self.assertIn('facebook', share.get_share_url())

    def test_save_pin_by_authorized_user(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        pp = PinPage(self.driver)
        pp.open_pin()

        pin = pp.pin
        pin.click_on_save_pin()
        pin.save_pin()

        self.assertEqual(WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//*[@id='closeInfo']")).get_attribute('value'), "Ок")

    def test_save_pin_by_unauthorized_user(self):
        pp = PinPage(self.driver)
        pp.open_pin()

        pin = pp.pin
        pin.click_on_save_pin()

        self.assertEqual(WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//*[@id='modal']/div/div[2]/div[1]").text), "Авторизация")

    def test_write_comment_by_auth_user(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        pp = PinPage(self.driver)
        pp.open_pin()

        comment = pp.pin.comment

        before = comment.get_amount_of_comments()
        comment.set_comment_text('text')
        comment.send_comment()
        comment.driver.refresh()

        self.assertEqual(comment.get_amount_of_comments(), before + 1)

    def test_write_empty_comment_by_auth_user(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        pp = PinPage(self.driver)
        pp.open_pin()

        comment = pp.pin.comment

        before = comment.get_amount_of_comments()
        comment.set_comment_text('')
        comment.send_comment()
        comment.driver.refresh()

        self.assertEqual(comment.get_amount_of_comments(), before)

    def test_write_comment_by_unauth_user(self):
        pp = PinPage(self.driver)
        pp.open_pin()

        comment = pp.pin.comment

        before = comment.get_amount_of_comments()
        comment.set_comment_text('')
        comment.send_comment()
        comment.driver.refresh()

        self.assertEqual(comment.get_amount_of_comments(), before)

    def test_click_on_pin_on_main(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        feed = Feed(self.driver)
        feed.open()
        feed.move_to_pin_page()

        self.assertIn('pin', self.driver.current_url)

    def test_click_on_pin_on_smart(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        feed = Feed(self.driver)
        feed.open()
        feed.switch_to_smart()
        feed.move_to_pin_page()

        self.assertIn('pin', self.driver.current_url)

    def test_click_on_pin_on_main_by_unauth_user(self):
        feed = Feed(self.driver)
        feed.open()
        feed.move_to_pin_page()

        self.assertIn('pin', self.driver.current_url)


class SearchAndMenuTest(unittest.TestCase):
    USERNAME = 'testuser'
    PASSWORD = 'testuser'
    EMPTYSEARCHPIN = 'Пины не найдены'
    EMPTYSEARCHUSER = 'Пользователи не найдены'
    SMARTFEEDTITLE = 'Умная лента'
    NOTIFICATIONSTITLE = 'Notifications'
    CHATSTITLE = 'Chats'
    PROFILETITLE = 'Profile'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        #browser = os.environ.get('BROWSER', 'CHROME')
        # self.driver = webdriver.Chrome('./chromedriver')

        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

    def tearDown(self):
        self.driver.quit()

    def test_search_empty_pin(self):
        search_page = Search_Page(self.driver)
        search_page.open()

        search_line = search_page.line

        #search_line.set_pin_filter()
        search_line.set_text('')
        search_line.search()
        self.assertEqual(search_line.get_info(), self.EMPTYSEARCHPIN)

    def test_switch_to_smart_feed(self):
        top = Page(self.driver).top
        top.switch_to_smart_feed()

        self.assertEqual(top.get_title(), self.SMARTFEEDTITLE)

    def test_switch_to_chat(self):
        top = Page(self.driver).top
        top.switch_to_chat()

        self.assertEqual(top.get_title(), self.CHATSTITLE)

    def test_switch_to_notifications(self):
        top = Page(self.driver).top
        top.switch_to_notifications()

        self.assertEqual(top.get_title(), self.NOTIFICATIONSTITLE)

    def test_switch_to_profile(self):
        top = Page(self.driver).top
        top.switch_to_profile()

        self.assertEqual(top.get_title(), self.PROFILETITLE)

    def test_check_search_line(self):
        search_page = Search_Page(self.driver)
        search_page.open()

        search_line = search_page.line
        search_line.set_text('cake')
        search_line.search()
        search_line.switch_menu()

        self.assertEqual(search_line.get_text(), 'cake')

    def test_search_pin(self):
        search_page = Search_Page(self.driver)
        search_page.open()

        search_line = search_page.line
        search_line.set_text('testpin')
        search_line.search()

        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//div[@id='columns']/div[@class='card'][1]/div/img")).click()

        search_line.pin.get_name_pin()

    def test_search_user(self):
        search_page = Search_Page(self.driver)
        search_page.open()

        search_line = search_page.line

        search_line.set_text('testpin')
        search_line.search()

        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//div[@id='columns']/div[@class='card'][1]/div/img")).click()

        search_line.pin.get_name_pin()

'''
    def test_search_empty_user(self):
        search_page = Search_Page(self.driver)
        search_page.open()

        search_line = search_page.line

        search_line.set_pin_filter()
        search_line.set_text('')
        search_line.search()
        self.assertEqual(search_line.get_info(), self.EMPTYSEARCHUSER)     
'''










