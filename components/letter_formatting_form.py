# coding=utf-8
import selenium
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from components.base_form import BaseForm


class LetterFormattingForm(BaseForm):

    # text formatting elements
    BOLD_BUTTON = '//button[@title="Жирный текст"]'
    MESSAGE_FIELD = '//div[@role="textbox"]/div/div'

    def click_on_bold_icon(self):
        self.driver.find_element_by_xpath(self.BOLD_BUTTON).click()

    def write_some_text(self, text):
        self.driver.find_element_by_xpath(self.MESSAGE_FIELD).click()
        ActionChains(self.driver).key_down(text).perform()
        # self.driver.execute_script(
        #     "document.evaluate('//div[@role=\"textbox\"]/div/div', "
        #     "document, null, 9, null).singleNodeValue.innerHTML=\'helloushki\'")

    def get_text(self):
        return self.driver.find_element_by_xpath(self.MESSAGE_FIELD).get_attribute('innerHTML')

    def text_selection(self):
        self.driver.find_element_by_xpath(self.MESSAGE_FIELD).click()
        ActionChains(self.driver).key_down(Keys.LEFT_CONTROL).perform()
        ActionChains(self.driver).key_down(Keys.LEFT_SHIFT).perform()
        ActionChains(self.driver).key_down(Keys.LEFT).perform()
