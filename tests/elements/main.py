# coding=utf-8
from selenium.webdriver.common.by import By

from base import *


class UserDropdown(BaseElement):
    locator = (By.XPATH, "//div[@class='dropdown-user']")
