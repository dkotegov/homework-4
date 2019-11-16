class DefaultPage:
    URL = None

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()

class Component:
    def __init__(self, driver):
        self.driver = driver