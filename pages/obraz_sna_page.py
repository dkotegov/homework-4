# coding=utf-8
from time import sleep

from selenium.common.exceptions import NoSuchElementException


class BlockFindNewObraz:
    def __init__(self, driver, page):
        self.driver = driver
        self.page = page

    def open(self):
        self.driver.get(self.page)

    def get_text_article(self):
        return self.driver.find_element_by_class_name("article__item").text

    def get_text_header_article(self):
        return self.driver.find_element_by_class_name("hdr__inner").text

    def get_text_header_search(self):
        return self.driver.find_element_by_class_name("hdr_search").text

    def find(self, obraz):
        input = self.driver.find_element_by_name("q")
        input.send_keys(obraz)

        self.driver.find_element_by_name("clb11934144").click()


class RepostBlock:
    def __init__(self, driver, page):
        self.driver = driver
        self.page = page

    def open(self):
        self.driver.get(self.page)

    def get_count_reposts(self):
        try:
            return int(self.driver.find_element_by_class_name("sharelist__count").text)
        except NoSuchElementException:
            return 0

    def share(self):
        self.driver.find_element_by_class_name("share_vk").click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)