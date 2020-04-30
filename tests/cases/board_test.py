import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities, Remote

from tests.cases.base import TestAuthorized
from tests.pages.create_board import CreateBoardPage


class Test(TestAuthorized):
    def setUp(self):
        super().setUp()
        self.page = CreateBoardPage(self.driver)

    def test_valid_data(self):
        board_name = "this is valid test board"
        board_content = "this is normal board description"
        self.page.form_list.set_board_name(board_name)
        self.page.form_list.set_board_content(board_content)
        self.page.form_list.create_board()
        self.page.form_concrete.wait_for_load()
        board_list = self.page.form_concrete.get_boards_list()
        for board in board_list:
            if board.text == board_name:
                return
        assert "board not found"

    def test_empty_name_description(self):
        self.page.form_list.create_board()
        assert self.page.form_list.get_error() == ''

    def test_empty_name(self):
        board_content = "this is normal board description"
        self.page.form_list.set_board_content(board_content)
        self.page.form_list.create_board()
        assert self.page.form_list.get_error() == ''

    def test_empty_description(self):
        board_name = "this is empty name board"
        self.page.form_list.set_board_name(board_name)
        self.page.form_list.create_board()
        self.page.form_concrete.wait_for_load()
        board_list = self.page.form_concrete.get_boards_list()
        for board in board_list:
            if board.text == board_name:
                return
        assert "board not found"

    def test_go_back(self):
        self.page.form_list.go_back()
