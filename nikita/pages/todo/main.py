from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from nikita.pages.todo.default import Page
from nikita.utils import wait_for_element_by_selector, wait_for_element_by_xpath, wait_for_url_to_match
from nikita.constants import TODO_MAIN_URL, TODO_BASE_URL, TODO_LIST_URL_REGEX

class MainPage(Page):
    URL = TODO_MAIN_URL
    LIST_NAME_INPUT = '.CreateInput_base__7NNLJ.CreateInput_sidebar__1VWLw input[type="text"]'
    LIST_NAME = './/li[@class="SidebarCustoms_item__3etv7"]//p[. = "{}"]/../..'
    DELETE = './/div[@class="ContextMenu_base__2Dkdw"]//p[. = "Удалить"]'
    LIST_CLASS = 'SidebarCustoms_item__3etv7'

    def create_list(self, name):
        wait_for_element_by_selector(self.driver, self.LIST_NAME_INPUT).send_keys(name + Keys.ENTER)

    def delete_list(self, name):
        actionChains = ActionChains(self.driver)
        element = wait_for_element_by_xpath(self.driver, self.LIST_NAME.format(name))
        actionChains.context_click(element).perform()
        wait_for_element_by_xpath(self.driver, self.DELETE).click()

    def count_lists(self):
        return len(self.driver.find_elements_by_class_name(self.LIST_CLASS))

    def count_lists_by_name(self, name):
        return len(self.driver.find_elements_by_xpath(self.LIST_NAME.format(name)))

    def wait_for_list(self, name):
        wait_for_element_by_xpath(self.driver, self.LIST_NAME.format(name))

    def wait_for_list_to_disappear(self, name):
        wait_for_element_by_xpath(self.driver, self.LIST_NAME.format(name), visible=False)

    def wait_for_list_not_to_appear(self, name, amount):
        try:
            WebDriverWait(self.driver, 1).until(lambda driver:
                len(driver.find_elements_by_xpath(self.LIST_NAME.format(name))) > amount
            )
            raise 'Appeared ' + self.LIST_NAME.format(name)
        except TimeoutException:
            pass

    def open_list(self, name):
        wait_for_element_by_xpath(self.driver, self.LIST_NAME.format(name)).click()
        wait_for_url_to_match(self.driver, TODO_LIST_URL_REGEX)
        splitted = self.driver.current_url.split('/')
        return splitted[len(splitted) - 1]

    def open_list_by_id(self, id):
        self.driver.get(TODO_BASE_URL + id)
