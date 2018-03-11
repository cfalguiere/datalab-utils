#-*- coding: utf-8 -*-

import os
import ConfigParser
import traceback

from sch.common.exceptions import ExecutionError, ConfigurationError
from sch.common.validator import PathValidator

# TODO finir les tests
class AppConfiguration:
    def __init__(self, cfgPath, theAppContext):
        self.cfgPath = cfgPath
        self.theAppContext = theAppContext
        self.parameters = None

    def __enter__(self):
        print( '===========================================================')
        print( "INFO - Preparing configuration"  )
        try:
            confLoader = AppConfigurationLoader(self.cfgPath)
            confLoader.load(self.cfgPath)
            print('INFO - Configuration loaded from %s' % self.cfgPath)

            confLoader.init_path()
            confLoader.init_custom_parameters()


        except ConfigurationError as e:
            raise ConfigurationError('Cfg File', 'error during configuration  - cfg path %s - %s' % (self.cfgPath, str(e) ) )

        print('INFO - Configuration verified')
        self.parameters = confLoader.get_configuration()
        self.theAppContext.set_configuration( self )
        #print( 'DEBUG - parameters ====' )
        print( '-----------------------------------------------------------')
        print( '| ')
        print( '| CONFIGURATION')
        print( '| ')
        for key, value in self.parameters.items():
              print( '| [%s]  = %s' % (key, value) )
        print( '-----------------------------------------------------------')
        print( '===========================================================')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
         pass

    def get_path_to_code(self):
          return self.parameters['pathToCode']

    def get_path_to_raw_data(self):
          return self.parameters['pathToRawData']

    def add_parameter(self, key, value):
          self.parameters[key] = value

    def get_parameter(self, key):
          try:
              value = self.parameters[key]
          except:
              raise ExecutionError('AppConfiguration', 'key %s not found' % key)
          return value

    def get_file_name(self, folder, filename):
          path = '%s/%s' % (self.parameters[folder], filename)
          if not os.path.exists(path):
                 raise ExecutionError(filename, 'file not found at %s' % path )
          return path

    def get_parameters_as_map(self, keyList):
          params = []
          params.append( '{0}={1}'.format('pathToRCode', self.get_path_to_code()) )
          for key in keyList:
              if key != 'pathToCode':
                    #print('reading %s from parameters' % key )
                    try:
                        params.append( "%s=%s" % (key,  self.parameters[key]  ) )
                    except:
                        #print( 'DEBUG - %s' % str( self.parameters ))
                        raise ExecutionError("Missing parameter", key)
          return params


    def __str__(self):
         return str(self.parameters)


class AppConfigurationLoader:
      def __init__(self, aConfigFileName):
            self.settings = None
            self.parameters = {}

      def load(self, path):
            cv = PathValidator()
            if  not cv.check_path_for_existence( path ):
                raise ConfigurationError('PATH', 'Config file not found at %s' % path)

            self.settings = ConfigParser.SafeConfigParser()
            self.settings.read(path)
            print( 'INFO - Settings loaded from %s' % path)

      def get_configuration(self):
            return self.parameters

      def init_path(self):
              cv = PathValidator()

              # internal
              def add_roots(segment):
                  path =  self.settings.get('PATH', segment)
                  #print('DEBUG - (AppConfigurationLoader) add_root %s ' % path)
                  if cv.check_path_for_existence( path ):
                      key =  'pathTo{0}{1}'.format(segment[0].capitalize(), segment[1:])
                      #print('DEBUG - (AppConfigurationLoader) adding %s to parameters' % key)
                      self.parameters[key] = path
                      #print('DEBUG - (AppConfigurationLoader) parameters[%s]  = %s' % (key, self.parameters[key]) )

              for segment in [ 'code', 'rScript', 'project',  'data' ]:
                   add_roots(segment)

              if cv.nb_errors() > 0:
                  cv.list_errors()
                  raise ConfigurationError('PATH', 'Please fix wrong path')

             #print( 'DEBUG - parameters in init %s' % str(self.parameters))

              # internal
              def add_subfolder(segment, parentFolder):
                  path = '{0}/{1}/'.format( parentFolder, segment )
                  #print('DEBUG - (AppConfigurationLoader) add_subfolder %s ' % path)
                  if not os.path.exists(path):
                       os.makedirs(path)
                       print('INFO - Created directory %s for %s ' % (path, segment) )

                  key =  'pathTo{0}{1}'.format(segment[0].capitalize(), segment[1:])
                  #print('DEBUG - (AppConfigurationLoader) adding %s to parameters' % key)
                  self.parameters[key] = path
                  #print('DEBUG - (AppConfigurationLoader) parameters[%s]  = %s' % (key, self.parameters[key]) )

              pathToData = self.parameters['pathToData']
              for segment in [ 'rawData', 'cleanData', 'finalData', 'log', 'models' ]:
                   add_subfolder(segment, pathToData)

              pathToRawData = self.parameters['pathToRawData']
              for segment in [ 'otherData', 'paiementsData' ]:
                   add_subfolder(segment, pathToRawData)

              pathToCleanData = self.parameters['pathToCleanData']
              for segment in [ 'agg' ]:
                   add_subfolder(segment, pathToCleanData)

              self.parameters['pathToLogs'] = self.parameters['pathToLog']

              #pathToRawData = self.parameters['pathToRawData']
              #for segment in [ 'otherData' , 'paiementsData' ]:
              #     add_subfolder(segment, pathToRawData)
              # TODO classe specialisee


     # TODO classe specialisee
      def init_custom_parameters(self):
              def add_parameter(section, key):
                    self.parameters[key] = self.settings.get(section, key)

              add_parameter('IDENTIFIANTS', 'varId')
              add_parameter('IDENTIFIANTS', 'numCR')
              add_parameter('DATES', 'dateMinPreparation')
              add_parameter('DATES', 'dateMaxPreparation')
              add_parameter('DATES', 'dateMaxEntrainement')
              add_parameter('WINDOWING', 'nbrMonths_paiements')
              add_parameter('WINDOWING', 'nbrMonths_epargne')
              add_parameter('CIBLE', 'namePretReal')
              add_parameter('CIBLE', 'varCible')
              add_parameter('SEEDS', 'seeds')
              add_parameter('PROPAGATION', 'predictionFileName')
              add_parameter('PROPAGATION', 'nbCluster')
              add_parameter('SPLIT', 'typeSplit')

              # TODO fixer l'incoherence de noms
              self.parameters['timeMinPreparation'] =  self.parameters['dateMinPreparation']
              self.parameters['timeMaxPreparation'] =  self.parameters['dateMaxPreparation']
              self.parameters['timeMaxEntrainement'] =  self.parameters['dateMaxEntrainement']


