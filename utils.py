from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def wait_for_element_by(driver, selector, by):
    WebDriverWait(driver, 10, 0.1).until(
        expected_conditions.visibility_of_element_located((by, selector))
    )


def wait_for_element_by_selector(driver, selector):
    WebDriverWait(driver, 10, 0.1).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector))
    )


def wait_for_url(driver, url):
    WebDriverWait(driver, 10, 0.1).until(
        expected_conditions.url_to_be(url)
    )
