from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

from base_classes.component import Component


class CreateTaskForm(Component):
    CONTAINER = '//div[contains(@class, "js-addNewTask")]'

    TITLE_INPUT = '//input[@id="inputNewTaskTitle"]'
    CLOSE_BUTTON = None
    SUBMIT_BUTTON = None
    CLOSED_FORM = '//div[contains(@class, "task-list-add-task-button")' \
                  ' and contains(@class,"js-addNewTask")]'

    def __init__(self, driver: WebDriver, column_id: int):
        Component.__init__(self, driver)
        self.column_id = column_id
        self.CONTAINER = f'//div[contains(@class, "js-addNewTask") and @data-column-id="{column_id}"]'
        self.SUBMIT_BUTTON = f'//div[@id="addTaskButton{column_id}"]'
        self.CLOSE_BUTTON = f'//div[@id="closeNewTaskFormButton{column_id}"]'
        self.CLOSED_FORM = f'//div[contains(@class, "task-list-add-task-button")' \
                           f' and contains(@class,"js-addNewTask")' \
                           f' and @data-column-id="{column_id}"]'

    def open(self):
        self.driver.find_element_by_xpath(self.CONTAINER).click()

    def close(self):
        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

    def set_title(self, title: str):
        self.driver.find_element_by_xpath(self.TITLE_INPUT).send_keys(title)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()

    def wait_for_closed(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(self.CLOSED_FORM)
        )
