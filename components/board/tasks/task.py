from selenium.webdriver.remote.webdriver import WebDriver

from base_classes.component import Component


class Task(Component):
    CONTAINER = '//div[contains(@class, "js-taskSettings")]'
    TITLE = '//div[@class="task-mini__description"]'

    def __init__(self, driver: WebDriver, column_id: int, task_id: int):
        Component.__init__(self, driver)

        self.column_id = column_id
        self.task_id = task_id

        self.CONTAINER = '//div[contains(@class, "js-taskSettings") ' \
                         f'and @data-column-id="{column_id}"' \
                         f'and @data-task-id="{task_id}"]'

    def get_title(self) -> str:
        return self.driver.find_element_by_xpath(self.CONTAINER).find_element_by_xpath(self.TITLE).text

    def open_settings(self):
        self.driver.find_element_by_xpath(self.CONTAINER).click()
