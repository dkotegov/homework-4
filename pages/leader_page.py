import os
import re

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LeaderPage:
    login_input = "mailbox:login-input"
    password_input = "mailbox:password-input"
    login_submit_button = "mailbox:submit-button"
    test_email = "testmail7171@mail.ru"
    test_password = os.environ.get('PASSWORD_2')
    letter_line = "dataset-letters"
    # leader_user = "[data-qa='avatar_link']"
    leader_user = "[class^='topUserItem']"
    leader_user_score = "[class^='pointsDiffTop']"
    leader_user_profile = "[class^='rank']"
    time_range_select = "[data-qa-value='week']"
    all_time_range_select = "[data-qa-value='all']"

    def __init__(self, browser):
        self.browser = browser

    def login(self):
        browser = self.browser
        browser.get("https://mail.ru/")
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, self.login_input)))
        browser.find_element_by_id(self.login_input).send_keys(self.test_email)
        browser.find_element_by_id(self.login_submit_button).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, self.password_input)))
        browser.find_element_by_id(self.password_input).send_keys(self.test_password)
        browser.find_element_by_id(self.login_submit_button).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.letter_line)))
        print("LOGIN")

    def open_leader_page(self):
        self.browser.get("https://otvet.mail.ru/top")

    def select_all_time_range_filter(self):
        browser = self.browser
        browser.find_element_by_css_selector(self.time_range_select).click()
        browser.find_element_by_css_selector(self.all_time_range_select).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.leader_user)))

    def focus_on_user(self):
        browser = self.browser
        user = browser.find_elements_by_css_selector(self.leader_user)[1]
        action = webdriver.ActionChains(browser)
        action.move_to_element(user)
        action.perform()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.leader_user_profile)))
        profile_text = browser.find_element_by_css_selector(self.leader_user_profile).text.replace(" ", "")
        profile_score = int(re.findall(r'\d+', profile_text)[0])
        return profile_score

    def get_user_score(self):
        browser = self.browser
        user = browser.find_elements_by_css_selector(self.leader_user)[1]
        user_score = int(user.find_element_by_css_selector(self.leader_user_score).text.replace(" ", ""))
        return user_score
