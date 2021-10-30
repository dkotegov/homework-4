from helpers import Test

from utils.natural_sort import natural_sort

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
        res_good = self.search.enterAmount("1000")
        self.assertTupleEqual(("1 000", "1 000"), res_good, "Некорректный результат")
        self.search.clearAmount()

        res_bad = self.search.enterAmount("incorrect")
        self.assertTupleEqual(("", ""), res_bad, "Некорректный результат")
        self.search.clearAmount()

        res_bad = self.search.enterAmount("10000000000000")
        self.assertTupleEqual(("1 000 000 000", "1 000 000 000"), res_bad, "Некорректный результат")

    def testSearchSortName(self):
        """Проверить, что при нажатии на "По имени" из списка “Сортировка по”, объявления выдаются в алфавитном
        порядке """
        self.search.changeSortName()
        products = self.search.getAllNameProducts()
        list_not_sorted = []
        list_sorted = []
        for item in products:
            list_not_sorted.append(item.text)
            list_sorted.append(item.text)
        list_sorted = natural_sort(list_sorted)
        self.assertListEqual(list_not_sorted, list_sorted, "Список упорядочен не по алфавиту")

    def testSearchSortAmountDown(self):
        """Проверить, что при нажатии на "По убыванию цены" из списка “Сортировка по”, объявления выдаются от
        наибольшей цены к наименьшей """
        self.search.changeSortAmountDown()
        products = self.search.getAllAmountProducts()
        list_not_sorted = []
        list_sorted = []
        for item in products:
            list_not_sorted.append(int(item.text[0:-1].replace(" ", "")))
            list_sorted.append(int(item.text[0:-1].replace(" ", "")))
        list_sorted = sorted(list_sorted, reverse=True)
        self.assertListEqual(list_not_sorted, list_sorted, "Список упорядочен не по убыванию цены")

    def testSearchSortAmountUp(self):
        """Проверить, что при нажатии на "По возрастанию цены" из списка “Сортировка по”, объявления выдаются от
        наименьшей цены к наибольшей """
        self.search.changeSortAmountUp()
        products = self.search.getAllAmountProducts()
        list_not_sorted = []
        list_sorted = []
        for item in products:
            list_not_sorted.append(int(item.text[0:-1].replace(" ", "")))
            list_sorted.append(int(item.text[0:-1].replace(" ", "")))
        list_sorted = sorted(list_sorted)
        self.assertListEqual(list_not_sorted, list_sorted, "Список упорядочен не по возрастанию цены")

    def testClickProduct(self):
        """Проверка, что при нажатии на товар открывается страница товара"""
        product = ProductPage(driver=self.driver)

        product_id = self.search.product_card.click_product()

        url = self.driver.current_url
        product.change_path(product_id)
        self.assertTrue(product.is_compare_url(url), "Не открылась страница товара")

    def testLikeProduct(self):
        """
            Лайк товара при нажатии кнопки "лайк",
            Снятие лайка с товара при нажатии кнопки "дизлайк"
        """
        self.search.product_card.like_product()
        self.assertTrue(self.search.login.is_opened(), "Не открыта авторизация")
        self.search.login.click_close()

        self.search.login.auth()

        index = self.search.product_card.like_product()
        self.assertTrue(self.search.product_card.check_like_product(), "Не удалось поставить лайк")

        self.search.product_card.remove_like_product(index)
        self.assertFalse(self.search.product_card.check_remove_like_product(index), "Не удалось убрать лайк")
