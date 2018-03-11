#-*- coding: utf-8 -*-
"""Validator Tests"""

import unittest

from sch.common.validator import PathValidator

class TestPathValidatorMethods(unittest.TestCase):

    def test_check_path_for_existence(self):
        cv = PathValidator()
        cv.check_path_for_existence('.')
        self.assertEqual(cv.nb_errors(), 0)

    def test_check_path_for_existence_rejected(self):
        cv = PathValidator()
        cv.check_path_for_existence('doesnotexist')
        self.assertEqual(cv.nb_errors(), 1)

    def test_str(self):
        cv = PathValidator()
        cv.check_path_for_existence('doesnotexist')
        self.assertEqual(str(cv), 'Validation has detected 1 error(s)')

if __name__ == '__main__':
    unittest.main()
