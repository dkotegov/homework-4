# -*- coding: utf-8 -*-


class Component(object):
    TIMEOUT = 5
    IMPLICIT_TIMEOUT = 5
    POLL_FREQUENCY = 0.1

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(self.IMPLICIT_TIMEOUT)
