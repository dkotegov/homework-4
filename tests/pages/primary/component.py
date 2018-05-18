from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def hover(self, element_xpath):
        WebDriverWait(self.driver, 20, 0.1).until(
            EC.presence_of_element_located((By.XPATH, element_xpath))
        )
        element = self.driver.find_element_by_xpath(element_xpath)

        from selenium.webdriver import ActionChains
        hov = ActionChains(self.driver).move_to_element(element)
        hov.perform()

    def hover_css(self, element_css):
        try:
            WebDriverWait(self.driver, 20, 0.1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, element_css))
            )
            element = self.driver.find_element_by_css_selector(element_css)
            from selenium.webdriver import ActionChains
            hov = ActionChains(self.driver).move_to_element(element)
            hov.perform()
        except TimeoutException:
            return 0
