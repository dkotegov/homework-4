# coding=utf-8
from selenium.webdriver.common.by import By

from base import *


class OpenLoginFormButton(BaseElement):
    locator = (By.XPATH, "//a[text()='Вход для участников']")


class LoginInput(BaseElement):
    locator = (By.XPATH, "//input[@name='login']")


class PasswordInput(BaseElement):
    locator = (By.XPATH, "//input[@name='password']")


class SubmitLoginButton(BaseElement):
    locator = (By.XPATH, "//button[@name='submit_login']")
