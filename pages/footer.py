from pages.default_page import DefaultPage


class FooterPage(DefaultPage):
    PATH = ""
    LOGO = ".footer-urls-logo__img"
    CREATE_BUTTON = "//div[@class=\"footer-urls-container\"]/a[contains(text(),'Разместить объявление')]"
    SEARCH = "//div[@class=\"footer-urls-container\"]/a[contains(text(),'Поиск')]"
    SETTINGS = "//div[@class=\"footer-urls-container\"]/a[contains(text(),'Настройки')]"
    AD = "//div[@class=\"footer-urls-container\"]/a[contains(text(),'Мои объявления')]"
    CHATS = "//div[@class=\"footer-urls-container\"]/a[contains(text(),'Мои сообщения')]"
    FAVORITES = "//div[@class=\"footer-urls-container\"]/a[contains(text(),'Избранное')]"
    REGISTRATION_BUTTON = "//div[@class=\"footer-urls-container\"]/a[contains(text(),'Регистрация')]"

    def click_logo(self):
        self.__click_button__(self.LOGO)

    def click_create(self):
        self.__click_button_xpath__(self.CREATE_BUTTON)

    def click_search(self):
        self.__click_button_xpath__(self.SEARCH)

    def click_settings(self):
        self.__click_button_xpath__(self.SETTINGS)

    def click_ad(self):
        self.__click_button_xpath__(self.AD)

    def click_chats(self):
        self.__click_button_xpath__(self.CHATS)

    def click_favorites(self):
        self.__click_button_xpath__(self.FAVORITES)

    def click_registration(self):
        self.__click_button_xpath__(self.REGISTRATION_BUTTON)
