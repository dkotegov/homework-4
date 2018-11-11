# coding=utf-8
import selenium
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import Component


class BaseForm(Component):
    # base elements
    WRITING_LETTER_BTN = '//span[@data-qa-id="compose"]'
    SEND_LETTER_BTN = '//span[@data-qa-id="send"]'

    MSG_SENT_LINK = '//a[@data-qa-id="is-sent"]'
    # DESTINATION_INPUT = '//div[@class="contactsContainer--3RMuQ"]/div/label/div/div/input'
    DESTINATION_INPUT = '//input[@data-test-id="input"]'  # defines 2 elements. First is needed
    # CLOSE_MSG_SENT = '//div[@class="layer__controls"]/span/span/span/*/*'
    CLOSE_MSG_SENT = '//div[@class="layer-window__block"]'

    SENT_MSG_HREF = '//div[@title="Отправленные"]'
    DRAFT_MSG_HREF = '//div[@title="Черновики"]'



    DESTINATION_MAIL = 'park.test.testovich@mail.ru'

    def set_destionation_email(self):
        try:
            dest_input = WebDriverWait(self.driver, 1) \
                .until(lambda driver: driver.find_elements_by_xpath(self.DESTINATION_INPUT)[0])
            dest_input.send_keys(self.DESTINATION_MAIL)
            print 'destination email is set'
        except WebDriverException:
            print 'destination input not found'

    def open_writing_letter(self):
        try:
            WebDriverWait(self.driver, 5) \
                .until(lambda driver: driver.find_element_by_xpath(self.WRITING_LETTER_BTN))
            elem = self.driver.find_element_by_xpath(self.WRITING_LETTER_BTN)
            ActionChains(self.driver).move_to_element(elem).click().perform()
        except WebDriverException:
            print 'is not clickable element'

    def click_send_button(self):

        try:
            print 'clicking send message button'
            button = WebDriverWait(self.driver, 1) \
                .until(lambda driver: driver.find_element_by_xpath(self.SEND_LETTER_BTN))
            button.click()
            print 'clicked!'
        except WebDriverException:
            print 'no send msg button'

    def click_cancel_button(self):
        try:
            elem=self.driver.find_element_by_xpath(self.CANCEL_LETTER_BTN)
            ActionChains(self.driver).move_to_element(elem).click().perform()
        except WebDriverException:
            print 'no cancel button'

    def click_save_button(self):
        try:
            elem=self.driver.find_element_by_xpath(self.SAVE_LETTER_BTN)
            ActionChains(self.driver).move_to_element(elem).click().perform()
        except WebDriverException:
            print 'no save msg button'

    def checkMessageSent(self):
        try:
            WebDriverWait(self.driver, 20) \
                .until(lambda driver: driver.find_element_by_xpath(self.MSG_SENT_LINK))
            return True
        except WebDriverException, e:
            print 'exception ' + str(e)
            print 'message not sent'
            return False

    def closeMessageSent(self):
        try:
            print 'trying to close msg sent'
            WebDriverWait(self.driver, 20) \
                .until(lambda driver: driver.find_element_by_xpath(self.CLOSE_MSG_SENT).send_keys(Keys.ESCAPE))
        except WebDriverException:
            print 'msg_sent unable to close'

