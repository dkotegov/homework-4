from pages.helpers.component import Component


class Header(Component):
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
        self.helpers.click_button(self.LOGO)

    def click_search(self):
        self.helpers.click_button(self.SEARCH)

    def click_create(self):
        self.helpers.click_button(self.CREATE)

    def click_auth(self):
        self.helpers.click_button(self.AUTH)

    def click_dropdown(self):
        self.helpers.click_button(self.ACCOUNT)

    def is_opened_dropdown(self):
        return self.helpers.is_contains(self.DROPDOWN)

    def click_settings(self):
        self.helpers.click_button(self.SETTINGS, self.helpers.SELECTOR.XPATH)

    def click_ad(self):
        self.helpers.click_button(self.AD, self.helpers.SELECTOR.XPATH)

    def click_chats(self):
        self.helpers.click_button(self.CHATS, self.helpers.SELECTOR.XPATH)

    def click_favorites(self):
        self.helpers.click_button(self.FAVORITES, self.helpers.SELECTOR.XPATH)

    def click_achievements(self):
        self.helpers.click_button(self.ACHIEVEMENTS, self.helpers.SELECTOR.XPATH)

    def click_reviews(self):
        self.helpers.click_button(self.REVIEWS, self.helpers.SELECTOR.XPATH)
