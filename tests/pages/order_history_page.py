from tests.pages.page import Page


class OrderHistoryPage(Page):
    def wait_visible(self):
        pass


def title(driver):
    return driver.find_element_by_css_selector(
        'h1.order-history__main-content_title'
    )
