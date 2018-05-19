#!/usr/bin/env python2

import sys
import unittest
from tests.tests import Tests
from tests.suites.tests_send_document import TestsSendDocuments
from tests.suites.test_send_stickers import TestsSendStickers
from tests.suites.two_accaunts_management import TwoAccauntsManagement
from tests.suites.tests_send_messages import TestsSendMessages
from tests.suites.tests_find_dialog_msg import TestsFindDialogMsg

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(Tests),
    ))
    suite1 = unittest.TestSuite((
        unittest.makeSuite(TestsSendDocuments),
    ))

    suite2 = unittest.TestSuite((
        unittest.makeSuite(TestsSendStickers),
    ))

    suite3 = unittest.TestSuite((
        unittest.makeSuite(TwoAccauntsManagement),
    ))

    suite4 = unittest.TestSuite((
        unittest.makeSuite(TestsSendMessages),
    ))

    suite5 = unittest.TestSuite((
        unittest.makeSuite(TestsFindDialogMsg),
    ))
    # result = unittest.TextTestRunner().run(suite)
    # result1 = unittest.TextTestRunner().run(suite1)
    # result2 = unittest.TextTestRunner().run(suite2)
    # result3 = unittest.TextTestRunner().run(suite3)
    # result4 = unittest.TextTestRunner().run(suite4)
    result5 = unittest.TextTestRunner().run(suite5)
    sys.exit(not result5.wasSuccessful())
