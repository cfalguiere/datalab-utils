#-*- coding: utf-8 -*-
from __future__ import print_function

import unittest

from easydatalab.common.confloader import AppConfigurationLoader
from easydatalab.common.exceptions import ConfigurationError

class TestAppConfigurationLoader(unittest.TestCase):

    def test_constructor(self):
        cfgFile = 'easydatalab/tests/resources/config_for_unittests.cfg'
        loader = AppConfigurationLoader()
        loader.load( cfgFile )

    def test_constructor(self):
        cfgFile = 'does_not_exist'
        loader = AppConfigurationLoader()
        with self.assertRaises(ConfigurationError) as ctx:
            loader.load( cfgFile )
            raise ConfigurationError('pathToCode', 'does not exist')
            self.assertTrue('ConfigurationError' in ctx.exception)

