from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from tests.pages.primary.component import Component
from tests.pages.primary.components.photos.toolbar import PhotoToolbar
from util import config


class PhotoComponent(Component):
    PHOTO_BUTTON_XPATH = '//div[contains(@class, "photo-card")][contains(@data-l, "photoCardPlace")]/a'
    PHOTO_CLOSE_BUTTON_XPATH = '//div[contains(@class, "js-photoLayerClose")][contains(@data-l, "t,close")]'

    PHOTO_GET_LINK = 'showLink'
    PHOTO_LINK_FIELD_ID = 'showLinkInput'

    PHOTO_SET_MAIN_XPATH = '//div[@id="hook_Block_QuickSetProfilePhoto"]/span[contains(@class, "h-mod")]' \
                           '[@data-module="utils/requireBlock"]'
    PHOTO_SET_MAIN_BUTTON_XPATH = '//button[@name="button_plpscp_confirm"]'

    VALUE_ATTR = 'value'

    def get_photo_link(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.ID, self.PHOTO_GET_LINK)))
        self.driver.find_element_by_id(self.PHOTO_GET_LINK).click()
        return self.driver.find_element_by_id(self.PHOTO_LINK_FIELD_ID).get_attribute(self.VALUE_ATTR)

    def open_overlay(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.PHOTO_BUTTON_XPATH)))
        self.driver.find_element_by_xpath(self.PHOTO_BUTTON_XPATH).click()

    def close_overlay(self):
        self.driver.find_element_by_xpath(self.PHOTO_CLOSE_BUTTON_XPATH).click()

    def set_as_avatar(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.PHOTO_SET_MAIN_XPATH)))
        self.driver.find_element_by_xpath(self.PHOTO_SET_MAIN_XPATH).click()
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.PHOTO_SET_MAIN_BUTTON_XPATH)))
        self.driver.find_element_by_xpath(self.PHOTO_SET_MAIN_BUTTON_XPATH).click()
        self.driver.implicitly_wait(config.WAITING_TIME)

    def toolbar(self):
        return PhotoToolbar(self.driver)
