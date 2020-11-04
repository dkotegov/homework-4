import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from pages.board_page import BoardPage
from pages.boards_page import BoardsPage
from pages.login_page import LoginPage

from components.task.task_settings_popup import TaskSettingsPopup
from components.task.add_label_to_task_popup import AddLabelToTaskPopup
from components.task.create_label_popup import CreateLabelPopup

class TaskSettingsPopupTest(unittest.TestCase):
    BOARD_NAME = 'TEST BOARD NAME'

    # TODO: интеграция с колонками
    url = 'https://drello.works/boards/245/columns/942/tasks/1172'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)

        self.login_page = LoginPage(self.driver)
        self.login_page.open()

        login = os.environ.get('LOGIN')
        password = os.environ.get('PASSWORD')

        self.login_page.login(login, password)
        BoardsPage(self.driver).wait_for_container()
        
    def tearDown(self):
        self.driver.quit()

    def test_rename_task(self):
        self.driver.get(self.url)
        popup = TaskSettingsPopup(self.driver)
        popup.wait_for_container()

        new_name = "Your new name"
        popup.rename_task(new_name)

        self.driver.get(self.url)
        popup = TaskSettingsPopup(self.driver)
        popup.wait_for_container()

        self.assertEqual(popup.get_task_name(), new_name)
    
    def test_change_task_description(self):
        self.driver.get(self.url)
        popup = TaskSettingsPopup(self.driver)
        popup.wait_for_container()

        description = "Your new description"
        popup.change_description(description)

        self.driver.get(self.url)
        popup = TaskSettingsPopup(self.driver)
        popup.wait_for_container()

        self.assertEqual(popup.get_task_description(), description)

    def test_add_label_to_task(self):
        self.driver.get(self.url)
        popup = TaskSettingsPopup(self.driver)
        popup.wait_for_container()
        popup.click_add_new_label_button()

        add_label_popup = AddLabelToTaskPopup(self.driver)
        add_label_popup.wait_for_container()
        add_label_popup.click_create_new_label_button()

        create_label_popup = CreateLabelPopup(self.driver)
        create_label_popup.wait_for_container()
        label_name = 'Second test name'
        create_label_popup.set_label_name(label_name)
        create_label_popup.click_create_label_button()

        label_exist = add_label_popup.is_label_with_provided_name_exist(label_name)      
        self.assertTrue(label_exist)

    #def 

    # def test_delete_task(self):
    #     self.driver.get(self.url)
    #     popup = TaskSettingsPopup(self.driver)
    #     popup.wait_for_container()

    #     popup.delete_task()


