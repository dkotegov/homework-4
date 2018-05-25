from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from tests.pages.primary.page import Page

from util import config


class MainPage(Page):
    AVATAR_LINK_XPATH = '//div[contains(@class, "lcTc_avatar")]/a[@class="card_wrp"]'
    MAIN_PAGE_A_XPATH = '//a[contains(@class, "compact-profile_a")]'

    PHOTO_PAGE_A_XPATH = '//a[contains(@href, "/photos")][contains(@hrefattrs, "_aid=NavMenu_User_Photos")]'

    def get_avatar(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.AVATAR_LINK_XPATH)))
        self.driver.find_element_by_xpath(self.AVATAR_LINK_XPATH).click()

    def goto(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.MAIN_PAGE_A_XPATH)))
        self.driver.find_element_by_xpath(self.MAIN_PAGE_A_XPATH).click()
        self.driver.implicitly_wait(config.WAITING_TIME)

    def goto_photo(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.PHOTO_PAGE_A_XPATH)))
        self.driver.find_element_by_xpath(self.PHOTO_PAGE_A_XPATH).click()
        self.driver.implicitly_wait(config.WAITING_TIME)
