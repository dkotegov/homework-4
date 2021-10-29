from pages.default_page import DefaultPage


class AchievementsPage(DefaultPage):
    PATH = "user/78/achievements"

    def change_path(self, path):
        self.PATH = "user/" + path + "/achievements"
