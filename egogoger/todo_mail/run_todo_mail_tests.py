import unittest

from .tests.auth_test import AuthTest
from .tests.priority_test import PriorityTest


def run_todo_mail_tests():
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(PriorityTest),
    ))
    unittest.TextTestRunner().run(suite)
