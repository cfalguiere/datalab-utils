#-*- coding: utf-8 -*-
from __future__ import print_function

import unittest

from lab.common.exceptions import ConfigurationError, ExecutionError


class TestConfigurationError(unittest.TestCase):

    def test_exception(self):
        with self.assertRaises(ConfigurationError) as ctx:
            raise ConfigurationError('pathToCode', 'does not exist')
            self.assertTrue('ConfigurationError' in ctx.exception)
            self.assertEqual('ConfigurationError: error on pathToCode: does not exist', str(ctx.exception))


class TestExecutionError(unittest.TestCase):

    def test_exception(self):
        with self.assertRaises(ExecutionError) as ctx:
            raise ExecutionError('pathToCode', 'does not exist')
            self.assertTrue('ExecutionError' in ctx.exception)
            self.assertEqual('ExecutionError: error in step step2 - wrong parameter', str(ctx.exception))
