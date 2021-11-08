from utils import get_file_text

from helpers import Test

from pages import CreateProductPage, MainPage

# У нас нет теста на успешное создание товара, потому что мы используем Яндекс Апи
# Яндекс Апи не стабильное и тесты будут мигать, поэтому мы решили отказаться от них


class CreateProductTest(Test):
    def setUp(self):
        super().setUp()
        self.create_page = CreateProductPage(driver=self.driver)
        main_page = MainPage(driver=self.driver)

        main_page.open()
        main_page.login.auth()
        self.create_page.open()

    def __test_name__(self, test):
        self.create_page.form.input_name_value(test)

        self.create_page.form.enter_submit()
        self.assertTrue(self.create_page.form.is_error_name(), "Нет ошибки")

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
        self.create_page.form.input_price_value(test)

        self.create_page.form.enter_submit()
        self.assertTrue(self.create_page.form.is_error_price(), "Нет ошибки")

    def testErrorPriceInput(self):
        """Проверка создания с неправильными данными цены"""
        # создание с пустой ценой
        test1 = ""

        self.__test_price__(test1)

    def __test_description__(self, test):
        self.create_page.form.input_description_value(test)

        self.create_page.form.enter_submit()
        self.assertTrue(self.create_page.form.is_error_description(), "Нет ошибки")

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
        self.create_page.form.input_address_value(test)

        self.create_page.form.enter_submit()
        self.assertTrue(self.create_page.form.is_error_address(), "Нет ошибки")

    def testErrorAddressInput(self):
        """Проверка сохранения с неправильными данными адрес"""
        # сохранение с пустым адресом
        test1 = ""

        self.__test_address__(test1)
