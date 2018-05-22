#!/usr/bin/env python2

import sys
import unittest
from tests.tests import Tests
from tests.suites.tests_send_document import TestsSendDocuments
from tests.suites.test_send_stickers import TestsStickers
from tests.suites.two_accaunts_management import TwoAccauntsManagement
from tests.suites.tests_send_messages import TestsSendMessages
from tests.suites.tests_find_dialog_msg import TestsFindDialogMsg
from tests.suites.tests_group_dialogs import TestsGroupDialogs


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(Tests),
    ))
    testsSendDocumentsSuite = unittest.TestSuite((
        unittest.makeSuite(TestsSendDocuments),
    ))

    testsSendStickersSuite = unittest.TestSuite((
        unittest.makeSuite(TestsStickers),
    ))

    twoAccauntsManagementSuite = unittest.TestSuite((
        unittest.makeSuite(TwoAccauntsManagement),
    ))

    testsSendMessagesSuite = unittest.TestSuite((
        unittest.makeSuite(TestsSendMessages),
    ))

    testsFindDialogMsgSuite = unittest.TestSuite((
        unittest.makeSuite(TestsFindDialogMsg),
    ))

    testsGroupDialogsSuite = unittest.TestSuite((
        unittest.makeSuite(TestsGroupDialogs),
    ))

    # result = unittest.TextTestRunner().run(suite)
    # result1 = unittest.TextTestRunner().run(testsSendDocumentsSuite)
    # result2 = unittest.TextTestRunner().run(testsSendStickersSuite)
    result3 = unittest.TextTestRunner().run(twoAccauntsManagementSuite)
    # result4 = unittest.TextTestRunner().run(testsSendMessagesSuite)
    # result5 = unittest.TextTestRunner().run(testsFindDialogMsgSuite)
    # result6 = unittest.TextTestRunner().run(testsGroupDialogsSuite)
    
    sys.exit(not result3.wasSuccessful())
