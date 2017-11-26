from selenium.webdriver.common.by import By

from base import BaseElement


class LoginForm(BaseElement):
    SUBMIT_BUTTON = (By.XPATH, '//input[@data-l="t,loginButton"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="st.password"]')
    LOGIN_INPUT = (By.XPATH, '//input[@name="st.email"]')
