from tests.components.component import Component

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class MainForm(Component):
    NAME_INPUT = '//input[@id="signup-field__fname-input"]'
    NAME_ERROR = '//div[@id="signup-field__fname-input-wrapper_err"]'
    RECOMMENDATION_ITEMS = '//div[@class="recommend-bar__list"]'
    REST_ITEM = '//div[@id="restaurant-list"]/div'
    RESTS = '//div[@id="restaurant-list"]'
    RESTAURANTS_LIST = '//div[@id="restaurant-list"]/div/a/div/div[@class="restaurant__info"]/span[@class="restaurant__name"]'
    RECOMMENDATION_LIST = '//div[@class="recommend-bar__list"]/div/a/div/div[@class="restaurant__info"]/span[@class="restaurant__name"]'
    TAGS_LIST = '//div[@class="category-bar"]'
    TAG = '//button[@id="category_{}"]'

    def wait_open(self):
        return WebDriverWait(self.driver, 5).until(
            lambda d: d.find_element_by_xpath(self.RECOMMENDATION_ITEMS).is_displayed()
        )

    def wait_restaurants(self):
        return WebDriverWait(self.driver, 5).until(
            lambda d: len(d.find_elements_by_xpath(self.REST_ITEM)) > 0
        )

    # def set_name(self, name):
    #     self.driver.find_element_by_xpath(self.NAME_INPUT).send_keys(name)
    #
    # def get_name_error(self):
    #     curr_error = self.driver.find_element_by_xpath(self.NAME_ERROR).text
    #     WebDriverWait(self.driver, 30, 1).until(
    #         lambda d: d.find_element_by_xpath(self.NAME_ERROR).text == curr_error
    #                   and
    #                   d.find_element_by_xpath(self.NAME_ERROR).text != ''
    #     )
    #     return self.driver.find_element_by_xpath(self.NAME_ERROR).text
    #
    # def get_name(self):
    #     return self.driver.find_element_by_xpath(self.NAME_INPUT).get_attribute('value')
    #
    # def set_surname(self, surname):
    #     self.driver.find_element_by_xpath(self.SURNAME_INPUT).send_keys(surname)
    #
    # def get_surname_error(self):
    #     curr_error = self.driver.find_element_by_xpath(self.SURNAME_ERROR).text
    #     WebDriverWait(self.driver, 30, 1).until(
    #         lambda d: d.find_element_by_xpath(self.SURNAME_ERROR).text != curr_error
    #                   and
    #                   d.find_element_by_xpath(self.SURNAME_ERROR).text != ''
    #     )
    #     return self.driver.find_element_by_xpath(self.SURNAME_ERROR).text
    #
    # def get_surname(self):
    #     return self.driver.find_element_by_xpath(self.SURNAME_INPUT).get_attribute('value')
    #
    # def set_phone(self, email):
    #     self.driver.find_element_by_xpath(self.PHONE_INPUT).send_keys(email)
    #
    # def get_phone_error(self):
    #     WebDriverWait(self.driver, 30, 1).until(
    #         lambda d: d.find_element_by_xpath(self.PHONE_ERROR).text != ''
    #     )
    #     return self.driver.find_element_by_xpath(self.PHONE_ERROR).text
    #
    # def get_phone(self):
    #     return self.driver.find_element_by_xpath(self.PHONE_INPUT).get_attribute('value')
    #
    # def set_password1(self, email):
    #     self.driver.find_element_by_xpath(self.PASSWORD1_INPUT).send_keys(email)
    #
    # def get_password1_error(self):
    #     WebDriverWait(self.driver, 30, 1).until(
    #         lambda d: d.find_element_by_xpath(self.PASSWORD1_ERROR).text != ''
    #     )
    #     return self.driver.find_element_by_xpath(self.PASSWORD1_ERROR).text
    #
    # def get_password1(self):
    #     return self.driver.find_element_by_xpath(self.PASSWORD1_INPUT).get_attribute('value')
    #
    # def set_password2(self, email):
    #     self.driver.find_element_by_xpath(self.PASSWORD2_INPUT).send_keys(email)
    #
    # def get_password2_error(self):
    #     WebDriverWait(self.driver, 30, 1).until(
    #         lambda d: d.find_element_by_xpath(self.PASSWORD2_ERROR).text != ''
    #     )
    #     return self.driver.find_element_by_xpath(self.PASSWORD2_ERROR).text
    #
    # def get_password2(self):
    #     return self.driver.find_element_by_xpath(self.PASSWORD2_INPUT).get_attribute('value')
    #
    # def get_confirm_error(self):
    #     WebDriverWait(self.driver, 30, 1).until(
    #         lambda d: d.find_element_by_xpath(self.CONFIRM_ERROR).text != ''
    #     )
    #     return self.driver.find_element_by_xpath(self.CONFIRM_ERROR).text
    #
    # def register(self):
    #     self.driver.find_element_by_xpath(self.REGISTER_BUTTON).click()

    def get_recommendations(self):
        WebDriverWait(self.driver, 5).until(
            lambda d: d.find_element_by_xpath(self.RECOMMENDATION_LIST).is_displayed()
        )
        return self.driver.find_elements_by_xpath(self.RECOMMENDATION_LIST)

    def get_restaurants(self):
        WebDriverWait(self.driver, 5).until(
            lambda d: d.find_element_by_xpath(self.RESTAURANTS_LIST).is_displayed()
        )
        return self.driver.find_elements_by_xpath(self.RESTAURANTS_LIST)

    def set_tag(self, tag_id):
        WebDriverWait(self.driver, 5).until(
            lambda d: d.find_element_by_xpath(self.TAGS_LIST).is_displayed()
        )
        self.driver.find_element_by_xpath(self.TAGS_LIST).find_element_by_xpath(self.TAG.format(tag_id)).click()    

    def get_tag_button_by_name(self, tag_name):
        return self.driver.find_element_by_xpath('//button[./span[contains(text(), "{}")]]'.format(tag_name))
