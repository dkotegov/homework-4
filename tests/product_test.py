import time
import unittest
from selenium import webdriver

from pages.all_seller_products import AllSellerProducts
from pages.product import ProductPage


class ProductTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.product = ProductPage(driver=self.driver)
        self.driver.implicitly_wait(10)

    def testFirstImgSrcEqualPreview(self):
        """Проверить, что при открытии страницы первая картинка слайдера совпадает с превью товара"""
        self.product.open()
        self.assertEqual(
            self.product.selected_img_src_from_slider(),
            self.product.preview_img_src(),
            "Первая картинка слайдера не совпадает с превью товара")

    def testChangePreview(self):
        """Проверить, что по нажатию на картинку из слайдера изменяется превью товара"""
        self.product.open()
        self.product.click_different_preview()
        self.assertEqual(
            self.product.selected_img_src_from_slider(),
            self.product.preview_img_src(),
            "Выбранная картинка слайдера не совпадает с превью товара")

    def testOpenAllItemsBySellerName(self):
        """Успешный редирект на страницу всех объявлений при нажатии на имя"""
        self.all_items = AllSellerProducts(driver=self.driver)
        self.product.open()
        self.product.click_on_seller_name()
        self.assertEqual(
            self.all_items.get_title(),
            "Все объявления",
            "Ошибка редиректа на страницу всех объявлений")

    def testOpenAllItemsBySellerImg(self):
        """Успешный редирект на страницу всех объявлений при нажатии на фото"""
        self.all_items = AllSellerProducts(driver=self.driver)
        self.product.open()
        self.product.click_on_seller_img()
        self.assertEqual(
            self.all_items.get_title(),
            "Все объявления",
            "Ошибка редиректа на страницу всех объявлений")

    def testOpenAllItemsBySellerRate(self):
        """Успешный редирект на страницу всех объявлений при нажатии на оценку"""
        self.all_items = AllSellerProducts(driver=self.driver)
        self.product.open()
        self.product.click_on_seller_rate()
        self.assertEqual(
            self.all_items.get_title(),
            "Все объявления",
            "Ошибка редиректа на страницу всех объявлений")

    def tearDown(self):
        self.driver.close()
