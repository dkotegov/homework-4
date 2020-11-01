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

    def login(self):
        browser = self.browser
        browser.get("https://mail.ru/")
        browser.find_element_by_id('mailbox:login-input').send_keys("testmail7171@mail.ru")
        browser.find_element_by_id("mailbox:submit-button").click()
        browser.find_element_by_id('mailbox:password-input').send_keys("cooltest1999")
        browser.find_element_by_id("mailbox:submit-button").click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "dataset-letters")))
        print("LOGIN")

    # def send_query(self, text):
    #     browser = self.browser
    #     input = browser.find_element_by_css_selector("[data-qa='input']")
    #     input.send_keys(text)
    #     input.send_keys(Keys.ENTER)

    def test_nav_search_input(self,text):
        self.browser.get("https://otvet.mail.ru")
        browser = self.browser
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.nav_search)))
        search = browser.find_element_by_css_selector(self.nav_search)
        search.send_keys(text)
        button = browser.find_element_by_css_selector(self.nav_search_button)
        button.click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "search_value")))
        nav_text = browser.find_element_by_css_selector(self.nav_search).get_attribute('value')
        str_text = browser.find_element_by_name("search_value").get_attribute('value')
        self.assertEqual(nav_text, str_text)

    def test_empty_query(self, text):
        self.browser.get("https://otvet.mail.ru/search")
        browser = self.browser
        input = browser.find_element_by_css_selector("[data-qa='input']")
        input.send_keys(text)
        input.send_keys(Keys.ENTER)
        input.send_keys(text)
        # Deleting hear
        # input.clear()
        input.send_keys(Keys.COMMAND, 'a')
        input.send_keys(Keys.BACKSPACE)
        input.send_keys(Keys.ENTER)
        WebDriverWait(browser, 20)
        empty_text = browser.find_element_by_css_selector("[class^='noResultsTitle']").text
        self.assertEqual(empty_text, EMPTY_TEXT)

    def test_special_symb(self, text):
        self.browser.get("https://otvet.mail.ru/search")
        browser = self.browser
        input = browser.find_element_by_css_selector("[data-qa='input']")
        input.send_keys(text)
        input.send_keys(Keys.ENTER)
        input.send_keys(text)

        input.send_keys(Keys.COMMAND, 'a')
        input.send_keys(Keys.BACKSPACE)
        input.send_keys("!@#$%^&*()")
        input.send_keys(Keys.ENTER)
        WebDriverWait(browser, 20)
        empty_res = browser.find_element_by_css_selector("[class^='noResultsTitle']").text
        self.assertEqual(empty_res, EMPTY_RES)

    def test_question_only_button(self, text):
        self.browser.get("https://otvet.mail.ru/search")
        browser = self.browser
        input = browser.find_element_by_css_selector("[data-qa='input']")
        input.send_keys(text)
        input.send_keys(Keys.ENTER)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='question__link_holder']")))
        total_count = browser.find_element_by_css_selector("[class^='totalResults']").text.replace(" ", "")
        browser.find_element_by_css_selector("[class^='checkbox']").click()
        input.send_keys(Keys.ENTER)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='question__link_holder']")))
        only_quest_count = browser.find_element_by_css_selector("[class^='totalResults']").text.replace(" ", "")
        self.assertGreaterEqual(
            re.findall(r'\d+', total_count)[0], re.findall(r'\d+', only_quest_count)[0])
