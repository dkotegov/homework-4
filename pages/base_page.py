from components.container_component import Container
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Page(object):
    BASE_URL = 'https://id.mail.ru/'
    PATH = ''
    ROOT = '#root'
    TIME_FOR_WAIT = 1
    VISIBILITY_TIMEOUT = 30
    FREQUENCY = 0.1

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(self.TIME_FOR_WAIT)
        self.container = Container(self)
        self.container.set_root(self.ROOT)

    def waiting_for_invisible_by_selector(self, element):
        wait = WebDriverWait(self.driver, self.VISIBILITY_TIMEOUT, self.FREQUENCY)
        wait.until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, element)))

    def waiting_for_invisible_by_text(self, element):
        wait = WebDriverWait(self.driver, self.VISIBILITY_TIMEOUT, self.FREQUENCY)
        wait.until(expected_conditions.invisibility_of_element_located((By.LINK_TEXT, element)))

    def wait_for_clickable_by_selector(self, element):
        wait = WebDriverWait(self.driver, self.VISIBILITY_TIMEOUT, self.FREQUENCY)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, element)))

    def waiting_for_visible_by_selector(self, element):
        wait = WebDriverWait(self.driver, self.VISIBILITY_TIMEOUT, self.FREQUENCY)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, element)))

    def waiting_for_visible_by_id(self, element):
        wait = WebDriverWait(self.driver, self.VISIBILITY_TIMEOUT, self.FREQUENCY)
        wait.until(expected_conditions.visibility_of_element_located((By.ID, element)))

    def waiting_for_visible_by_xpath(self, element):
        wait = WebDriverWait(self.driver, self.VISIBILITY_TIMEOUT, self.FREQUENCY)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, element)))

    def wait_for_url(self, url):
        wait = WebDriverWait(self.driver, self.VISIBILITY_TIMEOUT, self.FREQUENCY)
        wait.until(
            lambda driver: driver.current_url == url)
