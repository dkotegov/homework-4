from tests.pages.primary.photo_page import PhotoPage
from tests.photo_manipulation import PhotoManipulationTest


class LikesTest(PhotoManipulationTest):
    def setUp(self):
        super(LikesTest, self).setUp()
        self.to_photos()
        self.open_overlay()

    def tearDown(self):
        self.driver.back()
        super(LikesTest, self).tearDown()

    # wip test
    def button_like(self):
        toolbar = PhotoPage(self.driver).get_photo().toolbar().get_left_toolbar()

        old_likes_count = toolbar.get_likes_count()
        toolbar.put_like()
        new_likes_count = toolbar.get_likes_count()
        self.assertEquals(int(old_likes_count) + 1, int(new_likes_count))

        toolbar.put_unlike()
        new_likes_count = toolbar.get_likes_count()
        self.assertEquals(int(old_likes_count), int(new_likes_count))

    def test_thumbs_like(self):
        toolbar = PhotoPage(self.driver).get_photo().toolbar().get_left_toolbar()

        old_likes_count = toolbar.get_likes_count()
        toolbar.put_like_thumbs()
        self.driver.refresh()
        new_likes_count = toolbar.get_likes_count()
        self.assertEquals(int(old_likes_count) + 1, int(new_likes_count))

        toolbar.put_unlike_thumbs()
        self.driver.refresh()
        new_likes_count = toolbar.get_likes_count()
        self.assertEquals(old_likes_count, new_likes_count)

    def test_likes_list(self):
        toolbar = PhotoPage(self.driver).get_photo().toolbar().get_left_toolbar()

        liker_names_before = toolbar.get_liker_names()
        self.assertEquals(len(liker_names_before), 0)

        toolbar.put_like_thumbs()
        liker_names_after = toolbar.get_liker_names()
        self.assertEquals(liker_names_after.count(toolbar.get_photo_author_name()), 1)

    def test_reactions_change(self):
        for reaction in PhotoPage(self.driver).get_photo().toolbar().get_left_toolbar().DATA_REACTION_IDS:
            self.check_reaction_change(reaction)

    def check_reaction_change(self, reaction):
        toolbar = PhotoPage(self.driver).get_photo().toolbar().get_left_toolbar()

        toolbar.put_like_thumbs()
        toolbar.open_likers_list()
        old_likers_count = toolbar.get_likers_count_by_reactions(reaction)
        toolbar.close_likers_list()
        self.assertEquals(int(old_likers_count[toolbar.DATA_REACTION_IDS.index(reaction)]), 0)

        toolbar.set_reaction(reaction)
        toolbar.open_likers_list()
        new_likers_count = toolbar.get_likers_count_by_reactions(reaction)
        toolbar.close_likers_list()
        self.assertEquals(int(new_likers_count[toolbar.DATA_REACTION_IDS.index(reaction)]), 1)
