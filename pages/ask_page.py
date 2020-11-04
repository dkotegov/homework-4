from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os

from pages.page import Page


class AskPage(Page):
    PATH = '/ask'

    IMAGE_PATH = os.getcwd() + '/media/utka.png'
    VIDEO_PATH = os.getcwd() + '/media/utochka.webm'

    TOPIC_INPUT = '//textarea[@name="question_text"]'
    TEXT_INPUT = '//textarea[@name="question_additional"]'
    ATTACHED_MEDIA = '//div[@data-qa="input-media-container-item"]'
    ATTACH_IMAGE_LINK = '//a[@data-qa="input-media-photo"]'
    IMAGE_LOADER_INPUT = '//input[@data-qa="image-loader-input"]'
    TAB_EXTERNAL = '//li[@data-qa="tab-item_external"]'
    IMAGE_LINK_INPUT = '//input[@name="external_upload"]'
    MODAL = '//div[@data-modal="ModalMessage"]'
    ATTACH_VIDEO_LINK = '//a[@data-qa="input-media-video"]'
    VIDEO_LOADER_INPUT = '//input[@data-type="video-input-file"]'
    VIDEO_SUBMIT_BUTTON = '//button[@data-button-name="submit"]'
    CATEGORY_BUTTON = '//div[@name="select_parents_categories"]'
    CATEGORY_ITEM = '//div[@data-qa="select-list-item"][@data-qa-value="38"]'
    SUBCATEGORY_BUTTON = '//div[@name="select_childs_categories"]'
    SUBCATEGORY_ITEM = '//div[@data-qa="select-list-item"][@data-qa-value="1356"]'
    PUBLISH_BUTTON = '//a[@data-qa="input-question_submit"]'
    PUBLISH_BUTTON_ENABLED = '//a[@data-qa="input-question_submit"][@data-qa-disabled="false"]'
    QUESTION_TOPIC = '//h1[contains(@class,"qtext")]'

    def topic_has_error(self):
        driver = self.driver
        topic_input = driver.find_element_by_xpath(self.TOPIC_INPUT)
        return topic_input.get_attribute('data-qa-error') != 'undefined'

    def text_has_error(self):
        driver = self.driver
        text_input = driver.find_element_by_xpath(self.TEXT_INPUT)
        return text_input.get_attribute('data-qa-error') != 'undefined'

    def is_media_attached(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath(self.ATTACHED_MEDIA)
        except NoSuchElementException:
            return False
        return True

    def has_error_modal(self):
        driver = self.driver
        try:
            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, self.MODAL)))
        except TimeoutException:
            return False
        return True

    def is_button_disabled(self):
        button = self.driver.find_element_by_xpath(self.PUBLISH_BUTTON)
        return button.get_attribute('data-qa-disabled') == 'true'

    def get_question_topic(self):
        driver = self.driver
        topic_element = driver.find_element_by_xpath(self.QUESTION_TOPIC)
        return topic_element.text

    def set_topic(self, topic):
        driver = self.driver
        driver.find_element_by_xpath(self.TOPIC_INPUT).send_keys(topic)

    def set_text(self, text):
        driver = self.driver
        driver.find_element_by_xpath(self.TEXT_INPUT).send_keys(text)

    def attach_photo_from_computer(self):
        driver = self.driver
        driver.find_element_by_xpath(self.ATTACH_IMAGE_LINK).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.IMAGE_LOADER_INPUT)))
        driver.find_element_by_xpath(self.IMAGE_LOADER_INPUT).send_keys(self.IMAGE_PATH)

    def attach_photo_by_link(self, link):
        driver = self.driver
        driver.find_element_by_xpath(self.ATTACH_IMAGE_LINK).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.IMAGE_LOADER_INPUT)))
        driver.find_element_by_xpath(self.TAB_EXTERNAL).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.IMAGE_LINK_INPUT)))
        driver.find_element_by_xpath(self.IMAGE_LINK_INPUT).send_keys(link)

    def attach_video_from_computer(self):
        driver = self.driver
        window_before = driver.window_handles[0]
        driver.find_element_by_xpath(self.ATTACH_VIDEO_LINK).click()
        WebDriverWait(driver, 10).until(EC.new_window_is_opened)
        window_after = driver.window_handles[1]

        driver.switch_to_window(window_after)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.VIDEO_LOADER_INPUT)))
        driver.find_element_by_xpath(self.VIDEO_LOADER_INPUT).send_keys(self.VIDEO_PATH)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.VIDEO_SUBMIT_BUTTON)))
        driver.find_element_by_xpath(self.VIDEO_SUBMIT_BUTTON).click()

        driver.switch_to_window(window_before)
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, self.ATTACHED_MEDIA)))

    def set_category(self):
        driver = self.driver
        driver.find_element_by_xpath(self.CATEGORY_BUTTON).click()
        driver.find_element_by_xpath(self.CATEGORY_ITEM).click()

    def set_subcategory(self):
        driver = self.driver
        driver.find_element_by_xpath(self.SUBCATEGORY_BUTTON).click()
        driver.find_element_by_xpath(self.SUBCATEGORY_ITEM).click()

    def publish_question(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.PUBLISH_BUTTON_ENABLED)))
        driver.find_element_by_xpath(self.PUBLISH_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_contains('otvet.mail.ru/question/'))
        return driver.current_url
