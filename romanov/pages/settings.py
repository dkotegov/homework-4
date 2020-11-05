from romanov.app.driver import connect
import os

file_avatar = '#fileAvatar'
modal_settings = 'div[class="great_title"]'
error_message = '#infoPageMessage div.mini_title'
pass_input = 'userPass'
email_input = 'userEmail'
user_input = 'userName'
user_desc = 'userAbout'
save_pass_btn = 'sendPass'
save_data_btn = 'saveData'
close_modal_btn = 'closeInfo'

class Pages:
    @staticmethod
    def load_avatar(url):
        connect.load_wait(css=file_avatar)
        change_avatar = connect.find_el_css(file_avatar)
        change_avatar.input(os.getcwd() + url)

    @staticmethod
    def find_success_modal():
        connect.load_wait(css=modal_settings)

    @staticmethod
    def find_info_error():
        connect.load_wait(css=error_message)
        label = connect.find_el_css(error_message).el.text
        assert label != ''

    @staticmethod
    def enter_pass(password=connect.password):
        input = connect.find_el_id(pass_input)
        input.click_after_wait()
        input.input(password)

    @staticmethod
    def enter_email(email):
        input = connect.find_el_id(email_input)
        input.click_after_wait()
        input.el.clear()
        input.input(email)

    @staticmethod
    def enter_login(username=connect.username):
        input = connect.find_el_id(user_input)
        input.click_after_wait()
        input.el.clear()
        input.input(username)

    @staticmethod
    def enter_desc(desc):
        input = connect.find_el_id(user_desc)
        input.click_after_wait()
        input.el.clear()
        input.input(desc)

    @staticmethod
    def save_pass():
        save_btn = connect.find_el_id(save_pass_btn)
        save_btn.click_after_wait()

    @staticmethod
    def save_data():
        save_btn = connect.find_el_id(save_data_btn)
        save_btn.click_after_wait()

    @staticmethod
    def close_done():
        connect.load_wait(id=close_modal_btn)
        close_btn = connect.find_el_id(close_modal_btn)
        close_btn.click_after_wait()

    @staticmethod
    def equal_data(email, desc, username=connect.username):
        connect.load_wait(id=email_input)
        label = connect.find_el_id(email_input).el.get_attribute('value')
        assert label == email

        connect.load_wait(id=user_desc)
        label = connect.find_el_id(user_desc).el.get_attribute('value')
        assert label == desc

        connect.load_wait(id=user_input)
        label = connect.find_el_id(user_input).el.get_attribute('value')
        assert label == username
