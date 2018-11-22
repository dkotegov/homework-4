# -*- coding: utf-8 -*-



class Message:
    title = ""
    selectors = []

    def __init__(self, title, selectors=list()):
        self.title = title
        self.selectors = selectors

    def has_selectors(self, *selectors):
        for s in selectors:
            if s not in self.selectors:
                return False
        return True