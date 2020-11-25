import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CategoryPage:
    CATEGORY_BUTTON = "[data-item-id='category']"
    CATEGORY_LINE = "[name='clb1828220']"
    GOLD_FOND_LINE = "[name='clb1828015']"
    ALL_CATEGORIES_LINE = "[href='/categories/']"
    ALL_CATEGORIES_HEADER = "[class^='categoriesHeading']"
    PAGE_MAIN_CATEGORY = "[class^='page-index--h1']"
    PAGE_BORDER_CATEGORY = "[class='black list__title']"
    LOGIN_INPUT = "mailbox:login-input"
    PASSWORD_INPUT = "mailbox:password-input"
    LOGIN_SUBMIT_BUTTON = "mailbox:submit-button"
    TEST_EMAIL = os.environ.get('LOGIN_1')
    TEST_PASSWORD = os.environ.get('PASSWORD_1')
    LETTER_LINE = "dataset-letters"
    GOLD_FOND_TEXT = "//*[contains(text(), 'Золотой Фонд проекта Ответы@Mail.Ru')]"

    def __init__(self, browser):
        self.browser = browser

    def open_main_page(self):
        self.browser.get("https://otvet.mail.ru")

    def click_category_button(self):
        browser = self.browser
        browser.find_element_by_css_selector(self.CATEGORY_BUTTON).click()

    def select_category(self):
        browser = self.browser
        category = browser.find_element_by_css_selector(self.CATEGORY_LINE)
        category_text = category.find_element_by_css_selector("*").text
        category.click()
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.PAGE_MAIN_CATEGORY)))
        return category_text

    def get_main_category_text(self):
        browser = self.browser
        page_main_category = browser.find_element_by_css_selector(self.PAGE_MAIN_CATEGORY).text
        return page_main_category

    def get_border_category_text(self):
        browser = self.browser
        page_border_category = browser.find_element_by_css_selector(self.PAGE_BORDER_CATEGORY).text
        return page_border_category

    def select_all_categories(self):
        browser = self.browser
        category = browser.find_element_by_css_selector(self.ALL_CATEGORIES_LINE)
        category_text = category.find_element_by_css_selector("*").text
        category.click()
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.ALL_CATEGORIES_HEADER)))
        return category_text

    def select_gold_fond(self):
        browser = self.browser
        category = browser.find_element_by_css_selector(self.GOLD_FOND_LINE)
        category_text = category.find_element_by_css_selector("*").text
        category.click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, self.GOLD_FOND_TEXT)))
        return category_text

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
        print("LOGIN")
