from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT = 30
POLL_FREQUENCY = 0.1


# element can be selector or xpath
def wait_for_visible(driver, element, by=By.CSS_SELECTOR):
    return WebDriverWait(driver, TIMEOUT, POLL_FREQUENCY)\
        .until(expected_conditions.visibility_of_element_located((by, element)))
