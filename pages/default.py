import urllib.parse as urlparse

class Page(object):
    BASE_URL = 'https://cloud.mail.ru/'
    PATH = ''

    AUTH_URL = 'https://account.mail.ru'
    AUTH_LOGIN = 'input[name="username"]'
    AUTH_PASSWORD = 'input[name="password"]'
    AUTH_NEXT_BUTTON = '[data-test-id="next-button"]'
    AUTH_SUBMIT_BUTTON = '[data-test-id="submit-button"]'
    USER_EMAIL_HEADER = '[data-testid="whiteline-account"]'

    def set_login(self, login):
        self.driver.find_element_by_css_selector(self.AUTH_LOGIN).send_keys(login)

    def continue_authorize(self):
        self.driver.find_element_by_css_selector(self.AUTH_NEXT_BUTTON).click()

    def set_password(self, pwd):
        self.driver.find_element_by_css_selector(self.AUTH_PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_css_selector(self.AUTH_SUBMIT_BUTTON).click()

    def waitForAuthorize(self):
        self.driver.find_element_by_css_selector(self.USER_EMAIL_HEADER).click()



    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def openAuthorize(self):
        url = urlparse.urljoin(self.AUTH_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()