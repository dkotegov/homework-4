from component import Component
from selenium.webdriver.support.ui import WebDriverWait
from sidebar import Sidebar


class FolderCreate(Component):
    BASE = '//div[@data-qa-id="layer-window-block"] '

    INPUT_FOLDER_NAME = BASE + '//input[@data-test-id="name"]'
    SUBMIT = BASE + '//button[@data-test-id="submit"]'
    MORE_SETTINGS = BASE + '//a[@data-test-id="moreSettings"]'
    SELECT_PARENT_FOLDER = BASE + \
        '//span[@data-test-id="createFolder-select-value"]'
    SELECT_INBOX_AS_PARENT = BASE + '//div[@data-test-id="select-value:0"]'
    SELECT_INBOX_AS_PARENT_FOLDER_WITH_PASSWORD = BASE + \
        '//div[@data-test-id="select-value:1"]'
    SELECT_FOLDER_AS_PARENT = BASE + '//div[@aria-label="{}"]'
    PASSWORD_CHECKBOX = BASE + '//label[@data-test-id="hasPassword"]'
    INPUT_FOLDER_PASSWORD = '//input[@data-test-id="password"]'
    INPUT_FOLDER_PASSWORD_REPEAT = '//input[@data-test-id="passwordRepeat"]'
    INPUT_FOLDER_PASSWORD_QUESTION = '//input[@data-test-id="question"]'
    INPUT_FOLDER_PASSWORD_ANSWER = '//input[@data-test-id="answer"]'
    INPUT_FOLDER_PASSWORD_USER_PWD = '//input[@data-test-id="userPassword"]'

    def set_name(self, name):
        name_input = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INPUT_FOLDER_NAME)
        )
        name_input.send_keys(name)

    def submit(self):
        submit = WebDriverWait(self.driver, 1, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT)
        )
        submit.click()

    def click_more_settings(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MORE_SETTINGS)
        ).click()

    def click_select_parent_inbox(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SELECT_PARENT_FOLDER)
        ).click()

    def select_parent_inbox(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SELECT_INBOX_AS_PARENT)
        ).click()

    def select_parent_folder(self, name):
        PARENT = self.SELECT_FOLDER_AS_PARENT.format(name)
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(PARENT)
        ).click()

    def click_set_password(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PASSWORD_CHECKBOX)
        ).click()

    def set_password(self, password):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INPUT_FOLDER_PASSWORD)
        ).send_keys(password)

    def set_password_repeat(self, password):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(
                self.INPUT_FOLDER_PASSWORD_REPEAT)
        ).send_keys(password)

    def set_question(self, question):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(
                self.INPUT_FOLDER_PASSWORD_QUESTION)
        ).send_keys(question)

    def set_answer(self, answer):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(
                self.INPUT_FOLDER_PASSWORD_ANSWER)
        ).send_keys(answer)

    def set_user_password(self, password):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(
                self.INPUT_FOLDER_PASSWORD_USER_PWD)
        ).send_keys(password)

    def select_parent_inbox_folder_with_password(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(
                self.SELECT_INBOX_AS_PARENT_FOLDER_WITH_PASSWORD)
        ).click()

    def create_folder(self, folder_name):
        sidebar = Sidebar(self.driver)
        sidebar.create_new_dir()
        self.set_name(folder_name)
        self.submit()

    def create_folder_with_password(self, folder_name, folder_pwd, user_pwd):
        sidebar = Sidebar(self.driver)
        sidebar.create_new_dir()
        self.set_name(folder_name)
        self.click_more_settings()
        self.click_set_password()
        self.submit()
        self.set_password(folder_pwd)
        self.set_password_repeat(folder_pwd)
        self.set_question(folder_pwd)
        self.set_answer(folder_pwd)
        self.set_user_password(user_pwd)
        self.submit()

    def create_folder_in_inbox(self, folder_name):
        sidebar = Sidebar(self.driver)
        sidebar.create_new_dir()
        self.set_name(folder_name)
        self.click_more_settings()
        self.click_select_parent_inbox()
        self.select_parent_inbox()
        self.submit()

    def create_folder_with_subfolder(self, folder_name, subfolder_name):
        sidebar = Sidebar(self.driver)
        sidebar.create_new_dir()
        self.set_name(subfolder_name)
        self.click_more_settings()
        self.click_select_parent_inbox()
        self.select_parent_folder(folder_name)
        self.submit()
