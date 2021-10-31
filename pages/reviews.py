from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from helpers import Page
from components import Login, SideBar
import time


class ReviewsPage(Page):
    PATH = "user/78/reviews"
    TITLE = ".reviews-head__title"
    PRODUCT_TITLE = ".one-review-head-info__product"
    USER_TITLE = ".one-review-head-info__user"
    SORT_BY_DATE = "//label[@for=\"reviews-buyer-date\"]"
    SORT_BY_RATING = "//label[@for=\"reviews-buyer-rate\"]"
    DATE = ".one-review-head-stat__date"
    STARS = ".one-review-head-stat__rate"

    def change_path(self, path):
        self.PATH = "user/" + path + "/reviews"

    @property
    def login(self):
        return Login(self.driver)

    @property
    def side_bar(self):
        return SideBar(self.driver)

    def get_title(self):
        return self.helpers.get_element(self.TITLE).text

    def click_product_name(self):
        product_titles = self.helpers.get_elements(self.PRODUCT_TITLE)
        product_url = product_titles[0].get_attribute("href")
        product_titles[0].click()
        return product_url

    def click_user_name(self):
        user_names = self.helpers.get_elements(self.USER_TITLE)
        user_url = user_names[0].get_attribute("href")
        user_names[0].click()
        return user_url

    def set_sort_by_date(self):
        self.helpers.click_button(self.SORT_BY_DATE)

    def set_sort_by_ratting(self):
        self.helpers.click_button(self.SORT_BY_RATING)

    def check_sort_by_date(self):
        dates = self.helpers.get_elements(self.DATE)
        for i in range(len(dates) - 1):
            time1 = time.strptime(dates[i].text, "%d.%m.%Y")
            time2 = time.strptime(dates[i + 1].text, "%d.%m.%Y")
            if time1 < time2:
                return False
        return True

    def check_sort_by_rating(self):
        stars = self.helpers.get_elements(self.STARS)
        for i in range(len(stars) - 1):
            count1 = stars[i].find_elements(By.CSS_SELECTOR, ".star-active")
            count2 = stars[i].find_elements(By.CSS_SELECTOR, ".star-active")
            if count1 < count2:
                return False
        return True
