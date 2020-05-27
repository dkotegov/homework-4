from selenium.webdriver.common.by import By
from tests.pages.base import Page
from tests.pages.component import FormComponent
from tests.pages.solarsunrise_urls import IndexPage, DialogPage, AuthPage


class ProfilePage(Page):
    PATH = '/profile'
    ROOT = {
        'method': By.ID,
        'key': 'profile-page'
    }

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
        self.fill_input(self.driver.find_element_by_xpath(self.question_field), question)

    def submit_message_button(self):
        self.driver.find_element_by_xpath(self.question_btn).click()

    def submit_send_button(self):
        self.driver.find_element_by_xpath(self.submit_button).click()

    def get_message_from_field(self):
        self.submit_message_button()
        self.submit_message_button()
        return self.driver.find_element_by_xpath(self.question_field).get_attribute('value')


class HeaderForm(ProfileForm):
    index_btn = '//a[@href="/index/new"]'
    profile_btn = '//a[@href="/profile"]'
    messages_btn = '//a[@href="/dialog"]'
    exit_btn = '//ul[@id="headerSettingsView"]/li/a[@href="/login"]'

    def go_to_index(self):
        self.submit(self.index_btn)
        IndexPage(self.driver, open=False).wait_for_load()

    def go_to_profile(self):
        self.submit(self.profile_btn)
        ProfilePage(self.driver, open=False).wait_for_load()

    def go_to_dialog(self):
        self.submit(self.messages_btn)
        DialogPage(self.driver, open=False).wait_for_load()

    def go_to_exit(self):
        self.submit(self.menu_btn)
        self.submit(self.exit_btn)
        AuthPage(self.driver, open=False).wait_for_load()
