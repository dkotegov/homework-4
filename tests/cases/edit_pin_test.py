import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities, Remote

from tests.cases.base import TestAuthorized
from tests.pages.edit_pin import EditPinPage
from tests.pages.create_pin import CreatePinPage
from tests.pages.create_board import CreateBoardPage
from tests.pages.profile import ProfilePage

BOARD_NAME = "TEST BOARD"


class Test(TestAuthorized):
    file_path = ''
    board_id = ''
    pin_id = ''

    def setUp(self):
        super().setUp()
        self.file_path = os.environ.get('FILE_PATH')
        board_name = BOARD_NAME
        self.page = CreateBoardPage(self.driver)
        self.page.form_list.set_board_name(board_name)
        self.page.form_list.create_board()
        self.page.form_concrete.wait_for_load()
        for board in self.page.form_concrete.get_href_boards_list():
            board_text = board.find_element_by_tag_name('div')
            if board_text.text == BOARD_NAME:
                self.board_id = board.find_element_by_tag_name('a').get_attribute('href')[30:]
                break

        self.page = CreatePinPage(self.driver)
        pin_name = "this is valid test pin name"
        pin_content = "this is normal pin description"
        file_name = self.file_path
        self.page.form_list.set_pin_name(pin_name)
        self.page.form_list.set_pin_content(pin_content)
        self.page.form_list.load_file(file_name)
        self.page.form_list.set_select_board(self.board_id)
        self.page.form_list.create_pin()

        for board in self.page.form_concrete.get_href_boards_list():
            board_text = board.find_element_by_tag_name('div')
            if board_text.text == BOARD_NAME:
                current_board_id = board.find_element_by_tag_name('a').get_attribute('href')[30:]
                if current_board_id == self.board_id:
                    board.click()
                    break
                    
        print(self.board_id, self.pin_id)
        board = self.page.form_list.select_board(self.board_id)
        pins = board.find_elements_by_tag_name('div')
        for pin in pins:
            href = pin.find_elements_by_class('pin-for-user-view__content')
            if href.text == pin_name:
                print(href.get_attribute('href'))
                self.pin_id = href.get_attribute('href')[30:]
                break
        print(self.pin_id)
        self.page = EditPinPage(self.driver)

    def test_valid_data(self):
        pin_name = "this is valid test pin"
        pin_content = "this is normal pin description"
        self.page.form_list.set_pin_name(pin_name)
        self.page.form_list.set_pin_content(pin_content)
        self.page.form_list.create_pin()
        if self.page.form_list.get_error() != '':
            assert "error"
        print("success")

    def test_empty_name(self):
        file_name = "C:/312207-Lastochka.jpg"
        pin_content = "this is normal pin description"
        self.page.form_list.set_pin_content(pin_content)
        self.page.form_list.load_file(file_name)
        self.page.form_list.create_pin()
        assert self.page.form_list.get_error() == ''
        print("success")

    def test_empty_description(self):
        pin_name = "this is valid test pin"
        file_name = "C:/312207-Lastochka.jpg"
        self.page.form_list.set_pin_name(pin_name)
        self.page.form_list.load_file(file_name)
        self.page.form_list.create_pin()
        print("success")
