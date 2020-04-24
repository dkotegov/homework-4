# -*- coding: utf-8 -*-
import sys
import unittest

from tests.profile.auto_complete_city_test import AutoCompleteCityTest
from tests.profile.change_gender_test import GenderTest
from tests.profile.change_name_english_test import EnglishNameTest
from tests.profile.change_name_russian_test import RussianNameTest
from tests.profile.change_photo_error_test import ChangePhotoErrorTest
from tests.profile.empty_field_test import EmptyTest
from tests.profile.future_birthday_test import FutureBirthdayTest
from tests.profile.leap_year_test import LeapYearTest
from tests.profile.long_name_test import NameTest
from tests.profile.narrow_photo_error_test import NarrowPhotoTest
from tests.profile.not_change_test import NotChangeTest
from tests.profile.pop_up_test import PopUpTest
from tests.profile.update_photo_bmp_test import BmpPhotoTest
from tests.profile.update_photo_gif_test import GifPhotoTest
from tests.profile.update_photo_jpg_test import JpgPhotoTest
from tests.profile.wrong_city_test import WrongCityTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(AutoCompleteCityTest),
        # unittest.makeSuite(GenderTest),
        # unittest.makeSuite(EnglishNameTest),
        # unittest.makeSuite(RussianNameTest),
        # unittest.makeSuite(ChangePhotoErrorTest),
        unittest.makeSuite(EmptyTest),
        # unittest.makeSuite(FutureBirthdayTest),
        # unittest.makeSuite(LeapYearTest),
        # unittest.makeSuite(NameTest),
        # unittest.makeSuite(NarrowPhotoTest),
        # unittest.makeSuite(NotChangeTest),
        # unittest.makeSuite(PopUpTest),
        # unittest.makeSuite(BmpPhotoTest),
        # unittest.makeSuite(GifPhotoTest),
        # unittest.makeSuite(JpgPhotoTest),
        # unittest.makeSuite(WrongCityTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
