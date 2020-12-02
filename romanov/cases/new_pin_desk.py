import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from romanov.steps.auth import Steps as AuthSteps
from romanov.steps.profile import Steps as ProfileSteps
from romanov.steps.new_pin_desk import Steps

from romanov.app.driver import connect

EMPTY = ""
PIN_ADDED = "Ваш пин добавлен"
DESK_ADDED = "Новая доска создана"

class NewPinDeskTest(unittest.TestCase):
    def test_new_pin_image_upload(self):
        new_pin_desk = Steps()
        AuthSteps.login_app(self)
        new_pin_desk.open_new_pin()
        new_pin_desk.add_image('/testData/octopus.png')
        label = new_pin_desk.find_no_error()
        self.assertEqual(label, EMPTY)

    def test_new_pin_large_image_upload(self):
        new_pin_desk = Steps()
        AuthSteps.login_app(self)
        new_pin_desk.open_new_pin()
        new_pin_desk.add_image('/testData/largeImage.jpg')
        label = new_pin_desk.find_pin_error()
        self.assertNotEqual(label, EMPTY)

    def test_new_pin_empty_create(self):
        new_pin_desk = Steps()
        AuthSteps.login_app(self)
        new_pin_desk.open_new_pin()
        new_pin_desk.create_pin()
        label = new_pin_desk.find_pin_error()
        self.assertNotEqual(label, EMPTY)

    def test_new_pin_empty_input_create(self):
        new_pin_desk = Steps()
        AuthSteps.login_app(self)
        new_pin_desk.open_new_pin()
        new_pin_desk.add_true_image('/testData/octopus.png')
        new_pin_desk.clear_name()
        new_pin_desk.create_pin()
        label = new_pin_desk.find_pin_error()
        self.assertNotEqual(label, EMPTY)

    def test_new_pin_create(self):
        new_pin_desk = Steps()
        AuthSteps.login_app(self)
        new_pin_desk.open_new_pin()
        new_pin_desk.add_true_image('/testData/octopus.png')
        new_pin_desk.create_pin()
        label = new_pin_desk.find_ok_messsage()
        self.assertEqual(label, PIN_ADDED)

    def test_new_desk_empty_create(self):
        new_pin_desk = Steps()
        AuthSteps.login_app(self)
        new_pin_desk.open_new_desk()
        new_pin_desk.create_desk()
        label = new_pin_desk.find_desk_error()
        self.assertNotEqual(label, EMPTY)

    def test_new_desk_create(self):
        new_pin_desk = Steps()
        AuthSteps.login_app(self)
        new_pin_desk.open_new_desk()
        new_pin_desk.enter_name('123')
        new_pin_desk.enter_desc('123')
        new_pin_desk.create_desk()
        label = new_pin_desk.find_ok_messsage()
        self.assertEqual(label, DESK_ADDED)

    def test_new_desk_long_name_create(self):
        new_pin_desk = Steps()
        AuthSteps.login_app(self)
        new_pin_desk.open_new_desk()
        new_pin_desk.enter_name('123123123454783487437843783'
            '478434378347834784378347834478334873783784347833'
            '478437843783478347834348767098765432456') # более 60-ти символов
        new_pin_desk.create_desk()
        label = new_pin_desk.find_desk_error()
        self.assertNotEqual(label, EMPTY)

    def test_new_desk_on_pin_page_create(self):
        new_pin_desk = Steps()
        AuthSteps.login_app(self)
        new_pin_desk.open_new_pin()
        desk_name = '1234'
        new_pin_desk.create_end_desk(desk_name, '123')
        new_pin_desk.check_created_desk_pin_page(desk_name)

    def test_new_desk_on_user_page_create(self):
        new_pin_desk = Steps()
        AuthSteps.login_app(self)
        ProfileSteps.open_user_profile()
        desk_name = '123456'
        new_pin_desk.create_end_desk(desk_name, '123')
        new_pin_desk.check_created_desk_user_page(desk_name)