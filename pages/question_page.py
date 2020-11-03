from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.common import Common


class QuestionPage:
    ask_question_page = "https://otvet.mail.ru/ask"
    publish_question_timeout = 60

    topic_input_xpath = '/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/form/div/div[1]/label/div[4]/div/div/textarea'
    text_input_xpath = '/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/form/div/div[2]/label/div[4]/div[1]/div/textarea'
    category_list_xpath = '/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/form/div/div[3]/label[1]/div[2]/div/div[1]/div/span'
    category_xpath = '/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/form/div/div[3]/label[1]/div[2]/div/div[2]/div/div[2]/div[1]/div/span'
    subcategory_list_xpath = '/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/form/div/div[3]/label[2]/div[2]'
    subcategory_xpath = '/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/form/div/div[3]/label[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/span'
    publish_button_xpath = '/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/form/div/div[5]/a/div'
    # publish_confirm_xpath = '/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[1]'

    question_like_button_xpath = '/html/body/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div[4]/div/div/div[2]/div/a/div'

    answer_input_xpath = '/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/form/div[1]/div/label/div[2]/div[1]/div[1]/textarea'
    answer_button_xpath = '/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/form/div[2]/a/div'

    def __init__(self, browser):
        self.browser = browser
        self.common = Common(browser)

    def ask_question(self, topic, text) -> str:
        self.common.open_page(self.ask_question_page)
        WebDriverWait(self.browser, self.common.wait_timeout).until(
            EC.presence_of_element_located((By.XPATH, self.publish_button_xpath)))

        self.browser.find_element_by_xpath(self.topic_input_xpath).clear()
        self.browser.find_element_by_xpath(self.topic_input_xpath).send_keys(topic)

        self.browser.find_element_by_xpath(self.text_input_xpath).clear()
        self.browser.find_element_by_xpath(self.text_input_xpath).send_keys(text)

        self.browser.find_element_by_xpath(self.category_list_xpath).click()
        self.browser.find_element_by_xpath(self.category_xpath).click()

        self.browser.find_element_by_xpath(self.subcategory_list_xpath).click()
        self.browser.find_element_by_xpath(self.subcategory_xpath).click()

        self.browser.find_element_by_xpath(self.publish_button_xpath).click()

        WebDriverWait(self.browser, self.publish_question_timeout).until(
            EC.presence_of_element_located((By.XPATH, self.question_like_button_xpath)))

        return self.browser.current_url

    def answer_question(self, question_url, text):
        self.common.open_page(question_url)
        WebDriverWait(self.browser, self.common.wait_timeout).until(
            EC.presence_of_element_located((By.XPATH, self.answer_button_xpath)))

        self.browser.find_element_by_xpath(self.answer_input_xpath).clear()
        self.browser.find_element_by_xpath(self.answer_input_xpath).send_keys(text)
        self.browser.find_element_by_xpath(self.answer_button_xpath).click()

    def like_question(self, question_url):
        self.common.open_page(question_url)
        WebDriverWait(self.browser, self.common.wait_timeout).until(
            EC.presence_of_element_located((By.XPATH, self.question_like_button_xpath)))

        self.browser.find_element_by_xpath(self.question_like_button_xpath).click()
