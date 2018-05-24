from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.group_components import ApplicationPortlet, CommentPopup, CreateTopicPopup, GroupPortlet, LeftActionBar, \
    MainNavBar
from pages.page import Page
from pages.photo_page import PhotoPage
from pages.settings_page import SettingsPage


class GroupPage(Page):
    JOIN_BUTTON = '//*[@id="hook_Block_LeftColumnTopCardAltGroup"]/ul/div[2]/a'
    DROPDOWN_BUTTON = '//*[@id="hook_Block_LeftColumnTopCardAltGroup"]/ul/div[2]/div[1]/span'
    UNJOIN_BUTTON_CLASS = 'dropdown_cnt'
    NAME_TEXT = '//*[@id="hook_Block_MiddleColumnTopCardAltGroup"]/div[2]/div/div[1]/div/span/h1'
    DESCRIPTION_TEXT = '//*[@id="hook_Block_MiddleColumnTopCardAltGroup"]/div[2]/div/div[2]/div[1]/div[2]'
    CATEGORY_TEXT = '//*[@id="hook_Block_MiddleColumnTopCardAltGroup"]/div[2]/div/div[2]/div[1]/div[1]'
    APPLICATION_PORTLET = '//*[@id="hook_Block_AltGroupAppsPortletRB"]/div'
    CREATE_NEW_TOPIC = 'input_placeholder'
    COMMENT_DIALOG = 'mdialog_chat_window_cnt'
    COMMENT = '//a[@data-location="WideFeed_FeedItem_CommentWidget"]'

    @property
    def left_action_bar(self) -> LeftActionBar:
        return LeftActionBar(self.driver)

    @property
    def main_nav_bar(self) -> MainNavBar:
        return MainNavBar(self.driver)

    def create_topic_popup(self):
        return CreateTopicPopup(self.driver)

    def comment_popup(self):
        el = self.driver.find_element_by_xpath(self.COMMENT)
        self.driver.execute_script("arguments[0].click()", el)
        popup = CommentPopup(self.driver)
        return popup

    def to_photo_page(self) -> PhotoPage:
        photo_page = self.main_nav_bar.photo_page
        photo_page.open()
        return photo_page

    def to_settings_page(self) -> SettingsPage:
        setting_page = self.left_action_bar.to_settings_page
        return setting_page

    def delete_group(self):
        self.open()
        self.left_action_bar.delete()

    def join(self):
        self.driver.find_element_by_xpath(self.JOIN_BUTTON).click()
        return self

    def unjoin(self):
        # self.driver.execute_script(
        #     "document.getElementsByClassName('{}')[0].style.display = 'block';".format(self.UNJOIN_BUTTON_CLASS))
        # self.driver.find_elements_by_class_name(self.UNJOIN_BUTTON_CLASS).click()
        self.driver.find_element_by_xpath(self.DROPDOWN_BUTTON).click()
        unjoin_button = self.driver.find_element_by_class_name(self.UNJOIN_BUTTON_CLASS)
        unjoin_button.click()
        return self

    def get_name(self):
        return self.driver.find_element_by_xpath(self.NAME_TEXT).text

    def get_description(self):
        return self.driver.find_element_by_xpath(self.DESCRIPTION_TEXT).text

    def get_category(self):
        return self.driver.find_element_by_xpath(self.CATEGORY_TEXT).text

    def get_type(self):
        return self.driver.find_element_by_xpath(self.TYPE_TEXT).text

    def is_app_added(self, name):
        portlet = self.driver.find_element_by_xpath(self.APPLICATION_PORTLET)
        return ApplicationPortlet(self.driver, portlet).find_app(name)

    def is_group_added(self, name):
        portlet = GroupPortlet(self.driver)
        return portlet.check_presence_group(name)

    def create_post(self, msg: str):
        self.driver.find_element_by_class_name(self.CREATE_NEW_TOPIC).click()
        popup = self.create_topic_popup()
        popup.enter_message(msg)
        popup.send()

    def create_comment(self, msg: str):
        popup = self.comment_popup()
        popup.enter_message(msg)
        popup.send()
        return popup.save_id_comment()

    def get_comment_message(self):
        self.driver.find_element_by_xpath(self.COMMENT).click()
        popup = self.comment_popup()
        return popup.find_comment_text()

    def open_comment_popup(self):
        return self.comment_popup()

    def check_presence_section(self, section: str):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, section)))
        except TimeoutException as e:
            return False
        return True
