from helpers.component import Component


class UserSideBar(Component):
    SETTINGS_BUTTON = "#profile-menu-settings"
    PRODUCTS_BUTTON = "#profile-menu-posts"
    MESSAGES_BUTTON = "#profile-menu-messages"
    FAVORITES_BUTTON = "#profile-menu-favorites"
    ACHIEVEMENTS_BUTTON = "#profile-menu-achievements"
    REVIEWS_BUTTON = "#profile-menu-comments"
    REVIEW_AWAITS_BUTTON = "#profile-menu-review-await"

    def click_settings(self):
        self.helpers.click_element(self.SETTINGS_BUTTON)

    def click_products(self):
        self.helpers.click_element(self.PRODUCTS_BUTTON)

    def click_messages(self):
        self.helpers.click_element(self.MESSAGES_BUTTON)

    def click_favorites(self):
        self.helpers.click_element(self.FAVORITES_BUTTON)

    def click_achievements(self):
        self.helpers.click_element(self.ACHIEVEMENTS_BUTTON)

    def click_reviews(self):
        self.helpers.click_element(self.REVIEWS_BUTTON)

    def click_review_awaits(self):
        self.helpers.click_element(self.REVIEW_AWAITS_BUTTON)
