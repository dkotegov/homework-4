# coding=utf-8



from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from components.base_form import BaseForm


class FileAttachingForm(BaseForm):
    # file attach elements
    FILE_ATTACH_INPUT = '//button[@class="container--1mFoS type_wide--2rZSG color_base--3bx-5 hoverable--ys0Ko"]/input'

    def send_keys_to_input(self, data):
        print 'sending keys to file attach input'
        self.file_attach_input_element.send_keys(data)


        # TODO дождаться загрузки файла!

        # WebDriverWait(self.driver, 30) \
        #     .until(lambda _ :

    def set_file_attach_input(self):
        try:
            self.file_attach_input_element = WebDriverWait(self.driver, 100) \
                .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_INPUT))
            print 'file attach input found'
        except WebDriverException:
            print 'file attach input element not found'
