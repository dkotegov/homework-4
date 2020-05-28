import os
import random

from tests.cases.base import TestAuthorized
from tests.pages.board import BoardPage
from tests.pages.edit_pin import EditPinPage
from tests.pages.create_pin import CreatePinPage
from tests.pages.create_board import CreateBoardPage

BOARD_NAME = "TEST BOARD "
EDIT_BOARD_NAME = "EDIT BOARD "
EMPTY_ERROR = ''
EDIT_PIN_ERROR = "edit pin error"
NO_TITLE_ERROR = "Название должно быть заполнено"
NO_BOARD_ERROR = "Не выбрана доска для пина!"
NOT_DETECTED_ERROR = "error not detected"


class Test(TestAuthorized):
    file_path = ''
    board_id = ''
    pin_id = ''

    def setUp(self):
        super().setUp()
        self.file_path = os.environ.get('FILE_PATH')
        self.create_board()
        self.page = CreatePinPage(self.driver)
        self.create_pin()
        self.page = EditPinPage(self.driver, self.pin_id)

    def test_edit_pin_valid_data(self):
        pin_name = "test_edit_pin_valid_data name"
        pin_content = "test_edit_pin_valid_data description"
        self.page.form_list.set_pin_name(pin_name)
        self.page.form_list.set_pin_content(pin_content)
        self.page.form_list.edit_pin()

        self.assertEqual(self.page.form_list.get_error(self.pin_id), EMPTY_ERROR, EDIT_PIN_ERROR)

    def test_edit_pin_empty_name(self):
        pin_content = "test_edit_pin_empty_name description"
        self.page.form_list.set_pin_content(pin_content)
        self.page.form_list.edit_pin()

        self.assertNotEqual(self.page.form_list.get_error(self.pin_id), NO_TITLE_ERROR, NOT_DETECTED_ERROR)

    def test_edit_pin_empty_description(self):
        pin_name = "test_edit_pin_empty_description name"
        self.page.form_list.set_pin_name(pin_name)
        self.page.form_list.edit_pin()

        self.assertEqual(self.page.form_list.get_error(self.pin_id), EMPTY_ERROR, EDIT_PIN_ERROR)

    def test_edit_pin_edit_board(self):
        new_board_name = EDIT_BOARD_NAME + str(random.randint(100, 10000))
        self.page = CreateBoardPage(self.driver)
        self.page.form_list.set_board_name(new_board_name)
        self.page.form_list.create_board()
        self.page.form_concrete.wait_for_load()
        new_board_id = self.page.form_concrete.get_id_by_board_name(new_board_name)
        self.page = EditPinPage(self.driver, self.pin_id)
        pin_name = "test_edit_pin_edit_board name"
        self.page.form_list.set_pin_name(pin_name)
        self.page.form_list.set_select_board(new_board_id)
        self.page.form_list.edit_pin()

        self.assertEqual(self.page.form_list.get_error(self.pin_id), EMPTY_ERROR, NOT_DETECTED_ERROR)

    def test_edit_pin_go_back(self):
        self.page.form_list.go_back(self.pin_id)

    def test_edit_pin_delete_pin(self):
        self.page.form_list.delete_pin(self.pin_id)

    def create_board(self):
        board_name = BOARD_NAME + str(random.randint(100, 10000))
        self.page = CreateBoardPage(self.driver)
        self.page.form_list.set_board_name(board_name)
        self.page.form_list.create_board()
        self.page.form_concrete.wait_for_load()
        self.board_id = self.page.form_concrete.get_id_by_board_name(board_name)

    def create_pin(self):
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
