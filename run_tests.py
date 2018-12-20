# -*- coding: utf-8 -*-
import sys
import unittest

from tests.attach_tests.attach_tests import *
from tests.letter_formatting.formatting_tests import BoldTest, ItalicTest, UnderlinedTest, StrikeThroughTest, \
    ColorTextTest, BackgroundColorTest, FontIconTest, TextAlignTest, MarginIconTest, NumberedListTest, MarkedListTest, \
    CancelButtonTest, LinkInsertionTest, ImageInsertTest, ClearFormatingTest
from tests.letter_functions.functions_tests import *
from tests.send_tests.send_tests import *

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ImportantMarkTest),
        unittest.makeSuite(NotificationMarkTest),
        unittest.makeSuite(ReminderMarkTest),
        unittest.makeSuite(DelayedMarkTest),
        unittest.makeSuite(CrossFuncsTest),
        unittest.makeSuite(TemplateTest),
        unittest.makeSuite(BoldTest),
        unittest.makeSuite(ItalicTest),
        unittest.makeSuite(UnderlinedTest),
        unittest.makeSuite(StrikeThroughTest),
        unittest.makeSuite(ColorTextTest),
        unittest.makeSuite(BackgroundColorTest),
        unittest.makeSuite(FontIconTest),
        unittest.makeSuite(TextAlignTest),
        unittest.makeSuite(MarginIconTest),
        unittest.makeSuite(NumberedListTest),
        unittest.makeSuite(MarkedListTest),
        unittest.makeSuite(CancelButtonTest),
        unittest.makeSuite(LinkInsertionTest),
        unittest.makeSuite(ImageInsertTest),
        unittest.makeSuite(ClearFormatingTest),
        unittest.makeSuite(AttachTestDocument),
        unittest.makeSuite(AttachTestMedia),
        unittest.makeSuite(AttachTestExecutable),
        unittest.makeSuite(AttachTest25MbAndMoreThroughCloud),
        unittest.makeSuite(AttachTestLess25MbWithoutCloud),
        unittest.makeSuite(AttachCloudDocument),
        unittest.makeSuite(AttachCloudMedia),
        unittest.makeSuite(AttachCloudExecutable),
        unittest.makeSuite(AttachCloudAlmost2GigFile),
        unittest.makeSuite(SendEmailToMeTest),
        unittest.makeSuite(SendEmailToCorrectEmailTest),
        unittest.makeSuite(SendEmailToGroupCorrectEmailsTest),
        unittest.makeSuite(SendEmailToWrongEmailTest),
        unittest.makeSuite(SendEmailToGroupWrongEmailsTest),
        unittest.makeSuite(SendEmailToMeWithCopyTest),
        unittest.makeSuite(SendEmailToCorrectEmailWithCopyTest),
        unittest.makeSuite(SendEmailToGroupWrongEmailsWithCopyTest)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())()
