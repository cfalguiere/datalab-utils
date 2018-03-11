#-*- coding: utf-8 -*-
from __future__ import print_function

from lab.common.configuration

# TODO finir les tests - show - custom init - enter / exit
class AppConfiguration:

      def __init__(self, cfgPath, theAppContext=None):
            self.cfgPath = cfgPath
            self.theAppContext = theAppContext
            self.parameters = None

      def __repr__(self):
            return 'AppConfiguration: from={0}'.format(self.cfgPath)

      def __enter__(self):
            print( '===========================================================')
            print( "INFO - Preparing configuration"  )
            try:
                confLoader = AppConfigurationLoader(self.cfgPath)
                confLoader.load(self.cfgPath)

                print('INFO - Configuration loaded from %s' % self.cfgPath)

                self.custom_init()

            except ConfigurationError as e:
                raise ConfigurationError('Cfg File', 'error during configuration  - cfg path %s - %s' % (self.cfgPath, str(e) ) )

            print('INFO - Configuration verified')
            self.show()

            self.parameters = confLoader.get_configuration()
            self.theAppContext.set_configuration( self )

            print( '===========================================================')
            return self

      def __exit__(self, exc_type, exc_value, exc_traceback):
             pass

      def __custom_init(self):
            pass

      def show(self):
            print( '-----------------------------------------------------------')
            print( '| ')
            print( '| CONFIGURATION')
            print( '| ')
            for key, value in self.parameters.items():
                  print( '| [%s]  = %s' % (key, value) )
            print( '-----------------------------------------------------------')

