import os

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

EMPTY_TEXT = "Задан пустой\nпоисковый запрос"
EMPTY_RES = "По вашему запросу\nничего не найдено"


class SearchPage:
    NAV_SEARCH = "[bem-id='182']"
    NAV_SEARCH_BUTTON = "[bem-id='185']"
    PAGE_SEARCH = "[bem-id='191']"
    MAIN_SEARCH_TEX = "search_value"
    VALUE_ATTRIBUTE = "value"
    NO_RESULTS_TITLE = "[class^='noResultsTitle']"
    MAIN_SEARCH_INPUT = "[data-qa='input']"
    RESULTS_NUMB = "[class^='totalResults']"
    ONLY_QUESTION_CHECKBOX = "[class^='checkbox']"
    RESULT_QUESTION_LINK = "[class^='question__link']"
    LOGIN_INPUT = "mailbox:login-input"
    PASSWORD_INPUT = "mailbox:password-input"
    LOGIN_SUBMIT_BUTTON = "mailbox:submit-button"
    TEST_EMAIL = os.environ.get('LOGIN_1')
    TEST_PASSWORD = os.environ.get('PASSWORD_1')
    LETTER_LINE = "dataset-letters"
    SELECT_CATEGORY_BUTTON = "[data-qa='select-button']"
    CATEGORY_LINE = "[data-qa-value='1']"
    SELECT_SUBCATEGORY_BUTTON = "[data-qa-value='allSubCats']"
    SUBCATEGORY_LINE = "[data-qa-value='1394']"
    ASK_MORE_BUTTON = "[href^='/ask/']"
    QUESTION_INPUT_AREA = "[name='question_text']"

    def __init__(self, browser):
        self.browser = browser

    def input_in_nav_search(self, text):
        browser = self.browser
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.NAV_SEARCH)))
        search = browser.find_element_by_css_selector(self.NAV_SEARCH)
        search.send_keys(text)

    def submit_nav_search(self):
        browser = self.browser
        button = browser.find_element_by_css_selector(self.NAV_SEARCH_BUTTON)
        button.click()

    def get_nav_search_text(self):
        browser = self.browser
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, self.MAIN_SEARCH_TEX)))
        nav_text = browser.find_element_by_css_selector(self.NAV_SEARCH).get_attribute(self.VALUE_ATTRIBUTE)
        return nav_text

    def get_main_search_text(self):
        browser = self.browser
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, self.MAIN_SEARCH_TEX)))
        str_text = browser.find_element_by_name(self.MAIN_SEARCH_TEX).get_attribute(self.VALUE_ATTRIBUTE)
        return str_text

    def open_otvet_page(self):
        self.browser.get("https://otvet.mail.ru")

    def open_search_page(self):
        self.browser.get("https://otvet.mail.ru/search")

    def check_empty_text(self):
        browser = self.browser
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.NO_RESULTS_TITLE)))
        empty_text = browser.find_element_by_css_selector(self.NO_RESULTS_TITLE).text
        return empty_text

    def check_empty_res(self):
        browser = self.browser
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.NO_RESULTS_TITLE)))
        empty_res = browser.find_element_by_css_selector(self.NO_RESULTS_TITLE).text
        return empty_res

    def input_in_main_search(self, text):
        browser = self.browser
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.MAIN_SEARCH_INPUT)))
        input = browser.find_element_by_css_selector(self.MAIN_SEARCH_INPUT)
        input.send_keys(text)

    def submit_main_search(self):
        browser = self.browser
        input = browser.find_element_by_css_selector(self.MAIN_SEARCH_INPUT)
        input.send_keys(Keys.ENTER)
        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            self.RESULT_QUESTION_LINK + ", " + self.NO_RESULTS_TITLE)))

    def get_total_count(self):
        browser = self.browser
        total_count = browser.find_element_by_css_selector(self.RESULTS_NUMB).text.replace(" ", "")
        total_count = int(re.findall(r'\d+', total_count)[0])
        return total_count

    def toggle_only_question_checkbox(self):
        browser = self.browser
        browser.find_element_by_css_selector(self.ONLY_QUESTION_CHECKBOX).click()

    def login(self):
        browser = self.browser
        browser.get("https://mail.ru/")
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, self.LOGIN_INPUT)))
        browser.find_element_by_id(self.LOGIN_INPUT).send_keys(self.TEST_EMAIL)
        browser.find_element_by_id(self.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, self.PASSWORD_INPUT)))
        browser.find_element_by_id(self.PASSWORD_INPUT).send_keys(self.TEST_PASSWORD)
        browser.find_element_by_id(self.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.LETTER_LINE)))

    def click_select_category(self):
        browser = self.browser
        browser.find_element_by_css_selector(self.SELECT_CATEGORY_BUTTON).click()

    def select_category(self):
        browser = self.browser
        browser.find_element_by_css_selector(self.CATEGORY_LINE).click()

    def click_select_subcategory(self):
        browser = self.browser
        browser.find_element_by_css_selector(self.SELECT_SUBCATEGORY_BUTTON).click()

    def select_subcategory(self):
        browser = self.browser
        browser.find_element_by_css_selector(self.SUBCATEGORY_LINE).click()

    def click_ask_more_button(self):
        browser = self.browser
        browser.find_element_by_css_selector(self.ASK_MORE_BUTTON).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.QUESTION_INPUT_AREA)))

    def get_question_input_text(self):
        browser = self.browser
        question_text = browser.find_element_by_css_selector(self.QUESTION_INPUT_AREA). \
            get_attribute(self.VALUE_ATTRIBUTE)
        return question_text
