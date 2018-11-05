# coding=utf-8
import selenium
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import Component


class BaseForm(Component):
    # base elements
    WRITING_LETTER_BTN = '//span[text()="Написать письмо"]'
    SEND_LETTER_BTN = '//span[@title="Отправить"]'
    MSG_SENT_DIV = '//div[@class="layer__header"]'
    DESTINATION_INPUT = '//div[@class="contactsContainer--3RMuQ"]/div/label/div/div/input'
    # CLOSE_MSG_SENT = '//div[@class="layer__controls"]/span/span/span/*/*'
    CLOSE_MSG_SENT = '//div[@class="layer-window__block"]'

    DESTINATION_MAIL = 'park.test.testovich@mail.ru'

    def set_destionation_email(self):
        try:
            dest_input = WebDriverWait(self.driver, 5) \
                .until(lambda driver: driver.find_element_by_xpath(self.DESTINATION_INPUT))
            dest_input.send_keys(self.DESTINATION_MAIL)
        except WebDriverException:
            print 'destination input not found'

    def open_writing_letter(self):
        try:
            WebDriverWait(self.driver, 50) \
                .until(lambda driver: driver.find_element_by_xpath(self.WRITING_LETTER_BTN).click())
        except WebDriverException:
            print 'is not clickable element'

    def click_send_button(self):

        try:
            WebDriverWait(self.driver, 5) \
                .until(lambda driver: driver.find_element_by_xpath(self.SEND_LETTER_BTN).click())

        except WebDriverException:
            print 'no send msg button'

    def checkMessageSent(self):
        try:
            WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.MSG_SENT_DIV))
            return True
        except WebDriverException:
            print 'message not sent'
            return False

    def closeMessageSent(self):
        try:
            print 'trying to close msg sent'
            WebDriverWait(self.driver, 20) \
            .until(lambda driver: driver.find_element_by_xpath(self.CLOSE_MSG_SENT).send_keys(Keys.ESCAPE))
        except WebDriverException:
            print 'msg_sent unable to close'
