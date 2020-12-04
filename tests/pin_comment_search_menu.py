import os
import unittest
from urllib.parse import urljoin
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import DesiredCapabilities, Remote, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
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
    PINID = os.environ['PIN_ID']
    PATH = '/pin/'

    def open_pin(self, pin_path=''):
        if pin_path == '':
            url = urljoin(super().BASE_URL, self.PATH + self.PINID)
        else:
            url = urljoin(super().BASE_URL, pin_path)
        self.driver.get(url)
        self.driver.maximize_window()

    @property
    def pin(self):
        return Pin(self.driver)


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN_ELEM = 'loginUser'
    PASSWORD_ELEM = 'passUser'
    SUBMIT = "//input[@value='Войти']"
    LOGIN_BUTTON = 'loginModal'
    INFO = 'closeInfo'
    TITLE = "title"

    def open_form(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id(self.LOGIN_BUTTON)
        ).click()

    def set_login(self, login):
        self.driver.find_element_by_id(self.LOGIN_ELEM).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_id(self.PASSWORD_ELEM).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
        confirm_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id(self.INFO)
        )
        confirm_button.click()

    def get_form_name(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_class_name(self.TITLE).text)


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
    PIN = "//div[@class='container']/img"

    def move_to_pin_page(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PIN)).click()

    def switch_to_smart(self):
        WebDriverWait(self.driver, 20, 0.1).until(lambda d: d.find_element_by_id(self.SMARTFEED)).click()


class SearchPage(Page):

    @property
    def line(self):
        return SearchLine(self.driver)


class SearchLine(Component):
    SMARTFEED = 'smartLink'
    SEARCH_LINE = 'search_main_input'
    SEARCH_BUTTON = 'search_main_img'
    LIST = "search_selected_obj"
    USER_FILTER = "search_select_user_vars"
    INFO = "main_page_info"
    USER = "find_user_login"
    PIN = "//div[@class='container']/img"

    @property
    def pin(self):
        return Pin(self.driver)

    def set_user_filter(self):
        array = WebDriverWait(self.driver, 15, 0.1).until(
            lambda d: d.find_element_by_id(self.LIST))
        elem = WebDriverWait(self.driver, 15, 0.1).until(
            lambda d: d.find_element_by_id(self.USER_FILTER))

        action = ActionChains(self.driver)
        action.move_to_element(array)
        action.move_to_element(elem)
        action.click().perform()

    def set_text(self, text):
        WebDriverWait(self.driver, 15, 0.1).until(
            lambda d: d.find_element_by_id(self.SEARCH_LINE)
        ).send_keys(text)

    def get_text(self):
        return WebDriverWait(self.driver, 15, 0.1).until(
            lambda d: d.find_element_by_id(self.SEARCH_LINE)
        ).get_attribute('value')

    def search(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            element_to_be_clickable((By.ID, self.SEARCH_BUTTON))
        ).click()

    def get_info(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id(self.INFO).text
        )

    def switch_menu(self):
        self.driver.find_element_by_id(self.SMARTFEED).click()

    def open_pin(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PIN)).click()

    def get_user_name(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_class_name(self.USER)).text


class Pin(Component):
    PINNAME = "//div[@class='header']/h1"
    AUTHORNAME = "//div[@class='author']/div"
    AUTHORAVATAR = "//div[@class='author']/img"
    SAVEFORM = "saveBtnModal"
    SAVEPIN = "saveChoosePin"
    SELECTNAME = '//*[@id="deskSelect"]'
    SELECTTAG = 'option'
    MESSAGE = "//*[@id='closeInfo']"

    def get_name_pin(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PINNAME).text
        )

    def get_author_pin(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.AUTHORNAME).text
        )

    def click_on_author_name(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.AUTHORNAME)
        ).click()

    def click_on_author_avatar(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.AUTHORAVATAR)
        ).click()

    def click_on_save_pin(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id(self.SAVEFORM)
        ).click()

    def save_pin(self):
        e = self.driver.find_element_by_xpath(self.SELECTNAME)
        WebDriverWait(e, 30, 0.1).until(lambda el: el.find_element_by_tag_name(self.SELECTTAG))
        elem = WebDriverWait(self.driver, 30, 0.1).until(EC.element_to_be_clickable((By.ID, self.SAVEPIN)))
        elem.click()
        return self.driver.current_url.split('/')[-1]

    def get_save_info(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MESSAGE)).get_attribute('value')

    @property
    def auth_form(self):
        return AuthForm(self.driver)

    @property
    def comment(self):
        return Comment(self.driver)

    @property
    def share(self):
        return Share(self.driver)

    @property
    def user(self):
        return User(self.driver)


class User(Component):
    USERNAME = "nickname"

    def get_name(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_class_name(self.USERNAME).text)


class Comment(Component):
    TEXTCOMMENTID = "commentUser"
    SENDCOMMENTID = 'sendComment'
    COMMENTS = 'commentBlock'
    COMMENTBLOCK = "//div[@class='comment_item']"
    COMMENT = "//*[@id='commentBlock']/div[%d]"

    def set_comment_text(self, text):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id(self.TEXTCOMMENTID)
        ).send_keys(text)

    def send_comment(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id(self.SENDCOMMENTID)
        ).click()

    def wait_new_comment(self, before):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.COMMENT % (before + 1)))

    def get_amount_of_comments(self):
        try:
            WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.COMMENT % 1))
            parent = WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_id(self.COMMENTS)
            )

            return len(parent.find_elements_by_xpath(self.COMMENTBLOCK))
        except TimeoutException:
            return 0


