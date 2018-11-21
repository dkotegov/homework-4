# -*- coding: utf-8 -*-
import sys
import unittest

from tests.attach_tests.attach_tests import *
from tests.letter_formatting_tests import LetterFormattingTests
from tests.letter_functions.functions_tests import *
from tests.send_tests.send_tests import *

# TODO комментьте чужие тесты, если не хотите страдать! 😇

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(SendTestEmailToMe),
        unittest.makeSuite(SendTestEmailToCorrectEmail),
        unittest.makeSuite(SendTestEmailToGroupCorrectEmails),
        unittest.makeSuite(SendTestEmailToWrongEmail),
        unittest.makeSuite(SendTestEmailToGroupWrongEmails),
        unittest.makeSuite(SendTestEmailToMeWithCopy),
        unittest.makeSuite(SendTestEmailToCorrectEmailWithCopy),
        unittest.makeSuite(SendTestEmailToGroupWrongEmailsWithCopy)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())()
