from tests.pages.base import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from components.navbar import NavbarComponent
from components.address_popup import AddressPopupComponent
from selenium.common.exceptions import NoSuchElementException


class MainPage(Page):
    PATH = '/'
    FIRST_RESTAURANT = '//ul[@id="restaurants_list"]/li'
    PIZZA_CATEGORY = '//li[@data-category="pizza"]'
    BURGERS_CATEGORY = '//li[@data-category="burgers"]'
    TIME_FILTER = '//div[@data-params="time"]'
    TIME_FILTER_90_MIN = '//div[text()="< 90 мин"]'
    RECEIPT_FILTER = '//div[@data-params="receipt"]'
    RECEIPT_FILTER_2000 = '//div[text()="< 2000 ₽"]'
    RATING_FILTER = '//div[@data-params="rating"]'
    RATING_FILTER_3_STARS = '//div[text()="3★"]'

    @property
    def navbar(self):
        return NavbarComponent(self.driver)

    @property
    def address_popup(self):
        return AddressPopupComponent(self.driver)

    def check_if_restaurants_displayed(self):
        try:
            self.driver.find_element_by_xpath(self.FIRST_RESTAURANT)
        except NoSuchElementException:
            return False
        return True

    def click_sushi_category(self):
        self.driver.find_element_by_xpath(self.PIZZA_CATEGORY).click()

    def click_burgers_category(self):
        self.driver.find_element_by_xpath(self.BURGERS_CATEGORY).click()

    def wait_restaurants_displayed(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, self.FIRST_RESTAURANT)))

    def choose_time_filter(self):
        self.driver.find_element_by_xpath(self.TIME_FILTER).click()
        self.driver.find_element_by_xpath(self.TIME_FILTER_90_MIN).click()

    def choose_receipt_filter(self):
        self.driver.find_element_by_xpath(self.RECEIPT_FILTER).click()
        self.driver.find_element_by_xpath(self.RECEIPT_FILTER_2000).click()

    def choose_rating_filter(self):
        self.driver.find_element_by_xpath(self.RATING_FILTER).click()
        self.driver.find_element_by_xpath(self.RATING_FILTER_3_STARS).click()
