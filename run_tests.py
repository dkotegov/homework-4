# -*- coding: utf-8 -*-
import sys
import unittest

from tests.auto_complete_city_test import AutoCompleteCityTest
from tests.change_gender_test import GenderTest
from tests.change_name_english_test import EnglishNameTest
from tests.change_name_russian_test import RussianNameTest
from tests.change_photo_error_test import ChangePhotoErrorTest
from tests.empty_field_test import EmptyTest
from tests.future_birthday_test import FutureBirthdayTest
from tests.leap_year_test import LeapYearTest
from tests.long_name_test import NameTest
from tests.narrow_photo_error_test import NarrowPhotoTest
from tests.not_change_test import NotChangeTest
from tests.pop_up_test import PopUpTest
from tests.update_photo_bmp_test import BmpPhotoTest
from tests.update_photo_gif_test import GifPhotoTest
from tests.update_photo_jpg_test import JpgPhotoTest
from tests.wrong_city_test import WrongCityTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AutoCompleteCityTest),
        unittest.makeSuite(GenderTest),
        unittest.makeSuite(EnglishNameTest),
        unittest.makeSuite(RussianNameTest),
        unittest.makeSuite(ChangePhotoErrorTest),
        unittest.makeSuite(EmptyTest),
        unittest.makeSuite(FutureBirthdayTest),
        unittest.makeSuite(LeapYearTest),
        unittest.makeSuite(NameTest),
        unittest.makeSuite(NarrowPhotoTest),
        unittest.makeSuite(NotChangeTest),
        unittest.makeSuite(PopUpTest),
        unittest.makeSuite(BmpPhotoTest),
        unittest.makeSuite(GifPhotoTest),
        unittest.makeSuite(JpgPhotoTest),
        unittest.makeSuite(WrongCityTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
