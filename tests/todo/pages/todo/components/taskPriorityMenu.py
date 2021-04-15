from selenium.webdriver.common.by import By

from testutils import Component


class TaskPriorityMenu(Component):
    container = 'div[class^="TaskPriorityDropdown"]'

    class Selectors:
        high_priority = '[class^="MenuButton_base"]:nth-child(1)'
        medium_priority = '[class^="MenuButton_base"]:nth-child(2)'
        low_priority = '[class^="MenuButton_base"]:nth-child(3)'
        none_priority = '[class^="MenuButton_base"]:nth-child(4)'

    def choose_priority(self, priority_selector):
        self.wait_self()
        self._wait_visible(By.CSS_SELECTOR, self.container + ' ' + priority_selector)
        self._wait_clickable(By.CSS_SELECTOR, self.container + ' ' + priority_selector)
        self.driver.find_element_by_css_selector(self.container).\
            find_element_by_css_selector(priority_selector).click()
