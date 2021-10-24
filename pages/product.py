from random import randrange
from selenium.webdriver.common.by import By
from pages.default_page import DefaultPage


class ProductPage(DefaultPage):
    PATH = "product/48"
    PREVIEW = ".slider-preview__picture"
    SLIDER_IMG = '.slider-carousel img'
    SLIDER_SELECTED_IMG = '.slider-carousel img[style = \'padding-top: 1vh; padding-bottom: 1vh; opacity: 1;\']'
    SELLER_NAME = '.info-card__name'
    SELLER_IMAGE = '.info-card__image'
    SELLER_RATING = '.info-card-rating'

    def selected_img_src_from_slider(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.SLIDER_SELECTED_IMG).get_attribute("src")

    def preview_img_src(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.PREVIEW).get_attribute("src")

    def click_different_preview(self):
        img = self.driver.find_elements(By.CSS_SELECTOR, self.SLIDER_IMG)
        img[randrange(len(img))].click()

    def click_on_seller_name(self):
        self.__click_link(self.SELLER_NAME)

    def click_on_seller_img(self):
        self.__click_link(self.SELLER_IMAGE)

    def click_on_seller_rate(self):
        self.__click_link(self.SELLER_RATING)

    def __click_link(self, selector):
        link = self.driver.find_element(By.CSS_SELECTOR, self.SELLER_RATING)
        link.click()
