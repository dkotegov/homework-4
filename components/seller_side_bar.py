from helpers.component import Component


class SellerSideBar(Component):
    PRODUCTS_BUTTON = "#profile-menu-landing"
    ACHIEVEMENTS_BUTTON = "#profile-menu-achievements"
    REVIEWS_BUTTON = "#profile-menu-comments"

    def click_products(self):
        self.helpers.click_element(self.PRODUCTS_BUTTON)

    def click_achievements(self):
        self.helpers.click_element(self.ACHIEVEMENTS_BUTTON)

    def click_reviews(self):
        self.helpers.click_element(self.REVIEWS_BUTTON)
