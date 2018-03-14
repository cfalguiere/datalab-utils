#-*- coding: utf-8 -*-
from __future__ import print_function

import unittest

from easydatalab.common.app import AppContext

class TestCompound(unittest.TestCase):

    def test_with_context(self):
        with AppContext() as appContext:
             self.assertEqual( str(appContext), 'App' )

    def test_with_step(self):
        with AppContext() as appContext:
            with appContext.new_step ('echo') as step:
                 self.assertEqual( str(step), 'echo' )

    def test_with_configuration(self):
        cfgFile = 'easydatalab/tests/resources/config/config_for_unittests.cfg'
        with AppContext() as appContext:
             with appContext.new_configuration(cfgFile) as appConfiguration:
                  appConfiguration.show()
                  value = appConfiguration.get_parameter('A:a1')
                  self.assertEqual( value, 'val_a1' )
                  appConfiguration.add_parameter('z1', 'val_z1')
                  value = appConfiguration.get_parameter('z1')
                  self.assertEqual( value, 'val_z1' )
