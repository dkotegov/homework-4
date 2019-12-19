# -*- coding: utf-8 -*-
class ElementEqualSubcategory(object):
    def __init__(self, className, subcategory):
        self.className = className
        self.subcategory = subcategory

    def __call__(self, driver):
        element = driver.find_element_by_class_name(self.className)
        if self.subcategory in element.get_attribute("innerHTML"):
            return element
        else:
            return False
