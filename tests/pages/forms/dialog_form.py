# -*- coding: utf-8 -*-
from base_element import BaseElement


class DialogForm(BaseElement):
    MENU_BUTTON = '//div[@data-additional-button="js-open-menu"]'
    SEND_MESSAGE_BUTTON = '//button[@title="Отправить"]'
    NO_MESSAGES_TEXT = '//div[contains(@class,"stub-empty_t")]'
    MESSAGE_INPUT = '//div[@name="st.txt"]'
    STICKER_BUTTON = '//span[contains(@class, " emoji-m")]'
    STICKER_LIST_BUTTON = '//a[contains(@data-l, "stickersTab")]'

    STICKERS = {
        'USMILE_STICKER': '//div[@data-code="#u9b43ee364as#"]',
        'USMILE_STICKER_2': '//div[@data-code="#u9b4399ed9bs#"]',
        'DOG_STICKER': '//div[@data-code="#uced34a1000s#"]',
        'HEART_STICKER': '//div[@data-code="#ucdb3367600s#"]',
        'FOX_STICKER': '//div[@data-code="#ucf1b357200s#"]'
    }

    ATTACH_BUTTON = "//div[contains(@class, 'comments_attach')]"
    GAME_BUTTON = '//a[contains(@class, "comments_action_game_trigger")]'
    GAME_CLOSE_BUTTON = '//span[contains(@class, "media-layer_close_ico")]'
    GAME_INVITE_MESSAGE = '//div[contains(@class, "msg_game_cnt")]'
    GAME_INVITE_MESSAGE_TEMPLATE = '//div[contains(@data-app-id, "{AppID}")]'
    GAME_INVITE_APPLY_TEMPLATE = '//div[contains(@data-app-id, "{AppID}")]/a[1]'
    GAME_INVITE_REJECT_TEMPLATE = '//div[contains(@data-app-id, "{AppID}")]/a[2]'
    GAME_INVITE_PLAY_AGAIN_TEMPLATE = '//a[contains(@id, "{AppID}-play-again")]'
    MESSAGE_WITH_STICKER = '//div[contains(@class, "msg_sticker ")]'
    SENT_MESSAGE = '//div[contains(@class,"msg_tx")]'
    SMILES_LIST_BUTTON = '//a[contains(@data-l, "smilesTab")]'
    SMILE_GOVNA = '//img[contains(@class, "emoji_1f4a9")]'
    SMILE_WHALE = '//img[contains(@class, "emoji_1f40b")]'
    SMILE_GAS = '//img[contains(@class, "emoji_1f4a8")]'
    POSTCARDS_LIST_BUTTON = '//a[contains(@data-l, "postcardsTab")]'
    FIRST_POSTCARD_IN_LIST = '//div[contains(@class, "comments_smiles_lst")]/div[1]/div'
    SENT_POSTCARD = '//div[contains(@data-module,"LiveSticker")]'
    POSTCARD_SEARCH = '//input[contains(@id, "PostcardsSearch_field_query")]'
    POSTCARD_SEARCH_SUGGEST = '(//span[contains(@class, "search-input_suggest_i")])[1]'
    POSTCARD_SEARCH_LOADER = '//div[contains(@class, "search-input_process")]'
    USER_AVATAR = '//div[contains(@id, "hook_Block_MessageActionMenu")]/div[1]/div[1]/a/img'
    AVATAR_LOADER = '//div[@class, "photo-layer_process"]'
    BIG_AVATAR = '//div[contains(@id, "photo-layer_photo")]'

    VIDEO_CALL_BUTTON = '//a[contains(@class, "video-chat-buttons_i __only-icon")]'
    VIDEO_CALL_WINDOW = '//div[contains(@id, "hook_Block_VideoChatCall")]'
    SUPPORT_BUTTON = '//a[contains(@class, "ic ic_i_support")]'
    SUPPORT_WINDOW = '//div[contains(@id, "hook_Block_HelpFeedbackForm")]'
    STICKER_BAR_CLOSE = '//div[contains(@class, "hello-stickers __empty js-hello-stickers __closed")]'
    STICKER_BAR_BUTTON = '//div[contains(@class, "hello-sticker-toggler js-hello-sticker-toggler")]'
    PRESENT_CONTENT = '//div[contains(@class, "gift-front_cnt")]'
    MONEY_WINDOW = '//iframe[contains(@class, "modal-new_payment-frame")]'
    MONEY_TRANSFERS_ICON = '//div[contains(@class,"nav-side")]/a[2]'
    NAV_LOADER = '//div[contains(@id ,"navProgress")]'
    PAYMENT_LOADER = '//div[contains(@class, "new_payment-preloader")]'
    PROFILE_BUTTON = '//a[contains(@title, "Перейти на профиль")]'
    PROFILE_CONTENT = '//div[@class="portlet user-main-page"]'

    SMILES = {
        'OK_SMILE': '//img[contains(@alt, ":-)")]',
        'PEOPLE_SMILE': '//img[contains(@alt, "😄")]',
        'NATURE_SMILE': '//img[contains(@alt, "🐶")]',
        'OBJECT_SMILE': '//img[contains(@alt, "🎍")]',
        'PLACES_SMILE': '//img[contains(@alt, "🏠")]',
        'SYMBOLS_SMILE': '//img[contains(@alt, "🔟")]',
        'ANIMATION_SMILE': '//img[contains(@alt, "#u298cbf40cbs#")]',
    }

    SMILES_LIST = {
        'OK_SMILES': '//ul[@class="comments_smiles_nav_cnt"]/li[2]',
        'PEOPLE_SMILES': '//ul[@class="comments_smiles_nav_cnt"]/li[3]',
        'NATURE_SMILES': '//ul[@class="comments_smiles_nav_cnt"]/li[4]',
        'OBJECT_SMILES': '//ul[@class="comments_smiles_nav_cnt"]/li[5]',
        'PLACES_SMILES': '//ul[@class="comments_smiles_nav_cnt"]/li[6]',
        'SYMBOLS_SMILES': '//ul[@class="comments_smiles_nav_cnt"]/li[7]',
        'ANIMATION_SMILES': '//ul[@class="comments_smiles_nav_cnt"]/li[8]',
    }

    SMILE_LOADER = '//li[contains(@class, "comments_smiles_nav_i __active")]'

    STICKER_IN_BAR1 = '//div[contains(@class, "ugrid __xl postcards_3 js-data-holder")]/div/div[1]/div/img'
    STICKER_IN_BAR2 = '//div[contains(@class, "ugrid __xl postcards_3 js-data-holder")]/div/div[2]/div/img'

    STICKERS_SET_INSTALL_BUTTON = '//a[contains(@data-l, "button_install")]'
    STICKERS_SET_UNINSTALL_BUTTON = '//a[contains(@data-l, "button_uninstall")]'
    OPEN_STICKERS_SET_LIST = '//a[contains(@data-l, "add")]'
    CLOSE_STICKERS_SET_LIST = '//a[contains(@id, "nohook_modal_close")]'
    MY_STICKERS_BUTTON = '//a[contains(@hrefattrs, "Installed")]'
    FIND_MY_SET_TEMPLATE = '//div[contains(@data-set-id, "{ID}")]'
    FIND_NEW_SET_TEMPLATE = '//a[contains(@hrefattrs, "set={ID}")]'
    SINGLE_STICKER_SET = '//div[contains(@class,"sticker-set-single")]'

    SENT_MESSAGE_TEXT = '//span[contains(@class, "js-copy-text")]/span[1]'
    GAME_LIST = '//div[contains(@id, "hook_Block_ChatGames")]'
    ACTIVE_GAME_TEMPLATE = '//div[contains(@data-appid, "{AppID}")]'
    PICK_GAME_TEMPLATE = '(//a[contains(@href, "appId={AppID}")])[2]'
    DIALOG_LOADER = '//div[contains(@class, "chat_loader")]'

    COMPANION_NAME = '//span[contains(@data-l,"menu_opponent_name")]'

    MESSAGE_INPUT = '//div[contains(@name, "st.txt")]'

    DELETE_MESSAGE_BUTTON = "//a[contains(@data-l, 'deleteMsg')]"
    PIN_MESSAGE_BUTTON = "//a[contains(@data-l, 'pinMsg')]"
    EDIT_MESSAGE_BUTTON = "//a[contains(@data-l, 'editMsg')]"
    ANSWER_MESSAGE_BUTTON = "//span[contains(@data-l, 'replyToMsg')]"
    REPORT_MESSAGE_BUTTON = "//a[contains(@data-l, 'reportSpamMsg')]"
    ANSWERED_MESSAGE = '//div[contains(@data-l,"reply")]'
    FORWARD_MESSAGE = "//span[contains(@data-l, 'forward')]"
    FORWARDED_MESSAGE_TITLE = '//div[contains(@class,"msg_forward_title")]'
    ADD_COMPANION_BUTTON = '//span[contains(@class, " ic_add-user")]'
    CONTROL_USERS_BUTTON = '//span[contains(@class, " ic_ffriend")]'
    GROUP_CHAT_CREATED_TITLE = '//a[contains(@data-l,"user1FromSysMsg")]'
    EMPTY_POSTCARDS_SEARCH = '//div[.="Таких открыток не нашлось "]'

    GROUP_CHAT_REMOVED_TITLE = '//a[contains(@data-l,"removedUserFromSysMsg")]'

    PINNED_MESSAGE = '//div[contains(@class, "chat_pinned_text")]'
    UNPIN_MESSAGE_BUTTON = "//a[contains(@class,'chat_pinned_close')]"

    CHANGED_PHOTO_NOTIFICATION = '//div[.="Вы изменили иконку чата"]'
    REPORTED_MESSAGE = '//div[.="Сообщение расценено как спам и удалено."]'

    WRONG_PHOTO_FORMAT = '//span[contains(@class,"ic12 ic12_warning attach-photo_err")]'

    LONG_MESSAGE_ERROR = '//div[contains(@class, "msg_error")]'

    def get_menu_button(self):
        return self.get_button_by_xpath(self.MENU_BUTTON)

    def get_send_message_button(self):
        return self.get_button_by_xpath(self.SEND_MESSAGE_BUTTON)

    def get_send_message_button_exists(self):
        return self.existance_of_element_by_xpath(self.SEND_MESSAGE_BUTTON)

    def get_no_messages_text_exists(self):
        return self.existance_of_element_by_xpath(self.NO_MESSAGES_TEXT)

    def get_message_input(self):
        return self.get_field_by_xpath(self.MESSAGE_INPUT)

    def get_sticker_button(self):
        return self.get_button_by_xpath(self.STICKER_BUTTON)

    def get_sticker_list_button(self):
        return self.get_button_by_xpath(self.STICKER_LIST_BUTTON)

    def get_sticker(self, name):
        return self.get_button_by_xpath(self.STICKERS[name])

    def get_attach_button(self):
        return self.get_button_by_xpath(self.ATTACH_BUTTON)

    def get_message_with_sticker(self):
        return self.existance_of_element_by_xpath(self.MESSAGE_WITH_STICKER)

    def get_sent_message(self):
        return self.existance_of_element_by_xpath(self.SENT_MESSAGE)

    def wait_dialog_loader(self):
        self.existance_of_element_by_xpath(self.DIALOG_LOADER)
        self.invisibility_of_element_by_xpath(self.DIALOG_LOADER)

    def get_companion_name(self):
        return self.get_field_by_xpath(
            self.COMPANION_NAME).get_attribute('innerHTML')

    def existance_wrong_photo_format_ic(self):
        return self.existance_of_element_by_xpath(self.WRONG_PHOTO_FORMAT)

    # Nick112
    def get_long_message_error(self):
        return self.existance_of_element_by_xpath(self.LONG_MESSAGE_ERROR)

    def get_edit_message_button(self):
        return self.get_hidden_input_by_xpath(self.EDIT_MESSAGE_BUTTON)

    def get_delete_message_button(self):
        return self.get_hidden_input_by_xpath(self.DELETE_MESSAGE_BUTTON)

    def get_answer_message_button(self):
        return self.get_hidden_input_by_xpath(self.ANSWER_MESSAGE_BUTTON)

    def get_sent_message_text(self):
        return self.get_button_by_xpath(
            self.SENT_MESSAGE_TEXT).get_attribute("innerHTML")

    def get_answered_message(self):
        return self.existance_of_element_by_xpath(self.ANSWERED_MESSAGE)

    def get_forward_message(self):
        return self.get_hidden_input_by_xpath(self.FORWARD_MESSAGE)

    def get_forward_message_title(self):
        return self.existance_of_element_by_xpath(self.FORWARDED_MESSAGE_TITLE)

    def get_add_companion_button(self):
        return self.get_button_by_xpath(self.ADD_COMPANION_BUTTON)

    def get_group_chat_created_title(self):
        return self.existance_of_element_by_xpath(
            self.GROUP_CHAT_CREATED_TITLE)

    def get_group_chat_delete_title(self):
        return self.existance_of_element_by_xpath(
            self.GROUP_CHAT_REMOVED_TITLE)

    def get_control_users_button(self):
        return self.get_button_by_xpath(self.CONTROL_USERS_BUTTON)

    def get_pin_button(self):
        return self.get_hidden_input_by_xpath(self.PIN_MESSAGE_BUTTON)

    def get_pinned_message(self):
        return self.existance_of_element_by_xpath(self.PINNED_MESSAGE)

    def get_unpin_button(self):
        return self.get_button_by_xpath(self.UNPIN_MESSAGE_BUTTON)

    # Trubnikov

    def existence_changed_photo_notification(self):
        return self.existance_of_element_by_xpath(
            self.CHANGED_PHOTO_NOTIFICATION)

    def get_smiles_list_button(self):
        return self.get_button_by_xpath(self.SMILES_LIST_BUTTON)

    def pick_chocolate_smile(self):
        return self.get_button_by_xpath(self.SMILE_GOVNA)

    def pick_whale_smile(self):
        return self.get_button_by_xpath(self.SMILE_WHALE)

    def pick_gas_smile(self):
        return self.get_button_by_xpath(self.SMILE_GAS)

    def get_postcards_list_button(self):
        return self.get_button_by_xpath(self.POSTCARDS_LIST_BUTTON)

    def pick_first_postcard(self):
        return self.get_button_by_xpath(self.FIRST_POSTCARD_IN_LIST).click()

    def get_sent_postcard(self):
        return self.existance_of_element_by_xpath(self.SENT_POSTCARD)

    def search_postcards(self, request):
        self.get_button_by_xpath(self.POSTCARD_SEARCH).send_keys(request)

    def search_postcards_by_suggest(self):
        self.get_button_by_xpath(self.POSTCARD_SEARCH_SUGGEST).click()

    def wait_search_loading(self):
        self.existance_of_element_by_xpath(self.POSTCARD_SEARCH_LOADER)
        self.invisibility_of_element_by_xpath(self.POSTCARD_SEARCH_LOADER)

    def get_more_stickers(self):
        self.get_button_by_xpath(self.OPEN_STICKERS_SET_LIST).click()

    def close_stickers_set_list(self):
        self.get_button_by_xpath(self.CLOSE_STICKERS_SET_LIST).click()

    def install_stickers_set(self, set_id):
        if self.open_single_sticker_set(set_id):
            self.get_button_by_xpath(self.STICKERS_SET_INSTALL_BUTTON).click()

    def uninstall_stickers_set(self, set_id):
        if self.open_single_sticker_set(set_id):
            self.get_button_by_xpath(
                self.STICKERS_SET_UNINSTALL_BUTTON).click()

    def open_my_stickers_set_list(self):
        self.get_button_by_xpath(self.MY_STICKERS_BUTTON).click()

    def open_single_sticker_set(self, set_id):
        find_new_set = self.FIND_NEW_SET_TEMPLATE.replace("{ID}", set_id)
        self.get_button_by_xpath(find_new_set).click()
        return self.existance_of_element_by_xpath(self.SINGLE_STICKER_SET)

    def find_my_stickers_set(self, set_id):
        find_my_set = self.FIND_MY_SET_TEMPLATE.replace("{ID}", set_id)
        return self.existance_of_element_by_xpath(find_my_set)

    def open_avatar(self):
        self.get_button_by_xpath(self.USER_AVATAR).click()
        self.existance_of_element_by_xpath(self.AVATAR_LOADER)
        self.invisibility_of_element_by_xpath(self.AVATAR_LOADER)

    def existence_big_avatar(self):
        return self.existance_of_element_by_xpath(self.BIG_AVATAR)

    def get_report_message_button(self):
        return self.get_hidden_input_by_xpath(self.REPORT_MESSAGE_BUTTON)

    def existence_reported_message(self):
        return self.existance_of_element_by_xpath(self.REPORTED_MESSAGE)

    def get_game_button(self):
        return self.get_button_by_xpath(self.GAME_BUTTON)

    def get_game_close_button(self):
        return self.get_button_by_xpath(self.GAME_CLOSE_BUTTON)

    def find_game_invite(self):
        return self.existence_of_game_by_xpath(self.GAME_INVITE_MESSAGE)

    def find_game_invite_by_id(self, app_id):
        game_invite = self.GAME_INVITE_MESSAGE_TEMPLATE.replace("{AppID}", app_id)
        return self.existence_of_game_by_xpath(game_invite)

    def wait_game_list(self):
        self.existance_of_element_by_xpath(self.GAME_LIST)

    def pick_game(self, app_id):
        pick_game = self.PICK_GAME_TEMPLATE.replace("{AppID}", app_id)
        self.get_button_by_xpath(pick_game).click()

    def existence_game(self, app_id):
        find_game = self.ACTIVE_GAME_TEMPLATE.replace("{AppID}", app_id)
        return self.existance_of_element_by_xpath(find_game)

    def apply_game_invite(self, app_id):
        apply_button = self.GAME_INVITE_APPLY_TEMPLATE.replace("{AppID}", app_id)
        self.get_button_by_xpath(apply_button).click()

    def reject_game_invite(self, app_id):
        reject_button = self.GAME_INVITE_REJECT_TEMPLATE.replace("{AppID}", app_id)
        self.get_button_by_xpath(reject_button).click()

    def play_again_game_invite(self, app_id):
        play_again_button = self.GAME_INVITE_PLAY_AGAIN_TEMPLATE.replace("{AppID}", app_id)
        self.get_button_by_xpath(play_again_button).click()

    def existence_play_again_button(self):
        play_again_button = self.GAME_INVITE_PLAY_AGAIN_TEMPLATE.replace("{AppID}", "")
        return self.existance_of_element_by_xpath(play_again_button)

    def is_empty_postcard_search(self):
        return self.existance_of_element_by_xpath(self.EMPTY_POSTCARDS_SEARCH)

    # AndersRichter

    def get_video_call_button(self):
        return self.get_button_by_xpath(self.VIDEO_CALL_BUTTON)

    def get_video_call_window(self):
        return self.get_button_by_xpath(self.VIDEO_CALL_WINDOW)

    def get_support_button(self):
        return self.get_button_by_xpath(self.SUPPORT_BUTTON)

    def get_support_window(self):
        return self.get_button_by_xpath(self.SUPPORT_WINDOW)

    def get_sticker_bar_close(self):
        return self.get_button_by_xpath(self.STICKER_BAR_CLOSE)

    def get_sticker_bar_button(self):
        return self.get_button_by_xpath(self.STICKER_BAR_BUTTON)

    def get_present_page(self):
        return self.get_button_by_xpath(self.PRESENT_CONTENT)

    def wait_nav_loader(self):
        self.existance_of_element_by_xpath(self.NAV_LOADER)
        self.invisibility_of_element_by_xpath(self.NAV_LOADER)

    def wait_payment_loader(self):
        self.existance_of_element_by_xpath(self.PAYMENT_LOADER)
        self.invisibility_of_element_by_xpath(self.PAYMENT_LOADER)

    def wait_smile_loader(self):
        self.existance_of_element_by_xpath(self.SMILE_LOADER)
        self.invisibility_of_element_by_xpath(self.SMILE_LOADER)

    def get_money_window(self):
        return self.get_button_by_xpath(self.MONEY_WINDOW)

    def get_money_transfers_icon(self):
        self.driver.switch_to_frame(self.get_field_by_xpath(self.MONEY_WINDOW))
        return self.get_button_by_xpath(self.MONEY_TRANSFERS_ICON)

    def get_profile_button(self):
        return self.get_button_by_xpath(self.PROFILE_BUTTON)

    def get_profile_page(self):
        return self.get_button_by_xpath(self.PROFILE_CONTENT)

    def get_smile(self, name):
        return self.get_button_by_xpath(self.SMILES[name])

    def get_smile_list(self, name):
        return self.get_button_by_xpath(self.SMILES_LIST[name])

    def get_sticker1_from_bar(self):
        return self.get_button_by_xpath(self.STICKER_IN_BAR1)

    def get_existance_of_sticker1_in_bar(self):
        return self.existance_of_element_by_xpath(self.STICKER_IN_BAR1)

    def get_sticker2_from_bar(self):
        return self.get_button_by_xpath(self.STICKER_IN_BAR2)
