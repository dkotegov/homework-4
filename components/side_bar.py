from helpers.component import Component


class SideBar(Component):
    MY_SETTINGS = "#profile-menu-settings"
    MY_PRODUCTS = "#profile-menu-posts"
    MY_MESSAGES = "#profile-menu-messages"
    MY_FAVORITES = "#profile-menu-favorites"
    MY_REVIEW_AWAITS = "#profile-menu-review-await"

    ACHIEVEMENTS = "#profile-menu-achievements"
    REVIEWS = "#profile-menu-comments"

    SELLER_PRODUCTS = "#profile-menu-landing"

    def click_my_settings(self):
        self.helpers.click_button(self.MY_SETTINGS)

    def click_my_products(self):
        self.helpers.click_button(self.MY_PRODUCTS)

    def click_my_messages(self):
        self.helpers.click_button(self.MY_MESSAGES)

    def click_my_favorites(self):
        self.helpers.click_button(self.MY_FAVORITES)

    def click_my_review_awaits(self):
        self.helpers.click_button(self.MY_REVIEW_AWAITS)

    def click_achievements(self):
        self.helpers.click_button(self.ACHIEVEMENTS)

    def click_reviews(self):
        self.helpers.click_button(self.REVIEWS)

    def click_seller_products(self):
        self.helpers.click_button(self.SELLER_PRODUCTS)
