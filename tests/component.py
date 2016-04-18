from selenium.common.exceptions import NoSuchElementException


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
