from urllib.parse import urljoin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page(object):
    BASE_URL = 'https://geomap.2035school.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def waitRedirect(self, redirectUrl):
        return WebDriverWait(self.driver, 5, 0.1).until(EC.url_to_be(redirectUrl))

    def waitAlert(self):
        return WebDriverWait(self.driver, 5, 0.1).until(EC.alert_is_present())

    def do_not_wait_alert(self):
        try:
            alert = self.driver.switch_to.alert
            return alert
        except EC.NoAlertPresentException:
            return False

    def accept_alert_text(self):
        self.waitAlert()
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    def accept_alert_input(self, text):
        self.waitAlert()
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()


class wait_for_the_attribute_value(object):
    def __init__(self, locator, attribute, value):
        self.locator = locator
        self.attribute = attribute
        self.value = value

    def __call__(self, driver):
        try:
            element_attribute = EC._find_element(driver, self.locator).get_attribute(self.attribute)
            return element_attribute == self.value
        except EC.StaleElementReferenceException:
            return False


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_for_visible(self, xpath):
        WebDriverWait(self.driver, 5, 0.1).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def wait_for_presence(self, xpath):
        WebDriverWait(self.driver, 5, 0.1).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def do_not_wait_presence(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
            return False
        except EC.NoSuchElementException:
            return True
