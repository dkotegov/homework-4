from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

TIMEOUT = 5
POLL_FREQUENCY = 0.1


# element can be selector or xpath
def wait_for_visible(driver, element, by=By.CSS_SELECTOR, timeout=TIMEOUT):
    return WebDriverWait(driver, timeout, POLL_FREQUENCY).until(
        expected_conditions.visibility_of_element_located((by, element)))


def if_element_exists(driver, element, by=By.CSS_SELECTOR):
    try:
        wait_for_visible(driver, element, by, timeout=2)
        return True
    except TimeoutException:
        return False
