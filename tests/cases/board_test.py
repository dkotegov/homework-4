from tests.cases.base import TestAuthorized
from tests.pages.create_board import CreateBoardPage

EMPTY_TITLE_ERROR = "Некорректный заголовок"
CREATE_BOARD_ERROR = "board not found"
NOT_DETECTED_ERROR = "error not detected"


class Test(TestAuthorized):
    def setUp(self):
        super().setUp()
        self.page = CreateBoardPage(self.driver)

    def test_create_board_valid_data(self):
        board_name = "test_create_board_valid_data name"
        board_content = "test_create_board_valid_data description"
        self.page.form_list.set_board_name(board_name)
        self.page.form_list.set_board_content(board_content)
        self.page.form_list.create_board()
        self.page.form_concrete.wait_for_load()

        self.assertTrue(
            self.page.form_concrete.find_board(board_name), CREATE_BOARD_ERROR
        )

    def test_create_board_empty_name_description(self):
        self.page.form_list.create_board()

        self.assertNotEqual(
            self.page.form_list.get_error(), EMPTY_TITLE_ERROR, NOT_DETECTED_ERROR
        )

    def test_create_board_empty_name(self):
        board_content = "test_create_board_empty_name description"
        self.page.form_list.set_board_content(board_content)
        self.page.form_list.create_board()

        self.assertNotEqual(
            self.page.form_list.get_error(), EMPTY_TITLE_ERROR, NOT_DETECTED_ERROR
        )

    def test_create_board_empty_description(self):
        board_name = "test_create_board_empty_description name"
        self.page.form_list.set_board_name(board_name)
        self.page.form_list.create_board()
        self.page.form_concrete.wait_for_load()

        self.assertTrue(
            self.page.form_concrete.find_board(board_name), CREATE_BOARD_ERROR
        )

    def test_create_board_go_back(self):
        self.page.form_list.go_back()
