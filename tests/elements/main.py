# coding=utf-8
from selenium.webdriver.common.by import By

from base import BaseElement


class UserDropdown(BaseElement):
    locator = (By.XPATH, "//div[@class='dropdown-user']")
