
class Component(object):
    LOCATORS = {}

    def get_locators(self):
        return self.LOCATORS

    def __init__(self, page):
        self.page = page
