# coding=utf-8
from selenium.webdriver.common.by import By

from base import *


class CreateTopicPage(BaseElement):

    def block_select(self):
        self.locator = (By.XPATH, "//a[@class='chzn-single']")
        return self

    def block_title(self, title):
        self.locator = (By.XPATH, "//li[text()='{}']".format(title))
        return self

    def topic_title_input(self):
        self.locator = (By.XPATH, "//input[@id='id_title']")
        return self

    def topic_text_area(self):
        self.locator = (By.XPATH, "//textarea[@id='id_text']")
        return self

    def h4_font_button(self):
        self.locator = (By.XPATH, "//a[@title='H4']")
        return self

    def h5_font_button(self):
        self.locator = (By.XPATH, "//a[@title='H5']")
        return self

    def h6_font_button(self):
        self.locator = (By.XPATH, "//a[@title='H6']")
        return self

    def bold_font_button(self):
        self.locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-bold')]/a")
        return self

    def italic_font_button(self):
        self.locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-italic')]/a")
        return self

    def stroke_font_button(self):
        self.locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-stroke')]/a")
        return self

    def underline_font_button(self):
        self.locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-underline')]/a")
        return self

    def quote_font_button(self):
        self.locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-quote')]/a")
        return self

    def editor_code_font_button(self):
        self.locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-code')]/a")
        return self

    def insert_code_button(self):
        self.locator = (By.XPATH, "//form[@id='code-language-list']/button[contains(@class, 'button-primary')]")
        return self

    def picture_button(self):
        self.locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-picture')]/a")
        return self

    def picture_from_internet_button(self):
        self.locator = (By.XPATH, "//li[@class='js-block-upload-img-item']/a")
        return self

    def picture_address_input(self):
        self.locator = (By.XPATH, "//input[@id='img_url']")
        return self

    def picture_create_button(self):
        self.locator = (By.XPATH, "//button[@id='submit-image-upload-link']")
        return self

    def link_confirm_button(self):
        self.locator = (By.XPATH, "//form[@id='block_upload_link']/button[contains(@class, 'button-primary')]")
        return self

    def add_poll_button(self):
        self.locator = (By.XPATH, "//input[@name='add_poll']")
        return self

    def disable_comment_button(self):
        self.locator = (By.XPATH, "//input[@name='forbid_comment']")
        return self

    def disable_publish_button(self):
        self.locator = (By.XPATH, "//input[@name='publish']")
        return self

    def create_button(self):
        self.locator = (By.XPATH, "//button[contains(text(),'Создать')]")
        return self

    def topic_created_notice(self):
        self.locator = (By.XPATH, "//li[contains(text(), 'Топик успешно создан')]")
        return self

    def topic_error_notice(self):
        self.locator = (By.XPATH, "//li[contains(text(), 'Это поле обязательно для заполнения.')]")
        return self


class CreatePollBlock(BaseElement):
    locator = (By.XPATH, "//div[@class='poll-create']")

    class PollHeaderInput(BaseElement):
        locator = (By.XPATH, "//div[@class='poll-create']//input[@id='id_question']")

    class PollAnswerInput(BaseElement):
        def __init__(self, driver, order):
            self.locator = (By.XPATH, "//div[@class='poll-create']//input[@id='id_form-{}-answer']".format(order))
            super(CreatePollBlock.PollAnswerInput, self).__init__(driver)

    def get_header_input(self):
        return self.PollHeaderInput(self.driver).wait_for_visible().get()

    def get_answer_input(self, order):
        return self.PollAnswerInput(self.driver, order).wait_for_visible().get()


class Alert(object):
    @staticmethod
    def wait_for_alert(driver):
        return WebDriverWait(driver, BaseElement.DEFAULT_WAIT_TIME, 0.1).until(
            EC.alert_is_present()
        )
