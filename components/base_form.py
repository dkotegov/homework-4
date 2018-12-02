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
    SAVE_LETTER_BTN = '//span[@data-qa-id="save"]'
    CANCEL_LETTER_BTN = '//span[@data-qa-id="cancel"]'
    CLOSE_MSG_SENT_BTN = '//span[@data-qa-id="close"]'

    MSG_SENT_LINK = '//a[@data-qa-id="is-sent"]'
    DESTINATION_INPUT ='//input[@data-test-id="input"]'  # defines 1 element. First is needed
    CLOSE_MSG_SENT = '//div[@class="layer-window__block"]'
    MESSAGE_FIELD = '//div[@role="textbox"]/div/div'
    SUBJECT_FIELD = '//div[@data-test-id="subject"]'
    INCOMING_MSG_HREF = '//a[@data-qa-id="0"]'
    SENT_MSG_HREF = '//a[@data-qa-id="500000"]'
    DRAFT_MSG_HREF = '//a[@data-qa-id="500001"]'
    CLOSE_MSG_BTN ='//button[@data-test-id="close"]'
    ADD_COPY_EMAIL_BTN = '//button[@data-test-id="cc"]'
    COPY_FIELD = '//div[@data-test-id="cc"]'

    MSG_SUBJECT = '//a[@data-qa-id="letter-item:subject:{}"]'

    DESTINATION_MAIL = 'park.test.testovich@mail.ru\n'

    def set_destionation_email(self):
        try:
            dest_input = WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_elements_by_xpath(self.DESTINATION_INPUT))

            dest_input[0].send_keys(self.DESTINATION_MAIL)
            print 'destination email is set'
        except WebDriverException:
            print 'destination input not found'

    def add_destionation_email(self, destination_email):
        try:
            dest_input = WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_elements_by_xpath(self.DESTINATION_INPUT))

            dest_input[0].send_keys(destination_email)
            print 'destination email is added'
        except WebDriverException:
            print 'destination input not found'

    def open_writing_letter(self):
        try:
            WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.WRITING_LETTER_BTN))
            elem = self.driver.find_element_by_xpath(self.WRITING_LETTER_BTN)
            ActionChains(self.driver).move_to_element(elem).click().perform()
        except WebDriverException:
            print 'is not clickable element'

    def click_send_button(self):
        try:
            print 'clicking send message button'
            button = WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.SEND_LETTER_BTN))
            # button.click()
            ActionChains(self.driver).move_to_element(button).click().perform()
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

    def click_copy_button(self):
        try:
            print 'clicking copy email button'
            button = WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.ADD_COPY_EMAIL_BTN))
            button.click()
            print 'clicked!'
        except WebDriverException:
            print 'no copy email button'

    def click_incoming_emails_button(self):
        try:
            print 'clicking incoming emails button'
            button = WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.INCOMING_MSG_HREF))
            button.click()
            print 'clicked!'
        except WebDriverException:
            print 'no incoming emails button'

    def click_close_msg_sent_button(self):
        try:
            print 'clicking close msg sent button'
            button = WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.CLOSE_MSG_SENT_BTN))
            button.click()
            print 'clicked!'
        except WebDriverException:
            print 'no  close msg sent button'

    def checkMessageSent(self):
        try:
            WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.MSG_SENT_LINK))
            return True
        except WebDriverException, e:
            print 'exception ' + str(e)
            print 'message not sent'
            return False

    def closeMessageSent(self):
        try:
            print 'trying to close msg sent'
            elem = WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.CLOSE_MSG_SENT))
            ActionChains(self.driver).move_to_element(elem).click().send_keys(Keys.ESCAPE).perform()
        except WebDriverException:
            print 'msg_sent unable to close'

    # shit that does not work
    def show_message_incoming(self):
        try:
            elem = self.driver.find_element_by_xpath(self.INCOMING_MSG_HREF)
            ActionChains(self.driver).move_to_element(elem).click().perform()
        except WebDriverException:
            print 'Messages are unnable to open.'

    def show_message_sent(self):
        try:
            elem =  WebDriverWait(self.driver, 10) \
                .until(lambda driver: self.driver.find_element_by_xpath(self.SENT_MSG_HREF))
            ActionChains(self.driver).move_to_element(elem).click().perform()
        except WebDriverException:
            print 'Messages are unnable to open.'


    def show_message_draft(self):
        try:
            elem = self.driver.find_element_by_xpath(self.DRAFT_MSG_HREF)
            ActionChains(self.driver).move_to_element(elem).click().click().perform()
        except WebDriverException:
            print 'Drafts are unnable to open.'


    # Клик на поле ввода
    def click_on_message_field(self):
        element =  WebDriverWait(self.driver, 10) \
                .until(lambda driver: self.driver.find_element_by_xpath(self.MESSAGE_FIELD))
        ActionChains(self.driver).move_to_element(element).click().perform()

    # Клик на поле темы
    def click_on_subject_field(self):
        element =  WebDriverWait(self.driver, 10) \
                .until(lambda driver: self.driver.find_element_by_xpath(self.SUBJECT_FIELD))
        ActionChains(self.driver).move_to_element(element).click().perform()

    # Клик на поле копии письма
    def click_on_copy_field(self):
        element =  WebDriverWait(self.driver, 10) \
                .until(lambda driver: self.driver.find_element_by_xpath(self.COPY_FIELD))
        ActionChains(self.driver).move_to_element(element).click().perform()

    # Ввод текста
    def write_some_text(self, text):
        ActionChains(self.driver).key_down(text).perform()

    # Получение innerHTML элемента
    def get_text(self):
        return self.driver.find_element_by_xpath(self.MESSAGE_FIELD).get_attribute('innerHTML')

    def find_letter_by_subject(self, subject): 
        try:
            WebDriverWait(self.driver, 10) \
                .until(lambda driver: self.driver.find_element_by_xpath(self.MSG_SUBJECT.format(subject)))
            return True
        except WebDriverException:
            print 'not find letter with subject: ' + subject
            return False