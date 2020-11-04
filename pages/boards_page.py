from base_classes.page import Page


class BoardsPage(Page):
    PATH = 'boards'
    CONTAINER = '//div[contains(@class, "boards")]'
