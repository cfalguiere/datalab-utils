#-*- coding: utf-8 -*-
from __future__ import print_function

import unittest

from easydatalab.configuration.windowing import Windowing


class TestWindowing(unittest.TestCase):

    def test_validator_defaults(self):
        w = Windowing('201804')
        (min_available, max_available) = w.available_periods()
        (min_selected, max_selected) = w.selected_periods()

        self.assertEqual( min_available, '201505' )
        self.assertEqual( max_available, '201804' )
        self.assertEqual( min_selected, '201505' )
        self.assertEqual( max_selected, '201802' )

    def test_exception_custom_1(self):
        w = Windowing('201804',  window_length=4, nb_available_periods=5, nb_selected_periods=5, nb_staging_periods=0)
        (min_available, max_available) = w.available_periods()
        (min_selected, max_selected) = w.selected_periods()

        self.assertEqual( min_available, '201711' )
        self.assertEqual( max_available, '201804' )
        self.assertEqual( min_selected, '201711' )
        self.assertEqual( max_selected, '201804' )

    def test_exception_custom_2(self):
        w = Windowing('201804',  window_length=4, nb_available_periods=6, nb_selected_periods=3, nb_staging_periods=1)
        (min_available, max_available) = w.available_periods()
        (min_selected, max_selected) = w.selected_periods()

        self.assertEqual( min_available, '201710' )
        self.assertEqual( max_available, '201804' )
        self.assertEqual( min_selected, '201712' )
        self.assertEqual( max_selected, '201803' )
