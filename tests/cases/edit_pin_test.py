import os
import time
import unittest
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities, Remote

from tests.cases.base import TestAuthorized
from tests.pages.board import BoardPage
from tests.pages.edit_pin import EditPinPage
from tests.pages.create_pin import CreatePinPage
from tests.pages.create_board import CreateBoardPage
from tests.pages.profile import ProfilePage

BOARD_NAME = "TEST BOARD "


class Test(TestAuthorized):
    file_path = ''
    board_id = ''
    pin_id = ''

    def setUp(self):
        super().setUp()
        self.file_path = os.environ.get('FILE_PATH')
        board_name = BOARD_NAME + str(random.randint(100, 10000))
        # create board and save board name
        self.page = CreateBoardPage(self.driver)
        self.page.form_list.set_board_name(board_name)
        self.page.form_list.create_board()
        self.page.form_concrete.wait_for_load()
        for board in self.page.form_concrete.get_href_boards_list():
            board_text = board.find_element_by_tag_name('div')
            if board_text.text == board_name:
                self.board_id = board.find_element_by_tag_name('a').get_attribute('href')[30:]
                break
        # create pin
        self.page = CreatePinPage(self.driver)
        pin_name = "pin name " + str(random.randint(100, 10000))
        pin_content = "this is normal pin description"
        file_name = self.file_path
        self.page.form_list.set_pin_name(pin_name)
        self.page.form_list.set_pin_content(pin_content)
        self.page.form_list.load_file(file_name)
        self.page.form_list.set_select_board(self.board_id)
        # time.sleep(5)
        self.page.form_list.create_pin()
        self.page.form_list.wait_for_load_profile()
        # time.sleep(5)
        print('board id :', self.board_id)
        self.page = BoardPage(self.driver, self.board_id)
        self.page.wait_for_load()
        self.pin_id = self.page.form.find_pin_id_by_pin_name(pin_name)
        print('pin id :', self.pin_id)
        self.page = EditPinPage(self.driver, self.pin_id)

    def test_valid_data(self):
        pin_name = "this is valid test pin"
        pin_content = "this is normal pin description"
        self.page.form_list.set_pin_name(pin_name)
        self.page.form_list.set_pin_content(pin_content)
        self.page.form_list.edit_pin()
        if self.page.form_list.get_error(self.pin_id) != '':
            assert "error"
        print("success")

    def test_empty_name(self):
        pin_content = "this is normal pin description"
        self.page.form_list.set_pin_content(pin_content)
        self.page.form_list.edit_pin()
        assert self.page.form_list.get_error(self.pin_id) == ''
        print("success")

    def test_empty_description(self):
        pin_name = "this is valid test pin"
        self.page.form_list.set_pin_name(pin_name)
        self.page.form_list.edit_pin()
        if self.page.form_list.get_error(self.pin_id) != '':
            assert "error"
        print("success")

    def test_go_back(self):
        self.page.form_list.go_back(self.pin_id)

    def test_delete_pin(self):
        self.page.form_list.delete_pin(self.pin_id)
