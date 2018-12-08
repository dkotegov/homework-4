# -*- coding: utf-8 -*-

import time
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
    MESSAGE_IMAGE_BY_SUBJECT = MESSAGE_BY_SUBJECT + \
        '/div[@data-qa-id="avatar"]'
    RANDOM_MESSAGE = BASE + \
        '//a[contains(@data-qa-id, "letter-item:subject:")]'

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

    def open_rand(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable((By.XPATH, self.RANDOM_MESSAGE))
        ).click()

    # Перемещает первое письмо в папку @folder_name с помощью ПКМ
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

    # Переносит письмо с заголовком @subject в папку @folder_name с помощью ПКМ
    def move_letter_by_subject_to_folder(self, subject, folder_name):
        letter = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(
                self.MESSAGE_BY_SUBJECT.format(subject))
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
            lambda d: d.find_element_by_xpath(
                self.MESSAGE_BY_SUBJECT.format(subject))
        ).get_attribute('data-id')

    def open_letter_by_subject(self, subject):
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.MESSAGE_BY_SUBJECT.format(subject)))
        ).click()

    def has_letters(self):
        try:
            elems = WebDriverWait(self.driver, 3, 0.1).until(
                lambda d: d.find_elements_by_xpath(self.SELECT)
            )
            return len(elems)
        except:
            return 0

    def select_letters(self, number):
        letters = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_elements_by_xpath(self.MAIL_IMAGE)
        )
        for i in range(number):
            letters[i].click()
        return letters[0]

    def select_letters_by_subject(self, subject):
        letters_images = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_elements_by_xpath(
                self.MESSAGE_IMAGE_BY_SUBJECT.format(subject))
        )
        for letter_image in letters_images:
            letter_image.click()
        return letters_images[0]

    def get_letters_by_subject(self, subject):
        letters = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_elements_by_xpath(
                self.MESSAGE_BY_SUBJECT.format(subject))
        )
        return letters

    def get_letter(self):
        letter = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MAIL_IMAGE)
        )
        return letter

    def drag_and_drop(self, sidebar, letter_subject, target_dirname):
        letter_element = self.select_letters_by_subject(letter_subject)
        folder_element = sidebar.get_folder_element(target_dirname)
        ActionChains(self.driver).drag_and_drop(
            letter_element, folder_element).perform()

    def drag_and_drop_letters(self, sidebar, subject, number, target_dirname):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: len(d.find_elements_by_xpath(
                self.MESSAGE_IMAGE_BY_SUBJECT.format(subject))) == number
        )
        self.drag_and_drop(sidebar, subject, target_dirname)

    def remove_letters_by_subject(self, sidebar, subject):
        target_dirname = "Корзина"
        self.drag_and_drop(sidebar, subject, target_dirname)
