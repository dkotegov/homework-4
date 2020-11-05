#!/usr/bin/env python3

import sys
import unittest

from tests.chat.clickContactsFromChatMsgHistory import ClickContactFromMsgHistory
from tests.chat.noLoginChat import OpenChatNoLogin
from tests.chat.sendEmoji import SendEmoji
from tests.chat.sendMessage import SendMessage
from tests.chat.sendSticker import SendSticker
from tests.chat.simpleOpenChat import OpenChat
from tests.feed.getUserPinsNoLogin import GetUserPinsNoLogin
from tests.feed.mainFeed import MainFeed
from tests.feed.myDesk import MyDesk
from tests.feed.myPinsFeed import MyPins
from tests.feed.subscriptionsFeed import SubFeed
from tests.login import LoginTest
from tests.chat.supportPage import OpenSupportPage
from tests.notification.havaNotif import HaveNotif
from tests.notification.noHaveNotif import NoHaveNotif
from tests.notification.noLoginOpenNotification import NoLoginNotif
from tests.pin_comment_search_menu import PinAndCommentTest

from romanov.cases.auth_login import AuthLoginTest
from romanov.cases.auth_reg import AuthRegTest
from romanov.cases.profile import ProfileTest
from romanov.cases.settings import SettingsTest
from romanov.cases.new_pin_desk import NewPinDeskTest

from romanov.app.driver import connect



if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginTest),
        unittest.makeSuite(OpenSupportPage),
        unittest.makeSuite(SendMessage),
        unittest.makeSuite(SendEmoji),
        unittest.makeSuite(SendSticker),
        unittest.makeSuite(ClickContactFromMsgHistory),
        unittest.makeSuite(OpenChatNoLogin),
        unittest.makeSuite(OpenChat),
        unittest.makeSuite(NoHaveNotif),
        unittest.makeSuite(NoLoginNotif),
        unittest.makeSuite(MainFeed),
        unittest.makeSuite(MyPins),
        unittest.makeSuite(MyDesk),
        unittest.makeSuite(GetUserPinsNoLogin),
        unittest.makeSuite(SubFeed),
        unittest.makeSuite(HaveNotif),


        unittest.makeSuite(PinAndCommentTest),
        
        unittest.makeSuite(AuthLoginTest),
        unittest.makeSuite(AuthRegTest),
        unittest.makeSuite(ProfileTest),
        unittest.makeSuite(SettingsTest),
        unittest.makeSuite(NewPinDeskTest),

    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
