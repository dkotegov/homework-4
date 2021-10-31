import unittest
from selenium import webdriver

from pages.create_product import CreateProductPage
from pages.promotion import PromotionPage


class CreateProductTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.create = CreateProductPage(driver=self.driver)
        self.create.open()

    def __test_name__(self, test):
        self.create.clear_name_value()
        self.create.input_name_value(test)
        self.create.enter_submit()
        self.assertTrue(self.create.is_error_name(), "Нет ошибки")

    def testErrorNameInput(self):
        """Проверка создания продукта с неправильными данными названия"""
        # создрание с пустым названием
        test1 = ""
        # создание с названием, где больше 100 символов
        test2 = "ffsdfvgsdv fh bcvb g dg gb gfxdfg fxdfbffsdfvgsdv fh bcvb g dg gb gfxdfg fxdfbffsdfvgsdv fh bcvb g dg gb gfxdfg fxdfb"

        self.__test_name__(test1)
        self.__test_name__(test2)

    def __test_price__(self, test):
        self.create.clear_price_value()
        self.create.input_price_value(test)
        self.create.enter_submit()
        self.assertTrue(self.create.is_error_price(), "Нет ошибки")

    def testErrorPriceInput(self):
        """Проверка создания с неправильными данными цены"""
        # создание с пустой ценой
        test1 = ""

        self.__test_price__(test1)

    def __test_description__(self, test):
        self.create.clear_description_value()
        self.create.input_description_value(test)
        self.create.enter_submit()
        self.assertTrue(self.create.is_error_description(), "Нет ошибки")

    def testErrorDescriptionInput(self):
        """Проверка создания с неправильными данными описания"""
        # создание с пустым описанием
        test1 = ""
        # создание с описанием, где меньше 10
        test2 = "aaaaaaa"
        # создание с описанием, где больше 4000 символов
        test3 = open("./test_file/test_description.txt").read()

        self.__test_description__(test1)
        self.__test_description__(test2)
        self.__test_description__(test3)

    def __test_address__(self, test):
        self.create.clear_address_value()
        self.create.input_address_value(test)
        self.create.enter_submit()
        self.assertTrue(self.create.is_error_address(), "Нет ошибки")

    def testErrorAddressInput(self):
        """Проверка сохранения с неправильными данными адрес"""
        # сохранение с пустым адресом
        test1 = ""

        self.__test_password__(test1)

    def testClickProduct(self):
        """Проверка, что при нажатии на создание с правильно заполненными полями, открываеся страница продвижения"""
        name = "aaa"
        price = "111"
        description = "aaaaaaaaaaaaaaaaaaaaaaa"
        address = "aaaaaaaaaaaaa"

        self.create.input_name_value(name)
        self.create.input_price_value(price)
        self.create.input_description_value(description)
        self.create.input_address_value(address)

        promote = PromotionPage(driver=self.driver)

        self.create.enter_submit()

        url = self.driver.current_url
        self.assertTrue(promote.is_compare_url(url), "Не открылась страница продвижения")

    def tearDown(self):
        self.driver.close()
