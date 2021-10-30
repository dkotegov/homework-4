from helpers.component import Component


class SettingsCard(Component):
    SETTINGS_ITEM = "//a[@class=\"profile-menu-buttons-item\"]/span[contains(text(),'{}')]"
    SETTINGS = SETTINGS_ITEM.format("Настройки")
    AD = SETTINGS_ITEM.format("Мои объявления")
    CHATS = SETTINGS_ITEM.format("Мои сообщения")
    FAVORITES = SETTINGS_ITEM.format("Избранное")
    ACHIEVEMENTS = SETTINGS_ITEM.format("Достижения")
    REVIEWS = SETTINGS_ITEM.format("Отзывы")
    AWAIT_REVIEWS = SETTINGS_ITEM.format("Ожидает отзыв")

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

    def click_await_reviews(self):
        self.helpers.click_button(self.AWAIT_REVIEWS, self.helpers.SELECTOR.XPATH)
