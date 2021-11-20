from tests.pages.base import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class OrderingPage(Page):
    """
    Стриница оформления
    """

    INPUT_COMMENT = '//input[@id="input-comments"]'
    INPUT_ADDRESS = '//input[@id="input-address"]'
    INPUT_PHONE = '//input[@id="input-number"]'
    ORDER_PAGE = '//h1[@class="block-restaurant__name "]'
    BUTTON_SUBMIT = '//button[@id="button-order"]'
    MAIN_ERROR = '//p[@id="serverError"]'
    PHONE_ERROR = '//p[@id="input-numberError"]'

    def __init__(self, driver, order_id):
        self.order_id = order_id
        self.PATH = 'basket/' + str(order_id)
        super(OrderingPage, self).__init__(driver)

    def set_comment(self, comment):
        elem = self.driver.find_element_by_xpath(self.INPUT_COMMENT)
        elem.clear()
        elem.send_keys(comment)

    def set_phone(self, phone):
        elem = self.driver.find_element_by_xpath(self.INPUT_PHONE)
        elem.clear()
        elem.send_keys(phone)

    def set_address(self, address):
        elem = self.driver.find_element_by_xpath(self.INPUT_ADDRESS)
        elem.clear()
        elem.send_keys(address)

    def click_submit(self):
        self.driver.find_element_by_xpath(self.BUTTON_SUBMIT).click()

    def get_main_error(self):
        return self.driver.find_element_by_xpath(self.MAIN_ERROR).text

    def get_phone_error(self):
        return self.driver.find_element_by_xpath(self.PHONE_ERROR).text

    def wait_until_order_load(self):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.ORDER_PAGE)))

    def wait_page_load(self):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.BUTTON_SUBMIT)))
