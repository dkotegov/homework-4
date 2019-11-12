from selenium.common import exceptions as Ex
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import os


class Anonimazer:
    def __init__(self, driver):

        self._mail_url = os.getenv('TEST_MAIL_URL')
        self._anonimazer_url = os.getenv('TEST_ANONIMAZER_URL')
        self._login = os.getenv('TEST_EMAIL')
        self._pass = os.getenv('TEST_PASS')
        self.printenv()
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
        elem = self._driver.find_element_by_css_selector('body.compose__beautiful.layout-fixed.g-default-font:nth-child(2) div.theme.minwidth:nth-child(65) div.theme__left div.theme__right div.theme__top div.theme__bottom div.theme__left-center div.theme__right-center div.theme__top-center div.theme__bottom-center div.theme__center div.theme__top-left div.theme__top-right div.theme__bottom-left div.theme__bottom-right div.b-layout.b-layout_main:nth-child(2) div.b-layout__col.b-layout__col_2_2:nth-child(2) div.content__page:nth-child(3) div.js-content:nth-child(4) div.form div.form__row.b-settings-aliases__row > button.btn.btn_main.alias.js-create-alias')
        elem.click()

    def close_new_email_pop_up(self):
        elem = self._driver.find_element_by_css_selector("body.compose__beautiful.layout-fixed.g-default-font:nth-child(2) div.alertDiv:nth-child(68) div.popup.js-layer.popup_dark.popup_ div.is-aliases-add_in div.popup__form form.b-form.b-form_popup div.b-form__controls.b-form__controls_popup:nth-child(6) div.b-form__control:nth-child(2) button.btn > span.btn__text")
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
        captcha = self._driver.find_element_by_css_selector("body.compose__beautiful.layout-fixed.g-default-font:nth-child(2) div.alertDiv:nth-child(68) div.popup.js-layer.popup_dark.popup_ div.is-aliases-add_in div.popup__form form.b-form.b-form_popup div.b-form-row.b-form-row_popup:nth-child(4) div.b-form-field.b-form-field_popup div.b-form-field__widget div.b-form-field__input div.b-captcha.b-captcha_popup > img.js-captcha-img.b-captcha__captcha")
        return captcha.get_attribute("src")

    def change_captcha(self):
        link = self._driver.find_element_by_css_selector("body.compose__beautiful.layout-fixed.g-default-font:nth-child(2) div.alertDiv:nth-child(68) div.popup.js-layer.popup_dark.popup_ div.is-aliases-add_in div.popup__form form.b-form.b-form_popup div.b-form-row.b-form-row_popup:nth-child(4) div.b-form-field.b-form-field_popup div.b-form-field__widget div.b-form-field__input div.b-captcha.b-captcha_popup div.b-captcha__code > a.js-captcha-reload.b-captcha__code__reload:nth-child(4)")
        link.click()

    def is_pop_up_open(self):
        try:
            head = self._driver.find_element_by_css_selector("body.compose__beautiful.layout-fixed.g-default-font:nth-child(2) div.alertDiv:nth-child(68) div.popup.js-layer.popup_dark.popup_ div.is-aliases-add_in div:nth-child(1) > div.popup__head")
        except Ex.NoSuchElementException:
            return False
        else:
            return True



# a = Anonimazer(webdriver.Firefox())
#
# a.create_new_email()
# print(a.is_combobox_in_form())
# a.enter_email("@")
# print(a.is_combobox_in_form())


