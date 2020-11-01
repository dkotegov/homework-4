import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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

    def test_nav_search_input(self):
        self.browser.get("https://otvet.mail.ru")
        browser = self.browser
        print(browser.title)

        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.nav_search)))
        search = browser.find_element_by_css_selector(self.nav_search)
        search.send_keys("TEXT")

        button = browser.find_element_by_css_selector(self.nav_search_button)
        button.click()

        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "search_value")))
        nav_text = browser.find_element_by_css_selector(self.nav_search).get_attribute('value')
        str_text = browser.find_element_by_name("search_value").get_attribute('value')
        # str_text = browser.find_element_by_name("search_value").get_attribute('value')
        print(nav_text, " ! ", str_text)
        self.assertEqual(nav_text, str_text)
