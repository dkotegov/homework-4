import unittest

from es_check_list.all_marks_test import TestAllMarkValues
from es_check_list.self_mark_test import TestSelfMark
from es_check_list.check_marks_test import TestCheckMarks

tests = (
    # unittest.makeSuite(TestAllMarkValues),
    # unittest.makeSuite(TestSelfMark),
    unittest.makeSuite(TestCheckMarks)
)