from selenium.webdriver.support.wait import WebDriverWait

from tests.components.component import Component


class RestaurantFeedback(Component):
    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: submit_button(d).is_displayed() and
                      mark_container(d).is_displayed() and
                      feedback_input(d).is_displayed()
        )

    def set_feedback(self, feedback):
        feedback_input(self.driver).send_keys(feedback)

    def set_mark(self, new_mark):
        mark = self.mark()
        delta = new_mark - mark

        if delta == 0:
            return

        if delta > 0:
            self.inc_mark(delta)
        else:
            self.dec_mark(delta)

    def mark(self):
        return int(
            mark_input(self.driver).get_attribute('value')
        )

    def last_feedback(self):
        return feedback_input(self.driver).get_attribute('value')

    def submit(self):
        submit_button(self.driver).click()

    def inc_mark(self, delta):
        button = mark_inc_button(self.driver)
        for i in range(delta):
            button.click()

    def dec_mark(self, delta):
        button = mark_dec_button(self.driver)
        for i in range(-delta):
            button.click()

    def wait_feedback_change(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: submit_enabled(d)
        )

    def get_last_feedback(self):
        return not feedback_text_containers(
            self.driver
        )[0].get_attribute('innerText')


def feedback_text_containers(driver):
    return driver.find_elements_by_css_selector(
        '.restaurant-feedback-card__second-line'
    )

def submit_button(driver):
    return driver.find_element_by_css_selector(
        '#feedback-form__submit-button'
    )


def submit_enabled(driver):
    return 0 == len(
        driver.find_elements_by_css_selector(
            '#feedback-form__submit-button[disabled]'
        )
    )


def mark_input(driver):
    return driver.find_element_by_css_selector(
        'input#feedback-form__rate-input__input'
    )

def mark_container(driver):
    return driver.find_element_by_css_selector(
        '.feedback-form__stars-and-rate'
    )


def mark_inc_button(driver):
    return driver.find_element_by_css_selector(
        '#feedback-form__rate-input_plus-button'
    )


def feedback_input(driver):
    return driver.find_element_by_css_selector(
        '#text-input'
    )


def mark_dec_button(driver):
    return driver.find_element_by_css_selector(
        '#feedback-form__rate-input_minus-button'
    )
