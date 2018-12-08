# -*- coding: utf-8 -*-

from component import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class CloudFile(Component):
    BASE = '//*[@data-qa-id="layer-attachment-from-cloud"]'

    SAMPLE_IMAGE = BASE + '//*[@data-id="/{}"]'

    BUTTON_ATTACH = BASE + '//*[@data-qa-id="attach"]'

    def attach_cloud_file(self, filename):
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.SAMPLE_IMAGE.format(filename)))
        ).click()

        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable((By.XPATH, self.BUTTON_ATTACH))
        ).click()
