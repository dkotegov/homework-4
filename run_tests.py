#!/usr/bin/env python3

import sys
import unittest
import tests.signup_test as signup


if __name__ == '__main__':
    suite = unittest.TestSuite((
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
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
