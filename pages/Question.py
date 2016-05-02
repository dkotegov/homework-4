from selenium.webdriver import ActionChains

from pages.Common import Page, Element


class OtvetPageAsk(Page):
    PATH = "ask"

    def ask_form(self):
        return AskForm(self.driver)


class AskForm(Element):
    ASK_AREA_QUESTION_TITLE_NAME = "qtext"
    ASK_AREA_TEXT_NAME = "text"
    ASK_UPLOAD_PHOTO_BUTTON_CLASS = "action--upload-photo"
    ASK_UPLOAD_PHOTO_NAME = "file"
    # SUBMIT = "//button[@class='ask-btn-submit']"
    SUBMIT_CLASS = "ask-btn-submit"
    OPTION_VALUE = "//option[@value='2013']"
    OPTION_SUB_CATEGORY_VALUE = "//option[@value='1331']"
    SELECT_CATEGORY_ID = "ask-categories"
    SELECT_SUBCATEGORY_ID = "ask-sub-category"

    def __init__(self, driver):
        super(AskForm, self).__init__(driver)
        self.form = self.driver.find_element_by_class_name("ask-form")

    def set_question_title(self, qtext):
        self.form.find_element_by_name(self.ASK_AREA_QUESTION_TITLE_NAME).send_keys(qtext)

    def set_text(self, text):
        self.form.find_element_by_name(self.ASK_AREA_TEXT_NAME).send_keys(text)

    def set_category(self):
        category = self.form.find_element_by_id(self.SELECT_CATEGORY_ID)
        category.find_element_by_xpath(self.OPTION_VALUE).click()

    def set_subcategory(self):
        category = self.form.find_element_by_id(self.SELECT_SUBCATEGORY_ID)
        category.find_element_by_xpath(self.OPTION_SUB_CATEGORY_VALUE).click()

    def add_picture(self, path):
        self.form.find_element_by_class_name(self.ASK_UPLOAD_PHOTO_BUTTON_CLASS).click()
        self.driver.find_element_by_name(self.ASK_UPLOAD_PHOTO_NAME).send_keys(path)

    def submit(self):
        el = self.driver.find_element_by_class_name(self.SUBMIT_CLASS)
        actions = ActionChains(self.driver)
        actions.move_to_element(el)
        actions.click(el)
        actions.perform()

    def is_picture_setted(self):
        self.form = self.driver.find_element_by_class_name("ask-form")
        self.driver.implicitly_wait(1)
        return self.form.find_element_by_tag_name("img") is not None

    def is_symbol_extra_enabled(self):
        return self.form.find_element_by_class_name("count-symbol-extra") is not None
