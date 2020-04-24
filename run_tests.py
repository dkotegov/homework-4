# -*- coding: utf-8 -*-
import sys
import unittest

from tests.contacts.add_email_popup.add_email_cancel import AddPopupEmailCancelTest
from tests.contacts.add_email_popup.add_email_close import AddPopupEmailCloseTest
from tests.contacts.add_email_popup.add_invalid_email import AddPopupEmailInvalidTest
from tests.contacts.add_email_popup.add_valid_email import AddPopupEmailValidTest
from tests.contacts.add_phone_popup.add_invalid_phone import AddPopupPhoneInvalidTest
from tests.contacts.add_phone_popup.add_phone_cancel import AddPopupPhoneCancelTest
from tests.contacts.add_phone_popup.add_phone_close import AddPopupPhoneCloseTest
from tests.contacts.add_phone_popup.add_valid_phone import AddPopupPhoneValidTest
from tests.contacts.add_phone_popup.change_country_phone import AddPopupPhoneChangeCountryTest
from tests.contacts.change_data.refresh_page import ChangeDataRefreshTest
from tests.contacts.confirm_phone_popup.confirm_code_change_number import ConfirmPopupPhoneChangeNumberTest
from tests.contacts.confirm_phone_popup.confirm_code_close import ConfirmPopupPhoneCloseTest
from tests.contacts.confirm_phone_popup.confirm_code_empty import ConfirmPopupPhoneEmptyTest
from tests.contacts.confirm_phone_popup.confirm_phone_invalid import ConfirmPopupPhoneInvalidTest
from tests.contacts.func_email.func_add_first_email import FuncAddEmailFirstTest
from tests.contacts.func_email.func_add_nonexisting_email import FuncAddEmailNonexistingTest
from tests.contacts.func_email.func_add_second_email import FuncAddEmailSecondTest
from tests.contacts.func_email.func_delete_email import FuncDeleteEmailTest
from tests.contacts.func_phone.func_delete_phone import FuncDeletePhoneTest
from tests.contacts.func_phone.func_delete_phone_reserved import FuncDeletePhoneReservedTest
from tests.mainpage.services_test import ServicesTest
from tests.mainpage.service_cm_test import ServiceCMTest
from tests.mainpage.service_dc_test import ServiceDCTest
from tests.mainpage.service_auto_test import ServiceAutoTest
from tests.mainpage.service_calendar_test import ServiceCalendarTest
from tests.mainpage.service_deti_test import ServiceDetiTest
from tests.mainpage.service_dobro_test import ServiceDobroTest
from tests.mainpage.service_games_test import ServiceGamesTest
from tests.mainpage.service_health_test import ServiceHealthTest
from tests.mainpage.service_hi_tech_test import ServiceHiTechTest
from tests.mainpage.service_horo_test import ServiceHoroTest
from tests.mainpage.service_kino_test import ServiceKinoTest
from tests.mainpage.service_lady_test import ServiceLadyTest
from tests.mainpage.service_marusia_test import ServiceMarusiaTest
from tests.mainpage.service_my_test import ServiceMYTest
from tests.mainpage.service_pets_test import ServicePetsTest
from tests.mainpage.service_pogoda_test import ServicePogodaTest
from tests.mainpage.service_realty_test import ServiceRealtyTest
from tests.mainpage.service_vseapteki_test import ServiceVseaptekiTest
from tests.mainpage.services_less_test import ServicesLessTest
from tests.mainpage.tab_test import TabTest
from tests.mainpage.ref_mailru_test import RefMailRuTest
from tests.mainpage.ref_about_company_test import RefAboutCompanyTest
from tests.mainpage.ref_support_test import RefSupportTest
from tests.mainpage.ref_report_test import RefReportTest
from tests.mainpage.button_signin_test import ButtonSignInTest
from tests.mainpage.button_signup_test import ButtonSignUpTest
from tests.mainpage.ref_remind_test import RefRemindTest
from tests.mainpage.ref_signup_test import RefSignUpTest
from tests.mainpage.ref_vk_test import RefVKTest
from tests.mainpage.ref_tw_test import RefTwitterTest
from tests.mainpage.ref_fb_test import RefFacebookTest
from tests.mainpage.ref_ok_test import RefOdnoklassnikiTest
from tests.mainpage.ref_auth_account_info_test import RefAuthAccountInfoTest
from tests.mainpage.ref_auth_all_settings_test import RefAuthAllSettingsTest
from tests.mainpage.ref_auth_setup_account_info_test import RefAuthSetupAccountInfoTest
from tests.mainpage.ref_auth_setup_all_settings_test import RefAuthSetupAllSettingsTest
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

        # profile tests

        unittest.makeSuite(AutoCompleteCityTest),
        unittest.makeSuite(GenderTest),
        unittest.makeSuite(EnglishNameTest),
        unittest.makeSuite(RussianNameTest),
        unittest.makeSuite(ChangePhotoErrorTest),
        # unittest.makeSuite(EmptyTest),
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


        # contacts tests

        # нужен проверенный телефон, добавленный при создании аккаунта
        unittest.makeSuite(FuncDeletePhoneTest),
        # нужен непроверенный телефон, добавленный после создания аккаунта
        unittest.makeSuite(FuncDeletePhoneReservedTest),

        unittest.makeSuite(FuncAddEmailFirstTest),
        unittest.makeSuite(FuncAddEmailSecondTest),
        unittest.makeSuite(FuncAddEmailNonexistingTest),
        unittest.makeSuite(FuncDeleteEmailTest),

        unittest.makeSuite(AddPopupPhoneInvalidTest),
        unittest.makeSuite(AddPopupPhoneValidTest),
        unittest.makeSuite(AddPopupPhoneChangeCountryTest),
        unittest.makeSuite(AddPopupPhoneCancelTest),
        unittest.makeSuite(AddPopupPhoneCloseTest),

        # в этом блоке тесты могут не проходить, так как вылезает ошибка "слишком много смс"
        unittest.makeSuite(ConfirmPopupPhoneInvalidTest),
        unittest.makeSuite(ConfirmPopupPhoneEmptyTest),
        unittest.makeSuite(ConfirmPopupPhoneCloseTest),
        unittest.makeSuite(ConfirmPopupPhoneChangeNumberTest),

        unittest.makeSuite(AddPopupEmailInvalidTest),
        unittest.makeSuite(AddPopupEmailValidTest),
        unittest.makeSuite(AddPopupEmailCancelTest),
        unittest.makeSuite(AddPopupEmailCloseTest),

        unittest.makeSuite(ChangeDataRefreshTest),

        # main_page tests

        unittest.makeSuite(ServicesTest),
        unittest.makeSuite(ServiceCMTest),
        unittest.makeSuite(ServiceDCTest),
        unittest.makeSuite(ServiceAutoTest),
        unittest.makeSuite(ServiceCalendarTest),
        unittest.makeSuite(ServiceDetiTest),
        unittest.makeSuite(ServiceDobroTest),
        unittest.makeSuite(ServiceGamesTest),
        unittest.makeSuite(ServiceHealthTest),
        unittest.makeSuite(ServiceHiTechTest),
        unittest.makeSuite(ServiceHoroTest),
        unittest.makeSuite(ServiceKinoTest),
        unittest.makeSuite(ServiceLadyTest),
        unittest.makeSuite(ServiceMarusiaTest),
        unittest.makeSuite(ServiceMYTest),
        unittest.makeSuite(ServicePetsTest),
        unittest.makeSuite(ServicePogodaTest),
        unittest.makeSuite(ServiceRealtyTest),
        unittest.makeSuite(ServiceVseaptekiTest),
        unittest.makeSuite(ServicesLessTest),
        unittest.makeSuite(TabTest),
        unittest.makeSuite(RefMailRuTest),
        unittest.makeSuite(RefAboutCompanyTest),
        unittest.makeSuite(RefSupportTest),
        unittest.makeSuite(RefReportTest),
        unittest.makeSuite(ButtonSignInTest),
        unittest.makeSuite(ButtonSignUpTest),
        unittest.makeSuite(RefRemindTest),
        unittest.makeSuite(RefSignUpTest),
        unittest.makeSuite(RefVKTest),
        unittest.makeSuite(RefTwitterTest),
        unittest.makeSuite(RefFacebookTest),
        unittest.makeSuite(RefOdnoklassnikiTest),
        unittest.makeSuite(RefAuthAccountInfoTest),
        unittest.makeSuite(RefAuthAllSettingsTest),
        unittest.makeSuite(RefAuthSetupAccountInfoTest),
        unittest.makeSuite(RefAuthSetupAllSettingsTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
