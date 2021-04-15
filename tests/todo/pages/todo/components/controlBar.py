from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from testutils import Component
from .contextMenu import ContextMenu


class ControlBar(Component):
    container = '[class^="Sidebar_base"]'

    class Selectors:
        create_list_input = '[class^="CreateInput_base"] input'
        task_list = lambda name: f'//li[starts-with(@class, "SidebarCustoms_item")]//p[text()="{name}"]/..'

    def create_list(self, title):
        self._wait_clickable(By.CSS_SELECTOR, self.container + ' ' + self.Selectors.create_list_input)
        self._fill_input(By.CSS_SELECTOR, self.container + ' ' + self.Selectors.create_list_input, title, True)

    def open_task_list(self, title):
        self._wait_visible(By.XPATH, self.Selectors.task_list(title)).click()

    def delete_task_list(self, title):
        self._wait_visible(By.XPATH, self.Selectors.task_list(title))
        ActionChains(self.driver)\
            .context_click(self.driver.find_element_by_xpath(self.Selectors.task_list(title))).perform()
        menu = ContextMenu(self.driver)
        menu.wait_self()
        menu.delete_task_list()
