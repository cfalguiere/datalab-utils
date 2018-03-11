#-*- coding: utf-8 -*-
from __future__ import print_function

import unittest

from easydatalab.common.validator import PathValidator


class TestValidator(unittest.TestCase):

    def test_validator_nominal(self):
        pv = PathValidator()
        cfgFile = 'easydatalab/tests/resources/config_for_unittests.cfg'
        pv.check_path_for_existence( cfgFile )
        self.assertTrue( pv.nb_errors, 0 )
        self.assertTrue( pv.nb_warnings, 0 )

    def test_exception_error(self):
        pv = PathValidator()
        cfgFile = 'does_not_exist'
        pv.check_path_for_existence( cfgFile )
        self.assertTrue( pv.nb_errors, 1 )
        self.assertTrue( pv.nb_warnings, 1 )
