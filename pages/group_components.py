from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.page import Component, url_changer
from pages.photo_page import PhotoPage
from pages.settings_page import SettingsPage
from pages.waits import web_element_locator


class ConfirmModal(Component):
    CONFIRM = '//input[@name="button_delete"]'
    CANCEL = '//a[@data-l="t,cancel"]'

    @property
    @web_element_locator((By.XPATH, CONFIRM))
    def confirm_button(self):
        return self.driver.find_element_by_xpath(self.CONFIRM)

    @property
    @web_element_locator((By.XPATH, CANCEL))
    def cancel_button(self):
        return self.driver.find_element_by_xpath(self.CANCEL)

    def confirm(self):
        self.confirm_button.click()

    def cancel(self):
        self.cancel_button.click()


class LeftActionBar(Component):
    DELETE: str = '.ic_delete'
    SETTINGS: str = '//*[@id="hook_Block_LeftColumnTopCardAltGroup"]/ul/li[4]/a'

    @url_changer
    @web_element_locator((By.CSS_SELECTOR, DELETE))
    def delete(self):
        self.driver.execute_script('''
            document.querySelector('{}').click()
        '''.format(self.DELETE))
        ConfirmModal(self.driver).confirm()

    @property
    def to_settings_page(self) -> SettingsPage:
        path = self.settings.get_attribute('href')
        setting_page = SettingsPage(self.driver, path=path)
        setting_page.open()
        return setting_page

    @property
    @web_element_locator((By.XPATH, SETTINGS))
    def settings(self) -> WebElement:
        return self.driver.find_element_by_xpath(self.SETTINGS)


class MainNavBar(Component):
    PHOTO = '//a[@data-l="aid,NavMenu_AltGroup_Albums"]'

    @property
    def photo_page(self) -> PhotoPage:
        path = self.nav_photo.get_attribute('href')
        return PhotoPage(self.driver, path=path)

    @property
    @web_element_locator((By.XPATH, PHOTO))
    def nav_photo(self) -> WebElement:
        return self.driver.find_element_by_xpath(self.PHOTO)


class ApplicationPortlet(Component):
    APP_NAME = '//*[@id="hook_Block_AltGroupAppsPortletRB"]/div/div/div[2]/div/div/div/div[2]/div/div[1]'

    def __init__(self, driver, elem):
        super(ApplicationPortlet, self).__init__(driver)
        self.elem = elem

    def find_app(self, name):
        app = self.elem.find_element_by_xpath(self.APP_NAME)
        if app.text == name:
            return True
        return False

    @property
    @web_element_locator((By.XPATH, APP_NAME))
    def app(self) -> WebElement:
        return self.elem.find_element_by_xpath(self.APP_NAME)


class GroupPortlet(Component):
    GROUP_NAME = '//*[@id="altGroupsOfFriendsPanel"]'

    def check_presence_group(self, name):
        try:
            el = self.driver.find_element_by_xpath(self.GROUP_NAME)
        except WebDriverException:
            return None
        return el.find_element_by_link_text(name).text


class CreateTopicPopup(Component):
    MESSAGE = '//div[@data-module="postingForm/mediaText"]'
    SEND_BUTTON = 'posting_submit'
    TOPIC_POPUP = 'media-layer_close_ovr'

    def enter_message(self, msg: str):
        el = self.driver.find_element_by_xpath(self.MESSAGE)
        self.driver.execute_script('arguments[0].click()', el)
        self.driver.find_element_by_xpath(self.MESSAGE).send_keys(msg)

    def send(self):
        el = self.driver.find_element_by_xpath(self.MESSAGE)
        self.driver.execute_script('arguments[0].click()', el)
        el = self.driver.find_element_by_class_name(self.SEND_BUTTON)
        self.driver.execute_script('arguments[0].click();', el)


class CommentPopup(Component):
    MESSAGE = '//*[@id="ok-e-d"]'
    SEND_BUTTON = '//*[@id="ok-e-d_button"]'
    FIRST_COMMENT = 'd_comment_text'
    DISABLED_MESSAGE = 'disc_simple_input__im'
    POPLAYER = '//*[@id="hook_PopLayer_popLayer"]'

    def enter_message(self, msg: str):
        self.driver.find_element_by_xpath(self.MESSAGE).send_keys(msg)

    def send(self):
        self.driver.find_element_by_xpath(self.MESSAGE).click()
        self.driver.find_element_by_xpath(self.SEND_BUTTON).click()

    def save_id_comment(self):
        el = self.driver.find_element_by_class_name(self.FIRST_COMMENT)
        return el.find_element_by_tag_name("div").get_attribute('id')

    def find_comment_text(self):
        el = self.driver.find_element_by_class_name(self.FIRST_COMMENT)
        return el.find_element_by_tag_name("div").text

    def is_disabled_leave_comment_at_all(self):
        try:
            self.driver.find_element_by_class_name(self.DISABLED_MESSAGE)
        except WebDriverException:
            return False
        return True

    def is_disabled_leave_comments_not_members(self):
        try:
            self.driver.find_element_by_xpath(self.POPLAYER)
        except WebDriverException:
            return False
        return True
