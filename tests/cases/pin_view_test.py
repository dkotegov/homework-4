import os
import random

from tests.cases.base import TestAuthorized
from tests.pages.board import BoardPage
from tests.pages.pin import PinDetailsPage
from tests.pages.create_pin import CreatePinPage
from tests.pages.create_board import CreateBoardPage

BOARD_NAME = "NEW TEST BOARD "


class Test(TestAuthorized):
    file_path = ''
    board_id = ''
    pin_id = ''

    def setUp(self):
        super().setUp()
        self.file_path = os.environ.get('FILE_PATH')
        board_name = BOARD_NAME + str(random.randint(100, 10000))
        self.create_board(board_name)
        self.page = CreatePinPage(self.driver)
        pin_name = "pin name " + str(random.randint(100, 10000))
        pin_content = "this is normal pin description"
        file_name = self.file_path
        self.page.form_list.set_pin_name(pin_name)
        self.page.form_list.set_pin_content(pin_content)
        self.page.form_list.load_file(file_name)
        self.page.form_list.set_select_board(self.board_id)
        self.page.form_list.create_pin()
        self.page.form_list.wait_for_load_profile()
        self.page = BoardPage(self.driver, self.board_id)
        self.page.wait_for_load()
        self.pin_id = self.page.form.find_pin_id_by_pin_name(pin_name)
        self.page = PinDetailsPage(self.driver, pin_id=str(self.pin_id))

    def test_input_valid_comment(self):
        comment_text = "normal comment"
        self.page.form.set_comment(comment_text, self.pin_id)
        self.page.form.send_comment()

    def test_save_pin(self):
        board_name = BOARD_NAME + str(random.randint(100, 10000))
        self.create_board(board_name)
        self.page = PinDetailsPage(self.driver, pin_id=str(self.pin_id))
        self.page.form.set_board(self.pin_id, self.board_id)
        self.page.form.save_pin()

    def test_save_pin_empty_board(self):
        self.page.form.set_board(self.pin_id, 0)
        self.page.form.save_pin()

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
