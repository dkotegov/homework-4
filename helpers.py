from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_element(driver, selector):
    return WebDriverWait(driver, 30, 0.1).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector))
    )

def wait(driver, wait_until=None, timeout=15):
    return WebDriverWait(driver, timeout).until(wait_until)

def wait_redirect(driver, url=None):
    if url is None:
        wait(driver, expected_conditions.url_changes(driver.current_url))
    else:
        wait(driver, expected_conditions.url_matches(url))