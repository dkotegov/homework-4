from helpers.component import Component


class Footer(Component):
    FOOTER_ITEM = "//div[@class=\"footer-urls-container\"]/a[contains(text(),'{}')]"
    CREATE_BUTTON = FOOTER_ITEM.format("Разместить объявление")
    SEARCH_BUTTON = FOOTER_ITEM.format("Поиск")
    SETTINGS_BUTTON = FOOTER_ITEM.format("Настройки")
    PRODUCTS_BUTTON = FOOTER_ITEM.format("Мои объявления")
    MESSAGES_BUTTON = FOOTER_ITEM.format("Мои сообщения")
    FAVORITES_BUTTON = FOOTER_ITEM.format("Избранное")
    REGISTRATION_BUTTON = FOOTER_ITEM.format("Регистрация")
    AUTH_BUTTON = FOOTER_ITEM.format("Авторизация")

    def click_create(self):
        self.helpers.click_element(self.CREATE_BUTTON, self.helpers.SELECTOR.XPATH)

    def click_search(self):
        self.helpers.click_element(self.SEARCH_BUTTON, self.helpers.SELECTOR.XPATH)

    def click_settings(self):
        self.helpers.click_element(self.SETTINGS_BUTTON, self.helpers.SELECTOR.XPATH)

    def click_products(self):
        self.helpers.click_element(self.PRODUCTS_BUTTON, self.helpers.SELECTOR.XPATH)

    def click_messages(self):
        self.helpers.click_element(self.MESSAGES_BUTTON, self.helpers.SELECTOR.XPATH)

    def click_favorites(self):
        self.helpers.click_element(self.FAVORITES_BUTTON, self.helpers.SELECTOR.XPATH)

    def click_registration(self):
        self.helpers.click_element(self.REGISTRATION_BUTTON, self.helpers.SELECTOR.XPATH)

    def click_auth(self):
        self.helpers.click_element(self.AUTH_BUTTON, self.helpers.SELECTOR.XPATH)
