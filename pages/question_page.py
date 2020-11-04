from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.page import Page


class QuestionPage(Page):
    TOPIC = '//h1[contains(@class,"qtext")]'
    TEXT = '//div[contains(@class,"qcomment")]'
    CATEGORY = '//a[contains(@class,"header__link")]'
    SUBCATEGORY = '//a[contains(@class,"list__item_active")]//descendant::span//descendant::span'

    def __init__(self, driver, url):
        super(QuestionPage, self).__init__(driver)
        self.BASE_URL = url

    def get_topic(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.TOPIC)))
        topic = driver.find_element_by_xpath(self.TOPIC)
        return topic.text

    def get_text(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.TEXT)))
        text = driver.find_element_by_xpath(self.TEXT)
        return text.text

    def get_category(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.CATEGORY)))
        category = driver.find_element_by_xpath(self.CATEGORY)
        return category.text

    def get_subcategory(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.SUBCATEGORY)))
        subcategory = driver.find_element_by_xpath(self.SUBCATEGORY)
        return subcategory.text
