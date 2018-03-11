#-*- coding: utf-8 -*-
from __future__ import print_function

import unittest

class TestSCHContext(unittest.TestCase):

    def test_constructor(self):
        appContext = SCHAppContext('SCH')
        self.assertEqual( str(appContext), 'SCH' )

