from helpers import Page


class AchievementsPage(Page):
    PATH = "user/1/achievements"

    def change_path(self, path):
        self.PATH = "user/" + path + "/achievements"
