import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from egogoger.utils import wait_for_element_by_selector
from egogoger.default_page import DefaultPage, Component
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(DefaultPage):
    FINAL_PATH = 'https://todo.mail.ru/inbox'
    # Selectors
    CONTAINER = '#root'
    TITLE = '.ListTitle_base__1l0yT h1'
    OPTION_LIST = '.ContextMenu_base__2Dkdw'
    TODO_POPUP_ITEM = OPTION_LIST+' p.c019.c019.c0130'
    PRIORITY_LIST = '.Popup_base__2plk2'
    PRIORITY_LIST_ITEM = PRIORITY_LIST + ' .MenuButton_text__1DWJd'
    ACTIVE_PRIORITY_P = PRIORITY_LIST + \
        ' .MenuButton_base__2qd43.MenuButton_active__2j-To .MenuButton_text__1DWJd p'
    TODO = CONTAINER + ' li[data-task-id]'
    NEW_TODO_INPUT = "input.c0147[placeholder=\"Создать задачу\"]"
    SETTINGS_BUTTON = '.ASettingsButton_base__19nsY.ASettingsButton_normal__3ZTNb'
    SETTINGS_FRAME = '.ListMenu_base__2j-HN'
    SETTINGS_ITEM = SETTINGS_FRAME + ' .MenuButton_text__1DWJd'

    SORT_BY_PRIORITY = 'Сортировать по приоритету'

    TITLE_NAME = 'Основной'
    CHANGE_PRIORITY_TEXT = 'Изменить приоритет'
    TODO_DELETE_TEXT = 'Удалить'
    HIGH_PRIORITY = 'Высокий'
    MID_PRIORITY = 'Средний'
    LOW_PRIORITY = 'Низкий'
    NO_PRIORITY = 'Без приоритета'

    PRIORITY_NAMES = [HIGH_PRIORITY, MID_PRIORITY, LOW_PRIORITY, NO_PRIORITY]

    def __init__(self, driver, path='https://account.mail.ru/login?page=https://todo.mail.ru'):
        super().__init__(driver, path)

    def get_todos(self):
        return self.driver.find_elements_by_css_selector(self.TODO)

    def get_todo(self, index, test):
        try:
            todo = self.get_todos()[index]
            return todo
        except IndexError:
            test.fail(f'No todo at index {index}')
            return None

    def create_todo(self, name: str, index=None):
        self.driver.find_element_by_css_selector(self.NEW_TODO_INPUT).send_keys(name, Keys.RETURN)
        if index is not None:
            wait_for_element_by_selector(self.driver, f'{self.TODO}:nth-child({index+1})')
        else:
            wait_for_element_by_selector(self.driver, self.TODO)

    def delete_todos(self, test):
        try:
            self.driver.find_element_by_css_selector(self.PRIORITY_LIST_ITEM).click()
        except NoSuchElementException:
            pass
        
        # Delete all todos
        prev_length = len(self.get_todos())
        while len(self.get_todos()) != 0:
            self.open_todo_options(0, test)
            options = self.driver.find_element_by_css_selector(self.OPTION_LIST)
            for li in options.find_elements_by_css_selector(self.TODO_POPUP_ITEM):
                if li.text == self.TODO_DELETE_TEXT:
                    li.click()
                    wait_for_element_by_selector(self.driver, self.OPTION_LIST, False)
                    time.sleep(0.5)
                    break
            if prev_length == len(self.get_todos()):
                test.fail('Deletion failed')
            else:
                prev_length = len(self.get_todos())

    def open_todo_options(self, index, test):
        try:
            ActionChains(self.driver).context_click(self.get_todos()[index]).perform()
            wait_for_element_by_selector(self.driver, self.OPTION_LIST)
        except IndexError:
            test.fail('No todo was found')

    def open_priority_list(self):
        option_list = self.driver.find_element_by_css_selector(self.OPTION_LIST)
        for option in option_list.find_elements_by_css_selector(self.TODO_POPUP_ITEM):
            if option.text == self.CHANGE_PRIORITY_TEXT:
                option.click()
                break

    def choose_priority(self, priority):
        for priority_item in self.driver.find_elements_by_css_selector(self.PRIORITY_LIST_ITEM):
            if priority_item.text == priority:
                priority_item.click()
                break
        wait_for_element_by_selector(self.driver, self.PRIORITY_LIST, False)

    def open_settings(self):
        wait_for_element_by_selector(self.driver, self.SETTINGS_BUTTON)
        self.driver.find_element_by_css_selector(self.SETTINGS_BUTTON).click()
        wait_for_element_by_selector(self.driver, self.SETTINGS_FRAME)

    def set_priority(self, todo_index, priority, test):
        self.open_todo_options(todo_index, test)
        self.open_priority_list()
        self.choose_priority(priority)

    def set_sort(self, sort_name):
        self.open_settings()
        for setting in self.driver.find_elements_by_css_selector(self.SETTINGS_ITEM):
            if setting.text == self.SORT_BY_PRIORITY:
                setting.click()
                break
        wait_for_element_by_selector(self.driver, self.SETTINGS_FRAME, False)

    def get_priority(self, todo_index, test) -> str:
        self.open_todo_options(todo_index, test)
        self.open_priority_list()
        option = self.driver.find_element_by_css_selector(self.ACTIVE_PRIORITY_P)
        text = None
        if option is not None:
            text = option.text
        option.click()
        return text

    def check_priority(self, todo_index, priority, test):
        text = self.get_priority(todo_index, test)
        if text is None:
            test.fail('Active priority was not found')
        else:
            test.assertEqual(text, priority)


    def check_priority_list_open(self, test):
        wait_for_element_by_selector(self.driver, self.PRIORITY_LIST)
        priority_list_items = self.driver.find_elements_by_css_selector(self.PRIORITY_LIST_ITEM)
        test.assertEqual(len(self.PRIORITY_NAMES), len(priority_list_items))
            

    def check_for_self(self, test):
        wait_for_element_by_selector(self.driver, self.CONTAINER)
        wait_for_element_by_selector(self.driver, self.TITLE)
        title_name = self.driver.find_element_by_css_selector(self.TITLE).text
        test.assertEqual(self.TITLE_NAME, title_name)

        current_url = self.driver.current_url
        test.assertEqual(self.FINAL_PATH, current_url)

    def check_todo_order(self, test):
        prev_priority = None
        for iii in range(len(self.get_todos())):
            curr_priority = self.get_priority(iii, test)
            if prev_priority is not None:
                test.assertGreaterEqual(get_priority_number(prev_priority), get_priority_number(curr_priority))
            prev_priority = curr_priority
        

def get_priority_number(priority: str) -> int:
    if priority == MainPage.NO_PRIORITY:
        return 0
    elif priority == MainPage.LOW_PRIORITY:
        return 1
    elif priority == MainPage.MID_PRIORITY:
        return 2
    elif priority == MainPage.HIGH_PRIORITY:
        return 3
    else:
        return None
