from tests.helpers.database import DatabaseFiller
from tests.pages.feedback_page import FeedbackPage
from tests.tests_potapchuk.base_test import BaseTest


def create_restaurant():
    pass


class FeedbackTest(BaseTest):
    DEFAULT_REST_NAME = 'FeedbackTestBaseTest_________'

    def setUp(self):
        self.create_restaurant()
        super().setUp(auth='user')

        self.feedbackPage = FeedbackPage(self.driver, self.rest_id)
        self.feedbackPage.open()
        self.feedbackPage.wait_visible()

    def tearDown(self):
        super(FeedbackTest, self).tearDown()
        self.clear_restaurant()

    def test_feedback(self):
        feedback = self.test_feedback.__name__
        self.feedbackPage.set_feedback(feedback)
        self.assertEqual(
            feedback,
            self.feedbackPage.restaurant_last_feedback(),
        )

    def test_mark(self):
        for mark in [2, 5]:
            self.feedbackPage.set_mark(mark)
            self.assertEqual(
                mark,
                self.feedbackPage.restaurant_mark(),
            )

    def create_restaurant(self):
        self.filler = DatabaseFiller()
        self.filler.admin_auth()
        self.filler.create_restaurant(self.DEFAULT_REST_NAME)
        self.rest_id = self.filler.get_restaurant_id_by_name(
            self.DEFAULT_REST_NAME
        )

    def clear_restaurant(self):
        self.filler.delete_restaurant(self.rest_id)
