from tests.personal_data.page_component import Page, Component
from selenium.webdriver.support.ui import WebDriverWait


class MainForm(Component):
    PERSONAL_DATA = '//*[@data-test-id="personal-card"]//*[@data-test-id="card-footer"]'
    CONTACTS = '//*[@data-test-id="contacts-card"]//*[@data-test-id="card-footer"]'
    PERSONAL_DATA_CONTAINER = '//*[@data-test-id="mailid-profile-container"]'
    CONTACTS_CONTAINER = '//*[@data-test-id="mailId-contacts-wrapper"]'

    def open_contacts(self):
        contacts_link = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CONTACTS)
        )

        contacts_link.click()

    def open_personal_data(self):
        personal_data_link = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PERSONAL_DATA)
        )

        personal_data_link.click()

    def check_personal_data_opened(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PERSONAL_DATA_CONTAINER)
        )

    def check_contacts_opened(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CONTACTS_CONTAINER)
        )


class MainPage(Page):
    PATH = ''

    @property
    def form(self):
        return MainForm(self.driver)
