import unittest
import sys

from .tests.open_reg_form import OpenRegTest
from .tests.empty_fields import EmptyFieldsTest
from .tests.invalid_name import InvalidNameTest
from .tests.invalid_login import InvalidLoginTest
from .tests.invalid_pass2 import InvalidPassword2Test
from .tests.invalid_email import InvalidEmailTest
from .tests.have_account_click import HaveAccountClickTest
from .tests.valid_reg import ValidRegTest


def run_virusmusic_tests():
    suite = unittest.TestSuite((
        unittest.makeSuite(OpenRegTest),
        unittest.makeSuite(EmptyFieldsTest),
        unittest.makeSuite(InvalidNameTest),
        unittest.makeSuite(InvalidLoginTest),
        unittest.makeSuite(InvalidPassword2Test),
        unittest.makeSuite(InvalidEmailTest),
        unittest.makeSuite(HaveAccountClickTest),
        unittest.makeSuite(ValidRegTest),
    ))
    unittest.TextTestRunner().run(suite)
