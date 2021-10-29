from pages.default_page import DefaultPage, SELECTOR


class Header(DefaultPage):
    LOGO = ".header-left__brand"
    SEARCH = ".header-right__search-button"
    CREATE = ".header-right__create-button"
    AUTH = ".header-right__account"
    ACCOUNT = ".header-right-avatar"
    DROPDOWN = ".header-dropdown-content"

    DROPDOWN_ITEM = "//a[@class=\"header-dropdown-content-item\"]/span[contains(text(),'{}')]"
    SETTINGS = DROPDOWN_ITEM.format("Настройки")
    AD = DROPDOWN_ITEM.format("Мои объявления")
    CHATS = DROPDOWN_ITEM.format("Мои сообщения")
    FAVORITES = DROPDOWN_ITEM.format("Избранное")
    ACHIEVEMENTS = DROPDOWN_ITEM.format("Достижения")
    REVIEWS = DROPDOWN_ITEM.format("Отзывы")

    def click_logo(self):
        self.__click_button__(self.LOGO)

    def click_search(self):
        self.__click_button__(self.SEARCH)

    def click_create(self):
        self.__click_button__(self.CREATE)

    def click_auth(self):
        self.__click_button__(self.AUTH)

    def click_dropdown(self):
        self.__click_button__(self.ACCOUNT)

    def is_opened_dropdown(self):
        return self.is_contains(self.DROPDOWN)

    def click_settings(self):
        self.__click_button__(self.SETTINGS, SELECTOR.XPATH)

    def click_ad(self):
        self.__click_button__(self.AD, SELECTOR.XPATH)

    def click_chats(self):
        self.__click_button__(self.CHATS, SELECTOR.XPATH)

    def click_favorites(self):
        self.__click_button__(self.FAVORITES, SELECTOR.XPATH)

    def click_achievements(self):
        self.__click_button__(self.ACHIEVEMENTS, SELECTOR.XPATH)

    def click_reviews(self):
        self.__click_button__(self.REVIEWS, SELECTOR.XPATH)
