from tests.pages.feedback_page import FeedbackPage
from tests.tests_potapchuk.base_test import BaseTest


class FeedbackTest(BaseTest):
    def setUp(self):
        super().create_restaurant()
        super().setUp(auth='user')

        self.feedbackPage = FeedbackPage(self.driver, self.rest_id)
        self.feedbackPage.open()
        self.feedbackPage.wait_visible()

    def tearDown(self):
        super().clear_restaurant()
        super().tearDown()


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
