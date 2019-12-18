from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import string
import random

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


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

def wait_for_element_by_selector(driver, selector, visible=True):
    if visible:
        return WebDriverWait(driver, 30, 0.1).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector))
        )
    else:
        return WebDriverWait(driver, 30, 0.1).until(
            expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, selector))
        )

def wait_for_element_by_xpath(driver, xpath, visible=True):
    if visible:
        return WebDriverWait(driver, 30, 0.1).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath))
        )
    else:
        return WebDriverWait(driver, 30, 0.1).until(
            expected_conditions.invisibility_of_element_located((By.XPATH, xpath))
        )  

# def wait_redirect(self, url = None):
#     if url is None:
#         self.wait(expected_conditions.url_changes(self.driver.current_url))
#     else:
#         self.wait(expected_conditions.url_to_be(url))

# def wait_for_css_selector(self, selector = None):
#     if selector is None:
#         self.wait(expected_conditions.url_changes(self.driver.current_url))
#     else:
#         return WebDriverWait(self.driver, 10).until(
#             expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector))
#         )      