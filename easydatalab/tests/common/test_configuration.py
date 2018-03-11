#-*- coding: utf-8 -*-
from __future__ import print_function

import unittest

from easydatalab.common.configuration import AppConfiguration

class TestAppConfiguration(unittest.TestCase):

    def test_constructor(self):
        cfgFile = 'easydatalab/tests/resources/config_for_unittests.cfg'
        appConfiguration = AppConfiguration(cfgFile)
        self.assertEqual( repr(appConfiguration), 'AppConfiguration: from=sch/mocks/app-for-unittests.cfg' )
