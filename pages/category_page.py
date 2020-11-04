import os
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CategoryPage(unittest.TestCase):
    category_button = "[data-item-id='category']"
    category_line = "[name='clb1828220']"
    gold_fond_line = "[name='clb1828015']"
    all_categories_line = "[href='/categories/']"
    all_categories_header = "[class^='categoriesHeading']"
    browser = webdriver.Chrome('./chromedriver')
    page_main_category = "[class^='page-index--h1']"
    page_border_category = "[class='black list__title']"
    login_input = "mailbox:login-input"
    password_input = "mailbox:password-input"
    login_submit_button = "mailbox:submit-button"
    test_email = "testmail7171@mail.ru"
    test_password = os.environ.get('PASSWORD_2')
    letter_line = "dataset-letters"
    gold_fond_text = "//*[contains(text(), 'Золотой Фонд проекта Ответы@Mail.Ru')]"

    def open_main_page(self):
        self.browser.get("https://otvet.mail.ru")

    def click_category_button(self):
        browser = self.browser
        browser.find_element_by_css_selector(self.category_button).click()

    def select_category(self):
        browser = self.browser
        category = browser.find_element_by_css_selector(self.category_line)
        category_text = category.find_element_by_css_selector("*").text
        category.click()
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.page_main_category)))
        return category_text

    def compare_categories(self):
        browser = self.browser
        category_choosen = self.select_category()
        page_main_category = browser.find_element_by_css_selector(self.page_main_category).text
        page_border_category = browser.find_element_by_css_selector(self.page_border_category).text
        self.assertEqual(category_choosen, page_main_category, page_border_category)

    def select_all_categories(self):
        browser = self.browser
        category = browser.find_element_by_css_selector(self.all_categories_line)
        category_text = category.find_element_by_css_selector("*").text
        category.click()
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.all_categories_header)))
        return category_text

    def select_gold_fond(self):
        browser = self.browser
        category = browser.find_element_by_css_selector(self.gold_fond_line)
        category_text = category.find_element_by_css_selector("*").text
        category.click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, self.gold_fond_text)))
        return category_text

    def login(self):
        browser = self.browser
        browser.get("https://mail.ru/")
        browser.find_element_by_id(self.login_input).send_keys(self.test_email)
        browser.find_element_by_id(self.login_submit_button).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, self.password_input)))
        browser.find_element_by_id(self.password_input).send_keys(self.test_password)
        browser.find_element_by_id(self.login_submit_button).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.letter_line)))
        print("LOGIN")
