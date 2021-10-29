from pages.default_page import DefaultPage, SELECTOR


class Footer(DefaultPage):
    LOGO = ".footer-urls-logo__img"

    FOOTER_ITEM = "//div[@class=\"footer-urls-container\"]/a[contains(text(),'{}')]"
    CREATE = FOOTER_ITEM.format("Разместить объявление")
    SEARCH = FOOTER_ITEM.format("Поиск")
    SETTINGS = FOOTER_ITEM.format("Настройки")
    AD = FOOTER_ITEM.format("Мои объявления")
    CHATS = FOOTER_ITEM.format("Мои сообщения")
    FAVORITES = FOOTER_ITEM.format("Избранное")
    REGISTRATION = FOOTER_ITEM.format("Регистрация")
    AUTH = FOOTER_ITEM.format("Авторизация")

    def click_logo(self):
        self.__click_button__(self.LOGO)

    def click_create(self):
        self.__click_button__(self.CREATE, SELECTOR.XPATH)

    def click_search(self):
        self.__click_button__(self.SEARCH, SELECTOR.XPATH)

    def click_settings(self):
        self.__click_button__(self.SETTINGS, SELECTOR.XPATH)

    def click_ad(self):
        self.__click_button__(self.AD, SELECTOR.XPATH)

    def click_chats(self):
        self.__click_button__(self.CHATS, SELECTOR.XPATH)

    def click_favorites(self):
        self.__click_button__(self.FAVORITES, SELECTOR.XPATH)

    def click_registration(self):
        self.__click_button__(self.REGISTRATION, SELECTOR.XPATH)

    def click_auth(self):
        self.__click_button__(self.AUTH, SELECTOR.XPATH)