import os
import random

from tests.cases.base import TestAuthorized
from tests.pages.create_pin import CreatePinPage
from tests.pages.create_board import CreateBoardPage

BOARD_NAME = "TEST BOARD"


class Test(TestAuthorized):
    board_id = ''
    file_path = ''

    def setUp(self):
        super().setUp()
        self.file_path = os.environ.get('FILE_PATH')
        board_name = BOARD_NAME + str(random.randint(100, 10000))
        self.create_board(board_name)
        self.page = CreatePinPage(self.driver)

    def test_create_pin_valid_data(self):
        pin_name = "test_create_pin_valid_data name"
        pin_content = "test_create_pin_valid_data description"
        self.page.form_list.set_pin_name(pin_name)
        self.page.form_list.set_pin_content(pin_content)
        self.page.form_list.load_file(self.file_path)
        self.page.form_list.set_select_board(self.board_id)
        self.page.form_list.create_pin()
        if self.page.form_list.get_error() != '':
            assert "error"

    def test_create_pin_empty_file(self):
        pin_name = "test_create_pin_empty_file name"
        pin_content = "test_create_pin_empty_file description"
        self.page.form_list.set_pin_name(pin_name)
        self.page.form_list.set_pin_content(pin_content)
        self.page.form_list.set_select_board(self.board_id)
        self.page.form_list.create_pin()
        assert self.page.form_list.get_error() == ''

    def test_create_pin_empty_name(self):
        pin_content = "test_create_pin_empty_name description"
        self.page.form_list.set_pin_content(pin_content)
        self.page.form_list.load_file(self.file_path)
        self.page.form_list.set_select_board(self.board_id)
        self.page.form_list.create_pin()
        assert self.page.form_list.get_error() == ''

    def test_create_pin_empty_description(self):
        pin_name = "this is empty description test pin name"
        self.page.form_list.set_pin_name(pin_name)
        self.page.form_list.load_file(self.file_path)
        self.page.form_list.set_select_board(self.board_id)
        self.page.form_list.create_pin()

    def test_create_pin_empty_board(self):
        pin_name = "test_create_pin_empty_board name"
        pin_content = "test_create_pin_empty_board description"
        self.page.form_list.set_pin_name(pin_name)
        self.page.form_list.set_pin_content(pin_content)
        self.page.form_list.set_select_board(0)
        self.page.form_list.create_pin()
        assert self.page.form_list.get_error() != ''

    def test_create_pin_empty(self):
        self.page.form_list.create_pin()
        assert self.page.form_list.get_error() != ''

    def test_create_pin_go_back(self):
        self.page.form_list.go_back()

    def create_board(self, board_name):
        self.page = CreateBoardPage(self.driver)
        self.page.form_list.set_board_name(board_name)
        self.page.form_list.create_board()
        self.page.form_concrete.wait_for_load()
        for board in self.page.form_concrete.get_href_boards_list():
            board_text = board.find_element_by_tag_name('div')
            if board_text.text == board_name:
                self.board_id = board.find_element_by_tag_name('a').get_attribute('href')[30:]
                break
