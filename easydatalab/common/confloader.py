#-*- coding: utf-8 -*-
from __future__ import print_function

import ConfigParser

from easydatalab.common.validator import PathValidator
from easydatalab.common.exceptions import ConfigurationError

class AppConfigurationLoader:
      def __init__(self):
            self.settings = None
            self.parameters = {}

      def load(self, path):
          def check_item(item):
            cv = PathValidator()
            if  not cv.check_path_for_existence( item ):
                raise ConfigurationError('PATH', 'Config file not found at %s' % item)

          if isinstance( path, list ):
             for p in path:
                 check_item(p)
          else:
             check_item(path)

          self.settings = ConfigParser.SafeConfigParser()
          self.settings.read(path)

          return self.settings
