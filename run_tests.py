import sys
import unittest
from tests.userinfo.wrongtown_test import WrongTownTest
from tests.userinfo.suggesttown_test import SuggestTownTest
from tests.userinfo.longname_test import LongSurnameTest
from tests.userinfo.gender_test import GenderTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(WrongTownTest),
        unittest.makeSuite(SuggestTownTest),
        unittest.makeSuite(LongSurnameTest),
        unittest.makeSuite(GenderTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())