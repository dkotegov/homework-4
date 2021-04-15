class CurrentBrowser:
    def __init__(self):
        self.browser = None

    def set(self, browser):
        self.browser = browser

    def get(self):
        return self.browser
