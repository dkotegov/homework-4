from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class CompanyCreateFormLocators:
    def __init__(self):
        self.root = "//div[@class='sum-form-wrap']"

        self.title = "//input[@id='organizationName']"
        self.description = '//textarea[@id="description"]'
        self.submit = '//button[@id="send-form-empl"]'
        self.browse_image_btn = '//input[@id="sum-img-load"]'

        self.error_message_title = '(//span[@class="error"])[1]'
        self.error_message_description = '(//span[@class="error"])[2]'
        self.error_message_server = '(//span[@class="error"])[4]'


class CompanyCreateForm(BaseComponent):
    def __init__(self, driver):
        super(CompanyCreateForm, self).__init__(driver)
        self.wait = WebDriverWait(self.driver, 10, 0.1)
        self.locators = CompanyCreateFormLocators()

        self.error_message = 'Поле обязательно для заполнения.'
        self.error_message_link = 'Неправильные значения полей: неверный формат ссылки'

    def set_input(self, locator: str, data: str):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator))
        ).send_keys(data)

    def submit(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.submit))
        ).click()

    def is_error_input(self, locator: str, error_message):
        try:
            _ = self.wait.until(
                EC.text_to_be_present_in_element((By.XPATH, locator), error_message)
            )
            return True
        except (TimeoutException, AssertionError):
            return False

    def wait_for_company_page(self):
        self.wait.until(
            EC.url_matches("https://studhunt.ru/company")
        )

    def load_image(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.browse_image_btn))
        ).send_keys('test_data/big_img.png')

    def set_title(self, title: str):
        self.set_input(self.locators.title, title)

    def set_description(self, description: str):
        self.set_input(self.locators.description, description)

    def is_title_error(self, expected_msg=None):
        msg = expected_msg if expected_msg is not None else self.error_message
        locator = self.locators.error_message_title if expected_msg is None else self.locators.error_message_server
        return self.is_error_input(locator, msg)

    @property
    def is_description_error(self):
        return self.is_error_input(self.locators.error_message_description, self.error_message)

    @property
    def is_link_error(self):
        return self.is_error_input(self.locators.error_message_server, self.error_message_link)
