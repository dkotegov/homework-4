# -*- coding: utf-8 -*-
import sys
import unittest
from tests.registration_test import RegistrationTest


if __name__ == '__main__':

    suite = unittest.TestSuite((
        unittest.makeSuite(RegistrationTest)
    ))

    result = unittest.TextTestRunner().run(suite)