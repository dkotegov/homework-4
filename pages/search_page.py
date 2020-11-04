import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

EMPTY_TEXT = "Задан пустой\nпоисковый запрос"
EMPTY_RES = "По вашему запросу\nничего не найдено"


class SearchPage(unittest.TestCase):
    nav_search = "[bem-id='182']"
    nav_search_button = "[bem-id='185']"
    page_search = "[bem-id='191']"
    browser = webdriver.Chrome('./chromedriver')
    main_search_text = "search_value"
    value_attribute = "value"
    no_results_title = "[class^='noResultsTitle']"
    main_search_input = "[data-qa='input']"
    results_numb = "[class^='totalResults']"
    only_question_checkbox = "[class^='checkbox']"
    result_question_link = "[class^='question__link_holder']"
    login_input = "mailbox:login-input"
    password_input = "mailbox:password-input"
    login_submit_button = "mailbox:submit-button"
    test_email = os.environ.get('LOGIN_2')
    test_password = os.environ.get('PASSWORD_2')
    letter_line = "dataset-letters"
    select_category_button = "[data-qa='select-button']"
    # category = "[data-qa='select-list-item']"
    category_line = "[data-qa-value='1']"
    select_subcategory_button = "[data-qa-value='allSubCats']"
    subcategory_line = "[data-qa-value='1394']"
    ask_more_button = "[href^='/ask/']"
    question_input_area = "[name='question_text']"

    def input_in_nav_search(self, text):
        browser = self.browser
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.nav_search)))
        search = browser.find_element_by_css_selector(self.nav_search)
        search.send_keys(text)

    def submit_nav_search(self):
        browser = self.browser
        button = browser.find_element_by_css_selector(self.nav_search_button)
        button.click()

    def get_nav_search_text(self):
        browser = self.browser
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, self.main_search_text)))
        nav_text = browser.find_element_by_css_selector(self.nav_search).get_attribute(self.value_attribute)
        return nav_text

    def get_main_search_text(self):
        browser = self.browser
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, self.main_search_text)))
        str_text = browser.find_element_by_name(self.main_search_text).get_attribute(self.value_attribute)
        return str_text

    def compare_search_text(self):
        self.assertEqual(self.get_main_search_text(), self.get_nav_search_text())

    def open_otvet_page(self):
        self.browser.get("https://otvet.mail.ru")

    def open_search_page(self):
        self.browser.get("https://otvet.mail.ru/search")

    def check_empty_text(self):
        browser = self.browser
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.no_results_title)))
        empty_text = browser.find_element_by_css_selector(self.no_results_title).text
        self.assertEqual(empty_text, EMPTY_TEXT)

    def check_empty_res(self):
        browser = self.browser
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.no_results_title)))
        empty_text = browser.find_element_by_css_selector(self.no_results_title).text
        self.assertEqual(empty_text, EMPTY_RES)

    def input_in_main_search(self, text):
        browser = self.browser
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.main_search_input)))
        input = browser.find_element_by_css_selector(self.main_search_input)
        input.send_keys(text)

    def submit_main_search(self):
        browser = self.browser
        input = browser.find_element_by_css_selector(self.main_search_input)
        input.send_keys(Keys.ENTER)
        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            self.result_question_link + ", " + self.no_results_title)))

    def get_total_count(self):
        browser = self.browser
        total_count = browser.find_element_by_css_selector(self.results_numb).text.replace(" ", "")
        total_count = int(re.findall(r'\d+', total_count)[0])
        return total_count

    def toggle_only_question_checkbox(self):
        browser = self.browser
        browser.find_element_by_css_selector(self.only_question_checkbox).click()

    def compare_counts(self):
        total_count = self.get_total_count()
        self.toggle_only_question_checkbox()
        self.submit_main_search()
        only_question_count = self.get_total_count()
        self.assertGreaterEqual(total_count, only_question_count)

    def login(self):
        browser = self.browser
        browser.get("https://mail.ru/")
        browser.find_element_by_id(self.login_input).send_keys(self.test_email)
        browser.find_element_by_id(self.login_submit_button).click()
        browser.find_element_by_id(self.password_input).send_keys(self.test_password)
        browser.find_element_by_id(self.login_submit_button).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.letter_line)))
        print("LOGIN")

    def click_select_category(self):
        browser = self.browser
        browser.find_element_by_css_selector(self.select_category_button).click()

    def select_category(self):
        browser = self.browser
        browser.find_element_by_css_selector(self.category_line).click()

    def click_select_subcategory(self):
        browser = self.browser
        browser.find_element_by_css_selector(self.select_subcategory_button).click()

    def select_subcategory(self):
        browser = self.browser
        browser.find_element_by_css_selector(self.subcategory_line).click()

    def compare_categories_count(self):
        total_count = self.get_total_count()
        self.click_select_category()
        self.select_category()
        self.submit_main_search()
        category_count = self.get_total_count()
        self.assertGreaterEqual(total_count, category_count)
        self.click_select_subcategory()
        self.select_subcategory()
        self.submit_main_search()
        subcategory_count = self.get_total_count()
        self.assertGreaterEqual(category_count, subcategory_count)

    def click_ask_more_button(self):
        browser = self.browser
        browser.find_element_by_css_selector(self.ask_more_button).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.question_input_area)))

    def get_question_input_text(self):
        browser = self.browser
        question_text = browser.find_element_by_css_selector(self.question_input_area). \
            get_attribute(self.value_attribute)
        return question_text

    def compare_text(self, text):
        question_text = self.get_question_input_text()
        self.assertEqual(text, question_text)
