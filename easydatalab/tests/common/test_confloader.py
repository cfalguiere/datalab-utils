#-*- coding: utf-8 -*-
from __future__ import print_function

import unittest

from easydatalab.common.confloader import AppConfigurationLoader
from easydatalab.common.exceptions import ConfigurationError

class TestAppConfigurationLoader(unittest.TestCase):

    def test_constructor(self):
        cfgFile = 'easydatalab/tests/resources/config/config_for_unittests.cfg'
        loader = AppConfigurationLoader()
        settings = loader.load( cfgFile )
        self.assertEqual( settings.get('A','a1'), 'val_a1' )


    def test_constructor_failure(self):
        cfgFile = 'does_not_exist'
        loader = AppConfigurationLoader()
        with self.assertRaises(ConfigurationError) as ctx:
            loader.load( cfgFile )
            raise ConfigurationError('pathToCode', 'does not exist')
            self.assertTrue('ConfigurationError' in ctx.exception)

    def test_constructor_multiple_files(self):
        cfgFileA = 'easydatalab/tests/resources/config/multiple/A.cfg'
        cfgFileB = 'easydatalab/tests/resources/config/multiple/B.cfg'
        loader = AppConfigurationLoader()
        settings = loader.load( [ cfgFileA, cfgFileB ] )
        self.assertEqual( settings.get('A','a1'), 'val_a1' )
        self.assertEqual( settings.get('B','b1'), 'val_b1' )

