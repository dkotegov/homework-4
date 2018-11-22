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
    FILE_ATTACH_INPUT = '//input[@data-test-id="attach-file"]'
    FILE_ATTACH_CHECK = '//div[@class="container_progress--2uptg"]'
    FILE_ATTACH_CLOUD_ICON = '//div[@class="container_link--bxJaw"]'
    # FILE_ATTACH_CHECK_NOT_CLOUD = '//div[@class="item--3fh5V"]/div/div'
    FILE_ATTACH_PREVIEW = '//div[@class="item--1ZnwZ"]'

    FILE_ATTACHED = '//div[@data-test-id="attach:{}:loaded]'

    FILE_ATTACH_CLOUD_BTN = '//button[@data-test-id="attach-cloud"]'
    FILE_ATTACH_CLOUD_ELEMENT = '//div[@data-id="/{}"]'
    FILE_ATTACH_CLOUD_ATTACH = '//span[@data-qa-id="attach"]'
    FILE_ATTACH_CHECK_LOADED = '//div[@data-test-id="attach:{}:loaded"]'

    def send_keys_to_input(self, data, time_to_wait=3):
        print 'sending keys to file attach input'

        file_attach_input_element = WebDriverWait(self.driver, time_to_wait) \
            .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_INPUT))

        file_attach_input_element.send_keys(data)

        print 'sent!'

        # try:
        #     WebDriverWait(self.driver, time_to_wait) \
        #         .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACHED.format(data)))
        # except WebDriverException:
        #     print 'file not attached'

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
            self.file_attach_input_element = WebDriverWait(self.driver, 3) \
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

    def check_loaded(self, filename, timeout=2):
        try:
            WebDriverWait(self.driver, timeout) \
                .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_CHECK_LOADED.format(filename)))
            return True
        except Exception, e:
            print 'file not attached: ' + str(e)
            return False

    def check_loaded_without_cloud(self):

        # try:
        #     print 'checking loaded without cloud'
        #     self.driver.find_element_by_xpath(self.FILE_ATTACH_CLOUD_ICON)
        #     return False
        # except WebDriverException:
        #     print 'checked'
        #     return True
        # TODO разобраться, почему проверят так долго!
        try:
            print 'checking loaded without cloud'
            WebDriverWait(self.driver, 0) \
                .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_CLOUD_ICON))
            print 'some mistake in check_loaded_without_cloud'
            return False
        except WebDriverException:
            print 'checked'
            return True

    def check_file_attach_preview(self):
        try:
            return WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_PREVIEW))
        except WebDriverException:
            print 'file attach preview not found'
            return None

    def click_cloud_button(self):
        button = WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_CLOUD_BTN))
        button.click()

    def select_cloud_file(self, filename):
        print self.FILE_ATTACH_CLOUD_ELEMENT.format(filename)
        try:
            fileElements = WebDriverWait(self.driver, 100) \
                .until(lambda driver: driver.find_elements_by_xpath(self.FILE_ATTACH_CLOUD_ELEMENT.format(filename)))
            fileElements[0].click()
        except Exception, e:
            print e.message


    def do_cloud_attach(self):
        button = WebDriverWait(self.driver, 1) \
            .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_CLOUD_ATTACH))
        button.click()
