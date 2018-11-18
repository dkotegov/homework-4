# -*- coding: utf-8 -*-
import sys
import unittest

from tests.attach_tests.attach_tests import *
from tests.letter_formatting_tests import LetterFormattingTests
from tests.letter_functions.functions_tests import *

# TODO комментьте чужие тесты, если не хотите страдать! 😇

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(ImportantMarkTest),
        # unittest.makeSuite(NotificationMarkTest),
        # unittest.makeSuite(ReminderMarkTest),
        # unittest.makeSuite(DelayedMarkTest),
        # unittest.makeSuite(CrossFuncsTest),
        # unittest.makeSuite(TemplateTest)
        unittest.makeSuite(LetterFormattingTests),
        # unittest.makeSuite(AttachTest_document)
        # unittest.makeSuite(AttachTest_Media)
        # unittest.makeSuite(AttachTest_Executable),
        # unittest.makeSuite(AttachTestAlmostTwoGigFile),
        # unittest.makeSuite(AttachTest99Photos)
        # unittest.makeSuite(AttachTest25MbAndMoreThroughCloud)

        # unittest.makeSuite(AttachTestLess25MbWithoutCloud)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())()
