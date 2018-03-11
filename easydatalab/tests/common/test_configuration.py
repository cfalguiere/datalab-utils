#-*- coding: utf-8 -*-
from __future__ import print_function

import unittest

from easydatalab.common.configuration import AppConfiguration
from easydatalab.common.exceptions import ExecutionError

class TestAppConfiguration(unittest.TestCase):

    def test_constructor(self):
        cfgFile = 'easydatalab/tests/resources/config_for_unittests.cfg'
        appConfiguration = AppConfiguration(cfgFile)
        self.assertEqual( repr(appConfiguration), 'AppConfiguration: from=easydatalab/tests/resources/config_for_unittests.cfg' )

    def test_get_parameter_loaded(self):
        cfgFile = 'easydatalab/tests/resources/config_for_unittests.cfg'
        appConfiguration = AppConfiguration(cfgFile)
        appConfiguration.__enter__()
        value = appConfiguration.get_parameter('A:a1')
        self.assertEqual( value, 'val_a1' )


    def test_get_parameter_added(self):
        cfgFile = 'easydatalab/tests/resources/config_for_unittests.cfg'
        appConfiguration = AppConfiguration(cfgFile)
        appConfiguration.__enter__()
        appConfiguration.add_parameter('z1', 'val_z1')
        value = appConfiguration.get_parameter('z1')
        self.assertEqual( value, 'val_z1' )

    def test_get_parameter_not_found(self):
        cfgFile = 'easydatalab/tests/resources/config_for_unittests.cfg'
        appConfiguration = AppConfiguration(cfgFile)
        appConfiguration.__enter__()
        with self.assertRaises(ExecutionError) as ctx:
            value = appConfiguration.get_parameter('x1')
            raise ExecutionError('AppConfiguration', 'key x1 was not found')

