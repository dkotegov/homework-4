# coding=utf-8
from selenium.webdriver.common.by import By

from base import *


class BlogSelect(BaseElement):
    locator = (By.XPATH, "//a[@class='chzn-single']")


class BlogTitle(BaseElement):
    locator = None

    def __init__(self, driver, title):
        self.locator = (By.XPATH, "//li[text()='{}']".format(title))
        super(BlogTitle, self).__init__(driver)


class TopicTitleInput(BaseElement):
    locator = (By.XPATH, "//input[@id='id_title']")


class TopicTextArea(BaseElement):
    locator = (By.XPATH, "//textarea[@id='id_text']")


class H4Font(BaseElement):
    locator = (By.XPATH, "//a[@title='H4']")


class H5Font(BaseElement):
    locator = (By.XPATH, "//a[@title='H5']")


class H6Font(BaseElement):
    locator = (By.XPATH, "//a[@title='H6']")


class BoldFont(BaseElement):
    locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-bold')]/a")


class ItalicFont(BaseElement):
    locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-italic')]/a")


class StrokeFont(BaseElement):
    locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-stroke')]/a")


class UnderlineFont(BaseElement):
    locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-underline')]/a")


class QuoteFont(BaseElement):
    locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-quote')]/a")


class EditorCodeFont(BaseElement):
    locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-code')]/a")


class InsertCodeButton(BaseElement):
    locator = (By.XPATH, "//form[@id='code-language-list']/button[contains(@class, 'button-primary')]")


class OlList(BaseElement):
    locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-ol')]/a")


class UlList(BaseElement):
    locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-ul')]/a")


class PictureButton(BaseElement):
    locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-picture')]/a")


class PicureFromInternet(BaseElement):
    locator = (By.XPATH, "//li[@class='js-block-upload-img-item']/a")


class PictureInputAddress(BaseElement):
    locator = (By.XPATH, "//input[@id='img_url']")


class PictureCreateButton(BaseElement):
    locator = (By.XPATH, "//button[@id='submit-image-upload-link']")


class VideoButton(BaseElement):
    locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-video')]/a")


class LinkButton(BaseElement):
    locator = (By.XPATH, "//div[@id='container']//li[contains(@class,'editor-link')]/a")


class LinkInput(BaseElement):
    locator = (By.XPATH, "//input[@id='form-link']")


class LinkConfirmButton(BaseElement):
    locator = (By.XPATH, "//form[@id='block_upload_link']/button[contains(@class, 'button-primary')]")


class AddPollButton(BaseElement):
    locator = (By.XPATH, "//input[@name='add_poll']")


class DisableCommentButton(BaseElement):
    locator = (By.XPATH, "//input[@name='forbid_comment']")


class CreateButton(BaseElement):
    locator = (By.XPATH, "//button[contains(text(),'Создать')]")


class TopicCreatedNotice(BaseElement):
    locator = (By.XPATH, "//li[contains(text(), 'Топик успешно создан')]")


class TopicErrorNotice(BaseElement):
    locator = (By.XPATH, "//li[contains(text(), 'Это поле обязательно для заполнения.')]")


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
