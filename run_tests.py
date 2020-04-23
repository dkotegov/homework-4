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
from tests.services_test import ServicesTest
from tests.service_cm_test import ServiceCMTest
from tests.service_dc_test import ServiceDCTest
from tests.service_auto_test import ServiceAutoTest
from tests.service_calendar_test import ServiceCalendarTest
from tests.service_deti_test import ServiceDetiTest
from tests.service_dobro_test import ServiceDobroTest
from tests.service_games_test import ServiceGamesTest
from tests.service_health_test import ServiceHealthTest
from tests.service_hi_tech_test import ServiceHiTechTest
from tests.service_horo_test import ServiceHoroTest
from tests.service_kino_test import ServiceKinoTest
from tests.service_lady_test import ServiceLadyTest
from tests.service_marusia_test import ServiceMarusiaTest
from tests.service_my_test import ServiceMYTest
from tests.service_pets_test import ServicePetsTest
from tests.service_pogoda_test import ServicePogodaTest
from tests.service_realty_test import ServiceRealtyTest
from tests.service_vseapteki_test import ServiceVseaptekiTest
from tests.services_less_test import ServicesLessTest
from tests.tab_test import TabTest
from tests.ref_mailru_test import RefMailRuTest
from tests.ref_about_company_test import RefAboutCompanyTest
from tests.ref_support_test import RefSupportTest
from tests.ref_report_test import RefReportTest
from tests.button_signin_test import ButtonSignInTest
from tests.button_signup_test import ButtonSignUpTest
from tests.ref_remind_test import RefRemindTest
from tests.ref_signup_test import RefSignUpTest
from tests.ref_vk_test import RefVKTest
from tests.ref_tw_test import RefTwitterTest
from tests.ref_fb_test import RefFacebookTest
from tests.ref_ok_test import RefOdnoklassnikiTest
from tests.ref_auth_account_info_test import RefAuthAccountInfoTest
from tests.ref_auth_all_settings_test import RefAuthAllSettingsTest
from tests.ref_auth_setup_account_info_test import RefAuthSetupAccountInfoTest
from tests.ref_auth_setup_all_settings_test import RefAuthSetupAllSettingsTest



if __name__ == '__main__':
    suite = unittest.TestSuite((
        # Nastya Kuznecova tests
        # unittest.makeSuite(AutoCompleteCityTest),
        # unittest.makeSuite(GenderTest),
        # unittest.makeSuite(EnglishNameTest),
        # unittest.makeSuite(RussianNameTest),
        # unittest.makeSuite(ChangePhotoErrorTest),
        # unittest.makeSuite(EmptyTest),
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
        # unittest.makeSuite(ServicesTest),
        # unittest.makeSuite(ServiceCMTest),
        # unittest.makeSuite(ServiceDCTest),
        # unittest.makeSuite(ServiceAutoTest),
        # unittest.makeSuite(ServiceCalendarTest),
        # unittest.makeSuite(ServiceDetiTest),
        # unittest.makeSuite(ServiceDobroTest),
        # unittest.makeSuite(ServiceGamesTest),
        # unittest.makeSuite(ServiceHealthTest),
        # unittest.makeSuite(ServiceHiTechTest),
        # unittest.makeSuite(ServiceHoroTest),
        # unittest.makeSuite(ServiceKinoTest),
        # unittest.makeSuite(ServiceLadyTest),
        # unittest.makeSuite(ServiceMarusiaTest),
        # unittest.makeSuite(ServiceMYTest),
        # unittest.makeSuite(ServicePetsTest),
        # unittest.makeSuite(ServicePogodaTest),
        # unittest.makeSuite(ServiceRealtyTest),
        # unittest.makeSuite(ServiceVseaptekiTest),
        # unittest.makeSuite(ServicesLessTest),
        # unittest.makeSuite(TabTest),
        # unittest.makeSuite(RefMailRuTest),
        # unittest.makeSuite(RefAboutCompanyTest),
        # unittest.makeSuite(RefSupportTest),
        # unittest.makeSuite(RefReportTest),
        # unittest.makeSuite(ButtonSignInTest),
        # unittest.makeSuite(ButtonSignUpTest),
        # unittest.makeSuite(RefRemindTest),
        # unittest.makeSuite(RefSignUpTest),
        # unittest.makeSuite(RefVKTest),
        # unittest.makeSuite(RefTwitterTest),
        # unittest.makeSuite(RefFacebookTest),
        # unittest.makeSuite(RefOdnoklassnikiTest),
        unittest.makeSuite(RefAuthAccountInfoTest),
        # unittest.makeSuite(RefAuthAllSettingsTest),
        # unittest.makeSuite(RefAuthSetupAccountInfoTest),
        # unittest.makeSuite(RefAuthSetupAllSettingsTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
