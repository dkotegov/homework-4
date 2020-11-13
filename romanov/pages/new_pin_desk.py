from romanov.app.driver import connect
import os

new_element_modal_btn = '#addNewModal'
create_pin_btn = '#pinLink input'
create_desk_btn = '#newDeskModal input'
pin_file_input = '#filePin'
pin_image = '#pinImage'
pin_image_attr = 'loaded'
page_no_error_info = '#infoPageMessage'
page_error_info = '#infoPageMessage div.mini_title'
modal_error_info = '#infoModalMessage div.mini_title'
pin_name_input = 'pinName'
send_pin_btn = '#sendNewPin'
send_desk_btn = '#sendDesk input'
desk_name_input = 'deskName'
desk_desc_input = 'deskDesc'
last_desk_pin_page = '#deskSelect option:last-child'
last_desk_user_page = '#deskBlock a:last-child div.itemText'
modal_message = 'div[class="great_title"]'

class Pages:
    @staticmethod
    def click_new_menu():
        connect.load_wait(css=new_element_modal_btn)
        new = connect.find_el_css(new_element_modal_btn)
        new.click_after_wait()

    @staticmethod
    def click_new_pin():
        connect.load_wait(css=create_pin_btn)
        new = connect.find_el_css(create_pin_btn)
        new.click_after_wait()

    @staticmethod
    def click_new_desk():
        connect.load_wait(css=create_desk_btn)
        new = connect.find_el_css(create_desk_btn)
        new.click_after_wait()

    @staticmethod
    def add_image(url):
        connect.load_wait(css=pin_file_input)
        image = connect.find_el_css(pin_file_input)
        image.input(os.getcwd() + url)

    @staticmethod
    def wait_image():
        image = connect.find_el_css(pin_image)
        image.change_wait(pin_image_attr)

    @staticmethod
    def find_no_error():
        connect.load_wait(css=page_no_error_info)
        label = connect.find_el_css(page_no_error_info).el.text
        assert label == ''

    @staticmethod
    def find_pin_error():
        connect.load_wait(css=page_error_info)
        label = connect.find_el_css(page_error_info).el.text
        assert label != ''

    @staticmethod
    def find_desk_error():
        connect.load_wait(css=modal_error_info)
        label = connect.find_el_css(modal_error_info).el.text
        assert label != ''

    @staticmethod
    def clear_name():
        input = connect.find_el_id(pin_name_input)
        input.el.clear()

    @staticmethod
    def click_create_pin():
        connect.load_wait(css=send_pin_btn)
        new = connect.find_el_css(send_pin_btn)
        new.click_after_wait()

    @staticmethod
    def click_create_desk():
        connect.load_wait(css=send_desk_btn)
        new = connect.find_el_css(send_desk_btn)
        new.click_after_wait()

    @staticmethod
    def enter_name(name):
        input = connect.find_el_id(desk_name_input)
        input.click_after_wait()
        input.input(name)

    @staticmethod
    def enter_desc(desc):
        input = connect.find_el_id(desk_desc_input)
        input.click_after_wait()
        input.input(desc)

    @staticmethod
    def check_created_desk_pin_page(name):
        select = connect.find_el_css(last_desk_pin_page)
        assert select.el.text == name

    @staticmethod
    def check_created_desk_user_page(name):
        select = connect.find_el_css(last_desk_user_page)
        assert select.el.text == name

    @staticmethod
    def find_ok_messsage():
        connect.load_wait(css=modal_message)