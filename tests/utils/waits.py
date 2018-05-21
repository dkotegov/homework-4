from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ElementsCountChanged(object):
    def __init__(self, locator, count):
        self.locator = locator
        self.count = count

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        if self.count != len(elements):
            return elements
        else:
            return False


def wait_until_url_changes(method_to_decorate):
    def wrapper(self, *args, **kwargs):
        url = self.driver.current_url
        method_to_decorate(self, *args, **kwargs)
        WebDriverWait(self.driver, 2, 0.2).until(EC.url_changes(url))

    return wrapper
