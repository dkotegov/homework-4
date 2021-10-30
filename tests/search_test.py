import unittest
from selenium import webdriver
from utils.natural_sort import natural_sort

from pages.search import SearchPage
from pages.product import ProductPage
from components.product_card import ProductCard
from components.login import LoginPage


class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.search = SearchPage(driver=self.driver)
        self.search.open()

    def testInputAmount(self):
        """Поля "Цена от, ₽" и “до”
                        Запрет ввода в поля символов отличных от цифр в блоке с фильтрами
                        Запрет ввода в поля чисел больше, чем 10 знаков в блоке с фильтрами
        """
        resGood = self.search.enterAmount("1000")
        self.assertTupleEqual(("1 000", "1 000"), resGood, "Некорректный результат")
        self.search.clearAmount()

        resBad = self.search.enterAmount("incorrect")
        self.assertTupleEqual(("", ""), resBad, "Некорректный результат")
        self.search.clearAmount()

        resBad = self.search.enterAmount("10000000000000")
        self.assertTupleEqual(("1 000 000 000", "1 000 000 000"), resBad, "Некорректный результат")

    def testSearchSortName(self):
        """Проверить, что при нажатии на "По имени" из списка “Сортировка по”, объявления выдаются в алфавитном
        порядке """
        self.search.changeSortName()
        products = self.search.getAllNameProducts()
        listNotSorted = []
        listSorted = []
        for item in products:
            listNotSorted.append(item.text)
            listSorted.append(item.text)
        listSorted = natural_sort(listSorted)
        self.assertListEqual(listNotSorted, listSorted, "Список упорядочен не по алфавиту")

    def testSearchSortAmountDown(self):
        """Проверить, что при нажатии на "По убыванию цены" из списка “Сортировка по”, объявления выдаются от
        наибольшей цены к наименьшей """
        self.search.changeSortAmountDown()
        products = self.search.getAllAmountProducts()
        listNotSorted = []
        listSorted = []
        for item in products:
            listNotSorted.append(int(item.text[0:-1].replace(" ", "")))
            listSorted.append(int(item.text[0:-1].replace(" ", "")))
        listSorted = sorted(listSorted, reverse=True)
        self.assertListEqual(listNotSorted, listSorted, "Список упорядочен не по убыванию цены")

    def testSearchSortAmountUp(self):
        """Проверить, что при нажатии на "По возрастанию цены" из списка “Сортировка по”, объявления выдаются от
        наименьшей цены к наибольшей """
        self.search.changeSortAmountUp()
        products = self.search.getAllAmountProducts()
        listNotSorted = []
        listSorted = []
        for item in products:
            listNotSorted.append(int(item.text[0:-1].replace(" ", "")))
            listSorted.append(int(item.text[0:-1].replace(" ", "")))
        listSorted = sorted(listSorted)
        self.assertListEqual(listNotSorted, listSorted, "Список упорядочен не по возрастанию цены")

    def testClickProduct(self):
        """Проверка, что при нажатии на товар открывается страница товара"""
        product = ProductPage(driver=self.driver)
        product_card = ProductCard(driver=self.driver)

        product_id = product_card.click_product()

        url = self.driver.current_url
        product.change_path(product_id)
        self.assertTrue(product.is_compare_url(url), "Не открылась страница товара")

    def testLikeProduct(self):
        """
            Лайк товара при нажатии кнопки "лайк",
            Снятие лайка с товара при нажатии кнопки "дизлайк"
        """
        login = LoginPage(driver=self.driver)
        product_card = ProductCard(driver=self.driver)

        product_card.like_product()
        self.assertTrue(login.is_opened(), "Не открыта авторизация")
        login.click_close()

        login.auth()

        index = product_card.like_product()
        self.assertTrue(product_card.check_like_product(index), "Не удалось поставить лайк")

        product_card.remove_like_product(index)
        self.assertFalse(product_card.check_remove_like_product(index), "Не удалось убрать лайк")

    def tearDown(self):
        self.driver.close()
