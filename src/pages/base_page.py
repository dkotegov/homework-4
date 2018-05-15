class BasePage(object):
    
    def __init__(self, driver):
        self._driver = driver

    @property
    def driver(self):
        return self._driver
