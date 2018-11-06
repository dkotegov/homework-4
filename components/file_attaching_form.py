# coding=utf-8
import zipfile

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
    FILE_ATTACH_CLOUD_ICON = '//div[@class="container_link--bxJaw"]'
    # FILE_ATTACH_CHECK_NOT_CLOUD = '//div[@class="item--3fh5V"]/div/div'
    FILE_ATTACH_PREVIEW = '//div[@class="item--1ZnwZ"]'


    def send_keys_to_input(self, data):
        print 'sending keys to file attach input'
        self.file_attach_input_element.send_keys(data)

        # class waiter(object):
        #     def __call__(self, driver):
        #         return not driver.find_element_by_xpath(FileAttachingForm.FILE_ATTACH_CHECK)
        #
        # try:
        #     WebDriverWait(self.driver, 10) \
        #         .until(waiter())
        # except WebDriverException:
        #     print 'unable to send keys to input'


    def send_large_keys_to_input(self, data):
        print 'large file!!!'

        zf = zipfile.ZipFile('./test_files/large_data.zip', mode='w', allowZip64=True)
        zf.write(data)
        zf.close()

        self.send_keys_to_input('large_data.zip')

    def set_file_attach_input(self):
        try:
            self.file_attach_input_element = WebDriverWait(self.driver, 100) \
                .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_INPUT))
            print 'file attach input found'
        except WebDriverException:
            print 'file attach input element not found'

    def check_loaded_through_cloud(self):
        try:
            return WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_CLOUD_ICON))

        except WebDriverException:
            print 'file loaded not through cloud'
            return None

    def check_loaded_without_cloud(self):

        try:
            WebDriverWait(self.driver, 5) \
                .until_not(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_CLOUD_ICON))
            return True
        except WebDriverException:
            return False
            print 'some mistake in check_loaded_without_cloud'

    def check_file_attach_preview(self):
        try:
            return WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_PREVIEW))
        except WebDriverException:
            print 'file attach preview not found'
            return None
