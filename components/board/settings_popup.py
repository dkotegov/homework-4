from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from base_classes.component import Component
from components.board.settingc_search_from import SearchForm


class SettingsPopup(Component):
    CONTAINER = '//div[@class = "board-settings"]'
    DELETE_BOARD_BUTTON = '//div[contains(@class, "js-deleteBoard")]'
    NAME_INPUT = '//input[@id = "js-boardTitleInput"]'
    SAVE_BUTTON = '//div[contains(@class, "js-saveBoard")]'
    CLOSE_BUTTON = '//*[name()="svg"]//*[name()="g" and contains(@class, "js-closeBoardSettingsButton")]'

    INVITE_LINK = '//input[@id = "js-inviteLink"]'
    COPY_LINK = '//div[contains(@class, "js-copyLink")]'
    GENERATE_LINK = '//div[contains(@class, "js-generateLink")]'

    ADD_MEMBER = '//img[contains(@class, "js-findMember")]'
    MEMBER = '//div[contains(@class, "js-foldUnfoldUserInfo")]'
    MEMBER_NICK = '//div[contains(@class,"board-settings-members__options--profile-info")' \
                  ' and not(contains(@class,"board-settings-members__options--profile-info-and-actions"))]'

    @property
    def search_form(self):
        return SearchForm(self.driver)

    def delete_board(self):
        self.driver.find_element_by_xpath(self.DELETE_BOARD_BUTTON).click()

    def get_board_title(self) -> str:
        return self.driver.find_element_by_xpath(self.NAME_INPUT).get_attribute('value')

    def close_popup(self):
        WebDriverWait(self.driver, 5, 0.5).until(
            lambda d: d.find_element_by_xpath(self.CLOSE_BUTTON)
        )
        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

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

    def invite_member(self, nickname):
        self.driver.find_element_by_xpath(self.ADD_MEMBER).click()

        self.search_form.wait_for_container()
        self.search_form.set_input(nickname)
        self.search_form.wait_for_search_results()
        self.search_form.add_to_board(0)

    def get_members_count(self):
        WebDriverWait(self.driver, 5, 0.5).until(
            lambda d: self.driver.find_elements_by_xpath(self.MEMBER)
        )
        return len(self.driver.find_elements_by_xpath(self.MEMBER))

    def open_member(self, number):
        WebDriverWait(self.driver, 5, 0.5).until(
            lambda d: self.driver.find_elements_by_xpath(self.MEMBER)
        )
        self.driver.find_elements_by_xpath(self.MEMBER)[number].click()

    def get_member_nickname(self, number):
        WebDriverWait(self.driver, 5, 0.5).until(
            lambda d: self.driver.find_elements_by_xpath(self.MEMBER_NICK)
        )
        return self.driver.find_elements_by_xpath(self.MEMBER_NICK)[number].text.replace('@', '', 1)
