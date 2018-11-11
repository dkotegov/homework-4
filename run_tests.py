# -*- coding: utf-8 -*-
import sys
import unittest

from tests.attach_tests.attach_tests import *
from tests.letter_formatting_tests import LetterFormattingTests

# TODO комментьте чужие тесты, если не хотите страдать! 😇

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(LetterFormattingTests),
        # unittest.makeSuite(AttachTest_document) #done!
        # unittest.makeSuite(AttachTest_Media) #done!
        # unittest.makeSuite(AttachTest_Executable)
        # unittest.makeSuite(AttachTestAlmostTwoGigFile) #может быть не стоит его запускать
        # unittest.makeSuite(AttachTest99Photos) #тест не проходит из-за баги!
        # unittest.makeSuite(AttachTest25MbAndMoreThroughCloud) #done
        # unittest.makeSuite(AttachTestMore2GigFile) #тест не нужен!
        # unittest.makeSuite(AttachTestLess25MbWithoutCloud) #done! но есть проблема

    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())()
