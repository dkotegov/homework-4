from random import randrange
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from components import Login
from pages.default_page import DefaultPage


class ProductPage(DefaultPage):
    PATH = "product/48"

    PREVIEW = ".slider-preview__picture"
    SLIDER_IMG = '.slider-carousel img'
    SLIDER_SELECTED_IMG = '.slider-carousel img[style = \'padding-top: 1vh; padding-bottom: 1vh; opacity: 1;\']'
    SELLER_NAME = '.info-card__name'
    SELLER_IMAGE = '.info-card__image'
    SELLER_RATING = '.info-card-rating'
    PHONE = '.info-card-btn__number'
    MASSAGE = '.info-card-btn__massage'
    TITLE = ".board-title__product-name"
    EDIT = ".info-card-btn__change"

    def change_path(self, path):
        self.PATH = "product/" + path

    def selected_img_src_from_slider(self):
        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.SLIDER_SELECTED_IMG)))
        return self.driver.find_element(By.CSS_SELECTOR, self.SLIDER_SELECTED_IMG).get_attribute("src")

    def preview_img_src(self):
        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.PREVIEW)))
        return self.driver.find_element(By.CSS_SELECTOR, self.PREVIEW).get_attribute("src")

    def click_different_preview(self):
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.SLIDER_IMG)))
        img = self.driver.find_elements(By.CSS_SELECTOR, self.SLIDER_IMG)
        img[randrange(len(img))].click()

    def click_on_seller_name(self):
        self.__click_button__(self.SELLER_NAME)

    def click_on_seller_img(self):
        self.__click_button__(self.SELLER_IMAGE)

    def click_on_seller_rate(self):
        self.__click_button__(self.SELLER_RATING)

    def click_phone(self):
        self.__click_button__(self.PHONE)

    def click_edit(self):
        self.__click_button__(self.EDIT)

    def get_phone(self):
        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.PHONE)))
        phone = self.driver.find_element(By.CSS_SELECTOR, self.PHONE)
        while phone.get_attribute("value") == "Показать номер":
            continue
        return phone.get_attribute("value")

    def click_massage(self):
        self.__click_button__(self.MASSAGE)

    def page_exist(self):
        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.TITLE)))
        return self.driver.find_element(By.CSS_SELECTOR, self.TITLE) is not None

    @property
    def login(self):
        return Login(self.driver)
