#!/usr/bin/env python3

import sys
import unittest

import tests.signup_test as signup
import tests.acc_settings_test as accsettings
import tests.password_settings_test as passwordsettings
import tests.client_settings_test as client
import tests.freelancer_settings_test as freelancer

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # signup
        unittest.makeSuite(signup.SignupTestValidFreelancer),
        unittest.makeSuite(signup.SignupTestInvalidFreelancerExistingEmail),
        unittest.makeSuite(signup.SignupTestInvalidFreelancerShortPassword),
        unittest.makeSuite(signup.SignupTestInvalidFreelancerNameWithNumbers),
        unittest.makeSuite(signup.SignupTestInvalidFreelancerNameWithSymbols),
        unittest.makeSuite(signup.SignupTestInvalidFreelancerSurnameWithNumbers),
        unittest.makeSuite(signup.SignupTestInvalidFreelancerSurnameWithSymbols),

        unittest.makeSuite(signup.SignupTestValidClient),
        unittest.makeSuite(signup.SignupTestInvalidClientExistingEmail),
        unittest.makeSuite(signup.SignupTestInvalidClientShortPassword),
        unittest.makeSuite(signup.SignupTestInvalidClientNameWithNumbers),
        unittest.makeSuite(signup.SignupTestInvalidClientNameWithSymbols),
        unittest.makeSuite(signup.SignupTestInvalidClientSurnameWithNumbers),
        unittest.makeSuite(signup.SignupTestInvalidClientSurnameWithSymbols),

        # account settings
        unittest.makeSuite(accsettings.FreelancerChangeSurnameTestValid),
        unittest.makeSuite(accsettings.FreelancerChangeSurnameTestInvalidTooShort),
        unittest.makeSuite(accsettings.FreelancerChangeSurnameTestInvalidTooLong),
        unittest.makeSuite(accsettings.FreelancerChangeSurnameTestInvalidNumbers),
        unittest.makeSuite(accsettings.FreelancerChangeSurnameTestInvalidSpecialSymbols),

        unittest.makeSuite(accsettings.FreelancerChangeNameTestValid),
        unittest.makeSuite(accsettings.FreelancerChangeNameTestInvalidTooShort),
        unittest.makeSuite(accsettings.FreelancerChangeNameTestInvalidTooLong),
        unittest.makeSuite(accsettings.FreelancerChangeNameTestInvalidNumbers),
        unittest.makeSuite(accsettings.FreelancerChangeNameTestInvalidSpecialSymbols),

        # client settings
        unittest.makeSuite(client.ClientSettingsChangeCompanyTestValid),
        unittest.makeSuite(client.ClientSettingsChangeCompanyTestInvalidTooShortName),
        unittest.makeSuite(client.ClientSettingsChangeCompanyTestInvalidTooLongName),
        unittest.makeSuite(client.ClientSettingsChangeCompanyTestInvalidTooShortSite),
        unittest.makeSuite(client.ClientSettingsChangeCompanyTestInvalidTooLongSite),
        unittest.makeSuite(client.ClientSettingsChangeCompanyTestInvalidTooShortTitle),
        unittest.makeSuite(client.ClientSettingsChangeCompanyTestInvalidTooLongTitle),

        unittest.makeSuite(client.ClientChangeContactsValid),
        unittest.makeSuite(client.ClientChangeContactsInvalidTooShortAddress),
        unittest.makeSuite(client.ClientChangeContactsInvalidTooLongAddress),
        unittest.makeSuite(client.ClientChangeContactsInvalidWrongPhone),

        # freelancer settings
        unittest.makeSuite(freelancer.FreelancerChangeDescTestValid),
        unittest.makeSuite(freelancer.FreelancerSetSkillsTestValid),
        unittest.makeSuite(freelancer.FreelancerSetSkillsTestInvalidTooManyTags),

        unittest.makeSuite(freelancer.FreelancerChangeSpecializationTest),

        unittest.makeSuite(freelancer.FreelancerChangeExperienceJuniorTest),
        unittest.makeSuite(freelancer.FreelancerChangeExperienceMiddleTest),
        unittest.makeSuite(freelancer.FreelancerChangeExperienceSeniorTest),

        unittest.makeSuite(freelancer.FreelancerChangeContactsValid),
        unittest.makeSuite(freelancer.FreelancerChangeContactsInvalidTooShortAddress),
        unittest.makeSuite(freelancer.FreelancerChangeContactsInvalidTooLongAddress),
        unittest.makeSuite(freelancer.FreelancerChangeContactsInvalidWrongPhone),

        # password settings
        unittest.makeSuite(passwordsettings.FreelancerChangePasswordTestInvalidDiffPasswords),
        unittest.makeSuite(passwordsettings.FreelancerChangePasswordTestInvalidWrongPassword),
        unittest.makeSuite(passwordsettings.FreelancerChangePasswordTestValid),
        unittest.makeSuite(passwordsettings.ClientChangePasswordTestInvalidDiffPasswords),
        unittest.makeSuite(passwordsettings.ClientChangePasswordTestInvalidWrongPassword),
        unittest.makeSuite(passwordsettings.ClientChangePasswordTestValid),

    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
