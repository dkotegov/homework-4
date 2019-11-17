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

    def _wait_visibility_css(self, selector):
        return self._wait(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def _wait_visibility_xpath(self, path):
        return self._wait(EC.visibility_of_element_located((By.XPATH, path)))

    def _authorization(self):
        submit = 'button[type=submit]'
        login_input = 'input[name=Login]'
        password_input = 'input[name=Password]'
        self._driver.get(self._mail_url)
        frame = self._driver.find_element_by_css_selector('#auth-form iframe')
        self._driver.switch_to.frame(frame)
        elem = self._wait_visibility_css(login_input)
        elem.send_keys(self._login)
        elem = self._driver.find_element_by_css_selector(submit)
        elem.click()
        elem = self._wait_visibility_css(password_input)
        elem.send_keys(self._pass)
        elem = self._driver.find_element_by_css_selector(submit)
        elem.click()
        self._driver.switch_to.default_content()

    def create_new_email(self):
        add_email_button = self._wait_visibility_xpath("//div[@class='form__row b-settings-aliases__row']//button[@class='btn btn_main alias js-create-alias']")
        add_email_button.click()

    def close_new_email_pop_up(self):
        cancel_button = self._wait_visibility_xpath("//div[@class='b-form__control']//button[@data-name='close']")
        cancel_button.click()

    def enter_email(self, email):
        input_field = self._wait_visibility_xpath("//span[@class='b-email__name']//input")
        input_field.send_keys(email)

    def clear_email(self):
        input_field = self._wait_visibility_xpath("//span[@class='b-email__name']//input")
        input_field.clear()

    def is_combobox_in_form(self):
        try:
            combobox = WebDriverWait(self._driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, "b-select__dropdown")))
            combobox.click()
        except Ex.TimeoutException:
            return False
        else:
            return True

    def get_captcha_url(self):
        captcha = self._wait_visibility_xpath("//img[@class='js-captcha-img b-captcha__captcha']")
        return captcha.get_attribute("src")

    def change_captcha(self):
        link = self._wait_visibility_xpath("//a[@class='js-captcha-reload b-captcha__code__reload']")
        link.click()

    def is_pop_up_open(self):
        try:
            self._wait_visibility_xpath("//div[@class='popup js-layer popup_dark popup_']")
        except Ex.TimeoutException:
            return False
        else:
            return True

    def more_details(self):
        link = self._wait_visibility_xpath("//a[@class='js-more']")
        link.click()

    def is_more_details_pop_up_open(self):
        try:
            self._wait_visibility_xpath("//div[@class='b-promoter']")
        except Ex.TimeoutException:
            return False
        else:
            return True

    def delete_email(self, email):
        settings_blocks = self._driver.find_elements_by_xpath("//a[@class='b-settings-aliases__remove js-remove']")
        for block in settings_blocks:
            if block.get_attribute("data-id") == email:
                block.click()


    def is_delete_pop_up_open(self):
        try:
            self._wait_visibility_xpath("//div[@class='is-aliases-remove_in']")
        except Ex.TimeoutException:
            return False
        else:
            return True

    def submit_delete_email(self):
        submit_button = self._wait_visibility_xpath("//div[@class='popup__controls']//button[contains(@class,'btn btn_main btn_stylish')]")
        submit_button.click()

    def cancel_delete_email(self):
        cancel_button = self._wait_visibility_xpath("//button[contains(@class,'btn btn_cancel')]")
        cancel_button.click()

    def is_email_alive(self, email):
        try:
            self._driver.find_element_by_link_text(email)
        except Ex.TimeoutException:
            return False
        else:
            return True

    def edit_email(self, email):
        links = self._driver.find_elements_by_xpath("//a[@class='b-settings-aliases__name js-edit']")
        for link in links:
            if link.get_attribute("data-id") == email:
                link.click()

    def is_edit_pop_up_open(self):
        try:
            self._wait_visibility_xpath("//div[contains(@class,'popup js-layer popup_dark popup_')]")
        except Ex.TimeoutException:
            return False
        else:
            return True

    def edit_comment(self, comment):
        input_field = self._wait_visibility_xpath("//input[@name='comment']")
        input_field.clear()
        input_field.send_keys(comment)

    def submit_edit(self):
        submit_button = self._wait_visibility_xpath("//div[contains(@class,'b-form__control b-form__control_main b-form__control_stylish')]//button[contains(@class,'btn btn_main btn_stylish')]")
        submit_button.click()

    def get_comment(self, email):
        settings_blocks = self._driver.find_elements_by_xpath("//div[@class='b-list__item__content']//div")
        for block in settings_blocks:
            if block.get_attribute("data-alias-id") == email:
                comment = self._wait_visibility_xpath("//div[@class='b-settings-aliases__comment']")
                return comment.text
        return "None"
