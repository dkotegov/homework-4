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

    def more_details(self):
        link = self._driver.find_element_by_xpath(
            "/html/body/div[5]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[6]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/a")
        # link = self._driver.find_element_by_css_selector("body.compose__beautiful.layout-fixed.g-default-font:nth-child(2) div.theme.minwidth:nth-child(65) div.theme__left div.theme__right div.theme__top div.theme__bottom div.theme__left-center div.theme__right-center div.theme__top-center div.theme__bottom-center div.theme__center div.theme__top-left div.theme__top-right div.theme__bottom-left div.theme__bottom-right div.b-layout.b-layout_main:nth-child(2) div.b-layout__col.b-layout__col_2_2:nth-child(2) div:nth-child(1) div.content__page:nth-child(3) div.js-content:nth-child(4) div.form__row.b-settings-aliases__row > a.js-more:nth-child(2)")
        link.click()

    def is_more_details_pop_up_open(self):
        try:
            self._driver.find_element_by_xpath("/html/body/div[13]/div/div[1]/div/div/div/div/ul/li[2]")
            # self._driver.find_element_by_css_selector("body.compose__beautiful.layout-fixed.g-default-font:nth-child(2) div.js-layer_anonim:nth-child(78) div.b-layer div.b-layer__wrapper div.b-layer__container.b-layer__container_anonim div.b-layer__placeholder > div.b-promoter")
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
            # self._driver.find_elements_by_class_name("alertDiv")
            # self._driver.find_element_by_xpath("/html/body/div[7]/div/div[3]/form/div[1]")
        except Ex.NoSuchElementException:
            return False
        else:
            return True

    def submit_delete_email(self):
        elem = self._driver.find_element_by_xpath("/html/body/div[7]/div/div[3]/form/div[2]/button[1]")
        # elem = self._driver.find_element_by_css_selector("body.compose__beautiful.layout-fixed.g-default-font:nth-child(2) div.alertDiv:nth-child(68) div.popup.js-layer.popup_dark.popup_ div.is-aliases-remove_in form:nth-child(1) div.popup__controls:nth-child(3) > button.btn.btn_main.btn_stylish:nth-child(1)")
        elem.click()

    def cancel_delete_email(self):
        elem = self._driver.find_element_by_class_name("b-form__control")
        elem.click()

    # def get_first_email(self):
    #     elem = self._driver.find_element_by_css_selector("body.compose__beautiful.layout-fixed.g-default-font:nth-child(2) div.theme.minwidth:nth-child(65) div.theme__left div.theme__right div.theme__top div.theme__bottom div.theme__left-center div.theme__right-center div.theme__top-center div.theme__bottom-center div.theme__center div.theme__top-left div.theme__top-right div.theme__bottom-left div.theme__bottom-right div.b-layout.b-layout_main:nth-child(2) div.b-layout__col.b-layout__col_2_2:nth-child(2) div.content__page:nth-child(3) div.js-content:nth-child(4) div.form div.b-list.b-list_settings div.b-list__list div.b-list__item.b-list__list__item:nth-child(1) div.b-list__item__content div.b-settings-aliases.b-settings-aliases__list-item.b-settings-aliases_selected div.b-settings-aliases__content > a.b-settings-aliases__name.js-edit")
    #     return elem.text

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
        elem = self._driver.find_element_by_css_selector(
            ".b-form__control.b-form__control_main.b-form__control_stylish")
        elem.click()

    def get_comment(self):
        elem = self._driver.find_element_by_xpath("//*[@class='b-input b-input_popup']")
        return elem.get_attribute("value")

