# coding=utf-8
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from tests.Lilbs.Lib import Lib
from tests.constants.Constants import waitTime
from tests.models.Component import Component
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class TopMenu(Component):
    NOTIFICATION_TOOLBAR = '//ul[@class="toolbar_nav"]//li[@data-l="t,notifications"]'
    FRIENDS_TOOLBAR = '//ul[@class="toolbar_nav"]//li[@data-l="t,friends"]'

    NOTIFICATION_CONTAINER = '//div[@class="notifs_cnt"]'
    NOTIFICATION_TAB_TITLE = '//*[@id="hook_Block_NotificationsLayerTitle"]/div'
    NOTIFICATION_TAB_CONTENT = '//*[@id="hook_Block_NotificationsLayerContent"]'

    FIRST_ACCOUNT_NAME = '//ul[@class="ugrid_cnt"]//li//div[@class="ellip"]//a[text()="Name Female"]'
    INVITE_TO_GROUP = '//div[@class="gwt-shortcutMenu-content"]//ul//li[@class="ic_group"]//a'
    GROUP_TO_INVITE = '//div[@id="hook_Block_InviteUserToGroup2GroupsList"]//div[@class="ugrid_i"]//a'

    NOTIFICATION_ELEMENT = '//div[@id="ntf_layer_content_inner"]/div[position() = 1]'
    NOTIFICATION_ELEMENT_WITH_ID = NOTIFICATION_ELEMENT + '/div'
    NOTIFICATION_REPORT = NOTIFICATION_ELEMENT + '//div[@class="notif_ac fade-on-hover"]//i[@data-l="t,spam"]'
    NOTIFICATION_REPORT_SPAM = NOTIFICATION_ELEMENT + '//div[@class="notif_ac fade-on-hover"]//div[@data-l="t,shortcutMenu"]//a'
    NOTIFICATION_REMOVED = NOTIFICATION_ELEMENT + '//div[@data-module="NotificationRemoved"]'

    NOTIFICATION_BUTTON_CLOSE = NOTIFICATION_ELEMENT + '//button[@data-l="t,btn_ignore"]'

    NOTIFICATION_TABS = ['//*[@id="ntf_layer_menu_link_All"]/span',
                         '//*[@id="ntf_layer_menu_link_Friendships"]/span[1]',
                         '//*[@id="ntf_layer_menu_link_Presents"]',
                         '//*[@id="ntf_layer_menu_link_Groups"]',
                         '//*[@id="ntf_layer_menu_link_Games"]/span[1]',
                         '//*[@id="ntf_layer_menu_link_Payments"]',
                         '//*[@id="ntf_layer_menu_link_Video"]',
                         '//*[@id="ntf_layer_menu_link_Other"]']

    def select_notification(self):
        Lib.simple_wait_element(self.driver, self.NOTIFICATION_TOOLBAR).click()
        Lib.simple_wait_element(self.driver, self.NOTIFICATION_CONTAINER)

    def select_friends(self):
        Lib.simple_wait_element(self.driver, self.FRIENDS_TOOLBAR).click()

    def invite_to_group(self):
        element = Lib.simple_wait_element(self.driver, self.FIRST_ACCOUNT_NAME)
        Lib.hover(self.driver, element)
        Lib.visibility_wait_element(self.driver, self.INVITE_TO_GROUP).click()
        Lib.simple_wait_elements(self.driver, self.GROUP_TO_INVITE)[0].click()

    def report_notification(self):
        self.wait_process_after_choose_tab()

        element = Lib.simple_wait_element(self.driver, self.NOTIFICATION_ELEMENT)
        Lib.hover(self.driver, element)
        Lib.visibility_wait_element(self.driver, self.NOTIFICATION_REPORT).click()
        Lib.visibility_wait_element(self.driver, self.NOTIFICATION_REPORT_SPAM).click()

    def place_first_notification(self):
        return Lib.simple_wait_element(self.driver, self.NOTIFICATION_REMOVED).text

    def close_notification(self):
        self.wait_process_after_choose_tab()

        Lib.simple_wait_element(self.driver, self.NOTIFICATION_ELEMENT_WITH_ID)
        Lib.simple_wait_element(self.driver, self.NOTIFICATION_BUTTON_CLOSE).click()

    def check_notification_close(self):
        self.wait_process_after_choose_tab()
        return Lib.check_exist_element(self.driver, self.NOTIFICATION_ELEMENT_WITH_ID)

    def wait_process_after_choose_tab(self):
        try:
            Lib.wait_element_with_attribute(self.driver, True, self.NOTIFICATION_TAB_CONTENT, "__process")
        except TimeoutException:
            pass

        try:
            Lib.wait_element_with_attribute(self.driver, False, self.NOTIFICATION_TAB_CONTENT, "__process")
        except TimeoutException:
            pass

    def choose_tab_notification(self, index):
        Lib.simple_get_element(self.driver, self.NOTIFICATION_TABS[index]).click()
        self.wait_process_after_choose_tab()

    def get_tab_content_title(self):
        return Lib.visibility_wait_element(self.driver, self.NOTIFICATION_TAB_TITLE).text
