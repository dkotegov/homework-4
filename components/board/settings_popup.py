from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from base_classes.component import Component


class SettingsPopup(Component):
    CONTAINER = '//div[contains(@class, "board-settings")]'
    DELETE_BOARD_BUTTON = '//div[contains(@class, "js-deleteBoard")]'
    NAME_INPUT = '//input[@id = "js-boardTitleInput"]'
    SAVE_BUTTON = '//div[contains(@class, "js-saveBoard")]'
    CLOSE_BUTTON = '//*[name()="svg"]//*[name()="g" and contains(@class, "js-closeBoardSettingsButton")]'

    INVITE_LINK = '//input[@id = "js-inviteLink"]'
    COPY_LINK = '//div[contains(@class, "js-copyLink")]'
    GENERATE_LINK = '//div[contains(@class, "js-generateLink")]'

    def delete_board(self):
        self.driver.find_element_by_xpath(self.DELETE_BOARD_BUTTON).click()

    def close_popup(self):
        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

    def wait_for_visible(self):
        return WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(self.CONTAINER)
        )

    def change_name(self, new_name):
        self.driver.find_element_by_xpath(self.NAME_INPUT).clear()
        self.driver.find_element_by_xpath(self.NAME_INPUT).send_keys(new_name)
        self.driver.find_element_by_xpath(self.SAVE_BUTTON).click()

    def copy_link(self):
        self.driver.find_element_by_xpath(self.COPY_LINK).click()

    def generate_link(self):
        self.driver.find_element_by_xpath(self.GENERATE_LINK).click()

    def get_link_text(self):
        return self.driver.find_element_by_xpath(self.INVITE_LINK).get_attribute('value')
