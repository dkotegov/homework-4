import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import constants
from components.base_component import BaseComponent
from components.game_form import GameForm
from components.page import Page
from constants import profiles


class GamePage(Page):

    def __init__(self, driver):
        super(GamePage, self).__init__(driver)
        self.game_form = GameForm(self.driver)
        self.PAGE = "/game/vegamix"

    def game_delete(self):
        self.game_form.game_delete().click()
        self.game_form.game_delete_repead().click()