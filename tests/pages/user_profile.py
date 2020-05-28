from selenium.webdriver.common.by import By
from tests.pages.base import Page
from tests.pages.component import FormComponent


class ProfilePage(Page):
    PATH = "/profile"
    ROOT = {"method": By.ID, "key": "profile-page"}

    def __init__(self, driver, open=True):
        Page.__init__(self, driver)
        if open:
            self.open()

    @property
    def form(self):
        return ProfileForm(self.driver)

    @property
    def header_form(self):
        return HeaderForm(self.driver)


class ProfileForm(FormComponent):
    question_btn = '//img[@id="buttonForAsk"]'
    question_field = '//textarea[@id="profileMessageTextArea"]'
    submit_button = '//input[@class="feedback__form__button"]'
    question_id = 'profileMessageTextArea'

    def set_question(self, question):
        self.fill_input(
            self.driver.find_element_by_xpath(self.question_field), question
        )

    def submit_message_button(self):
        self.driver.find_element_by_xpath(self.question_btn).click()

    def submit_send_button(self):
        self.driver.find_element_by_xpath(self.submit_button).click()

    def get_message_from_field(self):
        self.submit_message_button()
        self.submit_message_button()
        return self.driver.find_element_by_xpath(self.question_field).get_attribute('value')
