from romanov.app.driver import connect

login_btn = 'loginModal'
reg_btn = 'regModal'
login_input = 'loginUser'
pass_input = 'passUser'
email_input = 'emailUser'
login_btn_modal = 'sendLogin'
reg_btn_modal = 'sendReg'
close_btn_modal = 'closeInfo'
modal_start = 'div[class="great_title"]'
modal_info = '#infoModalMessage div.mini_title'
menu_user = '#loginPart div.icons'
cookie_session = 'session_id'


class Pages:
    @staticmethod
    def click_login_modal():
        connect.load_wait(id=login_btn)
        btn = connect.find_el_id(login_btn)
        btn.click_after_wait()

    @staticmethod
    def click_reg_modal():
        connect.load_wait(id=reg_btn)
        btn = connect.find_el_id(reg_btn)
        btn.click_after_wait()

    @staticmethod
    def enter_login(login=connect.username):
        input = connect.find_el_id(login_input)
        input.click_after_wait()
        input.input(login)

    @staticmethod
    def enter_pass(password=connect.password):
        input = connect.find_el_id(pass_input)
        input.click_after_wait()
        input.input(password)

    @staticmethod
    def enter_email(email):
        input = connect.find_el_id(email_input)
        input.click_after_wait()
        input.input(email)

    @staticmethod
    def click_login():
        btn = connect.find_el_id(login_btn_modal)
        btn.click_after_wait()

    @staticmethod
    def click_reg():
        btn = connect.find_el_id(reg_btn_modal)
        btn.click_after_wait()

    @staticmethod
    def close_welcome():
        btn = connect.find_el_id(close_btn_modal)
        btn.click_after_wait()

    @staticmethod
    def wait_modal_welcome():
        connect.load_wait(css=modal_start)

    @staticmethod
    def find_info_error():
        connect.load_wait(css=modal_info)
        label = connect.find_el_css(modal_info).el.text
        assert label != ''

    @staticmethod
    def find_auth_menu():
        connect.load_wait(css=menu_user)

    @staticmethod
    def clear_auth():
        connect.delete_cookie(cookie_session)
