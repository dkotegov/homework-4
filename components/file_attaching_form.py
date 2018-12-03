# coding=utf-8
import zipfile

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from components.base_form import BaseForm


class FileAttachingForm(BaseForm):
    # file attach elements
    FILE_ATTACH_INPUT = '//input[@data-test-id="attach-file"]'
    FILE_ATTACH_CHECK = '//div[@class="container_progress--2uptg"]'
    FILE_ATTACH_CLOUD_ICON = '//div[@class="container_link--bxJaw"]'
    FILE_ATTACH_PREVIEW = '//div[@class="item--1ZnwZ"]'
    FILE_ATTACHED = '//div[@data-test-id="attach:{}:loaded]'
    FILE_ATTACH_CLOUD_BTN = '//button[@data-test-id="attach-cloud"]'
    FILE_ATTACH_CLOUD_ELEMENT = '//div[@data-id="/{}"]'
    FILE_ATTACH_CLOUD_ATTACH = '//span[@data-qa-id="attach"]'
    FILE_ATTACH_CHECK_LOADED = '//div[@data-test-id="attach:{}:loaded"]'

    def send_keys_to_input(self, data, time_to_wait=3):
        file_attach_input_element = WebDriverWait(self.driver, time_to_wait) \
            .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_INPUT))
        file_attach_input_element.send_keys(data)

    def send_large_keys_to_input(self, data):
        zf = zipfile.ZipFile('./test_files/large_data.zip', mode='w', allowZip64=True)
        zf.write(data)
        zf.close()
        self.send_keys_to_input('large_data.zip')

    def set_file_attach_input(self):
        self.file_attach_input_element = WebDriverWait(self.driver, 3) \
            .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_INPUT))

    def check_loaded_through_cloud(self):
        try:
            return WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_CLOUD_ICON))
        except WebDriverException:
            return None

    def check_loaded(self, filename, timeout=2):
        try:
            WebDriverWait(self.driver, timeout) \
                .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_CHECK_LOADED.format(filename)))
            return True
        except Exception:
            return False

    def check_loaded_without_cloud(self):
        try:
            WebDriverWait(self.driver, 0) \
                .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_CLOUD_ICON))
            return False
        except WebDriverException:
            return True

    def check_file_attach_preview(self):
        try:
            return WebDriverWait(self.driver, 10) \
                .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_PREVIEW))
        except WebDriverException:
            return None

    def click_cloud_button(self):
        button = WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_CLOUD_BTN))
        button.click()

    def select_cloud_file(self, filename):
        fileElements = WebDriverWait(self.driver, 100) \
            .until(lambda driver: driver.find_elements_by_xpath(self.FILE_ATTACH_CLOUD_ELEMENT.format(filename)))
        fileElements[0].click()


    def do_cloud_attach(self):
        button = WebDriverWait(self.driver, 1) \
            .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_CLOUD_ATTACH))
        button.click()
