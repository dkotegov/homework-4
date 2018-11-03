# coding=utf-8
import selenium
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import Component


class BaseForm(Component):
    # base elements
    WRITING_LETTER = '//span[text()="Написать письмо"]'
    SEND_LETTER_BTN = '//button[@title="Отправить"]'

    def open_writing_letter(self):
        try:
            WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.WRITING_LETTER).click())
        except WebDriverException:
            print 'is not clickable element'

    def click_send_button(self):
        try:
            WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.SEND_LETTER_BTN).click())
        except WebDriverException:
            print 'no send msg button'
