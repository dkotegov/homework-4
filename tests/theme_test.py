import unittest
from selenium import webdriver

from pages import MainPage


class ThemeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.main = MainPage(driver=self.driver)
        self.main.open()

    def testChangeTheme(self):
        """Проверка смены темы"""
        theme_0 = self.main.theme.get_theme()

        self.main.theme.change_theme()

        theme_1 = self.main.theme.get_theme()
        self.assertNotEqual(theme_0, theme_1, "Одинаковые темы")

        self.main.theme.change_theme()

        theme_2 = self.main.theme.get_theme()
        self.assertEqual(theme_0, theme_2, "Разные темы")
        self.assertNotEqual(theme_1, theme_2, "Одинаковые темы")

    def tearDown(self):
        self.driver.close()
