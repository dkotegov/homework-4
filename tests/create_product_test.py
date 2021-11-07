from helpers import Test

from pages.create_product import CreateProductPage
from pages.promotion import PromotionPage
from utils import get_file_text

import time


class CreateProductTest(Test):
    def setUp(self):
        super().setUp()
        self.create = CreateProductPage(driver=self.driver)
        self.create.open()
        self.create.login.auth()
        self.create.open()

    def __test_name__(self, test):
        self.create.form.input_name_value(test)

        self.create.form.enter_submit()
        self.assertTrue(self.create.form.is_error_name(), "Нет ошибки")

    def testErrorNameInput(self):
        """Проверка создания продукта с неправильными данными названия"""
        # создрание с пустым названием
        test1 = ""
        # создание с названием, где больше 100 символов
        test2 = "ffsdfvgsdv fh bcvb g dg gb gfxdfg fxdfbffsdfvgsdv fh bcvb g dg gb gfxdfg fxdfbffsdfvgsdv fh bcvb g " \
                "dg gb gfxdfg fxdfb "

        self.__test_name__(test1)
        self.__test_name__(test2)

    def __test_price__(self, test):
        self.create.form.input_price_value(test)

        self.create.form.enter_submit()
        self.assertTrue(self.create.form.is_error_price(), "Нет ошибки")

    def testErrorPriceInput(self):
        """Проверка создания с неправильными данными цены"""
        # создание с пустой ценой
        test1 = ""

        self.__test_price__(test1)

    def __test_description__(self, test):
        self.create.form.input_description_value(test)

        self.create.form.enter_submit()
        self.assertTrue(self.create.form.is_error_description(), "Нет ошибки")

    def testErrorDescriptionInput(self):
        """Проверка создания с неправильными данными описания"""
        # создание с пустым описанием
        test1 = ""
        # создание с описанием, где меньше 10
        test2 = "aaaaaaa"
        # создание с описанием, где больше 4000 символов
        test3 = get_file_text("./assets/test_description.txt")

        self.__test_description__(test1)
        self.__test_description__(test2)
        self.__test_description__(test3)

    def __test_address__(self, test):
        self.create.form.input_address_value(test)

        self.create.form.enter_submit()
        self.assertTrue(self.create.form.is_error_address(), "Нет ошибки")

    def testErrorAddressInput(self):
        """Проверка сохранения с неправильными данными адрес"""
        # сохранение с пустым адресом
        test1 = ""

        self.__test_address__(test1)

    # def testClickCreate(self):
    #     """Проверка, что при нажатии на создание с правильно заполненными полями, открываеся страница продвижения"""
    #     Мы используем яндекс апи для карт и оно работает иногда не стабильно, из-за чего тест может падать
    #     name = "aaa"
    #     price = "111"
    #     description = "aaaaaaaaaaaaaaaaaaaaaaa"
    #     address = "Сант-Петербург, Россия"
    #
    #     self.create.form.input_name_value(name)
    #     self.create.form.input_price_value(price)
    #     self.create.form.input_description_value(description)
    #     self.create.form.upload_photo("./assets/test.jpg")
    #     self.create.form.input_address_value(address)
    #     self.create.form.enter_address()
    #
    #     promote = PromotionPage(driver=self.driver)
    #
    #     self.create.form.enter_submit()
    #
    #     time.sleep(1)
    #     url = self.driver.current_url
    #     self.assertTrue(promote.is_compare_url(url), "Не открылась страница продвижения")
