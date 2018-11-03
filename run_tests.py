# -*- coding: utf-8 -*-
import sys
import unittest

from tests.letter_formatting_tests import LetterFormattingTests

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(LetterFormattingTests)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())()
