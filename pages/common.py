from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Common:
    login_page = "https://mail.ru/"
    main_page = "https://otvet.mail.ru"
    wait_timeout = 10

    headliner_xpath = '// *[ @ id = "portal-headline"] / table / tbody / tr / td[1]'

    login_input_xpath = '//*[@id=\"mailbox:login-input\"]'
    password_button_xpath = '//*[@id="mailbox:submit-button"]/input'
    password_input_xpath = '//*[@id="mailbox:password-input"]'
    confirm_password_button_xpath = '//*[@id="mailbox:submit-button"]/input'
    letter_line = 'dataset-letters'

    logout_button_xpath = '//*[@id="PH_logoutLink"]'

    def __init__(self, browser):
        self.browser = browser

    def open_page(self, url):
        self.browser.get(url)
        WebDriverWait(self.browser, self.wait_timeout).until(
            EC.presence_of_element_located((By.XPATH, self.headliner_xpath)))

    def login(self, login, password):
        self.open_page(self.login_page)
        WebDriverWait(self.browser, self.wait_timeout).until(
            EC.element_to_be_clickable((By.XPATH, self.login_input_xpath)))

        self.browser.find_element_by_xpath(self.login_input_xpath).clear()
        self.browser.find_element_by_xpath(self.login_input_xpath).send_keys(login)
        self.browser.find_element_by_xpath(self.password_button_xpath).click()
        WebDriverWait(self.browser, self.wait_timeout).until(
            EC.element_to_be_clickable((By.XPATH, self.password_input_xpath)))

        self.browser.find_element_by_xpath(self.password_input_xpath).clear()
        self.browser.find_element_by_xpath(self.password_input_xpath).send_keys(password)
        self.browser.find_element_by_xpath(self.confirm_password_button_xpath).click()

        WebDriverWait(self.browser, self.wait_timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.letter_line)))

    def logout(self):
        self.open_page(self.main_page)
        self.browser.find_element_by_xpath(self.logout_button_xpath).click()
