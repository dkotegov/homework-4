from utils import fill_name_list_and_sort_last_list, fill_amount_list_and_sort_last_list
from helpers import Test

from pages import SearchPage, ProductPage


class SearchTest(Test):
    def setUp(self):
        super().setUp()
        self.search_page = SearchPage(driver=self.driver)
        self.search_page.open()

    def __auth__(self):
        self.search_page.login.auth()
        self.search_page.open()

    def testMaxLenDigitsInputAmount(self):
        """Поля "Цена от, ₽" и “до”
                        Запрет ввода в поля чисел больше, чем 10 цифр в блоке с фильтрами
        """
        expected = ("1 000 000 000", "1 000 000 000")

        test_value = "10000000000000"

        self.search_page.search_settings.enter_amount(test_value, test_value)
        res = self.search_page.search_settings.get_amounts()
        self.assertTupleEqual(expected, res, "Некорректный результат")

    def testLettersErrorInputAmount(self):
        """Поля "Цена от, ₽" и “до”
                        Запрет ввода в поля символов отличных от цифр в блоке с фильтрами
        """
        expected = ("", "")
        test_value = "incorrect"

        self.search_page.search_settings.enter_amount(test_value, test_value)
        res_bad = self.search_page.search_settings.get_amounts()
        self.assertTupleEqual(expected, res_bad, "Некорректный результат")
        self.search_page.search_settings.clear_amount()

    def testSuccessInputAmount(self):
        """
            Корректный ввод в поля "Цена от, ₽" и “до”
        """
        expected = ("1 000", "1 000")
        test_value = "1000"

        self.search_page.search_settings.enter_amount(test_value, test_value)
        res_good = self.search_page.search_settings.get_amounts()
        self.assertTupleEqual(expected, res_good, "Некорректный результат")

    def testSearchSortName(self):
        """Проверить, что при нажатии на "По имени" из списка “Сортировка по”, объявления выдаются в алфавитном
        порядке """
        self.search_page.search_sort.change_sort_name()
        products = self.search_page.search_products.get_sorted_name_products()

        list_not_sorted, list_sorted = fill_name_list_and_sort_last_list(products)
        self.assertListEqual(list_not_sorted, list_sorted, "Список упорядочен не по алфавиту")

    def testSearchSortAmountDown(self):
        """Проверить, что при нажатии на "По убыванию цены" из списка “Сортировка по”, объявления выдаются от
        наибольшей цены к наименьшей """
        self.search_page.search_sort.change_sort_amount_down()
        products = self.search_page.search_products.get_sorted_amount_down_products()

        list_not_sorted, list_sorted = fill_amount_list_and_sort_last_list(products, reverse=True)
        self.assertListEqual(list_not_sorted, list_sorted, "Список упорядочен не по убыванию цены")

    def testSearchSortAmountUp(self):
        """Проверить, что при нажатии на "По возрастанию цены" из списка “Сортировка по”, объявления выдаются от
        наименьшей цены к наибольшей """
        self.search_page.search_sort.change_sort_amount_up()
        products = self.search_page.search_products.get_sorted_amount_up_products()

        list_not_sorted, list_sorted = fill_amount_list_and_sort_last_list(products, reverse=False)
        self.assertListEqual(list_not_sorted, list_sorted, "Список упорядочен не по возрастанию цены")

    def testClickProduct(self):
        """Проверка, что при нажатии на товар открывается страница товара"""
        product_page = ProductPage(driver=self.driver)

        product_id = self.search_page.search_products.get_product_id()
        self.search_page.search_products.click_product(product_id)

        url = self.driver.current_url
        product_page.change_path(product_id)
        self.assertTrue(product_page.is_compare_url(url), "Не открылась страница товара")

    def testLikeProductNotAuth(self):
        """Проверка, что без авторизации лайк поставить нельзя"""
        product_id = self.search_page.search_products.get_product_id()

        self.search_page.search_products.click_like_product(product_id)
        self.assertTrue(self.search_page.login.is_opened(), "Не открылась авторизация")

    def testLikeProduct(self):
        """
            Лайк товара при нажатии кнопки "лайк",
            Снятие лайка с товара при нажатии кнопки "дизлайк"
        """
        self.__auth__()
        product_id = self.search_page.search_products.get_product_id()

        self.search_page.search_products.click_like_product(product_id)
        self.search_page.search_products.wait_liked(product_id)
        self.assertTrue(self.search_page.search_products.is_product_liked(product_id), "Не удалось поставить лайк")

        self.search_page.search_products.click_like_product(product_id)
        self.search_page.search_products.wait_not_liked(product_id)
        self.assertFalse(self.search_page.search_products.is_product_liked(product_id), "Не удалось убрать лайк")
