import unittest

from es_check_list.set_marks_test import TestAllMarkValues, TestSelfMark
from es_check_list.remove_marks_test import TestRemoveMark, CancelRemoveMarkTest, TestSetNewMark


tests = (
    unittest.makeSuite(TestAllMarkValues),
    # unittest.makeSuite(TestSelfMark),
    # unittest.makeSuite(TestRemoveMark),
    # unittest.makeSuite(TestCancelRemoveMark),
    # unittest.makeSuite(TestSetNewMark)
)