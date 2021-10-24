import time
import unittest
from selenium import webdriver
from pages.product import ProductPage
from pages.search import SearchPage
from utils.natural_sort import natural_sort


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

    def testOpenProductPage(self):
        """Открытие страницы товара при нажатии на товар"""
        self.product = ProductPage(driver=self.driver)
        self.search.clickProduct()
        self.assertTrue(self.product.page_exist(),
                        "Не удалось открыть товар")

    def testSearchSortName(self):
        """Проверить, что при нажатии на "По имени" из списка “Сортировка по”, объявления выдаются в алфавитном
        порядке """
        self.search.changeSortName()
        time.sleep(1)
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
        time.sleep(2)
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
        time.sleep(2)
        products = self.search.getAllAmountProducts()
        listNotSorted = []
        listSorted = []
        for item in products:
            listNotSorted.append(int(item.text[0:-1].replace(" ", "")))
            listSorted.append(int(item.text[0:-1].replace(" ", "")))
        listSorted = sorted(listSorted)
        self.assertListEqual(listNotSorted, listSorted, "Список упорядочен не по возрастанию цены")

    def tearDown(self):
        self.driver.close()
