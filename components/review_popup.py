from helpers import Component


class ReviewPopup(Component):
    POPUP = ".review-user-content"
    CLOSE_BUTTON = ".review-user-content-inner__close"
    SKIP_BUTTON = ".review-user-content-inner-body-button__skip"
    RATE_BUTTON = ".review-user-content-inner-body-button__review"
    ERROR = ".review-user-content-inner-body__error"

    def is_popup_opened(self):
        return self.helpers.is_contains(self.POPUP)

    def is_error_form(self):
        return self.helpers.get_element(self.ERROR) is not None

    def click_close(self):
        self.helpers.click_element(self.CLOSE_BUTTON)

    def click_skip(self):
        self.helpers.click_element(self.SKIP_BUTTON)

    def click_rate(self):
        self.helpers.click_element(self.RATE_BUTTON)
