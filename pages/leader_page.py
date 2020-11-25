import os
import re

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LeaderPage:
    LOGIN_INPUT = "mailbox:login-input"
    PASSWORD_INPUT = "mailbox:password-input"
    LOGIN_SUBMIT_BUTTON = "mailbox:submit-button"
    TEST_EMAIL = os.environ.get('LOGIN_1')
    TEST_PASSWORD = os.environ.get('PASSWORD_1')
    LETTER_LINE = "dataset-letters"
    LEADER_USER = "[class^='topUserItem']"
    LEADER_USER_SCORE = "[class^='pointsDiffTop']"
    LEADER_USER_PROFILE = "[class^='rank']"
    TIME_RANGE_SELECT = "[data-qa-value='week']"
    ALL_TIME_RANGE_SELECT = "[data-qa-value='all']"

    def __init__(self, browser):
        self.browser = browser

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

    def open_leader_page(self):
        self.browser.get("https://otvet.mail.ru/top")

    def select_all_time_range_filter(self):
        browser = self.browser
        browser.find_element_by_css_selector(self.TIME_RANGE_SELECT).click()
        browser.find_element_by_css_selector(self.ALL_TIME_RANGE_SELECT).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.LEADER_USER)))

    def focus_on_user(self):
        browser = self.browser
        user = browser.find_elements_by_css_selector(self.LEADER_USER)[1]
        action = webdriver.ActionChains(browser)
        action.move_to_element(user)
        action.perform()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.LEADER_USER_PROFILE)))
        profile_text = browser.find_element_by_css_selector(self.LEADER_USER_PROFILE).text.replace(" ", "")
        profile_score = int(re.findall(r'\d+', profile_text)[0])
        return profile_score

    def get_user_score(self):
        browser = self.browser
        user = browser.find_elements_by_css_selector(self.LEADER_USER)[1]
        user_score = int(user.find_element_by_css_selector(self.LEADER_USER_SCORE).text.replace(" ", ""))
        return user_score
