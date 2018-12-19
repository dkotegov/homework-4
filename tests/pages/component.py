from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def get_elem_by_id(self, id_elem):
        return self.driver.find_element_by_id(id_elem)

    def get_one_elem_by_css(self, css_selector):
        return self.driver.find_element_by_css_selector(css_selector)

    def get_last_elem_by_css(self, css_selector):
        return self.driver.find_elements_by_css_selector(css_selector)[-1]

    def get_length_of_elem_list_by_css(self, css_selector):
        return len(self.driver.find_elements_by_css_selector(css_selector))

    def alert_accept(self):
        try:
            WebDriverWait(self.driver, 10, 0.1).until(
                EC.alert_is_present()
            )
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            alert_text = "no alert"
        return alert_text

    def alert_input_and_accept(self, input_int):
        try:
            WebDriverWait(self.driver, 10, 0.1).until(
                EC.alert_is_present()
            )
            alert = self.driver.switch_to.alert
            alert.send_keys(str(input_int))
            alert.accept()
        except TimeoutException:
            print "no alert"
