# coding=utf-8
import time
 
from selenium.webdriver.common.by import By

from base import BaseElement
 
 
class SendMessageElements(BaseElement):
 
    def send_to(self):
        self.locator = (By.XPATH, "//textarea[@data-original-name='To']")
        return self

    def send_subject(self):
        self.locator = (By.XPATH, "//input[@name='Subject']")
        return self


    def send_text(self):
        iframes = self.driver.find_elements_by_tag_name('iframe')
        iframe = iframes[len(iframes) - 1]
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe)
        self.locator = (By.XPATH, "//body[@id='tinymce']")
        return self
 
    def send_button(self):
        self.driver.switch_to_default_content()
        self.locator = (By.XPATH, "//div[@data-name='send']")
        return self