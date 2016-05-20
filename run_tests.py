# -*- coding: utf-8 -*-

import sys

from tests.car_showrooms.add_showroom_test import AddShowroomFormTest
from tests.car_showrooms.list_showroom_test import ShowroomListTest
from tests.car_showrooms.list_special_offers_test import SpecialOffersListTest
from tests.car_showrooms.search_showroom_tests import *

if __name__ == '__main__':
    os.environ["TTHA2BROWSER"] = "FIREFOX"

    results = []

    suite = unittest.TestSuite((
        unittest.makeSuite(RegionSelectFormTest),
    ))
    results.append(unittest.TextTestRunner().run(suite))

    suite = unittest.TestSuite((
        unittest.makeSuite(SelectCarModelTest),
    ))
    results.append(unittest.TextTestRunner().run(suite))

    suite = unittest.TestSuite((
        unittest.makeSuite(SelectStationTest),
    ))
    results.append(unittest.TextTestRunner().run(suite))

    suite = unittest.TestSuite((
        unittest.makeSuite(IsOfficialCheckboxTest),
    ))
    results.append(unittest.TextTestRunner().run(suite))

    suite = unittest.TestSuite((
            unittest.makeSuite(SearchFormTest),
        ))
    results.append(unittest.TextTestRunner().run(suite))

    suite = unittest.TestSuite((
        unittest.makeSuite(ShowroomListTest),
    ))
    results.append(unittest.TextTestRunner().run(suite))

    suite = unittest.TestSuite((
        unittest.makeSuite(SpecialOffersListTest),
    ))
    results.append(unittest.TextTestRunner().run(suite))

    suite = unittest.TestSuite((
        unittest.makeSuite(AddShowroomFormTest),
    ))
    results.append(unittest.TextTestRunner().run(suite))

    for result in results:
        if not result.wasSuccessful():
            sys.exit(result.wasSuccessful())

    sys.exit(0)
