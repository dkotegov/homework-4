import os

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from pages.default_page import DefaultPage, Component
from helpers import wait_for_element_by_selector, wait_for_element_by_xpath


class UserinfoPage(DefaultPage):
    URL = 'https://e.mail.ru/settings/userinfo'

    @property
    def form(self):
        return UserinfoForm(self.driver)


class UserinfoForm(Component):
    TOWN = 'input[name="your_town"]'
    SURNAME = 'input[name="LastName"]'            
    SAVE = 'div.form__actions__inner button[type="submit"]'
    TOP_MESSAGE = 'div.content__page > div.form__top-message.form__top-message_error > span'
    TOWN_ERROR = 'input[name="your_town"] ~ .form__message.form__message_error'
    SURNAME_ERROR = 'input[name="LastName"] ~ .form__message.form__message_error'
    SUGGESTS = '//*[@class="content__page"]/descendant::span[@class="div_inner ac-items form__field__suggest__inner"]'
    SUGGESTS_ITEM = '//form[@id="formPersonal"]//*[@class="form__field__suggest__item"]'
    GENDER_MALE = 'label[for="man1"] input'
    GENDER_FEMALE = 'label[for="man2"] input'

    def set_town(self, town):
        wait_for_element_by_selector(self.driver, self.TOWN)
        self.driver.find_element_by_css_selector(self.TOWN).send_keys(town)

    def set_surname(self, surname):
        wait_for_element_by_selector(self.driver, self.SURNAME)
        self.driver.find_element_by_css_selector(self.SURNAME).send_keys(surname)

    def save(self):
        wait_for_element_by_selector(self.driver, self.SAVE)
        self.driver.find_element_by_css_selector(self.SAVE).click()

    def get_top_message(self):
        wait_for_element_by_selector(self.driver, self.TOP_MESSAGE)
        return self.driver.find_element_by_css_selector(self.TOP_MESSAGE).text

    def get_town_message(self):
        wait_for_element_by_selector(self.driver, self.TOWN_ERROR)
        return self.driver.find_element_by_css_selector(self.TOWN_ERROR).text

    def get_surname_message(self):
        wait_for_element_by_selector(self.driver, self.SURNAME_ERROR)
        return self.driver.find_element_by_css_selector(self.SURNAME_ERROR).text

    def get_suggests_for_town(self):
        wait_for_element_by_xpath(self.driver, self.SUGGESTS_ITEM)
        suggests = self.driver.find_elements_by_xpath(self.SUGGESTS_ITEM)
        return [suggest.text for suggest in suggests]

    def wait_for_suggests_invisible(self):
        return wait_for_element_by_xpath(self.driver, self.SUGGESTS, False)

    def wait_for_last_suggest(self, text):
        locator = f'{self.SUGGESTS_ITEM}[last()]'
        return WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, locator), text)
        )

    def get_unselected_gender(self):
        wait_for_element_by_selector(self.driver, self.GENDER_MALE)
        gender_male = self.driver.find_element_by_css_selector(self.GENDER_MALE)
        wait_for_element_by_selector(self.driver, self.GENDER_FEMALE)
        gender_female = self.driver.find_element_by_css_selector(self.GENDER_FEMALE)
        return gender_female if gender_male.is_selected() else gender_male
