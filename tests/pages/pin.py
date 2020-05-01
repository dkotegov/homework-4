from selenium.webdriver.common.by import By

from tests.pages.base import Page
from tests.pages.component import FormComponent


class PinDetailsPage(Page):
    PATH = '/pin/{0}'

    ROOT = {
        'method': By.XPATH,
        'key': Page.get_xpath_visible('//div[@id="viewpin-page"]')
    }

    def __init__(self, driver, open=True, pin_id=''):
        Page.__init__(self, driver)
        if open:
            self.open(pin_id)

    @property
    def form(self):
        return PinForm(self.driver)


class PinForm(FormComponent):
    title = '.viewpin-block__right-column__title'
    tag = '.viewpin-block__right-column__context'
    comment_area = 'commentTextArea/pin/'

    def get_title(self):
        return self.find_element(By.CSS_SELECTOR, self.title).text

    def get_tag(self):
        return self.find_element(By.CSS_SELECTOR, self.tag).text

    def set_comment(self, query, pin_id):
        comment_area = '//textarea[@id="commentTextArea/pin/' + str(pin_id) + '"]'
        self.fill_input(self.driver.find_element_by_xpath(comment_area), query)

    def send_comment(self):
        comment_area = '//input[@class="viewpin-form__send-comment comment_margin"]'
        self.driver.find_element_by_xpath(comment_area).click()

    def save_pin(self):
        save_button = '//input[@class="viewpin-block__right-column__buttom-save viewpin-block__right-column__buttom-save_pos"]'
        self.driver.find_element_by_xpath(save_button).click()

    def set_board(self, pin_id, board_id):
        select = self.driver.find_element_by_id('pinviewBoardselect/pin/' + str(pin_id))
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options:
            if option.get_attribute('value') == board_id:
                option.click()
                return

    def wait_for_load(self):
        self.wait_for_presence(By.CSS_SELECTOR, self.title)
