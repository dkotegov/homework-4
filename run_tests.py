# -*- coding: utf-8 -*-
import sys
import unittest

from tests.QA_366 import TaskAddTest, TaskExecuteTest, TaskChangeDateTest, TaskCreateWithDateTest

if __name__ == '__main__':
    QA_366 = unittest.TestSuite((
        unittest.makeSuite(TaskAddTest),
        unittest.makeSuite(TaskExecuteTest),
        unittest.makeSuite(TaskChangeDateTest),
        unittest.makeSuite(TaskCreateWithDateTest),
    ))
    result = unittest.TextTestRunner().run(QA_366)
    sys.exit(not result.wasSuccessful())
