from romanov.app.driver import connect

user_page_btn = 'profileLink'
first_desk_user_page = '#deskBlock a:first-child'
settings_btn = '#settingsLink'
chat_btn = '#userChatsLink'
follow_btn = '#followingUser'
new_el_btn = '#addNew2Modal'
modal_new_el = '#modal .window'
subs_btn = '#subsUserLink'
user_pins_btn = '#allUserPinsLink'
info_feed = '#main_page_info'
exit_btn = '#logoutLink'
menu_alien = '#loginPart div.buttons'
followers_label = '#followersModal'
following_label = '#followingModal'
modal = '#modal'
follow_block = '#followBlockModal'

class Pages:
    @staticmethod
    def click_user_menu():
        connect.load_wait(id=user_page_btn)
        user_btn = connect.find_el_id(user_page_btn)
        user_btn.click_after_wait()

    @staticmethod
    def open_first_desk():
        connect.load_wait(css=first_desk_user_page)
        desk = connect.find_el_css(first_desk_user_page)
        link = desk.el.get_attribute('href')
        desk.click_after_wait()
        assert connect.driver.current_url == link

    @staticmethod
    def click_settings():
        connect.load_wait(css=settings_btn)
        settings = connect.find_el_css(settings_btn)
        link = settings.el.get_attribute('href')
        settings.click_after_wait()
        assert connect.driver.current_url == link

    @staticmethod
    def click_chat():
        connect.load_wait(css=chat_btn)
        chat = connect.find_el_css(chat_btn)
        link = chat.el.get_attribute('href')
        chat.click_after_wait()
        assert connect.driver.current_url == link

    @staticmethod
    def click_following_user():
        connect.load_wait(css=follow_btn)
        following = connect.find_el_css(follow_btn)
        following.click_after_wait()
        following.change_wait('value', 'Отписаться')

    @staticmethod
    def click_unfollowing_user():
        connect.load_wait(css=follow_btn)
        following = connect.find_el_css(follow_btn)
        following.click_after_wait()
        following.change_wait('value', 'Подписаться')

    @staticmethod
    def click_new_pin():
        connect.load_wait(css=new_el_btn)
        new_pin = connect.find_el_css(new_el_btn)
        new_pin.click_after_wait()
        connect.load_wait(css=modal_new_el)

    @staticmethod
    def click_subs():
        connect.load_wait(css=subs_btn)
        subs = connect.find_el_css(subs_btn)
        link = subs.el.get_attribute('href')
        subs.click_after_wait()
        assert connect.driver.current_url == link

    @staticmethod
    def click_user_pins():
        connect.load_wait(css=user_pins_btn)
        pins = connect.find_el_css(user_pins_btn)
        link = pins.el.get_attribute('href')
        pins.click_after_wait()
        assert connect.driver.current_url == link

    @staticmethod
    def find_empty_feed():
        connect.load_wait(css=info_feed)
        label = connect.find_el_css(info_feed).el.text
        assert label != ''

    @staticmethod
    def click_exit():
        connect.load_wait(css=exit_btn)
        exit = connect.find_el_css(exit_btn)
        exit.click_after_wait()
        connect.load_wait(css=menu_alien)

    @staticmethod
    def click_user_followers():
        connect.load_wait(css=followers_label)
        followers = connect.find_el_css(followers_label)
        followers.click_after_wait()

    @staticmethod
    def click_user_followings():
        connect.load_wait(css=following_label)
        followings = connect.find_el_css(following_label)
        followings.click_after_wait()

    @staticmethod
    def find_empty_modal():
        label = connect.find_el_css(css=modal).el.text
        assert label == ''

    @staticmethod
    def find_users_modal():
        connect.load_wait(css=follow_block)