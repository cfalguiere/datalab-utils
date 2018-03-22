#-*- coding: utf-8 -*-
from __future__ import print_function

from easydatalab.common.exceptions import ConfigurationError, ExecutionError
from easydatalab.common.confloader import AppConfigurationLoader
import logging

class AppConfiguration:

      def __init__(self, cfgPath, theAppContext=None):
            self.cfgPath = cfgPath
            self.theAppContext = theAppContext
            self.parameters = {}
            self.settings = None
            self.logger = logging.getLogger('common.AppConfiguration')
            self.logger.info('creating an instance of class AppConfiguration')

      def __repr__(self):
            return 'AppConfiguration: from={0}'.format(self.cfgPath)

      def __enter__(self):
            print( '===========================================================')
            print( "INFO - Preparing configuration"  )
            try:
                confLoader = AppConfigurationLoader()
                self.settings = confLoader.load(self.cfgPath)

                print('INFO - Configuration loaded from %s' % self.cfgPath)

            except ConfigurationError as e:
                raise ConfigurationError('AppConfiguration', 'error during configuration  - cfg path %s - %s' % (self.cfgPath, str(e) ) )

            if self.theAppContext:
               self.theAppContext.set_configuration( self )

            print( '===========================================================')
            return self

      def __exit__(self, exc_type, exc_value, exc_traceback):
            pass

      def __custom_init(self):
            pass

      def customize(self, f):
          params = f(self)

      def add_parameter(self, key, value):
          self.parameters[key] = value

      def get_parameter(self, key):
          try:
            if ':' in key:
              pair = key.split(':')
              value = self.settings.get(pair[0], pair[1])
            else:
              value = self.parameters[key]
          except:
              raise ExecutionError('AppConfiguration', 'key %s was not found' % key)
          return value

      def show(self):
          print( '-----------------------------------------------------------')
          print( '| ')
          print( '| CONFIGURATION')
          print( '| ')
          for key, value in self.parameters.items():
              print( '| [%s]  = %s' % (key, value) )
          print( '-----------------------------------------------------------')

