import time

from pages.defaultPage import Page, Component
from selenium.webdriver.support.ui import WebDriverWait

from pages.pin import PinPage


class FeedPage(Page):
    PATH = ''

    @property
    def feed_area(self):
        return FeedArea(self.driver)


class FeedArea(Component):
    FEED_AREA = '//*[@id="mainDesk"]'

    FEED_COLUMNS = '//*[@id="columns"]'

    MAIN_PAGE_INFO = '//*[@id="main_page_info"]'

    def get_pins_count(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FEED_COLUMNS)
        )
        html_history = self.driver.find_element_by_xpath(self.FEED_COLUMNS).get_attribute('innerHTML')
        return len(html_history.split('class="card"')) - 1

    def wait_new_pins(self, pin_number):
        x_path_selector = self.FEED_COLUMNS + '/div[' + str(pin_number) + ']'
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(x_path_selector)
        )

    def scroll(self):
        time.sleep(1)  # bad, replace until set scroll script
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_pins_authors(self):
        WebDriverWait(self.driver, 20, 0.8).until(
            lambda d: d.find_element_by_xpath(self.FEED_COLUMNS)
        )
        pins_count = self.get_pins_count()

        authors = []
        pin_page = PinPage(self.driver)
        pin_modal = pin_page.pin_modal

        for i in range(pins_count):
            selector = self.FEED_COLUMNS + '/div[' + str(i + 1) + ']'
            self.driver.find_element_by_xpath(selector).click()
            author = pin_modal.get_author()
            authors.append(author)
            self.driver.execute_script("window.history.go(-1)")

        return authors

    def get_load_msg(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MAIN_PAGE_INFO)
        )
        return self.driver.find_element_by_xpath(self.MAIN_PAGE_INFO).get_attribute('innerText')

    def show_sub(self):
        self.driver.get('https://zinterest.ru/subs')  # hardcore, replace tip menu acts


