# -*- coding: utf-8 -*-

import sys
import unittest

from tests.answer import AnswerQuestionTests
from tests.ask import AskQuestionTests


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AskQuestionTests),
        unittest.makeSuite(AnswerQuestionTests),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
