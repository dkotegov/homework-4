# coding=utf-8
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from components.base_form import BaseForm


class FileAttachingForm(BaseForm):
    # file attach elements
    FILE_ATTACH_INPUT = '//button[@class="container--1mFoS type_wide--2rZSG color_base--3bx-5 hoverable--ys0Ko"]/input'
    # FILE_ATTACH_CHECK = '//div[@class="items--2iyAh"]/div[{}]'
    FILE_ATTACH_CHECK = '//div[@class="container_progress--2uptg"]'


    def send_keys_to_input(self, data):
        print 'sending keys to file attach input'
        self.file_attach_input_element.send_keys(data)

        class waiter(object):

            def __call__(self, driver):
                result = driver.find_element_by_xpath(FileAttachingForm.FILE_ATTACH_CHECK)
                print result
                return result

        WebDriverWait(self.driver, 10) \
            .until(waiter())

        # WebDriverWait(self.driver, 5) \
        #     .until(lambda driver: not driver.find_element_by_xpath(self.FILE_ATTACH_CHECK))

        # WebDriverWait(self.driver, 10) \
        #     .until(EC.presence_of_element_located((By.XPATH, self.FILE_ATTACH_CHECK)))


    def set_file_attach_input(self):
        try:
            self.file_attach_input_element = WebDriverWait(self.driver, 100) \
                .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_INPUT))
            print 'file attach input found'
        except WebDriverException:
            print 'file attach input element not found'



