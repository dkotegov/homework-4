from selenium.common import exceptions as Ex
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os


class Anonimazer:
    AUTH_SUBMIT_BTN = 'button[type=submit]'
    AUTH_LOGIN_INPUT = 'input[name=Login]'
    AUTH_PASSWORD_INPUT = 'input[name=Password]'
    EMAIL_INPUT = "//span[@class='b-email__name']//input"
    COMMENT_INPUT = "//input[@name='comment']"
    ADD_EMAIL_BTN = "//div[@class='form__row b-settings-aliases__row']//button[@class='btn btn_main alias " \
                    "js-create-alias'] "
    CANCEL_EMAIL_BTN = "//div[@class='b-form__control']//button[@data-name='close']"
    GET_CAPTCHA = "//img[@class='js-captcha-img b-captcha__captcha']"
    CHANGE_CAPTCHA_LINK = "//a[@class='js-captcha-reload b-captcha__code__reload']"
    DELETE_EMAIL_LINK = "//a[@class='b-settings-aliases__remove js-remove']"
    MORE_LINK = "//a[@class='js-more']"
    POPUP_CLS = "//div[@class='popup js-layer popup_dark popup_']"
    POP_UP_PROMOTER = "//div[@class='b-promoter']"
    SUBMIT_EDIT_BTN = "//div[contains(@class,'b-form__control b-form__control_main " \
                      "b-form__control_stylish')]//button[contains(@class,'btn btn_main btn_stylish')] "
    SETTING_DIV = "//div[@class='b-list__item__content']//div"
    POPUP_DIV = "//div[contains(@class,'popup js-layer popup_dark popup_')]"
    SUBMIT_DEL_BTN = "//div[@class='popup__controls']//button[contains(@class,'btn btn_main btn_stylish')]"
    ALIASES_COMMENT_DIV = "//div[@class='b-settings-aliases__comment']"

    def __init__(self, driver):
        self._mail_url = "https://e.mail.ru/login"
        self._anonimazer_url = "https://e.mail.ru/settings/aliases?afterReload=1"
        self._login = "14cowperwood88"
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

    def _wait_visibility_css(self, selector):
        return self._wait(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def _wait_visibility_xpath(self, path):
        return self._wait(EC.visibility_of_element_located((By.XPATH, path)))

    def _authorization(self):
        self._driver.get(self._mail_url)
        frame = self._driver.find_element_by_css_selector('#auth-form iframe')
        self._driver.switch_to.frame(frame)
        elem = self._wait_visibility_css(self.AUTH_LOGIN_INPUT)
        elem.send_keys(self._login)
        elem = self._driver.find_element_by_css_selector(self.AUTH_SUBMIT_BTN)
        elem.click()
        elem = self._wait_visibility_css(self.AUTH_PASSWORD_INPUT)
        elem.send_keys(self._pass)
        elem = self._driver.find_element_by_css_selector(self.AUTH_SUBMIT_BTN)
        elem.click()
        self._driver.switch_to.default_content()

    def create_new_email(self):
        add_email_button = self._wait_visibility_xpath(self.ADD_EMAIL_BTN)
        add_email_button.click()

    def close_new_email_pop_up(self):
        cancel_button = self._wait_visibility_xpath(self.CANCEL_EMAIL_BTN)
        cancel_button.click()

    def enter_email(self, email):
        input_field = self._wait_visibility_xpath(self.EMAIL_INPUT)
        input_field.send_keys(email)

    def clear_email(self):
        input_field = self._wait_visibility_xpath(self.EMAIL_INPUT)
        input_field.clear()

    def is_combobox_in_form(self):
        try:
            combobox = WebDriverWait(self._driver, 3).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "b-select__dropdown")))
            combobox.click()
        except Ex.TimeoutException:
            return False
        else:
            return True

    def get_captcha_url(self):
        captcha = self._wait_visibility_xpath(self.GET_CAPTCHA)
        return captcha.get_attribute("src")

    def change_captcha(self):
        link = self._wait_visibility_xpath(self.CHANGE_CAPTCHA_LINK)
        link.click()

    def is_pop_up_open(self):
        try:
            self._wait_visibility_xpath("%s" % self.POPUP_CLS)
        except Ex.TimeoutException:
            return False
        else:
            return True

    def more_details(self):
        link = self._wait_visibility_xpath("%s" % self.MORE_LINK)
        link.click()

    def is_more_details_pop_up_open(self):
        try:
            self._wait_visibility_xpath("%s" % self.POP_UP_PROMOTER)
        except Ex.TimeoutException:
            return False
        else:
            return True

    def delete_email(self, email):
        settings_blocks = self._driver.find_elements_by_xpath("%s" % self.DELETE_EMAIL_LINK)
        for block in settings_blocks:
            if block.get_attribute("data-id") == email:
                block.click()

    def is_delete_pop_up_open(self):
        try:
            POPUP_REMOVE = "//div[@class='is-aliases-remove_in']"
            self._wait_visibility_xpath("%s" % POPUP_REMOVE)
        except Ex.TimeoutException:
            return False
        else:
            return True

    def submit_delete_email(self):
        submit_button = self._wait_visibility_xpath(
            "%s" % self.SUBMIT_DEL_BTN)
        submit_button.click()

    def cancel_delete_email(self):
        CANCEL_BUTTON = "//button[contains(@class,'btn btn_cancel')]"
        cancel_button = self._wait_visibility_xpath("%s" % CANCEL_BUTTON)
        cancel_button.click()

    def is_email_alive(self, email):
        try:
            self._driver.find_element_by_link_text(email)
        except Ex.TimeoutException:
            return False
        else:
            return True

    def edit_email(self, email):
        EDIT_LINK = "//a[@class='b-settings-aliases__name js-edit']"
        links = self._driver.find_elements_by_xpath("%s" % EDIT_LINK)
        for link in links:
            if link.get_attribute("data-id") == email:
                link.click()

    def is_edit_pop_up_open(self):
        try:
            self._wait_visibility_xpath("%s" % self.POPUP_DIV)

        except Ex.TimeoutException:
            return False
        else:
            return True

    def edit_comment(self, comment):
        input_field = self._wait_visibility_xpath(self.COMMENT_INPUT)
        input_field.clear()
        input_field.send_keys(comment)

    def submit_edit(self):
        submit_button = self._wait_visibility_xpath(
            "%s" % self.SUBMIT_EDIT_BTN)
        submit_button.click()

    def get_comment(self, email):
        settings_blocks = self._driver.find_elements_by_xpath(self.SETTING_DIV)
        for block in settings_blocks:
            if block.get_attribute("data-alias-id") == email:
                comment = self._wait_visibility_xpath(self.ALIASES_COMMENT_DIV)
                return comment.text
        return "None"
