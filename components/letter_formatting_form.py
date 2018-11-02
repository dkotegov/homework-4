# coding=utf-8
import selenium
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import Component


class LetterFormattingForm(Component):
    BOLD_BUTTON = '//button[@title="Жирный текст"]'
    WRITING_LETTER = '//span[text()="Написать письмо"]'
    MESSAGE_FIELD = '//div[@role="textbox"]/div/div'

    def open_writing_letter(self):
        try:
            WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.WRITING_LETTER).click())
        except WebDriverException:
            print 'is not clickable element'

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
