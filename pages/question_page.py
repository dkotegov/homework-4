from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.common import Common


class QuestionPage:
    ASK_QUESTION_PAGE = "https://otvet.mail.ru/ask"
    PUBLISH_QUESTION_TIMEOUT = 60

    TOPIC_INPUT_XPATH = '//textarea[@name="question_text"]'
    TEXT_INPUT_XPATH = '//textarea[@name="question_additional"]'
    CATEGORY_LIST_XPATH = '//div[@name="select_parents_categories"]'
    CATEGORY_XPATH = '//div[@data-qa="select-list-item"][@data-qa-value="1"]'
    SUBCATEGORY_LIST_XPATH = '//div[@name="select_childs_categories"]'
    SUBCATEGORY_XPATH = '//div[@data-qa="select-list-item"][@data-qa-value="1394"]'
    PUBLISH_BUTTON_XPATH = '//a[@data-qa="input-question_submit"]'
    QUESTION_LIKE_BUTTON_XPATH = '//div[@title="Нравится"]/a[@title="Нравится"]'
    ANSWER_INPUT_XPATH = '//textarea[@name="inputBody"]'
    ANSWER_BUTTON_XPATH = '//a[contains(@class,"btn__submit")]'
    COMMENT_INPUT_XPATH = '//textarea[@name="inputBody"][@placeholder="Написать комментарий"]'
    COMMENT_BUTTON_XPATH = '//a[contains(@class," submit_")]'

    def __init__(self, browser):
        self.browser = browser
        self.common = Common(browser)

    def ask_question(self, topic, text) -> str:
        self.common.open_page(self.ASK_QUESTION_PAGE)
        WebDriverWait(self.browser, self.common.WAIT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, self.PUBLISH_BUTTON_XPATH)))

        self.browser.find_element_by_xpath(self.TOPIC_INPUT_XPATH).clear()
        self.browser.find_element_by_xpath(self.TOPIC_INPUT_XPATH).send_keys(topic)

        self.browser.find_element_by_xpath(self.TEXT_INPUT_XPATH).clear()
        self.browser.find_element_by_xpath(self.TEXT_INPUT_XPATH).send_keys(text)

        self.browser.find_element_by_xpath(self.CATEGORY_LIST_XPATH).click()
        self.browser.find_element_by_xpath(self.CATEGORY_XPATH).click()

        self.browser.find_element_by_xpath(self.SUBCATEGORY_LIST_XPATH).click()
        self.browser.find_element_by_xpath(self.SUBCATEGORY_XPATH).click()

        self.browser.find_element_by_xpath(self.PUBLISH_BUTTON_XPATH).click()

        WebDriverWait(self.browser, self.PUBLISH_QUESTION_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, self.QUESTION_LIKE_BUTTON_XPATH)))

        return self.browser.current_url

    def answer_question(self, question_url, text):
        self.common.open_page(question_url)
        WebDriverWait(self.browser, self.common.WAIT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, self.ANSWER_BUTTON_XPATH)))

        self.browser.find_element_by_xpath(self.ANSWER_INPUT_XPATH).clear()
        self.browser.find_element_by_xpath(self.ANSWER_INPUT_XPATH).send_keys(text)
        self.browser.find_element_by_xpath(self.ANSWER_BUTTON_XPATH).click()

    def like_question(self, question_url):
        self.common.open_page(question_url)
        WebDriverWait(self.browser, self.common.WAIT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, self.QUESTION_LIKE_BUTTON_XPATH)))

        self.browser.find_element_by_xpath(self.QUESTION_LIKE_BUTTON_XPATH).click()

    def like_answer(self, question_url, answer):
        self.common.open_page(question_url)
        WebDriverWait(self.browser, self.common.WAIT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, self.QUESTION_LIKE_BUTTON_XPATH)))

        answer_like_xpath = '//div[text()="{}"]/../..//a[@title="Нравится"]'.format(answer)
        self.browser.find_element_by_xpath(answer_like_xpath).click()

    def comment_answer(self, question_url, answer, text):
        self.common.open_page(question_url)
        WebDriverWait(self.browser, self.common.WAIT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, self.QUESTION_LIKE_BUTTON_XPATH)))

        answer_comment_xpath = '//div[text()="{}"]/../..//a[contains(@class,"button_comment")]'.format(answer)
        self.browser.find_element_by_xpath(answer_comment_xpath).click()
        WebDriverWait(self.browser, self.common.WAIT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, self.COMMENT_INPUT_XPATH)))

        self.browser.find_element_by_xpath(self.COMMENT_INPUT_XPATH).clear()
        self.browser.find_element_by_xpath(self.COMMENT_INPUT_XPATH).send_keys(text)
        self.browser.find_element_by_xpath(self.COMMENT_BUTTON_XPATH).click()
