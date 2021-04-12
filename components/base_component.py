from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BaseComponent(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.1)

    def set_input(self, locator: str, data: str):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator))
        ).send_keys(data)

    def submit(self, locator):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator))
        ).click()

    def is_error_input(self, locator: str, error_message):
        try:
            _ = self.wait.until(
                EC.text_to_be_present_in_element((By.XPATH, locator), error_message)
            )
            return True
        except TimeoutException:
            return False
