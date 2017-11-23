# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.Component.Component import Component


class PollView(Component):
    XPATH = '//div[contains(@class, "posting-form_sctn__poll")]'

    def __init__(self, driver, elem):
        super(PollView, self).__init__(driver)
        self._elem = elem
        self._question_field = self._get_question_field()

    def write_question(self, question):
        self.driver.execute_script('arguments[0].value = "%s"' % question, self._question_field)

    def write_answer(self, answer, answer_num):
        answer_field = self._get_answer_fields()[answer_num]
        self.driver.execute_script('arguments[0].value = "%s"' % answer, answer_field)

    def _get_question_field(self):
        self._wait_self_loaded()
        question_xpath = './/textarea[contains(@class, "itx posting-form_poll__question")]'
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, question_xpath))
        )

    def _get_answer_fields(self):
        self._wait_self_loaded()
        answer_xpath = './/input[contains(@class, "posting-form_poll__answer")]'
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, answer_xpath))
        )
        return self.driver.find_elements_by_xpath(answer_xpath)

    def _wait_self_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PollView.XPATH))
        )
