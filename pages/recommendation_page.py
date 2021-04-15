import components
from pages.base_page import BasePage


class RecommendationPage(BasePage):
    PATH = 'candidatesList'

    def __init__(self, driver):
        super(RecommendationPage, self).__init__(driver, '//div[@class="main-list"]')
