from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Common:
    LOGIN_PAGE = 'https://mail.ru/'
    MAIN_PAGE = 'https://otvet.mail.ru'
    WAIT_TIMEOUT = 20

    HEADLINER_XPATH = '//div[@id="portal-headline"]'
    LOGIN_INPUT_XPATH = '//*[@id="mailbox:login-input"]'
    PASSWORD_BUTTON_XPATH = '//*[@id="mailbox:submit-button"]/input'
    PASSWORD_INPUT_XPATH = '//*[@id="mailbox:password-input"]'
    CONFIRM_PASSWORD_BUTTON_XPATH = '//*[@id="mailbox:submit-button"]/input'
    LOGOUT_BUTTON_XPATH = '//*[@id="PH_logoutLink"]'
    LETTER_LINE = 'dataset-letters'

    def __init__(self, browser):
        self.browser = browser

    def open_page(self, url):
        self.browser.get(url)
        WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, self.HEADLINER_XPATH)))

    def login(self, login, password):
        self.open_page(self.LOGIN_PAGE)
        WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, self.LOGIN_INPUT_XPATH)))

        self.browser.find_element_by_xpath(self.LOGIN_INPUT_XPATH).clear()
        self.browser.find_element_by_xpath(self.LOGIN_INPUT_XPATH).send_keys(login)
        self.browser.find_element_by_xpath(self.PASSWORD_BUTTON_XPATH).click()
        WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, self.PASSWORD_INPUT_XPATH)))

        self.browser.find_element_by_xpath(self.PASSWORD_INPUT_XPATH).clear()
        self.browser.find_element_by_xpath(self.PASSWORD_INPUT_XPATH).send_keys(password)
        self.browser.find_element_by_xpath(self.CONFIRM_PASSWORD_BUTTON_XPATH).click()

        WebDriverWait(self.browser, self.WAIT_TIMEOUT).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.LETTER_LINE)))

    def logout(self):
        self.open_page(self.MAIN_PAGE)
        self.browser.find_element_by_xpath(self.LOGOUT_BUTTON_XPATH).click()
