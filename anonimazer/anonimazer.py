from selenium.common import exceptions as Ex
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import os


class Anonimazer:
    def __init__(self, driver):

        self._mail_url = os.getenv("TEST_MAIL_URL")
        self._anonimazer_url = os.getenv("TEST_ANONIMAZER_URL")
        self._login = os.getenv("TEST_LOGIN")
        self._pass = os.getenv("TEST_PASS")
        self._driver = driver
        self._authorization()
        self.redirect_to_anonimazer()

    def redirect_to_anonimazer(self):
        self._driver.get(self._anonimazer_url)

    def printenv(self):
        print('TEST_MAIL_URL = ', self._mail_url)
        print('TEST_ANONIMAZER_URL = ', self._anonimazer_url)
        print('TEST_LOGIN = ', self._login)
        print('TEST_PASS = ', self._pass)

    def _wait(self, wait_until=None, timeout=5):
        return WebDriverWait(self._driver, timeout).until(wait_until)

    def _wait_visibility(self, selector):
        return self._wait(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def _authorization(self):
        self._driver.get(self._mail_url)
        frame = self._driver.find_element_by_css_selector('#auth-form iframe')
        self._driver.switch_to.frame(frame)
        elem = self._wait_visibility('input[name=Login]')
        elem.send_keys(self._login)
        elem = self._driver.find_element_by_css_selector('button[type=submit]')
        elem.click()
        elem = self._wait_visibility('input[name=Password]')
        elem.send_keys(self._pass)
        elem = self._driver.find_element_by_css_selector('button[type=submit]')
        elem.click()
        self._driver.switch_to.default_content()

    def create_new_email(self):
        elem = self._driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[6]/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/div[1]/button")
        elem.click()

    def close_new_email_pop_up(self):
        elem = self._driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/div/div[3]/form/div[6]/div[2]/button")
        elem.click()

    def enter_email(self, email):
        elem = self._driver.find_element_by_class_name("b-email__name")
        children_elems = elem.find_elements_by_css_selector("*")
        children_elems[0].send_keys(email)

    def clear_email(self):
        elem = self._driver.find_element_by_class_name("b-email__name")
        children_elems = elem.find_elements_by_css_selector("*")
        children_elems[0].clear()

    def is_combobox_in_form(self):
        try:
            elem = WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "b-select__dropdown")))
            elem.click()
        except Ex.TimeoutException:
            return False
        else:
            return True

    def get_captcha_url(self):
        captcha = self._driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/div/div[3]/form/div[4]/div/div[2]/div[1]/div/img")
        return captcha.get_attribute("src")

    def change_captcha(self):
        link = self._driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/div/div[3]/form/div[4]/div/div[2]/div[1]/div/div/a")
        link.click()

    def is_pop_up_open(self):
        try:
            self._driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/div")
        except Ex.NoSuchElementException:
            return False
        else:
            return True

    def more_details(self):
        link = self._driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[6]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/a")
        link.click()

    def is_more_details_pop_up_open(self):
        try:
            self._driver.find_element_by_xpath("/html/body/div[13]/div/div[1]/div/div/div/div/ul/li[2]")
        except Ex.NoSuchElementException:
            return False
        else:
            return True

    def delete_email(self, email):
        try:
            elem = self._driver.find_element_by_link_text(email)
            elem.click()
        except Ex.NoSuchElementException:
            print("No such Element")

    def is_delete_pop_up_open(self):
        try:
            self._driver.find_elements_by_css_selector("popup.js-layer.popup_dark.popup_")
        except Ex.NoSuchElementException:
            return False
        else:
            return True

    def submit_delete_email(self):
        elem = self._driver.find_element_by_xpath("/html/body/div[7]/div/div[3]/form/div[2]/button[1]")
        elem.click()

    def cancel_delete_email(self):
        elem = self._driver.find_element_by_class_name("b-form__control")
        elem.click()

    def is_email_alive(self, email):
        try:
            self._driver.find_element_by_link_text(email)
        except Ex.NoSuchElementException:
            return False
        else:
            return True

    def edit_email(self, email):
        link = self._driver.find_element_by_link_text(email)
        link.click()

    def is_edit_pop_up_open(self):
        try:
            self._driver.find_elements_by_class_name("is-aliases-edit_in")
        except Ex.NoSuchElementException:
            return False
        else:
            return True

    def edit_comment(self, comment):
        elem = self._driver.find_element_by_name("comment")
        elem.clear()
        elem.send_keys(comment)

    def submit_edit(self):
        elem = self._driver.find_element_by_css_selector(".b-form__control.b-form__control_main.b-form__control_stylish")
        elem.click()

    def get_comment(self):
        elem = self._driver.find_element_by_xpath("//*[@class='b-input b-input_popup']")
        return elem.get_attribute("value")
