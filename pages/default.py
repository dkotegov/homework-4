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
    SELECT_ALL = 'div[data-name="selectAll"]'
    REMOVE = 'div[data-name="remove"]'
    SUBMIT = 'div[id="react-modals"] button[data-name="confirm"]'
    COUNTER = 'span[class*="Toolbar__count"]'
    FILES = 'a[data-id^="/"]'
    FAV_FILES = []
    ALL_FILES = []

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def set_login(self, login):
        self.driver.find_element_by_css_selector(self.AUTH_LOGIN).send_keys(login)

    def continue_authorize(self):
        self.driver.find_element_by_css_selector(self.AUTH_NEXT_BUTTON).click()

    def set_password(self, pwd):
        self.driver.find_element_by_css_selector(self.AUTH_PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_css_selector(self.AUTH_SUBMIT_BUTTON).click()

    def wait_for_authorize(self):
        self.driver.find_element_by_css_selector(self.USER_EMAIL_HEADER).click()

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def open_alternative(self, alternative):
        url = urlparse.urljoin(self.BASE_URL, alternative)
        self.driver.get(url)
        self.driver.maximize_window()

    def open_authorize(self):
        url = urlparse.urljoin(self.AUTH_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def select_all(self):
        self.driver.find_element_by_css_selector(self.SELECT_ALL).click()

    def remove(self):
        try:
            self.driver.find_element_by_css_selector(self.REMOVE).click()
        except Exception:
            return False
        return True

    def remove_submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()

    def get_amount_of_files(self):
        return self.driver.find_element_by_css_selector(self.COUNTER).text

    def switch_to_nth_tab(self, n):
        self.driver.switch_to.window(self.driver.window_handles[n])

    def get_favorites(self):
        self.FAV_FILES = []
        try:
            for file_elem in self.driver.find_elements_by_css_selector(self.FILES):
                self.FAV_FILES.append(file_elem.get_attribute('data-id'))
        except Exception:
            return

    def get_all_files(self):
        self.ALL_FILES = []
        try:
            for file_elem in self.driver.find_elements_by_css_selector(self.FILES):
                self.ALL_FILES.append(file_elem.get_attribute('data-id'))
        except Exception:
            return