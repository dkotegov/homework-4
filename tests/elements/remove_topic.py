# coding=utf-8
from selenium.webdriver.common.by import By

from base import *


class SubmitRemoveButton(BaseElement):
    locator = (By.XPATH, "//input[@name='submit']")


class CancelRemoveButton(BaseElement):
    locator = (By.XPATH, "//button[@name='cancel']")
