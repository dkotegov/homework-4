# coding=utf-8
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from components.base_component import Component


class BaseForm(Component):
    # base elements
    WRITING_LETTER_BTN = '//span[@data-qa-id="compose"]'
    SEND_LETTER_BTN = '//span[@data-qa-id="send"]'
    SAVE_LETTER_BTN = '//span[@data-qa-id="save"]'
    CANCEL_LETTER_BTN = '//span[@data-qa-id="cancel"]'
    CLOSE_MSG_SENT_BTN = '//span[@data-qa-id="close"]'

    MSG_SENT_LINK = '//a[@data-qa-id="is-sent"]'
    DESTINATION_INPUT = '//input[@data-test-id="input"]'
    CLOSE_MSG_SENT = '//div[@class="layer-window__block"]'
    MESSAGE_FIELD = '//div[@role="textbox"]/div/div'
    SUBJECT_FIELD = '//div[@data-test-id="subject"]'
    INCOMING_MSG_HREF = '//a[@data-qa-id="0"]'
    SENT_MSG_HREF = '//a[@data-qa-id="500000"]'
    DRAFT_MSG_HREF = '//a[@data-qa-id="500001"]'
    CLOSE_MSG_BTN = '//button[@data-test-id="close"]'
    ADD_COPY_EMAIL_BTN = '//button[@data-test-id="cc"]'
    COPY_FIELD = '//div[@data-test-id="cc"]'
    MSG_SUBJECT = '//a[@data-qa-id="letter-item:subject:{}"]'
    DESTINATION_MAIL = 'park.test.testovich@mail.ru\n'

    def set_destionation_email(self):
        dest_input = WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_elements_by_xpath(self.DESTINATION_INPUT))
        dest_input[0].send_keys(self.DESTINATION_MAIL)

    def add_destionation_email(self, destination_email):
        dest_input = WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_elements_by_xpath(self.DESTINATION_INPUT))
        dest_input[0].send_keys(destination_email)

    def open_writing_letter(self):
        WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element_by_xpath(self.WRITING_LETTER_BTN))
        elem = self.driver.find_element_by_xpath(self.WRITING_LETTER_BTN)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    def click_send_button(self):
        button = WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element_by_xpath(self.SEND_LETTER_BTN))
        ActionChains(self.driver).move_to_element(button).click().perform()

    def click_cancel_button(self):
        elem = self.driver.find_element_by_xpath(self.CANCEL_LETTER_BTN)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    def click_save_button(self):
        elem = self.driver.find_element_by_xpath(self.SAVE_LETTER_BTN)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    def click_copy_button(self):
        button = WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element_by_xpath(self.ADD_COPY_EMAIL_BTN))
        button.click()

    def click_incoming_emails_button(self):
        button = WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element_by_xpath(self.INCOMING_MSG_HREF))
        button.click()

    def click_close_msg_sent_button(self):
        button = WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element_by_xpath(self.CLOSE_MSG_SENT_BTN))
        button.click()

    def checkMessageSent(self):
        try:
            WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.MSG_SENT_LINK))
            return True
        except WebDriverException, e:
            return False

    def closeMessageSent(self):
        elem = WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element_by_xpath(self.CLOSE_MSG_SENT))
        ActionChains(self.driver).move_to_element(elem).click().send_keys(Keys.ESCAPE).perform()

    # shit that does not work
    def show_message_incoming(self):
        elem = self.driver.find_element_by_xpath(self.INCOMING_MSG_HREF)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    def show_message_sent(self):
        elem = WebDriverWait(self.driver, 10) \
            .until(lambda driver: self.driver.find_element_by_xpath(self.SENT_MSG_HREF))
        ActionChains(self.driver).move_to_element(elem).click().perform()

    def show_message_draft(self):
        elem = self.driver.find_element_by_xpath(self.DRAFT_MSG_HREF)
        ActionChains(self.driver).move_to_element(elem).click().click().perform()

    def click_cancel_writing_message(self):
        cancel_btn = self.driver.find_element_by_xpath(self.CANCEL_LETTER_BTN)
        cancel_btn.click()
        WebDriverWait(self.driver, 2) \
            .until(ES.invisibility_of_element(cancel_btn))

    # Клик на поле ввода
    def click_on_message_field(self):
        element = WebDriverWait(self.driver, 10) \
            .until(lambda driver: self.driver.find_element_by_xpath(self.MESSAGE_FIELD))
        ActionChains(self.driver).move_to_element(element).click().perform()

    # Клик на поле темы
    def click_on_subject_field(self):
        element = WebDriverWait(self.driver, 10) \
            .until(lambda driver: self.driver.find_element_by_xpath(self.SUBJECT_FIELD))
        ActionChains(self.driver).move_to_element(element).click().perform()

    # Клик на поле копии письма
    def click_on_copy_field(self):
        element = WebDriverWait(self.driver, 10) \
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
            return False
