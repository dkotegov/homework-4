from helpers.component import Component


class SideBar(Component):
    MY_SETTINGS = "#profile-menu-settings"
    MY_PRODUCTS = "#profile-menu-posts"
    MY_MESSAGES = "#profile-menu-messages"
    MY_FAVORITES = "#profile-menu-favorites"
    MY_ACHIVEMENTS = "#profile-menu-achievements"
    MY_REVIEWS = "#profile-menu-comments"
    MY_REVIEW_AWAITS = "#profile-menu-review-await"
    ALL_PRODUCTS = "##profile-menu-landing"

    def click_my_settings(self):
        self.helpers.click_button(self.MY_SETTINGS)

    def click_my_products(self):
        self.helpers.click_button(self.MY_PRODUCTS)

    def click_my_messages(self):
        self.helpers.click_button(self.MY_MESSAGES)

    def click_my_favorites(self):
        self.helpers.click_button(self.MY_FAVORITES)

    def click_my_achivements(self):
        self.helpers.click_button(self.MY_ACHIVEMENTS)

    def click_my_comments(self):
        self.helpers.click_button(self.MY_COMMENTS)

    def click_my_review_awaits(self):
        self.helpers.click_button(self.MY_REVIEW_AWAITS)