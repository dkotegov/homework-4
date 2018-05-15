from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class BaseElement(object):
    
    def __init__(self, driver):
        self.driver = driver

    def get_button_by_xpath(self, xpath):
        return WebDriverWait(self.driver, 30, 0.3).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
            
    def get_field_by_xpath(self, xpath):
        return WebDriverWait(self.driver, 30, 0.3).until(
            EC.visibility_of_element_located((By.XPATH, xpath)))
    
   
    def get_hidden_input_by_xpath(self, xpath):
        return WebDriverWait(self.driver, 30, 0.3).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
    
    def existance_of_element_in_dom_by_xpath(self, xpath):
        try:
            return WebDriverWait(self.driver, 7, 0.3).until(
            EC.staleness_of(WebDriverWait(self.driver, 7, 0.3).until(
            EC.presence_of_element_located((By.XPATH, xpath)))))
        except TimeoutException as e:
            return True
        
    def invisibility_of_element_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 10, 0.5).until(
            EC.invisibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException as e:
            return False
        return True

    def existance_of_element_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 5, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException as e:
            return False
        return True