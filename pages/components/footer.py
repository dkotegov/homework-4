from pages.helpers.component import Component


class Footer(Component):
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
        self.helpers.click_button(self.LOGO)

    def click_create(self):
        self.helpers.click_button(self.CREATE, self.helpers.SELECTOR.XPATH)

    def click_search(self):
        self.helpers.click_button(self.SEARCH, self.helpers.SELECTOR.XPATH)

    def click_settings(self):
        self.helpers.click_button(self.SETTINGS, self.helpers.SELECTOR.XPATH)

    def click_ad(self):
        self.helpers.click_button(self.AD, self.helpers.SELECTOR.XPATH)

    def click_chats(self):
        self.helpers.click_button(self.CHATS, self.helpers.SELECTOR.XPATH)

    def click_favorites(self):
        self.helpers.click_button(self.FAVORITES, self.helpers.SELECTOR.XPATH)

    def click_registration(self):
        self.helpers.click_button(self.REGISTRATION, self.helpers.SELECTOR.XPATH)

    def click_auth(self):
        self.helpers.click_button(self.AUTH, self.helpers.SELECTOR.XPATH)
