class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def refresh(self):
        self.driver.refresh()
