from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class DefaultPage:
    URL = 'https://id.mail.ru/profile'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)


class DefaultSteps:
    TIME_FOR_WAIT = 1
    VISIBILITY_TIMEOUT = 30
    FREQUENCY = 0.1

    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(self.TIME_FOR_WAIT)

    def waiting_for_invisible(self, element):
        wait = WebDriverWait(self.driver, self.VISIBILITY_TIMEOUT, self.FREQUENCY)
        wait.until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, element)))

    def waiting_for_visible(self, element):
        wait = WebDriverWait(self.driver, self.VISIBILITY_TIMEOUT, self.FREQUENCY)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, element)))