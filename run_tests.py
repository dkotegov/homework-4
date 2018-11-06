# -*- coding: utf-8 -*-
import sys
import unittest

from tests.attach_tests.attach_tests import *
from tests.letter_formatting_tests import LetterFormattingTests

# TODO комментьте чужие тесты, если не хотите страдать! 😇

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(LetterFormattingTests),
        # unittest.makeSuite(AttachTest_document)
        # unittest.makeSuite(AttachTest_Media)
        # unittest.makeSuite(AttachTest_Executable),
        # unittest.makeSuite(AttachTestAlmostTwoGigFile),
        # unittest.makeSuite(AttachTest99Photos)
        # unittest.makeSuite(AttachTest25MbAndMoreThroughCloud)
        # unittest.makeSuite(AttachTestMore2GigFile)
        unittest.makeSuite(AttachTestLess25MbWithoutCloud)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())()
