from random import randrange

from consts import TEST_PRODUCT
from helpers import Page, Component
from components import Login


class Photos(Component):
    PREVIEW = ".slider-preview__picture"
    SLIDER_IMG = ".slider-carousel img"
    SLIDER_SELECTED_IMG = "//img[contains(@style,'opacity: 1')]"

    def selected_img_src_from_slider(self):
        return self.helpers.get_element(self.SLIDER_SELECTED_IMG, self.helpers.SELECTOR.XPATH).get_attribute("src")

    def preview_img_src(self):
        return self.helpers.get_element(self.PREVIEW).get_attribute("src")

    def click_different_preview(self):
        images = self.helpers.get_elements(self.SLIDER_IMG)
        if len(images) != 1:
            images[randrange(1, len(images))].click()


class InfoCard(Component):
    SELLER_NAME = ".info-card__name"
    SELLER_IMAGE = ".info-card__image"
    SELLER_RATING = ".info-card-rating"
    PHONE_BTN = ".info-card-btn__number"
    MESSAGE = ".info-card-btn__massage"
    EDIT = ".info-card-btn__change"
    PHONE_NUMBER = "//input[@data-action = \"numberClick\"][@value != \"Показать номер\"]"

    def click_on_seller_name(self):
        self.helpers.click_element(self.SELLER_NAME)

    def click_on_seller_img(self):
        self.helpers.click_element(self.SELLER_IMAGE)

    def click_on_seller_rate(self):
        self.helpers.click_element(self.SELLER_RATING)

    def click_phone(self):
        self.helpers.click_element(self.PHONE_BTN)

    def click_edit(self):
        self.helpers.click_element(self.EDIT)

    def get_phone(self):
        phone = self.helpers.get_element(self.PHONE_NUMBER, self.helpers.SELECTOR.XPATH)
        return phone.get_attribute("value")

    def click_message(self):
        self.helpers.click_element(self.MESSAGE)


class ProductPage(Page):
    PATH = "/product/{}".format(TEST_PRODUCT)

    PAGE = ".board"

    def wait_page(self):
        self.__wait_page__(self.PAGE)

    def change_path(self, path):
        self.PATH = "/product/" + path

    @property
    def login(self):
        return Login(self.driver)

    @property
    def photos(self):
        return Photos(self.driver)

    @property
    def info_card(self):
        return InfoCard(self.driver)
