#-*- coding: utf-8 -*-
"""R Steps Configuration Tests"""

import unittest
import ConfigParser

from sch.init.configuration import RStepsConfiguration
from  sch.common.app import AppContext

class TestRStepsConfigurationMethods(unittest.TestCase):

      def test_get_path_to_code(self):
        appContext = AppContext()
        config = ConfigParser.SafeConfigParser()
        config.read('sch/mocks/app-for-unittests.cfg')
        rc = RStepsConfiguration(config)
        self.assertEqual(rc.get_path_to_code(), config.get('PATH', 'code'))

      def test_get_parameters_as_table(self):
        appContext = AppContext()
        config = ConfigParser.SafeConfigParser()
        config.read('sch/mocks/app-for-unittests.cfg')
        rc = RStepsConfiguration(config)
        params = rc.get_parameters_as_map( [ 'pathToData', 'pathToRawData', 'pathToLog' ] )
        self.assertEqual(len(params), 4)
        self.assertEqual(params[0], 'pathToCode='+config.get('PATH', 'code'))
        pathToData =  config.get('PATH', 'data')
        self.assertEqual(params[1],  'pathToData={0}'.format( pathToData) )
        self.assertEqual(params[2], 'pathToRawData={0}/rawData'.format( pathToData ) )
        self.assertEqual(params[3], 'pathToLog={0}/log'.format( pathToData ) )
      def test_verify(self):
         pass
        #TODO existence de toutes les clés requises


if __name__ == '__main__':
    unittest.main()

