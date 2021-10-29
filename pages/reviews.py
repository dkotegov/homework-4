from pages.default_page import DefaultPage


class ReviewsPage(DefaultPage):
    PATH = "user/78/reviews"

    def change_path(self, path):
        self.PATH = "user/" + path + "/reviews"
