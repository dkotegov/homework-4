import unittest
from selenium import webdriver

from pages.theme import ThemePage


class ThemeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.theme = ThemePage(driver=self.driver)
        self.theme.open()

    def testChangeTheme(self):
        theme_0 = self.theme.get_theme()

        self.theme.change_theme()

        theme_1 = self.theme.get_theme()
        self.assertNotEqual(theme_0, theme_1, "Одинаковые темы")

        self.theme.change_theme()

        theme_2 = self.theme.get_theme()
        self.assertEqual(theme_0, theme_2, "Разные темы")
        self.assertNotEqual(theme_1, theme_2, "Одинаковые темы")

    def tearDown(self):
        self.driver.close()
