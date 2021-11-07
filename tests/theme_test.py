from helpers import Test

from pages import MainPage


class ThemeTest(Test):
    def setUp(self):
        super().setUp()
        self.main_page = MainPage(driver=self.driver)
        self.main_page.open()

    def __test_change_theme__(self, theme):
        # у нас в браузере тема ставиться в зависимости от темы системы
        # поэтому мы не можем изначально знать какая у нас будет тема
        # поэтому в зависимости от выбранной темы переключаем на другую и проверяем что тема поменялась
        if theme == self.main_page.theme.LIGHT:
            self.main_page.theme.change_theme()
            self.assertTrue(self.main_page.theme.is_dark_theme(), "Тема не темная")
        elif theme == self.main_page.theme.DARK:
            self.main_page.theme.change_theme()
            self.assertTrue(self.main_page.theme.is_light_theme(), "Тема не светлая")

    def testChangeTheme(self):
        """Проверка смены темы"""
        theme = self.main_page.theme.get_theme()
        self.__test_change_theme__(theme)

        theme = self.main_page.theme.get_theme()
        self.__test_change_theme__(theme)
