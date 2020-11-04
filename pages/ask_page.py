from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.page import Page


class AskPage(Page):
    PATH = '/ask'

    TOPIC_INPUT = '//textarea[@name="question_text"]'
    TEXT_INPUT = '//textarea[@name="question_additional"]'
    CATEGORY_BUTTON = '//div[@name="select_parents_categories"]'
    CATEGORY_ITEM = '//div[@data-qa="select-list-item"][@data-qa-value="1"]'
    SUBCATEGORY_BUTTON = '//div[@name="select_childs_categories"]'
    SUBCATEGORY_ITEM = '//div[@data-qa="select-list-item"][@data-qa-value="1394"]'
    PUBLISH_BUTTON = '//a[@data-qa="input-question_submit"]'
    PUBLISH_BUTTON_ENABLED = '//a[@data-qa="input-question_submit"][@data-qa-disabled="false"]'
    QUESTION_TOPIC = '//h1[contains(@class,"qtext")]'

    @property
    def topic_has_error(self):
        driver = self.driver
        topic_input = driver.find_element_by_xpath(self.TOPIC_INPUT)
        return topic_input.get_attribute('data-qa-error') != 'undefined'

    @property
    def is_button_disabled(self):
        button = self.driver.find_element_by_xpath(self.PUBLISH_BUTTON)
        return button.get_attribute('data-qa-disabled') == 'true'

    @property
    def question_topic(self):
        driver = self.driver
        topic_element = driver.find_element_by_xpath(self.QUESTION_TOPIC)
        return topic_element.text

    def set_topic(self, topic):
        driver = self.driver
        driver.find_element_by_xpath(self.TOPIC_INPUT).send_keys(topic)

    def set_text(self, text):
        driver = self.driver
        driver.find_element_by_xpath(self.TEXT_INPUT).send_keys(text)

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
