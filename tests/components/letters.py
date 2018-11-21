# -*- coding: utf-8 -*-

from component import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class Letters(Component):
    BASE = '//div[@data-qa-id="dataset-letters"] '
    MAIL_FROM = '//span[@class="ll-crpt"]'
    MAIL_TEXT = '//span[@class="ll-sp__normal"]'
    MAIL_TIME = '//div[@class="llc__item llc__item_date"]'
    MAIL_IMAGE = '//div[@data-qa-id="avatar"]'
    SELECT_MESSAGE = '//a[contains(@class, "llc_normal")]'
    MOVE_TO_BUTTON = '//span[contains(text(), "Переместить в папку")]'
    NEW_FOLDER_FOR_LETTER = '//div[@title="{}"]'
    SELECT = BASE + '//*[@data-qa-id="avatar"]'

    MESSAGE_BY_SUBJECT = BASE + '//a[@data-qa-id="letter-item:subject:{}"]'

    def get_letters(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SELECT_MESSAGE)
        )
        return self.driver.find_elements_by_xpath(self.SELECT_MESSAGE)

    def get_mail_from(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MAIL_FROM).text
        )

    def get_mail_text(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MAIL_TEXT).text
        )

    def get_mail_time(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MAIL_TIME).text
        )

    def select_one(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable((By.XPATH, self.SELECT))
        ).click()
        
    # Перемещает первое письмо в папку @folder_name
    def move_letter_to_folder(self, folder_name):
        letter = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SELECT_MESSAGE)
        )
        actionChains = ActionChains(self.driver)
        actionChains.context_click(letter).perform()

        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MOVE_TO_BUTTON)).click()
        
        new_folder = self.NEW_FOLDER_FOR_LETTER.format(folder_name)
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(new_folder)).click()

    def get_letter_id_by_subject(self, subject):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MESSAGE_BY_SUBJECT.format(subject))
        ).get_attribute('data-id')
    
    def open_letter_by_subject(self, subject):
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable((By.XPATH, self.MESSAGE_BY_SUBJECT.format(subject)))
        ).click()

    def has_letters(self):
        try:
            elems = WebDriverWait(self.driver, 3, 0.1).until(
                lambda d: d.find_elements_by_xpath(self.SELECT)
            )
            return len(elems)
        except:
            return 0

    def get_several_messages(self, number):
        messages = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_elements_by_xpath(self.MAIL_IMAGE)
        )
        for i in range(number):
            messages[i].click()
        return messages[0]

    def get_message(self):
        message = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MAIL_IMAGE)
        )
        return message

    def drag_and_drop_message(self, sidebar, target_dirname):
        message_element = self.get_message()
        folder_element = sidebar.get_folder_element(target_dirname)
        ActionChains(self.driver).drag_and_drop(message_element, folder_element).perform()

    def drag_and_drop_several_messages(self, sidebar, messages_number, target_dirname):
        first_message_element = self.get_several_messages(messages_number)
        folder_element = sidebar.get_folder_element(target_dirname)
        ActionChains(self.driver).drag_and_drop(first_message_element, folder_element).perform()
