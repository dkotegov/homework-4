class presence_number_of_elements(object):
    def __init__(self, locator, length):
        self.locator = locator
        self.length = length

    def __call__(self, driver):
        element = driver.find_elements(*self.locator)
        element_count = len(element)
        if element_count > self.length:
            return element
        else:
            return False
