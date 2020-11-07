from tests.components.restaurant_banner import RestaurantBanner
from tests.components.restaurant_feedback import RestaurantFeedback
from tests.pages.page import Page


class FeedbackPage(Page):
    def __init__(self, driver, rest_id):
        super(FeedbackPage, self).__init__(driver)
        self.PATH = 'restaurants/%s/info' % rest_id

        self.banner = RestaurantBanner(self.driver)
        self.feedback = RestaurantFeedback(self.driver)

    def wait_visible(self):
        return self.banner.wait_visible() and \
               self.feedback.wait_visible()

    def set_feedback(self, feedback):
        self.feedback.set_feedback(feedback)
        self.feedback.submit()
        self.feedback.wait_feedback_change()

    def set_mark(self, mark):
        self.feedback.set_mark(mark)
        self.feedback.submit()
        self.feedback.wait_feedback_change()

    def restaurant_last_feedback(self):
        return self.feedback.last_feedback()

    def restaurant_mark(self):
        return self.banner.mark()
