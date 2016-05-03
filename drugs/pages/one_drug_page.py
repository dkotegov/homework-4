# -*- coding: utf-8 -*-
__author__ = 'alla'
from drugs.pages.main_page import Component, Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import requests
from urlparse import urljoin

class DrugPage(Page):
    def __init__(self, driver, drugs_name):
        Page.__init__(self, driver)
        self.PATH = urljoin(self.BASE_URL, '/drug/')
        self.PATH = urljoin(self.PATH, drugs_name)

    @property
    def counter(self):
        return Counter(self.driver)

    @property
    def contraindication(self):
        return Links(self.driver, "//a[contains(@class, 'icon icon_medicament')]")

    @property
    def social_networks(self):
        return Links(self.driver, "//a[contains(@class, 'article__share')]")

    @property
    def instructions(self):
        return Links(self.driver, "//a[@class = 'catalog__item catalog__item_pseudo catalog__item_pseudo_dotted']")

    @property
    def analogs(self):
        return Analog(self.driver)


class Analog(Component):
    ALL_ITEMS = "//div[@class='columns columns_percent']"
    ITEMS = "//div[@class='entry entry_medicament margin_bottom_30']//a[@class='entry__link link-holder']"
    TITLE = '//h1[@class="page-info__title"]'

    def items(self):
        items = self.driver.find_element_by_xpath(self.ALL_ITEMS).find_elements_by_xpath(self.ITEMS)
        return items

    def get_names(self):
        items = self.driver.find_elements_by_xpath(self.ITEMS)
        return [item.text for item in items]

    def get_drags_name(self, n):
        result = self.items()[n].text
        return result

    def go_to_drugs_page(self, title):
        self.driver.find_element_by_link_text(title).click()

    def result_drag(self):
        result = self.driver.find_element_by_xpath(self.TITLE)
        return result.text


class Links(Component):
    def __init__(self, driver, icons_xpath):
        Component.__init__(self, driver)
        self.LINK = icons_xpath

    def links(self):
        items = self.driver.find_elements_by_xpath(self.LINK)
        return [item.get_attribute('href') for item in items]

    def check_link(self, link):
         return requests.get(link).status_code == 200

class Counter(Component):
    COUNTER = ".amount.margin_right_10"
    ORDER_BUTTON = "//div[text()='Заказать']"
    DO_ORDER_BUTTON = "//div[text()='Оформить заказ']"
    DROPDOWN_ITEMS = "//div[@class='dropdown__item dropdown__item_good js-cart_add'][%s]/span/span"
    DROPDOWN_ITEM = "//span[text()='%s']"
    BUY_COUNT = "//input[@class='amount__item__input js-buy_count']"
    PLUS = "//span[text()='+']"
    MINUS = "//span[text()='-']"
    RESULT_TYPE = '//div[@class = "entry entry_medicament"]//div[@class="entry__name"]'

    def selected_dropdown_item_by_number(self, n):
        type = self.driver.find_element_by_xpath(self.DROPDOWN_ITEMS % n).text
        self.driver.find_element_by_xpath(self.DROPDOWN_ITEMS % n).click()
        return type

    def counter_is_visible(self):
        return self.driver.find_element_by_css_selector(self.COUNTER).is_displayed()

    def to_order(self):
        WebDriverWait(self.driver, self.TIMEOUT).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.ORDER_BUTTON))
        )
        self.driver.find_element_by_xpath(self.ORDER_BUTTON).click()

    def get_counter_value(self):
        return self.driver.find_element_by_xpath(self.BUY_COUNT).get_attribute('value')

    def increment(self):
        WebDriverWait(self.driver, self.TIMEOUT).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.PLUS))
        )
        self.driver.find_element_by_xpath(self.PLUS).click()

    def decrement(self):
        WebDriverWait(self.driver, self.TIMEOUT).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.MINUS))
        )
        self.driver.find_element_by_xpath(self.MINUS).click()

    def selected_dropdown_item(self, text):
        WebDriverWait(self.driver, self.TIMEOUT).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.DROPDOWN_ITEM % text))
        )
        self.driver.find_element_by_xpath(self.DROPDOWN_ITEM % text).click()

    def dropdown_items(self):
        types = self.driver.find_elements_by_css_selector('span.dropdown__item__label.table__cell')
        return [item.text for item in types]

    def do_order(self):
        self.driver.find_element_by_xpath(self.DO_ORDER_BUTTON).click()

    def result_type(self):
        type = self.driver.find_element_by_xpath(self.RESULT_TYPE).text
        return type
