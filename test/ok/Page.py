from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from config import config

from logger import log_d

from hamcrest import *

timeout = config["timeout"]

class Page(object):
    def __init__(self, driver, name_page="unknown"):
        self.url = config["ok.scheme"] + "://" + config["ok.server"]
        self.driver = driver

        self.name_page = name_page
        self.wait = WebDriverWait(self.driver, timeout)
        self.actions = ActionChains(self.driver)

    def open(self, path='/'):
        self.driver.get(self.url + path)

    def close(self):
        # some destruct, override me
        log_d("page " + self.name_page + " is destruct")

    def get_element_by_class(self, parent, classname, tag="some form"):
        objs = parent.find_elements_by_class_name(classname)
        assert_that(objs, has_length(1), "bad button add in " + tag)
        return objs[0]

    def get_first_element_by_class(self, parent, classname, tag="some form"):
        objs = parent.find_elements_by_class_name(classname)
        assert_that(len(objs), greater_than_or_equal_to(1), "bad class count in " + tag)
        return objs[0]

    def get_parent(self, element):
        return element.find_element_by_xpath("..")
