from component import Component
from selenium.webdriver.support.ui import WebDriverWait

class Logout(Component):
    BASE = '//div[@id="PH_authView"] '
    SUBMIT = BASE + '//a[@id="PH_logoutLink"]'
    
    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()