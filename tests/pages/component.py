from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def get_elem_by_id(self, id_elem):
        return self.driver.find_element_by_id(id_elem)

    def get_one_elem_by_css(self, css_selector):
        return self.driver.find_element_by_css_selector(css_selector)

    def get_last_elem_by_css(self, css_selector):
        return self.driver.find_elements_by_css_selector(css_selector)[-1]

    def get_length_of_elem_list_by_css(self, css_selector):
        return len(self.driver.find_elements_by_css_selector(css_selector))