class Share(Component):
    SHAREID = 'sharePinModal'

    def open_form(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id(self.SHAREID)
        ).click()

    def share_in_service(self, name):
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"%s")]' % name)
                                       )).click()

    def new_window_is_exist(self):
        if len(self.driver.window_handles) > 1:
            return True
        return False


class PinTest(unittest.TestCase):
    USERNAME = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']
    PINURL = 'pin'
    INFOMESSAGE = 'Ок'
    LOGIN = 'Авторизация'
    TWITTER = 'twitter'
    WHATSAPP = 'whatsapp'
    FACEBOOK = 'facebook'
    MESSAGE = "//*[@id='closeInfo']"

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_reload_pin_page(self):
        pp = PinPage(self.driver)
        pp.open_pin()
        before = pp.pin.get_name_pin()
        pp.driver.refresh()

        self.assertEqual(pp.pin.get_name_pin(), before)

    def test_click_on_author_name(self):
        pp = PinPage(self.driver)
        pp.open_pin()

        pin = pp.pin
        name = pin.get_author_pin()
        pin.click_on_author_name()
        self.assertEqual(name, pin.user.get_name())

    def test_click_on_author_avatar(self):
        pp = PinPage(self.driver)
        pp.open_pin()

        pin = pp.pin
        name = pin.get_author_pin()
        pin.click_on_author_avatar()
        self.assertEqual(name, pin.user.get_name())

    def test_share_in_facebook(self):
        pp = PinPage(self.driver)
        pp.open_pin()

        share = pp.pin.share
        share.open_form()
        share.share_in_service('facebook')

        self.assertTrue(share.new_window_is_exist())

    def test_share_in_twitter(self):
        pp = PinPage(self.driver)
        pp.open_pin()

        share = pp.pin.share
        share.open_form()
        share.share_in_service('twitter')

        self.assertTrue(share.new_window_is_exist())

    def test_share_in_whatsapp(self):
        pp = PinPage(self.driver)
        pp.open_pin()

        share = pp.pin.share
        share.open_form()
        share.share_in_service('whatsapp')

        self.assertTrue(share.new_window_is_exist())

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

        self.assertEqual(pin.get_save_info(), self.INFOMESSAGE)

    def test_save_pin_by_unauthorized_user(self):
        pp = PinPage(self.driver)
        pp.open_pin()

        pin = pp.pin
        pin.click_on_save_pin()
        pin.auth_form.get_form_name()
        self.assertEqual(pin.auth_form.get_form_name(), self.LOGIN)

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

        self.assertIn(self.PINURL, self.driver.current_url)

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

        self.assertIn(self.PINURL, self.driver.current_url)

    def test_click_on_pin_on_main_by_unauth_user(self):
        feed = Feed(self.driver)
        feed.open()
        feed.move_to_pin_page()

        self.assertIn(self.PINURL, self.driver.current_url)


class CommentTest(unittest.TestCase):
    USERNAME = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']
    COMMENTMESSAGE = 'test'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

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
        comment.set_comment_text(self.COMMENTMESSAGE)
        comment.send_comment()
        comment.wait_new_comment(before)

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

        self.assertEqual(comment.get_amount_of_comments(), before)

    def test_write_comment_by_unauth_user(self):
        pp = PinPage(self.driver)
        pp.open_pin()

        comment = pp.pin.comment

        before = comment.get_amount_of_comments()
        comment.set_comment_text('')
        comment.send_comment()

        self.assertEqual(comment.get_amount_of_comments(), before)


class SearchTest(unittest.TestCase):
    USERNAME = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']
    TESTPIN = 'Testpin'
    EMPTYSEARCHPIN = 'Пины не найдены'
    EMPTYSEARCHUSER = 'Пользователи не найдены'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_search_empty_pin(self):
        search_page = SearchPage(self.driver)
        search_page.open()

        search_line = search_page.line

        search_line.set_text('')
        search_line.search()
        self.assertEqual(search_line.get_info(), self.EMPTYSEARCHPIN)

    def test_check_search_line(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        search_page = SearchPage(self.driver)
        search_page.open()

        search_line = search_page.line
        search_line.set_text(self.TESTPIN)
        search_line.search()
        search_line.switch_menu()

        self.assertEqual(search_line.get_text(), self.TESTPIN)

    def test_search_pin(self):
        search_page = SearchPage(self.driver)
        search_page.open()

        search_line = search_page.line
        search_line.set_text(self.TESTPIN)
        search_line.search()
        search_line.open_pin()

        self.assertEqual(self.TESTPIN, search_line.pin.get_name_pin())

    def test_search_user(self):
        search_page = SearchPage(self.driver)
        search_page.open()

        search_line = search_page.line

        search_line.set_user_filter()
        search_line.set_text(self.USERNAME)
        search_line.search()

        self.assertEqual(search_line.get_user_name(), self.USERNAME)


class MenuTest(unittest.TestCase):
    USERNAME = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']
    TESTPIN = 'Testpin'
    SMARTFEEDTITLE = 'Умная лента'
    NOTIFICATIONSTITLE = 'Notifications'
    CHATSTITLE = 'Chats'
    PROFILETITLE = 'Profile'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_switch_to_smart_feed(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        top = Page(self.driver).top
        top.switch_to_smart_feed()

        self.assertEqual(top.get_title(), self.SMARTFEEDTITLE)

    def test_switch_to_chat(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        top = Page(self.driver).top
        top.switch_to_chat()

        self.assertEqual(top.get_title(), self.CHATSTITLE)

    def test_switch_to_notifications(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        top = Page(self.driver).top
        top.switch_to_notifications()

        self.assertEqual(top.get_title(), self.NOTIFICATIONSTITLE)

    def test_switch_to_profile(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        top = Page(self.driver).top
        top.switch_to_profile()

        self.assertEqual(top.get_title(), self.PROFILETITLE)
