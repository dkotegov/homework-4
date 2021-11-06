from helpers import Test

from utils import fill_name_list_and_sort_last_list, fill_amount_list_and_sort_last_list

from pages import SearchPage, ProductPage


class SearchTest(Test):
    def setUp(self):
        super().setUp()
        self.search = SearchPage(driver=self.driver)
        self.search.open()

    def testInputAmount(self):
        """Поля "Цена от, ₽" и “до”
                        Запрет ввода в поля символов отличных от цифр в блоке с фильтрами
                        Запрет ввода в поля чисел больше, чем 10 знаков в блоке с фильтрами
        """
        expected_1 = ("1 000", "1 000")
        expected_2 = ("", "")
        expected_3 = ("1 000 000 000", "1 000 000 000")

        test_value_1 = "1000"
        test_value_2 = "incorrect"
        test_value_3 = "10000000000000"

        res_good = self.search.search_settings.enter_amount(test_value_1)
        self.assertTupleEqual(expected_1, res_good, "Некорректный результат")
        self.search.search_settings.clear_amount()

        res_bad = self.search.search_settings.enter_amount(test_value_2)
        self.assertTupleEqual(expected_2, res_bad, "Некорректный результат")
        self.search.search_settings.clear_amount()

        res_bad = self.search.search_settings.enter_amount(test_value_3)
        self.assertTupleEqual(expected_3, res_bad, "Некорректный результат")

    def testSearchSortName(self):
        """Проверить, что при нажатии на "По имени" из списка “Сортировка по”, объявления выдаются в алфавитном
        порядке """
        self.search.change_sort_name()
        products = self.search.search_products.get_all_name_products()

        list_not_sorted, list_sorted = fill_name_list_and_sort_last_list(products)
        self.assertListEqual(list_not_sorted, list_sorted, "Список упорядочен не по алфавиту")

    def testSearchSortAmountDown(self):
        """Проверить, что при нажатии на "По убыванию цены" из списка “Сортировка по”, объявления выдаются от
        наибольшей цены к наименьшей """
        self.search.change_sort_amount_down()
        products = self.search.search_products.get_all_amount_products()

        list_not_sorted, list_sorted = fill_amount_list_and_sort_last_list(products, reverse=True)
        self.assertListEqual(list_not_sorted, list_sorted, "Список упорядочен не по убыванию цены")

    def testSearchSortAmountUp(self):
        """Проверить, что при нажатии на "По возрастанию цены" из списка “Сортировка по”, объявления выдаются от
        наименьшей цены к наибольшей """
        self.search.change_sort_amount_up()
        products = self.search.search_products.get_all_amount_products()

        list_not_sorted, list_sorted = fill_amount_list_and_sort_last_list(products, reverse=False)
        self.assertListEqual(list_not_sorted, list_sorted, "Список упорядочен не по возрастанию цены")

    def testClickProduct(self):
        """Проверка, что при нажатии на товар открывается страница товара"""
        product_page = ProductPage(driver=self.driver)

        product_id = self.search.search_products.get_product_id()
        self.search.search_products.click_product(product_id)

        url = self.driver.current_url
        product_page.change_path(product_id)
        self.assertTrue(product_page.is_compare_url(url), "Не открылась страница товара")

    def testLikeProduct(self):
        """
            Лайк товара при нажатии кнопки "лайк",
            Снятие лайка с товара при нажатии кнопки "дизлайк"
        """
        product_id = self.search.search_products.get_product_id()

        self.search.search_products.click_like_product(product_id)
        self.assertTrue(self.search.login.is_opened(), "Не открылась авторизация")
        self.search.login.click_close()

        self.search.login.auth()

        self.search.search_products.click_like_product(product_id)
        self.assertTrue(self.search.search_products.is_product_liked(product_id), "Не удалось поставить лайк")

        self.search.search_products.click_like_product(product_id)
        self.assertFalse(self.search.search_products.is_product_liked(product_id), "Не удалось убрать лайк")
