from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def wait_for_element_by(driver, selector, by):
    return WebDriverWait(driver, 10, 0.1).until(
        expected_conditions.visibility_of_element_located((by, selector))
    )


def wait_for_element_by_selector(driver, selector):
    return wait_for_element_by(driver, selector, By.CSS_SELECTOR)


def wait_click_for_element_by_selector(driver, selector):
    wait_for_element_by_selector(driver, selector)
    driver.find_element_by_css_selector(selector).click()


def wait_for_url(driver, url):
    return WebDriverWait(driver, 10, 0.1).until(
        expected_conditions.url_to_be(url)
    )
