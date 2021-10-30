from helpers import Page


class ReviewsPage(Page):
    PATH = "user/1/reviews"

    def change_path(self, path):
        self.PATH = "user/" + path + "/reviews"
