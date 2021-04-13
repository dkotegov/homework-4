from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class ExperienceCreateFormLocators:
    def __init__(self):
        self.root = '//div[@class="popUp-main"]'

        self.submit = '//button[@class="btn-add-exp"]'
        self.close_btn = '//div[@class="popUp-main__exit"]'

        self.date_start = '//input[@id="start_work"]'
        self.date_end = '//input[@id="end_work"]'
        self.position = '//input[@id="position"]'
        self.name_job = '//input[@id="job"]'

        self.error_date = '(//span[@class="error"])[1]'
        self.error_position = '(//span[@class="error"])[4]'
        self.error_name_job = '(//span[@class="error"])[5]'


class ExperienceCreateForm(BaseComponent):
    def __init__(self, driver):
        super(ExperienceCreateForm, self).__init__(driver)
        self.locators = ExperienceCreateFormLocators()

        self.error_message_input = 'Поле обязательно для заполнения.'

    def form_is_open(self):
        try:
            self.driver.find_element_by_xpath(self.locators.root)
            return True
        except NoSuchElementException:
            return False

    def submit_exp(self):
        self.click_locator(self.locators.submit)

    def close_popup(self):
        self.click_locator(self.locators.close_btn)

    def is_date_error(self, error_message):
        return self.is_error_input(self.locators.error_date, error_message)

    def is_position_error(self):
        return self.is_error_input(self.locators.error_position, self.error_message_input)

    def is_name_job_error(self):
        return self.is_error_input(self.locators.error_name_job, self.error_message_input)

    def set_position(self, position: str):
        self.set_input(self.locators.position, position)

    def set_name_job(self, name_job: str):
        self.set_input(self.locators.name_job, name_job)

    def set_date_start(self, date_start: str):
        self.set_input(self.locators.date_start, date_start)

    def set_date_end(self, date_end: str):
        self.set_input(self.locators.date_end, date_end)

