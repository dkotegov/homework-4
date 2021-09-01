from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.main_page import Page


class AuthPage(Page):
    SUBMIT_IN = '//a[@data-action="login"]'
    LOGINS = '//input[@placeholder="Имя аккаунта"]'
    ADS = '//a[@class="summer-banner js-action-banner"]'
    SUBMIT_SIGIN = '//button[@data-test-id="next-button"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//button[@data-test-id="submit-button"]'
    LOGOUT = '//button[text()="Выйти"]'
    ENTRY = '//button[text()="Войти"]'
    LOG_CHECK = '//i[@id="PH_user-email"]'
    ERROR_MSG = '//div[@class="base-0-2-118 small-0-2-125 error-0-2-131"]'
    CLOUD = '//a[@data-click-counter="357831072, 61021866"]'
    NAV_FOLDERS = '//div[@class="nav-folders"]'

    def open_window_logins(self):
        self.driver.find_element_by_xpath(self.SUBMIT_IN).click()

    def ads_page(self):
        try:
            self.driver.find_element_by_xpath(self.ADS)
            return True
        except NoSuchElementException:
            return False

    def swap(self):
        self.driver.switch_to.frame(0)

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGINS).send_keys(login)

    def open_window_sign_in(self):
        self.driver.find_element_by_xpath(self.SUBMIT_SIGIN).click()

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def open_cloud(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.NAV_FOLDERS)))
        self.driver.find_element_by_xpath(self.CLOUD).click()

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.LOGOUT).click()

    def check_log(self):
        return self.driver.find_element_by_xpath(self.LOG_CHECK).text

    def get_current_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_MSG).text
