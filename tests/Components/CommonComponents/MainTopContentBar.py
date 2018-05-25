# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait

from tests.Components.Component import Component


class MainTopContentBar(Component):
    NAVBAR_MENU = '//div[@class="mctc_navMenu "]'
    PHOTO_SEGMENT_IN_NAVBAR_MENU = '//a[@class="mctc_navMenuSec mctc_navMenuActiveSec"]'
    REDIRECT_CONFIRM = '//div[@class="photo-stream"]'

    def redirect_to_photo_section(self):
        self.driver.find_element_by_xpath(self.NAVBAR_MENU)\
            .find_element_by_xpath(self.PHOTO_SEGMENT_IN_NAVBAR_MENU).click()
        WebDriverWait(self.driver, 30, 2).until(
            lambda d: d.find_element_by_xpath(self.REDIRECT_CONFIRM)
        )
