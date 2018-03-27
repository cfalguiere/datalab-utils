#-*- coding: utf-8 -*-
from __future__ import print_function

import unittest

from easydatalab.monitoring.filemonitor import FileMonitor


class TestFileMonitor(unittest.TestCase):

    def test_constructor(self):
        fm = FileMonitor()
        self.assertIsNotNone( fm )

    def test_track(self):
        fm = FileMonitor()
        monitor = fm.track('A', 'input', 'output')
        self.assertIsNotNone( monitor )

    def test_pre(self):
        fm = FileMonitor()
        monitor = fm.track('A', 'input', 'output')
        monitor.pre_condition()
        self.assertEquals( monitor.status, 'Started' )

    def test_post(self):
        fm = FileMonitor()
        monitor = fm.track('A', 'input', 'output')
        monitor.post_condition()
        self.assertEquals( monitor.status, 'Done' )
